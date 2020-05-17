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


class MavenDependencyEncoder(object):
    def __init__(self):
        pass

    def encode(self, package):
        """
        Encodes the maven package object as maven dependency
        :param package: an instance of MavenPackage
        :return:
        """
        return '<dependency>' + \
               ('<groupId>%s</groupId>' % package.get_group()) + \
               ('<artifactId>%s</artifactId>' % package.get_artifact()) +\
               ('<version>%s</version>' % package.get_version()) + \
               ('<type>%s</type>' % package.get_packaging()) +\
               '</dependency>'


class MavenPom(object):
    """
    Builds a pom.xml and populates it with specified dependencies
    """
    def __init__(self, group_id, artifact_id):
        self.group_id_ = group_id
        self.artifact_id_ = artifact_id

    def build(self, packages):
        dependency_encoder = MavenDependencyEncoder()

        dependencies = []

        for package in packages:
            dependencies.append(dependency_encoder.encode(package))

        dependencies = '\n'.join(dependencies)

        template = '<project xmlns="http://maven.apache.org/POM/4.0.0"\n' \
                   '        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n' \
                   '        xsi:schemaLocation="http://maven.apache.org/POM/4.0.0\n' \
                   '                            http://maven.apache.org/xsd/maven-4.0.0.xsd">\n' \
                   '\n' \
                   '<modelVersion>4.0.0</modelVersion>\n' \
                   '\n' \
                   '<groupId>%s</groupId>\n' \
                   '<artifactId>%s</artifactId>\n' \
                   '<version>1.0</version>\n' \
                   '<packaging>pom</packaging>\n' \
                   '\n' \
                   '<name>POM Dependency Generator</name>\n' \
                   '<url>https://www.singularix.com</url>\n' \
                   '\n' \
                   '<dependencies>  \n' \
                   '%s\n' \
                   '</dependencies>\n' \
                   '<build><plugins>\n' \
                   '  <plugin>\n' \
                   '      <groupId>org.apache.felix</groupId>\n' \
                   '      <artifactId>maven-bundle-plugin</artifactId>\n' \
                   '      <version>2.4.0</version>\n' \
                   '      <extensions>true</extensions>\n' \
                   '  </plugin>\n' \
                   '</plugins></build>\n' \
                   '</project>'
        return template % (self.group_id_, self.artifact_id_, dependencies)
