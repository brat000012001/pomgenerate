#  Copyright (c) 2020 Peter Nalyvayko
#
#    This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#    This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.

from maven import RepositoryService
from maven import MavenPom
import argparse


def main(params):
    svc = RepositoryService('https://search.maven.org/solrsearch/select')

    packages = svc.search(params.group, params.version)

    pom = MavenPom('com.singularix', 'pom-generate')
    print(pom.build(packages))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-g',
                        '--group',
                        dest='group',
                        help='groupId to search for in the Maven Central Repository',
                        required=True)
    parser.add_argument('-v',
                        '--version',
                        dest='version',
                        help='version to search for in the Maven Central Repository',
                        required=True)

    main(parser.parse_args())
