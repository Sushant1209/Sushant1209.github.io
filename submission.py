# The script code, adjusted to write directly to 'submissions.md'

import re

def convert_table_links():
    input_file = 'submissions.md'
    output_file = 'submissions.md'

    with open(input_file, 'r') as f:
        content = f.read()

    # Regular expressions to match table rows
    separator_pattern = re.compile(r'^\|[-| ]+\|[-| ]+\|[-| ]+\|$')
    row_pattern = re.compile(r'^\|([^|\n]+?)\|([^|\n]+?)\|([^|\n]+?)\|$')

    # Flag to start processing inside a table
    in_table = False
    output_lines = []

    def debug_log(line, status):
        print(f"Processing line: {line} | Status: {status}")

    # Process content
    for line in content.splitlines():
        if separator_pattern.match(line):
            in_table = True
            debug_log(line, "Table separator detected")
        elif row_pattern.match(line):
            if in_table:
                match = row_pattern.match(line)
                if match:
                    name, url1, url2 = [s.strip() for s in match.groups()]
                    url1 = f'[{url1}]({url1})' if url1 and not url1.startswith('[') else url1
                    url2 = f'[{url2}]({url2})' if url2 and not url2.startswith('[') else url2
                    line = f'| {name} | {url1} | {url2} |'
                    debug_log(line, "Row processed")
                else:
                    debug_log(line, "Row not matched")
            else:
                debug_log(line, "Row found outside of table")
        else:
            if in_table:
                in_table = False
                debug_log(line, "End of table detected")

        output_lines.append(line)

    new_content = '\n'.join(output_lines)

    with open(output_file, 'w') as f:
        f.write(new_content)

# Run the function
convert_table_links()





# import re

# def convert_table_links(input_file, output_file):
#     with open(input_file, 'r') as f:
#         content = f.read()

#     # Regular expressions to match table rows
#     separator_pattern = re.compile(r'^\|[-| ]+\|[-| ]+\|[-| ]+\|$')
#     row_pattern = re.compile(r'^\|([^|\n]+?)\|([^|\n]+?)\|([^|\n]+?)\|$')

#     # Flag to start processing inside a table
#     in_table = False

#     # Process content
#     def process_line(line):
#         nonlocal in_table
#         # Match separator
#         if separator_pattern.match(line):
#             in_table = True
#             return line
#         elif in_table and row_pattern.match(line):
#             match = row_pattern.match(line)
#             name, url1, url2 = [s.strip() for s in match.groups()]
#             url1 = f'[{url1}]({url1})' if url1 and not url1.startswith('[') else url1
#             url2 = f'[{url2}]({url2})' if url2 and not url2.startswith('[') else url2
#             return f'| {name} | {url1} | {url2} |'
#         elif in_table and not row_pattern.match(line):
#             in_table = False
#         return line

#     new_content = '\n'.join(process_line(line) for line in content.splitlines())

#     with open(output_file, 'w') as f:
#         f.write(new_content)

# # Usage
# input_file = 'submissions.md'
# output_file = 'submissions_updated.md'
# convert_table_links(input_file, output_file)
