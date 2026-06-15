#!/usr/bin/env python3
"""
文献去重脚本
用于 SKILL 2 (paper-novelty-check)：将新检索文献与已有文献台账进行去重比对

用法:
    python dedupe.py --ledger <ledger_file.json> --new_results <new_results.json> [--output <output_file.json>]

输入格式 (ledger.json):
    [
        {"reference_id": "S1", "title": "...", "first_author": "...", "year": 2024,
         "url_or_doi": "...", "dedupe_key": "DOI:10.xxx"},
        ...
    ]

输入格式 (new_results.json):
    [
        {"title": "...", "first_author": "...", "year": 2025,
         "url_or_doi": "..."},
        ...
    ]
"""

import json
import argparse
import sys
import re
from typing import Dict, List, Optional


def normalize_title(title: str) -> str:
    """标准化标题用于比对：小写、去标点、去多余空格"""
    t = title.lower().strip()
    t = re.sub(r'[^\w\s]', '', t)
    t = re.sub(r'\s+', ' ', t)
    return t


def make_dedupe_key(entry: Dict) -> None:
    """为条目生成 dedupe_key（如果没有）"""
    if entry.get('dedupe_key'):
        return
    doi = entry.get('url_or_doi', '')
    if doi and ('10.' in doi or 'doi' in doi.lower()):
        # 提取 DOI
        m = re.search(r'10\.\d{4,}/[^\s]+', doi)
        if m:
            entry['dedupe_key'] = f"DOI:{m.group()}"
            return
    # 回退：title + first_author + year
    title_norm = normalize_title(entry.get('title', ''))
    author = (entry.get('first_author', '') or '').lower().strip()
    year = str(entry.get('year', ''))
    entry['dedupe_key'] = f"{title_norm}|{author}|{year}"


def load_json(path: str) -> List[Dict]:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, dict) and 'references' in data:
        data = data['references']
    return data


def dedupe(ledger: List[Dict], new_results: List[Dict]) -> Dict:
    """核心去重逻辑"""
    # 建立已有 dedupe_key 集合
    existing_keys = set()
    for entry in ledger:
        make_dedupe_key(entry)
        existing_keys.add(entry['dedupe_key'])

    matched = []
    new_entries = []

    for entry in new_results:
        make_dedupe_key(entry)
        if entry['dedupe_key'] in existing_keys:
            matched.append({
                'title': entry.get('title', ''),
                'dedupe_key': entry['dedupe_key'],
                'status': 'duplicate'
            })
        else:
            new_entries.append({
                **entry,
                'status': 'new'
            })
            existing_keys.add(entry['dedupe_key'])  # 防止新结果内部重复

    return {
        'summary': {
            'total_new_results': len(new_results),
            'duplicates': len(matched),
            'new_unique': len(new_entries),
            'ledger_size': len(ledger)
        },
        'new_entries': new_entries,
        'duplicates': matched
    }


def main():
    parser = argparse.ArgumentParser(description='文献去重脚本')
    parser.add_argument('--ledger', required=True, help='已有文献台账 JSON 文件')
    parser.add_argument('--new_results', required=True, help='新检索结果 JSON 文件')
    parser.add_argument('--output', help='输出文件路径（默认打印到 stdout）')
    args = parser.parse_args()

    try:
        ledger = load_json(args.ledger)
        new_results = load_json(args.new_results)
    except Exception as e:
        print(f"Error loading files: {e}", file=sys.stderr)
        sys.exit(1)

    result = dedupe(ledger, new_results)

    output_json = json.dumps(result, ensure_ascii=False, indent=2)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(output_json)
        print(f"去重完成。新增 {result['summary']['new_unique']} 篇，"
              f"重复 {result['summary']['duplicates']} 篇。")
        print(f"结果已保存至: {args.output}")
    else:
        print(output_json)


if __name__ == '__main__':
    main()
