#!/usr/bin/env python

import sys
import os
import shutil
import codecs

from distutils.core import Command
from distutils.command.clean import clean as Clean

import package

ABSPATH_ROOTDIR              = os.path.dirname(os.path.abspath(__file__))
RELPATH_FILES_CLEAN          = ['build', 'dist', '{name}.egg-info'.format(name = package.name), '.cache']
RELPATH_WALK_FILES_EXT_CLEAN = ['.pyc']
RELPATH_WALK_DIRS_CLEAN      = ['__pycache__']

class CleanCommand(Clean):
    def run(self):
        Clean.run(self)

        for filename in RELPATH_FILES_CLEAN:
            if os.path.exists(filename):
                shutil.rmtree(filename)

        for dirpath, dirnames, filenames in os.walk(ABSPATH_ROOTDIR):
            for filename in filenames:
                for extension in RELPATH_WALK_FILES_EXT_CLEAN:
                    if filename.endswith(extension):
                        path = os.path.join(dirpath, filename)
                        os.unlink(path)

            for dirname in dirnames:
                if dirname in RELPATH_WALK_DIRS_CLEAN:
                    path = os.path.join(dirpath, dirname)
                    shutil.rmtree(path, ignore_errors = True)

class TestCommand(Command):
    user_options = [('pytest=', 'a', 'arguments to be passed to pytest')]

    def initialize_options(self):
        self.args_pytest = [ ]

    def finalize_options(self):
        pass

    def run(self):
        import pytest

        errno = pytest.main(self.args_pytest)

        sys.exit(errno)

def get_long_description(filepaths):
    content   = ''
    filepaths = filepaths if isinstance(filepaths, list) else [filepaths]

    if filepaths:
        for i, filepath in enumerate(filepaths):
            if os.path.exists(filepath):
                if os.path.isfile(filepath):
                    if os.path.getsize(filepath) > 0:
                        f        = codecs.open(filepath, mode = 'r', encoding = 'utf-8')
                        raw      = f.read()
                        content += '{prepend}{content}'.format(prepend = '' if i is 0 else '\n\n', content = raw)

                        f.close()
                else:
                    raise ValueError('Not a file: {filepath}'.format(filepath = filepath))
            else:
                raise FileNotFoundError('No such file found: {filepath}'.format(filepath = filepath))

    return content

def main():
    try:
        from setuptools import setup
        args_setuptools = dict(
            keywords      = ', '.join([keyword for keyword in package.keywords])
        )
    except ImportError:
        from distutils.core import setup
        args_setuptools = dict()

    metadata = dict(
        name             = package.name,
        version          = package.version,
        description      = package.description,
        long_description = get_long_description(package.long_description),
        author           = ','.join([author['name'] for author in package.authors]),
        author_email     = ','.join([author['email'] for author in package.authors]),
        maintainer       = ','.join([maintainer['name'] for maintainer in package.maintainers]),
        maintainer_email = ','.join([maintainer['email'] for maintainer in package.maintainers]),
        license          = package.license,
        packages         = package.modules,
        url              = package.homepage,
        cmdclass         = {
            'clean': CleanCommand,
            'test': TestCommand
        },
        **args_setuptools
    )

    setup(**metadata)

if __name__ == '__main__':
    main()
