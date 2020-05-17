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


class MavenInstallDependencyPluginEncoder(object):
    """ Not currently used.
    """
    def __init__(self, base_dir):
        self.base_dir_ = base_dir
        pass

    def encode(self, package):
        """
           ' <plugin>\n' \
           '   <groupId>org.apache.maven.plugins</groupId>\n' \
           '   <artifactId>maven-install-plugin</artifactId>\n' \
           '   <version>2.5.1</version>\n' \
           '   <executions>\n' \
           '     %s\n' \
           '   </executions>\n' \
           ' </plugin>\n' \

        :param package:
        :return:
        """
        if package.get_packaging() != "jar":
            return ""

        return '      <execution>\n' \
               '         <id>install-%s</id>\n' \
               '         <goals>\n' \
               '            <goal>install-file</goal>\n' \
               '         </goals>\n' \
               '         <phase>package</phase>\n' \
               '         <configuration>\n' \
               '            <groupId>%s</groupId>\n' \
               '            <artifactId>%s</artifactId>\n' \
               '            <version>%s</version>\n' \
               '            <packaging>%s</packaging>\n' \
               '            <file>%s</file>\n' \
               '            <generatePom>true</generatePom>\n' \
               '         </configuration>\n' \
               '      </execution>\n' % (
                                package.get_id(),
                                package.get_group(),
                                package.get_artifact(),
                                package.get_version(),
                                package.get_packaging(),
                                '%s/%s-%s.%s' % (self.base_dir_, package.get_artifact(), package.get_version(), package.get_packaging()))


class MavenPom(object):
    """
    Creates pom.xml using the specified dependencies
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
                   '<name>Maven Quick Start Archetype</name>\n' \
                   '<url>http://maven.apache.org</url>\n' \
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
