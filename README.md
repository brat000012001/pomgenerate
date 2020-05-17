# Dependency POM Generator

The python script generates `pom.xml` that is used as input to the the maven dependency plugin
to download project dependencies to a local repository for off-line development (disconnected from the Internet),
in air-gapped development environments.

Project Object Model (POM) generator searches the Central Maven Repository for the packages
with the groupId and version matching the values specified as input, and generates
a `pom.xml` that lists the matching packages in the `<dependencies>` section.
```
Usage: pomgenerate.py [-h] -g GROUP -v VERSION --basedir BASEDIR

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
- Scan the Maven Central Repository for packages with groupId `org.keycloak` and version `8.0.2`,
  add generate pom.xml:
```
$ python src/pomgenerate.py -g org.keycloak -v 8.0.2 > pom.xml
```
- Download the dependency tree for offline development to a local repository using Maven dependency plugin:
```
(venv) $ mvn dependency:go-offline -Dmaven.repo.local=temp -U
```
