import os


def replace(original, actual):
    original = 'var ' + original + ' = '
    counter_file = open(r'/Users/XG/.venv/YelpxPython/map.html', 'r+')
    content_lines = []

    for line in counter_file:
        if original in line:
            line_components = line.split('= ')
            line_components[1] = str(actual) + '\n'
            updated_line = "= ".join(line_components)
            content_lines.append(updated_line)
        else:
            content_lines.append(line)

    counter_file.seek(0)
    counter_file.truncate()
    counter_file.writelines(content_lines)
    counter_file.close()
