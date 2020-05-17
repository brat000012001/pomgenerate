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

import requests
from .response import SearchResult


class RepositoryService(object):

    def __init__(self, solrsearch_url):
        self.solrsearch_url_ = solrsearch_url
        self.rows_per_page_ = 20

    def interpolate_path_(self, group_id, version_id, start, rows):
        return '%s?q=g:%s AND v:%s&start=%s&rows=%s' % (self.solrsearch_url_, group_id, version_id, start, rows)

    def search(self, group_id, version_id):

        # the first request is to get a total number of expected rows
        url = self.interpolate_path_(group_id, version_id, 0, 0)

        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(repr(response))

        sr = SearchResult(response.json())
        num_found = sr.get_response().get_number_found()

        total_pages = int(num_found / self.rows_per_page_)
        rem = num_found % self.rows_per_page_

        search_results = []
        for page_index in range(total_pages):

            url = self.interpolate_path_(group_id, version_id, page_index * self.rows_per_page_, self.rows_per_page_)
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception(repr(response))
            for doc in SearchResult(response.json()).get_response().get_docs():
                search_results.append(doc)

        if rem != 0:
            url = self.interpolate_path_(group_id, version_id, total_pages * self.rows_per_page_, rem)
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception(repr(response))
            for doc in SearchResult(response.json()).get_response().get_docs():
                search_results.append(doc)

        return search_results

