#!/usr/bin/env python
# coding: utf-8
import os
import signal
from simplifier.simplifier import Simplifier

import sys

from simplifier.version import VERSION

def getopts():
    import argparse
    import textwrap

    '''
    Get the command line options.
    '''
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''Simplify shp files''')
    )
    parser.add_argument('-s', '--simplify', action='store', type=float, default=4,
                        required=False,
                        help='simplification factor (default %(default).2f)')
    parser.add_argument('-p', '--path', action='store', type=str,
                        required=False,
                        help='input file')
    parser.add_argument('-o', '--output', action='store', type=str,
                        required=False,
                        help='output path')
    parser.add_argument('-v', '--version', action='store_const', const=True,
                        required=False, help='show current version')
    opts = parser.parse_args()
    return opts


def run_console(opt):
    output = opt.output if opt.output else os.path.join('output')
    abspath = os.path.abspath(output)
    kwargs = {
        'input_file': opt.path,
        'simplify': opt.simplify,
        'output_format': 'geojson'
    }
    simplifier = Simplifier(**kwargs)

    result = simplifier.run()

    pathname, extension = os.path.splitext(opt.path)
    filename = pathname.split(os.sep)[-1]
    filename = '{}__simplified_{}.geojson'.format(filename, opt.simplify)
    geojson_path = os.path.join(abspath, 'geojson')
    if not os.path.isdir(geojson_path):
        os.makedirs(geojson_path)
    file_path = os.path.join(geojson_path, filename)
    f = open(file_path, 'w')
    f.write(result)
    f.close()
    print('output - {}'.format(file_path))


def console():

    opt = getopts()
    show_version = opt.version
    if show_version:
        print(VERSION)
    else:
        def signal_handler(signalnum, frame):
            print('You pressed Ctrl+C')
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)
        print('Press Ctrl+C to exit')

        run_console(opt)
