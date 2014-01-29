##
# Copyright 2009-2013 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# the Hercules foundation (http://www.herculesstichting.be/in_English)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
EasyBuild support for software that uses the ant build tool
i.e. 'ant all' implemented as an easyblock
"""

import easybuild.tools.environment as env
from easybuild.framework.easyblock import EasyBlock
from easybuild.framework.easyconfig import CUSTOM
from easybuild.tools.filetools import run_cmd


class Maven(EasyBlock):
    """
    Support for building and installing applications with ant install
    """
    @staticmethod
    def extra_options(extra_vars=None):
        """Extra easyconfig parameters specific to Java."""

        # using [] as default value is a bad idea, so we handle it this way
        if extra_vars == None:
            extra_vars = []

        extra_vars.extend([
                           ('repository', ['repository', 'Repository directory for JARs', CUSTOM]),
                           ( 'build_options', ['', "Custom build options.", CUSTOM]),
                          ])
        return EasyBlock.extra_options(extra_vars)


    def configure_step(self, cmd_prefix=''):
        """no op"""
        pass

    def build_step(self, java_version=None):
        """Custom build procedure for Maven."""
        pass

    def install_step(self):
        """no op"""
        cmd = 'mvn %(build_options)s -Dmaven.repo.local=%(localrepo)s install' % {
                'build_options': self.cfg['build_options'],
                'localrepo': '%s/%s' % (self.installdir, self.cfg["repository"])
                } 
        run_cmd(cmd, log_all=True, simple=True, log_output=True)


