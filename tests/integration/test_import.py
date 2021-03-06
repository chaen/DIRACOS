#!/usr/bin/env python
"""
Some imports to make sure that the DIRACOS environment is complete
"""

import os
import traceback
import warnings
import pytest

parametrize = pytest.mark.parametrize


# This list was obtained by checking all the imports in DIRAC v6r20
# Since the parsing was not precise, the list might not be exhaustive, but well...
# The starting point was these two searches
#  find . -name '*.py' -exec grep '^import ' {} \; | grep -v DIRAC | grep -v ' as ' |  sort -u
# find . -name '*.py' -exec grep '^from ' {} \; | grep -v DIRAC | awk
# {'print $2'} | sort -u | grep -v '\.'

# Notes that these scripts will make some false positive appear
# As of now, they are
# config
# diracdoctools
# diracdoctools.cmd
# dont_import_two
# local_stuff
# modules_in_one_line
# more_local_stuff
# some_third_party_lib
# some_third_party_other_lib


moduleNames = [
    'arc',
    'argparse',
    'array',
    'ast',
    'atexit',
    'backports.lzma',
    'base64',
    'BaseHTTPServer',
    'binascii',
    'builtins',
    'bz2',
    'calendar',
    'certifi',
    'cgi',
    'cmd',
    'collections',
    'commands',
    'contextlib',
    'copy',
    'cStringIO',
    'csv',
    'datetime',
    'difflib',
    'distutils.spawn',
    'elasticsearch',
    'elasticsearch_dsl',
    'errno',
    'fcntl',
    'filecmp',
    'fnmatch',
    'functools',
    '__future__',
    'getopt',
    'getpass',
    'gfal2',
    'git',
    'glob',
    'GSI',
    'gzip',
    'hashlib',
    'httplib',
    'hypothesis',
    'imp',
    'importlib',
    'inspect',
    'io',
    'itertools',
    'json',
    'ldap3',
    'logging',
    'lz4',
    'M2Crypto',
    'math',
    'matplotlib',
    'mock',
    'multiprocessing',
    'MySQLdb',
    'numpy',
    'operator',
    'optparse',
    'os',
    'os.path',
    'pickle',
    'pkgutil',
    'platform',
    'pprint',
    'psutil',
    'pwd',
    'pyasn1_modules',
    'pylab',
    'pyparsing',
    'pytest',
    'pytz',
    'pyxrootd.client',
    'Queue',
    'random',
    're',
    'readline',
    'requests',
    'resource',
    'select',
    'setuptools',
    'shlex',
    'shutil',
    'signal',
    'six',
    'smtplib',
    'socket',
    'SocketServer',
    'sqlalchemy',
    'sqlite3',
    'ssl',
    'stat',
    'stomp',
    'string',
    'StringIO',
    '_strptime',
    'struct',
    'subprocess',
    'subprocess32',
    'suds',
    'sys',
    'syslog',
    'tarfile',
    'tempfile',
    'textwrap',
    'thread',
    'threading',
    'time',
    'traceback',
    'types',
    'unittest',
    'uproot',
    'urllib',
    'urllib2',
    'urlparse',
    'xml.dom.minidom',
    'xml.sax',
    'xxhash',
    'zipfile',
    'zlib',
]

# List here the modules that are allowed to Fail.
# Ideally, this should always be empty...
ALLOWED_TO_FAIL = [ ]

# List of modules that need graphic libraries.
# When failing, these tests are just marked as skipped with a warning
GRAPHIC_MODULES = [
    'pylab',
]

diracosPath = os.environ['DIRACOS']


@parametrize('moduleName', moduleNames)
def test_module(moduleName):
  """ Try to import a module and check whether it is located in DIRACOS.

      Modules that are in the ALLOWED_TO_FAIL list are shown as skipped and generate a warning

      Modules that require graphic libraries on the system (GRAPHIC_MODULES) are skipped on container
  """

  try:
    module = __import__(moduleName)

    # Test whether it is correctly imported from DIRACOS

    try:
      modulePath = module.__file__
      # return true, if the common prefix of both is equal to directory
      # e.g. /a/b/c/d.rst and directory is /a/b, the common prefix is /a/b
      assert os.path.commonprefix([modulePath, diracosPath]) == diracosPath, \
          "ERROR %s not from DIRACOS: %s" % (moduleName, modulePath)

    # builtin modules like sys have no path
    except AttributeError as e:
      print "WARNING no path for %s" % moduleName

  except ImportError as e:
    msg = "could not import %s: %s" % (moduleName, repr(e))
    print traceback.print_exc()

    if moduleName in ALLOWED_TO_FAIL:
      warnings.warn(msg)
      pytest.skip("WARN: " + msg)
    elif moduleName in GRAPHIC_MODULES:
      warnings.warn(msg + "(Possibly due to system graphic libraries not present)")
      pytest.skip("WARN: " + msg + "(Possibly due to system graphic libraries not present)")
    else:
      pytest.fail("ERROR: " + msg)
