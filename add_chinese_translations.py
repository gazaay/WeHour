#!/usr/bin/env python3
"""
Script to add Chinese translations to WeHour documentation files.
This script adds Chinese translations below English content in markdown files.
"""

import os
import re
import glob

# Translation mappings for common terms
TRANSLATIONS = {
    # Headers and titles
    "Solution Overview": "解决方案概述",
    "Value Proposition": "价值主张",
    "Technical Architecture": "技术架构",
    "Business Model": "商业模式",
    "Implementation": "实施",
    "Tokenomics": "代币经济学",
    "Resources": "资源",
    "Metrics & KPIs": "指标与关键绩效指标",
    
    # Common terms
    "Volunteer": "义工",
    "Organization": "组织",
    "Platform": "平台",
    "Blockchain": "区块链",
    "Token": "代币",
    "Verification": "验证",
    "Reward": "奖励",
    "Service": "服务",
    "Impact": "影响",
    "Ecosystem": "生态系统",
    "Partnership": "合作伙伴关系",
    "Revenue": "收入",
    "Market": "市场",
    "Strategy": "策略",
    "Roadmap": "路线图",
    "Risk Management": "风险管理",
    "Pilot Program": "试点计划",
    "Success Metrics": "成功指标",
    "Token Metrics": "代币指标",
    "Platform Analytics": "平台分析",
    "Contact": "联系方式",
    "FAQ": "常见问题",
    "Glossary": "词汇表",
    "References": "参考资料",
    
    # Common phrases
    "Core Concepts": "核心概念",
    "System Overview": "系统概述",
    "Dual Token Model": "双代币模式",
    "Cross Chain": "跨链",
    "Smart Contracts": "智能合约",
    "Security Framework": "安全框架",
    "Privacy Compliance": "隐私合规",
    "Revenue Streams": "收入流",
    "Market Analysis": "市场分析",
    "Competitive Landscape": "竞争格局",
    "Go To Market": "市场推广",
    "Partnerships": "合作伙伴关系",
    "Pilot Programs": "试点计划",
    "Risk Management": "风险管理",
    "Roadmap": "路线图",
}

def add_chinese_translation(text):
    """Add Chinese translation below English text."""
    lines = text.split('\n')
    result = []
    
    for line in lines:
        result.append(line)
        
        # Skip if line is already translated or is empty
        if not line.strip() or line.startswith('#') and '#' in line[1:]:
            continue
            
        # Add Chinese translation for headers
        if line.startswith('# '):
            title = line[2:].strip()
            if title in TRANSLATIONS:
                result.append(f"# {TRANSLATIONS[title]}")
        elif line.startswith('## '):
            title = line[3:].strip()
            if title in TRANSLATIONS:
                result.append(f"## {TRANSLATIONS[title]}")
        elif line.startswith('### '):
            title = line[4:].strip()
            if title in TRANSLATIONS:
                result.append(f"### {TRANSLATIONS[title]}")
        elif line.startswith('#### '):
            title = line[5:].strip()
            if title in TRANSLATIONS:
                result.append(f"#### {TRANSLATIONS[title]}")
        elif line.startswith('##### '):
            title = line[6:].strip()
            if title in TRANSLATIONS:
                result.append(f"##### {TRANSLATIONS[title]}")
        elif line.startswith('###### '):
            title = line[7:].strip()
            if title in TRANSLATIONS:
                result.append(f"###### {TRANSLATIONS[title]}")
    
    return '\n'.join(result)

def process_file(file_path):
    """Process a single markdown file to add Chinese translations."""
    print(f"Processing: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if file already has Chinese translations
        if '解决方案' in content or '代币' in content or '义工' in content:
            print(f"  Skipping {file_path} - already has Chinese translations")
            return
        
        # Add Chinese translations
        translated_content = add_chinese_translation(content)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        
        print(f"  ✓ Added Chinese translations to {file_path}")
        
    except Exception as e:
        print(f"  ✗ Error processing {file_path}: {e}")

def main():
    """Main function to process all markdown files."""
    docs_dir = "/Users/gglam/Development/WeHour/docs"
    
    # Find all markdown files except README.md and _sidebar.md
    pattern = os.path.join(docs_dir, "**/*.md")
    files = glob.glob(pattern, recursive=True)
    
    # Filter out files that shouldn't be processed
    skip_files = ['README.md', '_sidebar.md', 'index.html']
    files = [f for f in files if not any(skip in f for skip in skip_files)]
    
    print(f"Found {len(files)} markdown files to process")
    
    for file_path in files:
        process_file(file_path)
    
    print("\nTranslation process completed!")

if __name__ == "__main__":
    main()
