import anyconfig


with open("template/template.yml", 'r', encoding='utf-8') as f:
    data = anyconfig.load(f)

with open("template/template.json", 'w', encoding='utf-8') as f:
    anyconfig.dump(data, f, ensure_ascii=False, indent=2, allow_unicode=True)
