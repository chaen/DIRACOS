DIRACOS
=======

|pipeline status| |documentation status|

DIRACOS aims at bringing in one archive all the dependencies needed by
DIRAC to run Agents, Services and clients. It is not intended to perform
interactive tasks (debugging, file editing, etc). We are aware than some
“basic” tools won’t work (less, emacs, etc). They won’t be fixed.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   0_concepts
   10_RPMs
   20_pythonPackages
   30_generatingDIRACOS
   40_grammar
   50_troubleshoot
   60_useDIRACOS
   70_release
   80_extendingDIRACOS

Search
======

* :ref:`search`
  
Disclaimer
==========

DIRACOS is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. We are aiming at supporting SLC6 and
CC7, whilst we test also on other platforms we do not provide support
for those.

.. |pipeline status| image:: https://gitlab.cern.ch/CLICdp/iLCDirac/DIRACOS/badges/master/pipeline.svg
   :target: https://gitlab.cern.ch/CLICdp/iLCDirac/DIRACOS/pipelines

.. |documentation status| image:: https://readthedocs.org/projects/diracos/badge/?version=latest
   :target: https://diracos.readthedocs.io/
