class MavenPackage(object):
    def __init__(self, json):
        self.json_ = json

    def __str__(self):
        return self.get_id()

    def get_id(self):
        """
        Package fully qualified identifier (e.g. org.keycloak:keycloak-services:8.0.2
        :return:
        """
        return self.json_['id']

    def get_group(self):
        """
        Package group id (e.g. org.keycloak)
        :return:
        """
        return self.json_['g']

    def get_artifact(self):
        """
        Package artifact id (e.g. keycloak-services)
        :return:
        """
        return self.json_['a']

    def get_version(self):
        """
        Package version (e.g. 8.0.2)
        :return:
        """
        return self.json_['v']

    def get_packaging(self):
        """
        Packaging type (e.g. jar, pom, etc)
        :return:
        """
        return self.json_['p']

    def get_ec(self):
        """
        File path extensions?
        :return:
        """
        return self.json_['ec']


class SearchResponse(object):
    def __init__(self, json):
        self.json_ = json

    def get_number_found(self):
        """
        Get a total number of rows found to match the criteria
        :return:
        """
        return self.json_['numFound']

    def get_start(self):
        """
        Get an index of the first row in the response
        :return:
        """
        return self.json_['start']

    def get_docs(self):
        for doc in self.json_['docs']:
            yield MavenPackage(doc)


class SearchResult(object):

    def __init__(self, json):
        self.json_ = json

    def get_header(self):
        return self.json_['responseHeader']

    def get_response(self):
        return SearchResponse(self.json_['response'])
