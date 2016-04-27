#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of "Umbrella content", that is the content used In the Umbrella App.
# Copyright © 2016 seamus tuohy, <s2e+code@seamustuohy.com>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the included LICENSE file for details.

# Example command line
# python3 scripts/write_markdown.py -i json/en -H html/en -M md/en

import argparse
import json
import os
import subprocess

import logging
logging.basicConfig(level=logging.ERROR)
log = logging.getLogger(__name__)

def main():
    """This is the main function. It runs things around here."""
    args = parse_arguments()
    set_logging(args.verbose, args.debug)
    files = os.listdir(args.input)
    for filename in files:
        log.debug("Processing {0}".format(filename))
        extension = os.path.basename(filename).split('.')[1:][0]
        if extension == "json":
            log.debug("File {0} is JSON and will be processed.".format(filename))
            write_html_from_json(filename, args.input, args.html_output)
            write_markdown_from_html(filename, args.html_output, args.md_output)
        else:
            print("File {0} is not JSON and will NOT be processed".format(filename))

def write_markdown_from_html(filename, in_path, out_path):
    """ Writes an markdown file from a HTML file."""
    base_filename = os.path.basename(filename).split('.')[:1][0]
    html_filepath = os.path.join(in_path, base_filename)
    md_filepath = os.path.join(out_path, base_filename)
    html_name = html_filepath + ".html"
    log.debug("Writing markdown file for {0}".format(html_name))
    md_name = md_filepath + ".md"
    log.debug("files {0} {1}".format(html_name, md_name))
    subprocess.check_output(["pandoc", "-f", "html", "-t", "markdown", "-o",  md_name, html_name])

def write_html_from_json(filename, in_path, out_path):
    """ Writes a HTML file from a JSON file."""
    log.debug("Writing markdown file for {0}".format(filename))
    original_filepath = os.path.join(in_path, filename)
    with open(original_filepath, 'r') as jsonfile:
        json_data = jsonfile.read()
        obj = json.loads(json_data)
        base_filename = os.path.basename(filename).split('.')[:1][0]
        full_filepath = os.path.join(out_path, base_filename)

        with open(full_filepath + ".html", 'w+') as html_file:
            if isinstance(obj, list):
                log.debug("File {0} is a text file".format(filename))
                for section in obj:
                    log.info("Writing section {0} to HTML file".format(section['title']))
                    html_file.write(section['body'])
                    html_file.write("\n\n")
            elif filename == "strings.json":
                log.debug("File {0} is the strings file for translation.".format(filename) +
                          " But, I will parse it anyway. Because I'm the best." +
                          " And, humble too!")
                for name, text_strings in obj.items():
                    html_file.write(name + " : " + text_strings + " \n\n ")
            else:
                log.warn("Sorry Rory, I have no idea what you put in this file." +
                         "Then again, seeing as I wrote this it is surely an error in the code.")

# Command Line Functions below this point

def set_logging(verbose=False, debug=False):
    if debug == True:
        log.setLevel("DEBUG")
    elif verbose == True:
        log.setLevel("INFO")

def parse_arguments():
    parser = argparse.ArgumentParser("Get a summary of some text")
    parser.add_argument("--verbose", "-v",
                        help="Turn verbosity on",
                        action='store_true')
    parser.add_argument("--debug", "-d",
                        help="Turn debugging on",
                        action='store_true')
    parser.add_argument("--input", "-i",
                        help="Input directory where input JSON files are.")
    parser.add_argument("--html_output", "-H",
                        help="Output directory where HTML should be placed.")
    parser.add_argument("--md_output", "-M",
                        help="Output directory where markdown should be placed.")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()
