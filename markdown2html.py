#!/usr/bin/python3
"""
markdown2html.py: Convert Markdown file to HTML.
"""

import sys
import os
import markdown


def convert_markdown_to_html(input_file, output_file):
    """
    Convert Markdown file to HTML.

    Args:
        input_file (str): Name of the Markdown file.
        output_file (str): Name of the output HTML file.
    """
    # Check if the Markdown file exists
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Read Markdown content and convert to HTML
    with open(input_file, 'r') as md_file:
        markdown_content = md_file.read()

    html_content = markdown.markdown(markdown_content)

    # Write HTML content to the output file
    with open(output_file, 'w') as html_file:
        html_file.write(html_content)


if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 3:
        print("Use: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    # Extract input and output file names from command-line arguments
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Convert Markdown to HTML
    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)
