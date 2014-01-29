##
# Copyright 2012-2014 Ghent University
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
EasyBlock for installing Hadoop, implemented as an easyblock
"""
import shutil
from easybuild.easyblocks.generic.maven import Maven


class EB_Hadoop(Maven):
    """Support for installing Java as a packed binary file (.tar.gz)
    Use the PackedBinary easyblock and set some extra paths.
    """

    def install_step(self):
        """Perform the normal Maven install and then copy the binary and lib files into place."""
        Maven.install_step(self) # Commented out to speed up testing.

        for d in ['bin', 'bin-mapreduce1', 'cloudera', 'etc', 'examples', 
                'examples-mapreduce1', 'include', 'lib', 'libexec', 'sbin', 'share']:
            shutil.copytree("../%s" % d, '%s/%s' % (self.installdir, d))
