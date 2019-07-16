#!/usr/bin/env python
import sys
import json
from diracos import Conf, diracoslib
import logging
import pprint


def main():
  logging.basicConfig(level=logging.DEBUG)
  jsonConf = sys.argv[1]

  cfg = Conf.load(jsonConf)

  extensionName = cfg['extensionName']
  diracOsVersion = cfg['diracOsVersion']
  diracOsExtVersion = cfg['version']
  pipRequirementFile = cfg['pipRequirements']

  diracosExtTar = diracoslib.buildDiracOSExtension(
      extensionName, diracOsVersion, diracOsExtVersion, pipRequirementFile)
  print "Tar file %s" % diracosExtTar


if __name__ == '__main__':
  main()
