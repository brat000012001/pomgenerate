from maven import RepositoryService
from maven import MavenPom
import argparse


def main(params):

    svc = RepositoryService('https://search.maven.org/solrsearch/select')

    packages = svc.search(params.group, params.version)

    pom = MavenPom('org.company', 'pom-generate')
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
