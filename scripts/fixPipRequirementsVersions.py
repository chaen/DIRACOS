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

  mockInstallConfig = cfg['mockInstallConfig']
  mockInstallRoot = cfg['mockInstallRoot']
  pipRequirements = cfg['pipRequirements']
  pipBuildDependencies = cfg['pipBuildDependencies']

  # No need to do it in mock if there are no build dependencies
  insideMock = bool(pipBuildDependencies)
  fixedVersionFile = diracoslib.fixPipRequirementsVersions(
      mockInstallConfig, mockInstallRoot, pipRequirements, pipBuildDependencies, insideMock=insideMock)
  print "Fixed version file in %s" % fixedVersionFile


if __name__ == '__main__':
  main()
