from pathlib import Path
import anyconfig


trans_path = "./template/i18n/English.json"
template_path = "./template/template.yml"

trans = {
    "Project": {
        "tasks": {
            "General": {
                "groups": {}
            }
        }
    }
}
with open(template_path, 'r', encoding='utf-8') as f:
    tpl = anyconfig.load(f)

for menu_name, menu_conf in tpl.items():
    if menu_name == "Project":
        if "General" in menu_conf.keys():

            group_trans = trans["Project"]["tasks"]["General"]["groups"]
            for group_name, group_conf in menu_conf["General"].items():
                if group_name == "_Base":
                    continue
                group_trans[group_name] = {
                        "name": group_name,
                        "help": group_conf.get("_help", {}).get("value", ""),
                        "items": {}
                    }
                
                item_trans = group_trans[group_name]["items"]
                for item_name, item_conf in group_conf.items():
                    if item_name == "_help":
                        continue
                    item_trans[item_name] = {
                            "name": item_name,
                            "help": item_conf.get("help", ""),
                        }
                    for option_name in item_conf.get("option", []):
                        item_trans[item_name].setdefault("options", {})[option_name] = option_name
    else:
        trans[menu_name] = {
            "name": menu_name,
            "tasks": {}
        }

        task_trans = trans[menu_name]["tasks"]
        for task_name, task_conf in menu_conf.items():
            task_trans[task_name] = {
                "name": task_name,
                "groups": {}
            }

            group_trans = task_trans[task_name]["groups"]
            for group_name, group_conf in task_conf.items():
                if group_name == "_Base":
                    continue
                group_trans[group_name] = {
                    "name": group_name,
                    "help": group_conf.get("_help", {}).get("value", ""),
                    "items": {}
                }

                item_trans = group_trans[group_name]["items"]
                for item_name, item_conf in group_conf.items():
                    if item_name == "_help":
                        continue
                    item_trans[item_name] = {
                        "name": item_name,
                        "help": item_conf.get("help", "")
                    }
                    for option_name in item_conf.get("option", []):
                        item_trans[item_name].setdefault("options", {})[option_name] = option_name

if Path(trans_path).exists():
    with open(trans_path, 'r', encoding='utf-8') as f:
        old_trans = anyconfig.load(f)
    anyconfig.merge(trans, old_trans)

with open(trans_path, 'w', encoding='utf-8') as f:
    anyconfig.dump(trans, f, ensure_ascii=False, indent=2, allow_unicode=True)
