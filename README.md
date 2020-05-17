# Dependency POM Generator

The tool searches the Central Maven Repository for packages matching specified groupId and version, 
and generates  `pom.xml` that can used to download the packages for off-line development. 

```
Usage: pomgenerate.py [-h] -g GROUP -v VERSION

optional arguments:
  -h, --help            show this help message and exit
  -g GROUP, --group GROUP
                        groupId to search for in the Maven Central
                        Repository
  -v VERSION, --version VERSION
                        version to search for in the Maven Central
                        Repository
```

# Usage Example

- Set up a virtual environment (Linux)
```
$ python3 -m venv venv
```
- Activate the virtual environment and install the dependencies
```
$ . venv/bin/activate
(venv) $ pip install -r requirements.txt
```
- Search the Maven Central Repository for packages with groupId `org.keycloak` and version `8.0.2`,
  add generate pom.xml:
```
$ python src/pomgenerate.py -g org.keycloak -v 8.0.2 > pom.xml
```
The output `pom.xml` looks likes this:
```
<project xmlns="http://maven.apache.org/POM/4.0.0"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                            http://maven.apache.org/xsd/maven-4.0.0.xsd">

<modelVersion>4.0.0</modelVersion>

<groupId>org.company</groupId>
<artifactId>pom-generate</artifactId>
<version>1.0</version>
<packaging>pom</packaging>

<name>Maven Quick Start Archetype</name>
<url>http://maven.apache.org</url>

<dependencies>  
  <dependency><groupId>org.keycloak</groupId><artifactId>keycloak-client-cli-parent</artifactId><version>8.0.2</version><type>pom</type></dependency>
  <dependency><groupId>org.keycloak</groupId><artifactId>keycloak-server-spi</artifactId><version>8.0.2</version><type>jar</type></dependency>
  <dependency><groupId>org.keycloak</groupId><artifactId>keycloak-wildfly-subsystem</artifactId><version>8.0.2</version><type>jar</type></dependency>
  <dependency><groupId>org.keycloak</groupId><artifactId>keycloak-services</artifactId><version>8.0.2</version><type>jar</type></dependency>
  ...
</dependencies>
<build><plugins>
  <plugin>
      <groupId>org.apache.felix</groupId>
      <artifactId>maven-bundle-plugin</artifactId>
      <version>2.4.0</version>
      <extensions>true</extensions>
  </plugin>
</plugins></build>
</project>

```

- Download the dependency tree for offline development to a local repository using Maven dependency plugin:
```
(venv) $ mvn dependency:go-offline -Dmaven.repo.local=temp -U
```
The dependencies are copied  to `./temp` directory; the directory tree should look like this:
```
/antlr
/asm
/biz
...
/org
    /keycloak
        /bom
        /keycloak-core
            /8.0.2
                keycloak-core-8.0.2.jar
                keycloak-core-8.0.2.jar.sha1
                keycloak-core-8.0.2.pom
                ...
```