import os
import difflib


def collect_files(root_dir):
    collected = {}
    if not os.path.exists(root_dir):
        return collected

    for base, _, files in os.walk(root_dir):
        for name in files:
            full_path = os.path.join(base, name)
            rel_path = os.path.relpath(full_path, root_dir).replace("\\", "/")
            collected[rel_path] = full_path
    return collected


def read_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def compare_directories(old_dir, new_dir, diff_output_path=None):
    old_files = collect_files(old_dir)
    new_files = collect_files(new_dir)

    old_set = set(old_files.keys())
    new_set = set(new_files.keys())

    removed = sorted(old_set - new_set)
    added = sorted(new_set - old_set)
    common = sorted(old_set & new_set)

    changed = []
    diff_lines = []

    if removed:
        diff_lines.append("REMOVED FILES:")
        for path in removed:
            diff_lines.append(f"  - {path}")
        diff_lines.append("")

    if added:
        diff_lines.append("ADDED FILES:")
        for path in added:
            diff_lines.append(f"  + {path}")
        diff_lines.append("")

    for rel_path in common:
        old_text = read_text_file(old_files[rel_path])
        new_text = read_text_file(new_files[rel_path])

        if old_text != new_text:
            changed.append(rel_path)
            diff_lines.append(f"CHANGED: {rel_path}")
            diff_lines.extend(
                difflib.unified_diff(
                    old_text.splitlines(),
                    new_text.splitlines(),
                    fromfile=f"{old_dir}/{rel_path}",
                    tofile=f"{new_dir}/{rel_path}",
                    lineterm="",
                )
            )
            diff_lines.append("")

    if changed:
        summary = f"Changed files: {len(changed)}"
    else:
        summary = "Changed files: 0"

    print(f"Added files: {len(added)}")
    print(f"Removed files: {len(removed)}")
    print(summary)

    if diff_output_path:
        with open(diff_output_path, "w", encoding="utf-8") as f:
            if diff_lines:
                f.write("\n".join(diff_lines) + "\n")
            else:
                f.write("No differences found.\n")

        print(f"✔ diff report written: {diff_output_path}")

    return {
        "added": added,
        "removed": removed,
        "changed": changed,
    }