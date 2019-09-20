# vim: set ts=4 sw=4 et: coding=UTF-8

#
# Copyright (c) 2008-2009, Novell, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#  * Neither the name of the <ORGANIZATION> nor the names of its contributors
#    may be used to endorse or promote products derived from this software
#    without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
#
# (Licensed under the simplified BSD license)
#
# Authors: Vincent Untz <vuntz@opensuse.org>
#

import difflib
import locale
import re
import select
import shutil
import subprocess
import tarfile
import tempfile
import time
import urllib

try:
    import configparser
    from http.client import BadStatusLine
    from urllib.error import HTTPError
    from urllib.parse import quote, urlparse
    from urllib.request import urlopen
except ImportError:
    # python 2.x
    import ConfigParser
    from httplib import BadStatusLine
    from urllib import quote
    from urllib2 import HTTPError, urlopen
    from urlparse import urlparse

try:
    import rpm
    have_rpm = True
except ImportError:
    have_rpm = False

from osc import cmdln
from osc import conf


OSC_COLLAB_VERSION = '0.102'

# This is a hack to have osc ignore the file we create in a package directory.
_osc_collab_helper_prefixes = [ 'osc-collab.', 'osc-gnome.' ]
_osc_collab_helpers = []
for suffix in [ 'NEWS', 'ChangeLog', 'configure', 'meson', 'meson_options' ]:
    for prefix in _osc_collab_helper_prefixes:
        _osc_collab_helpers.append(prefix + suffix)
for helper in _osc_collab_helpers:
    conf.DEFAULTS['exclude_glob'] += ' %s' % helper

_osc_collab_alias = 'collab'
_osc_collab_config_parser = None
_osc_collab_osc_conffile = None


class OscCollabError(Exception):
    def __init__(self, value):
        self.msg = value

    def __str__(self):
        return repr(self.msg)


class OscCollabWebError(OscCollabError):
    pass

class OscCollabDownloadError(OscCollabError):
    pass

class OscCollabDiffError(OscCollabError):
    pass

class OscCollabCompressError(OscCollabError):
    pass


def _collab_exception_print(e, message = ''):
    if message == None:
        message = ''

    if hasattr(e, 'msg'):
        print(message + e.msg, file=sys.stderr)
    elif str(e) != '':
        print(message + str(e), file=sys.stderr)
    else:
        print(message + e.__class__.__name__, file=sys.stderr)


#######################################################################


class OscCollabReservation:

    project = None
    package = None
    user = None

    def __init__(self, project = None, package = None, user = None, node = None):
        if node is None:
            self.project = project
            self.package = package
            self.user = user
        else:
            self.project = node.get('project')
            self.package = node.get('package')
            self.user = node.get('user')


    def __len__(self):
        return 3


    def __getitem__(self, key):
        if not type(key) == int:
            raise TypeError

        if key == 0:
            return self.project
        elif key == 1:
            return self.package
        elif key == 2:
            return self.user
        else:
            raise IndexError


    def is_relevant(self, projects, package):
        if self.project not in projects:
            return False
        if self.package != package:
            return False
        return True


#######################################################################


class OscCollabComment:

    project = None
    package = None
    user = None
    comment = None
    firstline = None

    def __init__(self, project = None, package = None, date = None, user = None, comment = None, node = None):
        if node is None:
            self.project = project
            self.package = package
            self.date = date
            self.user = user
            self.comment = comment
        else:
            self.project = node.get('project')
            self.package = node.get('package')
            self.date = node.get('date')
            self.user = node.get('user')
            self.comment = node.text
        if self.comment is None:
            self.firstline = None
        else:
            lines = self.comment.split('\n')
            self.firstline = lines[0]
            if len(lines) > 1:
                self.firstline += ' [...]'


    def __len__(self):
        return 4


    def __getitem__(self, key):
        if not type(key) == int:
            raise TypeError

        if key == 0:
            return self.project
        elif key == 1:
            return self.package
        elif key == 2:
            return self.user
        elif key == 3:
            return self.firstline
        else:
            raise IndexError


    def is_relevant(self, projects, package):
        if self.project not in projects:
            return False
        if self.package != package:
            return False
        return True


    def indent(self, spaces = '  '):
        lines = self.comment.split('\n')
        lines = [ spaces + line for line in lines ]
        return '\n'.join(lines)


#######################################################################


class OscCollabRequest():

    req_id = -1
    type = None
    source_project = None
    source_package = None
    source_rev = None
    dest_project = None
    dest_package = None
    state = None
    by = None
    at = None
    description = None

    def __init__(self, node):
        self.req_id = int(node.get('id'))

        # we only care about the first action here
        action = node.find('action')
        if action is None:
            action = node.find('submit') # for old style requests

        type = action.get('type', 'submit')

        subnode = action.find('source')
        if subnode is not None:
            self.source_project = subnode.get('project')
            self.source_package = subnode.get('package')
            self.source_rev = subnode.get('rev')

        subnode = action.find('target')
        if subnode is not None:
            self.target_project = subnode.get('project')
            self.target_package = subnode.get('package')

        subnode = node.find('state')
        if subnode is not None:
            self.state = subnode.get('name')
            self.by = subnode.get('who')
            self.at = subnode.get('when')

        subnode = node.find('description')
        if subnode is not None:
            self.description = subnode.text


#######################################################################


class OscCollabProject(dict):

    def __init__(self, node):
        self.name = node.get('name')
        self.parent = node.get('parent')
        self.ignore_upstream = node.get('ignore_upstream') == 'true'
        self.missing_packages = []


    def strip_internal_links(self):
        to_rm = []
        for package in self.values():
            if package.parent_project == self.name:
                to_rm.append(package.name)
        for name in to_rm:
            del self[name]


    def is_toplevel(self):
        return self.parent in [ None, '' ]


    def __eq__(self, other):
        return self.name == other.name


    def __ne__(self, other):
        return not self.__eq__(other)


    def __lt__(self, other):
        return self.name < other.name


    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)


    def __gt__(self, other):
        return other.__lt__(self)


    def __ge__(self, other):
        return other.__eq__(self) or other.__lt__(self)


#######################################################################


class OscCollabPackage:

    def __init__(self, node, project):
        self.name = None
        self.version = None
        self.parent_project = None
        self.parent_package = None
        self.parent_version = None
        self.devel_project = None
        self.devel_package = None
        self.devel_version = None
        self.upstream_version = None
        self.upstream_url = None
        self.is_link = False
        self.has_delta = False
        self.error = None
        self.error_details = None

        self.project = project

        if node is not None:
            self.name = node.get('name')

            parent = node.find('parent')
            if parent is not None:
                self.parent_project = parent.get('project')
                self.parent_package = parent.get('package')

            devel = node.find('devel')
            if devel is not None:
                self.devel_project = devel.get('project')
                self.devel_package = devel.get('package')

            version = node.find('version')
            if version is not None:
                self.version = version.get('current')
                if not project or not project.ignore_upstream:
                    self.upstream_version = version.get('upstream')
                self.parent_version = version.get('parent')
                self.devel_version = version.get('devel')

            if not project or not project.ignore_upstream:
                upstream = node.find('upstream')
                if upstream is not None:
                    url = upstream.find('url')
                    if url is not None:
                        self.upstream_url = url.text

            link = node.find('link')
            if link is not None:
                self.is_link = True
                if link.get('delta') == 'true':
                    self.has_delta = True

            delta = node.find('delta')
            if delta is not None:
                self.has_delta = True

            error = node.find('error')
            if error is not None:
                self.error = error.get('type')
                self.error_details = error.text

        # Reconstruct some data that we can deduce from the XML
        if project is not None and self.is_link and not self.parent_project:
            self.parent_project = project.parent
        if self.parent_project and not self.parent_package:
            self.parent_package = self.name
        if self.devel_project and not self.devel_package:
            self.devel_package = self.name


    def _compare_versions_a_gt_b(self, a, b):
        if have_rpm:
            # We're not really interested in the epoch or release parts of the
            # complete version because they're not relevant when comparing to
            # upstream version
            return rpm.labelCompare((None, a, '1'), (None, b, '1')) > 0

        split_a = a.split('.')
        split_b = b.split('.')

        # the two versions don't have the same format; we don't know how to
        # handle this
        if len(split_a) != len(split_b):
            return a > b

        for i in range(len(split_a)):
            try:
                int_a = int(split_a[i])
                int_b = int(split_b[i])
                if int_a > int_b:
                    return True
                if int_b > int_a:
                    return False
            except ValueError:
                if split_a[i] > split_b[i]:
                    return True
                if split_b[i] > split_a[i]:
                    return False

        return False


    def parent_more_recent(self):
        if not self.parent_version:
            return False

        return self._compare_versions_a_gt_b(self.parent_version, self.version)


    def needs_update(self):
        # empty upstream version, or upstream version meaning openSUSE is
        # upstream
        if self.upstream_version in [ None, '', '--' ]:
            return False

        return self._compare_versions_a_gt_b(self.upstream_version, self.parent_version) and self._compare_versions_a_gt_b(self.upstream_version, self.version)


    def devel_needs_update(self):
        # if there's no devel project, then it's as if it were needing an update
        if not self.devel_project:
            return True

        # empty upstream version, or upstream version meaning openSUSE is
        # upstream
        if self.upstream_version in [ None, '', '--' ]:
            return False

        return self._compare_versions_a_gt_b(self.upstream_version, self.devel_version)


    def is_broken_link(self):
        return self.error in [ 'not-in-parent', 'need-merge-with-parent' ]


    def __eq__(self, other):
        return self.name == other.name and self.project and other.project and self.project.name == other.project.name


    def __ne__(self, other):
        return not self.__eq__(other)


    def __lt__(self, other):
        if not self.project or not self.project.name:
            if other.project and other.project.name:
                return True
            else:
                return self.name < other.name

        if self.project.name == other.project.name:
            return self.name < other.name

        return self.project.name < other.project.name


    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)


    def __gt__(self, other):
        return other.__lt__(self)


    def __ge__(self, other):
        return other.__eq__(self) or other.__lt__(self)


#######################################################################


class OscCollabObs:

    apiurl = None


    @classmethod
    def init(cls, apiurl):
        cls.apiurl = apiurl


    @classmethod
    def get_meta(cls, project):
        what = 'metadata of packages in %s' % project

        # download the data (cache for 2 days)
        url = makeurl(cls.apiurl, ['search', 'package'], ['match=%s' % quote('@project=\'%s\'' % project)])
        filename = '%s-meta.obs' % project
        max_age_minutes = 3600 * 24 * 2

        return OscCollabCache.get_from_obs(url, filename, max_age_minutes, what)


    @classmethod
    def get_build_results(cls, project):
        what = 'build results of packages in %s' % project

        # download the data (cache for 2 hours)
        url = makeurl(cls.apiurl, ['build', project, '_result'])
        filename = '%s-build-results.obs' % project
        max_age_minutes = 3600 * 2

        return OscCollabCache.get_from_obs(url, filename, max_age_minutes, what)


    @classmethod
    def _get_request_list_url(cls, project, package, type, what):
        match = '(state/@name=\'new\'%20or%20state/@name=\'review\')'
        match += '%20and%20'
        match += 'action/%s/@project=\'%s\'' % (type, quote(project))
        if package:
            match += '%20and%20'
            match += 'action/%s/@package=\'%s\'' % (type, quote(package))

        return makeurl(cls.apiurl, ['search', 'request'], ['match=%s' % match])


    @classmethod
    def _parse_request_list_internal(cls, f, what):
        requests = []

        try:
            collection = ET.parse(f).getroot()
        except SyntaxError as e:
            print('Cannot parse %s: %s' % (what, e.msg), file=sys.stderr)
            return requests

        for node in collection.findall('request'):
            requests.append(OscCollabRequest(node))

        return requests


    @classmethod
    def _get_request_list_no_cache(cls, project, package, type, what):
        url = cls._get_request_list_url(project, package, type, what)

        try:
            fin = http_GET(url)
        except HTTPError as e:
            print('Cannot get %s: %s' % (what, e.msg), file=sys.stderr)
            return []

        requests = cls._parse_request_list_internal(fin, what)

        fin.close()

        return requests


    @classmethod
    def _get_request_list_with_cache(cls, project, package, type, what):
        url = cls._get_request_list_url(project, package, type, what)
        if url is None:
            return []

        # download the data (cache for 10 minutes)
        if package:
            filename = '%s-%s-requests-%s.obs' % (project, package, type)
        else:
            filename = '%s-requests-%s.obs' % (project, type)
        max_age_minutes = 60 * 10

        file = OscCollabCache.get_from_obs(url, filename, max_age_minutes, what)

        if not file or not os.path.exists(file):
            return []

        return cls._parse_request_list_internal(file, what)


    @classmethod
    def _get_request_list(cls, project, package, type, use_cache):
        if package:
            what_helper = '%s/%s' % (project, package)
        else:
            what_helper = project
        if type == 'source':
            what = 'list of requests from %s' % what_helper
        elif type == 'target':
            what = 'list of requests to %s' % what_helper
        else:
            print('Internal error when getting request list: unknown type \"%s\".' % type, file=sys.stderr)
            return None

        if use_cache:
            return cls._get_request_list_with_cache(project, package, type, what)
        else:
            return cls._get_request_list_no_cache(project, package, type, what)


    @classmethod
    def get_request_list_from(cls, project, package=None, use_cache=True):
        return cls._get_request_list(project, package, 'source', use_cache)


    @classmethod
    def get_request_list_to(cls, project, package=None, use_cache=True):
        return cls._get_request_list(project, package, 'target', use_cache)


    @classmethod
    def get_request(cls, id):
        url = makeurl(cls.apiurl, ['request', id])

        try:
            fin = http_GET(url)
        except HTTPError as e:
            print('Cannot get request %s: %s' % (id, e.msg), file=sys.stderr)
            return None

        try:
            node = ET.parse(fin).getroot()
        except SyntaxError as e:
            fin.close()
            print('Cannot parse request %s: %s' % (id, e.msg), file=sys.stderr)
            return None

        fin.close()

        return OscCollabRequest(node)


    @classmethod
    def change_request_state(cls, id, new_state, message, superseded_by=None):
        if new_state != 'superseded':
            result = change_request_state(cls.apiurl, id, new_state, message)
        else:
            result = change_request_state(cls.apiurl, id, new_state, message, supersed=superseded_by)

        return result == 'ok'


    @classmethod
    def supersede_old_requests(cls, user, project, package, new_request_id):
        requests_to = cls.get_request_list_to(project, package, use_cache=False)
        old_ids = [ request.req_id for request in requests_to if request.by == user and str(request.req_id) != new_request_id ]
        for old_id in old_ids:
            cls.change_request_state(str(old_id), 'superseded', 'superseded by %s' % new_request_id, superseded_by=new_request_id)
        return old_ids


    @classmethod
    def branch_package(cls, project, package, no_devel_project = False):
        query = { 'cmd': 'branch' }
        if no_devel_project:
            query['ignoredevel'] = '1'

        url = makeurl(cls.apiurl, ['source', project, package], query = query)

        try:
            fin = http_POST(url)
        except HTTPError as e:
            print('Cannot branch package %s: %s' % (package, e.msg), file=sys.stderr)
            return (None, None)

        try:
            node = ET.parse(fin).getroot()
        except SyntaxError as e:
            fin.close()
            print('Cannot branch package %s: %s' % (package, e.msg), file=sys.stderr)
            return (None, None)

        fin.close()

        branch_project = None
        branch_package = None

        for data in node.findall('data'):
            name = data.get('name')
            if not name:
                continue
            if name == 'targetproject' and data.text:
                branch_project = data.text
            elif name == 'targetpackage' and data.text:
                branch_package = data.text

        return (branch_project, branch_package)


#######################################################################


class OscCollabApi:

    _api_url = 'https://osc-collab.opensuse.org/api'
    _supported_api = '0.2'
    _supported_api_major = '0'

    @classmethod
    def init(cls, apiurl = None):
        if apiurl:
            cls._api_url = apiurl


    @classmethod
    def _append_data_to_url(cls, url, data):
        if url.find('?') != -1:
            return '%s&%s' % (url, data)
        else:
            return '%s?%s' % (url, data)


    @classmethod
    def _get_api_url_for(cls, api, project = None, projects = None, package = None, need_package_for_multiple_projects = True):
        if not project and len(projects) == 1:
            project = projects[0]

        items = [ cls._api_url, api ]
        if project:
            items.append(project)
        if package:
            items.append(package)
        url = '/'.join(items)

        if not project and (not need_package_for_multiple_projects or package) and projects:
            data = urlencode({'version': cls._supported_api, 'project': projects}, True)
            url = cls._append_data_to_url(url, data)
        else:
            data = urlencode({'version': cls._supported_api})
            url = cls._append_data_to_url(url, data)

        return url


    @classmethod
    def _get_info_url(cls, project = None, projects = None, package = None):
        return cls._get_api_url_for('info', project, projects, package, True)


    @classmethod
    def _get_reserve_url(cls, project = None, projects = None, package = None):
        return cls._get_api_url_for('reserve', project, projects, package, False)


    @classmethod
    def _get_comment_url(cls, project = None, projects = None, package = None):
        return cls._get_api_url_for('comment', project, projects, package, False)


    @classmethod
    def _get_root_for_url(cls, url, error_prefix, post_data = None, cache_file = None, cache_age = 10):
        if post_data and type(post_data) != dict:
            raise OscCollabWebError('%s: Internal error when posting data' % error_prefix)

        try:
            if cache_file and not post_data:
                fd = OscCollabCache.get_url_fd_with_cache(url, cache_file, cache_age)
            else:
                if post_data:
                    data = urlencode(post_data).encode('utf-8')
                else:
                    data = None
                fd = urlopen(url, data)
        except HTTPError as e:
            raise OscCollabWebError('%s: %s' % (error_prefix, e.msg))

        try:
            root = ET.parse(fd).getroot()
        except SyntaxError:
            raise OscCollabWebError('%s: malformed reply from server.' % error_prefix)

        if root.tag != 'api' or not root.get('version'):
            raise OscCollabWebError('%s: invalid reply from server.' % error_prefix)

        version = root.get('version')
        version_items = version.split('.')
        for item in version_items:
            try:
                int(item)
            except ValueError:
                raise OscCollabWebError('%s: unknown protocol used by server.' % error_prefix)
        protocol = int(version_items[0])
        if int(version_items[0]) != int(cls._supported_api_major):
            raise OscCollabWebError('%s: unknown protocol used by server.' % error_prefix)

        result = root.find('result')
        if result is None or not result.get('ok'):
            raise OscCollabWebError('%s: reply from server with no result summary.' % error_prefix)

        if result.get('ok') != 'true':
            if result.text:
                raise OscCollabWebError('%s: %s' % (error_prefix, result.text))
            else:
                raise OscCollabWebError('%s: unknown error in the request.' % error_prefix)

        return root


    @classmethod
    def _meta_append_no_devel_project(cls, url, no_devel_project):
        if not no_devel_project:
            return url

        data = urlencode({'ignoredevel': 'true'})
        return cls._append_data_to_url(url, data)


    @classmethod
    def _parse_reservation_node(cls, node):
        reservation = OscCollabReservation(node = node)
        if not reservation.project or not reservation.package:
            return None

        return reservation


    @classmethod
    def get_reserved_packages(cls, projects):
        url = cls._get_reserve_url(projects = projects)
        root = cls._get_root_for_url(url, 'Cannot get list of reserved packages')

        reserved_packages = []
        for reservation in root.findall('reservation'):
            item = cls._parse_reservation_node(reservation)
            if item is None or not item.user:
                continue
            reserved_packages.append(item)

        return reserved_packages


    @classmethod
    def is_package_reserved(cls, projects, package, no_devel_project = False):
        '''
            Only returns something if the package is really reserved.
        '''
        url = cls._get_reserve_url(projects = projects, package = package)
        url = cls._meta_append_no_devel_project(url, no_devel_project)
        root = cls._get_root_for_url(url, 'Cannot look if package %s is reserved' % package)

        for reservation in root.findall('reservation'):
            item = cls._parse_reservation_node(reservation)
            if item is None or (no_devel_project and not item.is_relevant(projects, package)):
                continue
            if not item.user:
                # We continue to make sure there are no other relevant entries
                continue
            return item

        return None


    @classmethod
    def reserve_package(cls, projects, package, username, no_devel_project = False):
        url = cls._get_reserve_url(projects = projects, package = package)
        data = urlencode({'cmd': 'set', 'user': username})
        url = cls._append_data_to_url(url, data)
        url = cls._meta_append_no_devel_project(url, no_devel_project)
        root = cls._get_root_for_url(url, 'Cannot reserve package %s' % package)

        for reservation in root.findall('reservation'):
            item = cls._parse_reservation_node(reservation)
            if not item or (no_devel_project and not item.is_relevant(projects, package)):
                continue
            if not item.user:
                raise OscCollabWebError('Cannot reserve package %s: unknown error' % package)
            if item.user != username:
                raise OscCollabWebError('Cannot reserve package %s: already reserved by %s' % (package, item.user))
            return item


    @classmethod
    def unreserve_package(cls, projects, package, username, no_devel_project = False):
        url = cls._get_reserve_url(projects = projects, package = package)
        data = urlencode({'cmd': 'unset', 'user': username})
        url = cls._append_data_to_url(url, data)
        url = cls._meta_append_no_devel_project(url, no_devel_project)
        root = cls._get_root_for_url(url, 'Cannot unreserve package %s' % package)

        for reservation in root.findall('reservation'):
            item = cls._parse_reservation_node(reservation)
            if not item or (no_devel_project and not item.is_relevant(projects, package)):
                continue
            if item.user:
                raise OscCollabWebError('Cannot unreserve package %s: reserved by %s' % (package, item.user))
            return item


    @classmethod
    def _parse_comment_node(cls, node):
        comment = OscCollabComment(node = node)
        if not comment.project or not comment.package:
            return None

        return comment


    @classmethod
    def get_commented_packages(cls, projects):
        url = cls._get_comment_url(projects = projects)
        root = cls._get_root_for_url(url, 'Cannot get list of commented packages')

        commented_packages = []
        for comment in root.findall('comment'):
            item = cls._parse_comment_node(comment)
            if item is None or not item.user or not item.comment:
                continue
            commented_packages.append(item)

        return commented_packages


    @classmethod
    def get_package_comment(cls, projects, package, no_devel_project = False):
        '''
            Only returns something if the package is really commented.
        '''
        url = cls._get_comment_url(projects = projects, package = package)
        url = cls._meta_append_no_devel_project(url, no_devel_project)
        root = cls._get_root_for_url(url, 'Cannot look if package %s is commented' % package)

        for comment in root.findall('comment'):
            item = cls._parse_comment_node(comment)
            if item is None or (no_devel_project and not item.is_relevant(projects, package)):
                continue
            if not item.user or not item.comment:
                # We continue to make sure there are no other relevant entries
                continue
            return item

        return None


    @classmethod
    def set_package_comment(cls, projects, package, username, comment, no_devel_project = False):
        if not comment:
            raise OscCollabWebError('Cannot set comment on package %s: empty comment' % package)

        url = cls._get_comment_url(projects = projects, package = package)
        data = urlencode({'cmd': 'set', 'user': username})
        url = cls._append_data_to_url(url, data)
        url = cls._meta_append_no_devel_project(url, no_devel_project)
        root = cls._get_root_for_url(url, 'Cannot set comment on package %s' % package, post_data = {'comment': comment})

        for comment in root.findall('comment'):
            item = cls._parse_comment_node(comment)
            if not item or (no_devel_project and not item.is_relevant(projects, package)):
                continue
            if not item.user:
                raise OscCollabWebError('Cannot set comment on package %s: unknown error' % package)
            if item.user != username:
                raise OscCollabWebError('Cannot set comment on package %s: already commented by %s' % (package, item.user))
            return item


    @classmethod
    def unset_package_comment(cls, projects, package, username, no_devel_project = False):
        url = cls._get_comment_url(projects = projects, package = package)
        data = urlencode({'cmd': 'unset', 'user': username})
        url = cls._append_data_to_url(url, data)
        url = cls._meta_append_no_devel_project(url, no_devel_project)
        root = cls._get_root_for_url(url, 'Cannot unset comment on package %s' % package)

        for comment in root.findall('comment'):
            item = cls._parse_comment_node(comment)
            if not item or (no_devel_project and not item.is_relevant(projects, package)):
                continue
            if item.user:
                raise OscCollabWebError('Cannot unset comment on package %s: commented by %s' % (package, item.user))
            return item


    @classmethod
    def _parse_package_node(cls, node, project):
        package = OscCollabPackage(node, project)
        if not package.name:
            return None

        if project is not None:
            project[package.name] = package

        return package


    @classmethod
    def _parse_missing_package_node(cls, node, project):
        name = node.get('name')
        parent_project = node.get('parent_project')
        parent_package = node.get('parent_package') or name

        if not name or not parent_project:
            return

        project.missing_packages.append((name, parent_project, parent_package))


    @classmethod
    def _parse_project_node(cls, node):
        project = OscCollabProject(node)
        if not project.name:
            return None

        for package in node.findall('package'):
            cls._parse_package_node(package, project)

        missing = node.find('missing')
        if missing is not None:
            for package in missing.findall('package'):
                cls._parse_missing_package_node(package, project)

        return project


    @classmethod
    def get_project_details(cls, project):
        url = cls._get_info_url(project = project)
        root = cls._get_root_for_url(url, 'Cannot get information of project %s' % project, cache_file = project + '.xml')

        for node in root.findall('project'):
            item = cls._parse_project_node(node)
            if item is None or item.name != project:
                continue
            return item

        return None


    @classmethod
    def get_package_details(cls, projects, package):
        url = cls._get_info_url(projects = projects, package = package)
        root = cls._get_root_for_url(url, 'Cannot get information of package %s' % package)

        for node in root.findall('project'):
            item = cls._parse_project_node(node)
            if item is None or item.name not in projects:
                continue

            pkgitem = item[package]
            if pkgitem:
                return pkgitem

        return None


#######################################################################


class OscCollabCache:

    _cache_dir = None
    _ignore_cache = False
    _printed = False

    @classmethod
    def init(cls, ignore_cache):
        cls._ignore_cache = ignore_cache
        cls._cleanup_old_cache()


    @classmethod
    def _print_message(cls):
        if not cls._printed:
            cls._printed = True
            print('Downloading data in a cache. It might take a few seconds...')


    @classmethod
    def _get_xdg_cache_home(cls):
        dir = None
        if 'XDG_CACHE_HOME' in os.environ:
            dir = os.environ['XDG_CACHE_HOME']
            if dir == '':
                dir = None

        if not dir:
            dir = '~/.cache'

        return os.path.expanduser(dir)


    @classmethod
    def _get_xdg_cache_dir(cls):
        if not cls._cache_dir:
            cls._cache_dir = os.path.join(cls._get_xdg_cache_home(), 'osc', 'collab')

        return cls._cache_dir


    @classmethod
    def _cleanup_old_cache(cls):
        '''
            Remove old cache files, when they're old (and therefore obsolete
            anyway).
        '''
        gnome_cache_dir = os.path.join(cls._get_xdg_cache_home(), 'osc', 'gnome')
        if os.path.exists(gnome_cache_dir):
            shutil.rmtree(gnome_cache_dir)

        cache_dir = cls._get_xdg_cache_dir()
        if not os.path.exists(cache_dir):
            return

        for file in os.listdir(cache_dir):
            # remove if it's more than 5 days old
            if cls._need_update(file, 60 * 60 * 24 * 5):
                cache = os.path.join(cache_dir, file)
                os.unlink(cache)


    @classmethod
    def _need_update(cls, filename, maxage):
        if cls._ignore_cache:
            return True

        cache = os.path.join(cls._get_xdg_cache_dir(), filename)

        if not os.path.exists(cache):
            return True

        if not os.path.isfile(cache):
            return True

        stats = os.stat(cache)

        now = time.time()
        if now - stats.st_mtime > maxage:
            return True
        # Back to the future?
        elif now < stats.st_mtime:
            return True

        return False


    @classmethod
    def get_url_fd_with_cache(cls, url, filename, max_age_minutes):
        if cls._need_update(filename, max_age_minutes * 60):
            # no cache available
            cls._print_message()
            fd = urlopen(url)
            cls._write(filename, fin = fd)

        return open(os.path.join(cls._get_xdg_cache_dir(), filename))


    @classmethod
    def get_from_obs(cls, url, filename, max_age_minutes, what):
        cache = os.path.join(cls._get_xdg_cache_dir(), filename)

        if not cls._need_update(cache, max_age_minutes):
            return cache

        # no cache available
        cls._print_message()

        try:
            fin = http_GET(url)
        except HTTPError as e:
            print('Cannot get %s: %s' % (what, e.msg), file=sys.stderr)
            return None

        fout = open(cache, 'w')

        while True:
            try:
                bytes = fin.read(500 * 1024)
                if len(bytes) == 0:
                    break
                fout.write(bytes.decode('utf-8'))
            except HTTPError as e:
                fin.close()
                fout.close()
                os.unlink(cache)
                print('Error while downloading %s: %s' % (what, e.msg), file=sys.stderr)
                return None

        fin.close()
        fout.close()

        return cache


    @classmethod
    def _write(cls, filename, fin = None):
        if not fin:
            print('Internal error when saving a cache: no data.', file=sys.stderr)
            return False

        cachedir = cls._get_xdg_cache_dir()
        if not os.path.exists(cachedir):
            os.makedirs(cachedir)

        if not os.path.isdir(cachedir):
            print('Cache directory %s is not a directory.' % cachedir, file=sys.stderr)
            return False

        cache = os.path.join(cachedir, filename)
        if os.path.exists(cache):
            os.unlink(cache)
        fout = open(cache, 'w')

        if fin:
            while True:
                try:
                    bytes = fin.read(500 * 1024)
                    if len(bytes) == 0:
                        break
                    fout.write(bytes.decode('utf-8'))
                except HTTPError as e:
                    fout.close()
                    os.unlink(cache)
                    raise e
            fout.close()
            return True


#######################################################################


def _collab_is_program_in_path(program):
    if not 'PATH' in os.environ:
        return False

    for path in os.environ['PATH'].split(':'):
        if os.path.exists(os.path.join(path, program)):
            return True

    return False


#######################################################################


def _collab_find_request_to(package, requests):
    for request in requests:
        if request.target_package == package:
            return request
    return None


def _collab_has_request_from(package, requests):
    for request in requests:
        if request.source_package == package:
            return True
    return False


#######################################################################


def _collab_table_get_maxs(init, list):
    if len(list) == 0:
        return ()

    nb_maxs = len(init)
    maxs = []
    for i in range(nb_maxs):
        maxs.append(len(init[i]))

    for item in list:
        for i in range(nb_maxs):
            maxs[i] = max(maxs[i], len(item[i]))

    return tuple(maxs)


def _collab_table_get_template(*args):
    if len(args) == 0:
        return ''

    template = '%%-%d.%ds' % (args[0], args[0])
    index = 1

    while index < len(args):
        template = template + (' | %%-%d.%ds' % (args[index], args[index]))
        index = index + 1

    return template


def _collab_table_print_header(template, title):
    if len(title) == 0:
        return

    dash_template = template.replace(' | ', '-+-')

    very_long_dash = ('--------------------------------------------------------------------------------',)
    dashes = ()
    for i in range(len(title)):
        dashes = dashes + very_long_dash

    print(template % title)
    print(dash_template % dashes)


#######################################################################


def _collab_todo_internal(apiurl, all_reserved, all_commented, project, show_details, exclude_commented, exclude_reserved, exclude_submitted, exclude_devel):
    # get all versions of packages
    try:
        prj = OscCollabApi.get_project_details(project)
        prj.strip_internal_links()
    except OscCollabWebError as e:
        print(e.msg, file=sys.stderr)
        return (None, None)

    # get the list of reserved packages for this project
    reserved_packages = [ reservation.package for reservation in all_reserved if reservation.project == project ]

    # get the list of commented packages for this project
    firstline_comments = {}
    for comment in all_commented:
        if comment.project == project:
            firstline_comments[comment.package] = comment.firstline
    commented_packages = firstline_comments.keys()

    # get the packages submitted
    requests_to = OscCollabObs.get_request_list_to(project)

    parent_project = None
    packages = []

    for package in prj.values():
        if not package.needs_update() and package.name not in commented_packages:
            continue

        broken_link = package.is_broken_link()

        if package.parent_version or package.is_link:
            package.parent_version_print = package.parent_version or ''
        elif broken_link:
            # this can happen if the link is to a project that doesn't exist
            # anymore
            package.parent_version_print = '??'
        else:
            package.parent_version_print = '--'

        if package.version:
            package.version_print = package.version
        elif broken_link:
            package.version_print = '(broken)'
        else:
            package.version_print = '??'

        package.upstream_version_print = package.upstream_version or ''
        package.comment = ''

        if package.name in commented_packages:
            if exclude_commented:
                continue
            if not show_details:
                package.version_print += ' (c)'
                package.upstream_version_print += ' (c)'
            package.comment = firstline_comments[package.name]

        if not package.devel_needs_update():
            if exclude_devel:
                continue
            package.version_print += ' (d)'
            package.upstream_version_print += ' (d)'

        if _collab_find_request_to(package.name, requests_to) != None:
            if exclude_submitted:
                continue
            package.version_print += ' (s)'
            package.upstream_version_print += ' (s)'

        if package.name in reserved_packages:
            if exclude_reserved:
                continue
            package.upstream_version_print += ' (r)'

        package.upstream_version_print = package.upstream_version_print.strip()

        if package.parent_project:
            if parent_project == None:
                parent_project = package.parent_project
            elif parent_project != package.parent_project:
                parent_project = 'Parent Project'

        packages.append(package)


    return (parent_project, packages)


#######################################################################


def _collab_todo(apiurl, projects, show_details, ignore_comments, exclude_commented, exclude_reserved, exclude_submitted, exclude_devel):
    packages = []
    parent_project = None

    # get the list of reserved packages
    try:
        reserved = OscCollabApi.get_reserved_packages(projects)
    except OscCollabWebError as e:
        reserved = []
        print(e.msg, file=sys.stderr)

    # get the list of commented packages
    commented = []
    if not ignore_comments:
        try:
            commented = OscCollabApi.get_commented_packages(projects)
        except OscCollabWebError as e:
            print(e.msg, file=sys.stderr)

    for project in projects:
        (new_parent_project, project_packages) = _collab_todo_internal(apiurl, reserved, commented, project, show_details, exclude_commented, exclude_reserved, exclude_submitted, exclude_devel)
        if not project_packages:
            continue
        packages.extend(project_packages)

        if parent_project == None:
            parent_project = new_parent_project
        elif parent_project != new_parent_project:
            parent_project = 'Parent Project'

    if len(packages) == 0:
        print('Nothing to do.')
        return

    show_comments = not (ignore_comments or exclude_commented) and show_details

    if show_comments:
        lines = [ (package.name, package.parent_version_print, package.version_print, package.upstream_version_print, package.comment) for package in packages ]
    else:
        lines = [ (package.name, package.parent_version_print, package.version_print, package.upstream_version_print) for package in packages ]

    # the first element in the tuples is the package name, so it will sort
    # the lines the right way for what we want
    lines.sort()

    if len(projects) == 1:
        project_header = projects[0]
    else:
        project_header = "Devel Project"

    # print headers
    if show_comments:
        if parent_project:
            title = ('Package', parent_project, project_header, 'Upstream', 'Comment')
            (max_package, max_parent, max_devel, max_upstream, max_comment) = _collab_table_get_maxs(title, lines)
        else:
            title = ('Package', project_header, 'Upstream', 'Comment')
            (max_package, max_devel, max_upstream, max_comment) = _collab_table_get_maxs(title, lines)
            max_parent = 0
    else:
        if parent_project:
            title = ('Package', parent_project, project_header, 'Upstream')
            (max_package, max_parent, max_devel, max_upstream) = _collab_table_get_maxs(title, lines)
        else:
            title = ('Package', project_header, 'Upstream')
            (max_package, max_devel, max_upstream) = _collab_table_get_maxs(title, lines)
            max_parent = 0
        max_comment = 0

    # trim to a reasonable max
    max_package = min(max_package, 48)
    max_version = min(max(max(max_parent, max_devel), max_upstream), 20)
    max_comment = min(max_comment, 48)

    if show_comments:
        if parent_project:
            print_line = _collab_table_get_template(max_package, max_version, max_version, max_version, max_comment)
        else:
            print_line = _collab_table_get_template(max_package, max_version, max_version, max_comment)
    else:
        if parent_project:
            print_line = _collab_table_get_template(max_package, max_version, max_version, max_version)
        else:
            print_line = _collab_table_get_template(max_package, max_version, max_version)

    _collab_table_print_header(print_line, title)

    for line in lines:
        if not parent_project:
            if show_comments:
                (package, parent_version, devel_version, upstream_version, comment) = line
                line = (package, devel_version, upstream_version, comment)
            else:
                (package, parent_version, devel_version, upstream_version) = line
                line = (package, devel_version, upstream_version)
        print(print_line % line)


#######################################################################


def _collab_todoadmin_internal(apiurl, project, include_upstream):

    try:
        prj = OscCollabApi.get_project_details(project)
        prj.strip_internal_links()
    except OscCollabWebError as e:
        print(e.msg, file=sys.stderr)
        return []

    # get the packages submitted to/from
    requests_to = OscCollabObs.get_request_list_to(project)
    requests_from = OscCollabObs.get_request_list_from(project)

    lines = []

    for package in prj.values():
        message = None

        # We look for all possible messages. The last message overwrite the
        # first, so we start with the less important ones.

        if include_upstream:
            if not package.upstream_version:
                message = 'No upstream data available'
            elif not package.upstream_url:
                message = 'No URL for upstream tarball available'

        if package.has_delta:
            # FIXME: we should check the request is to the parent project
            if not _collab_has_request_from(package.name, requests_from):
                if not package.is_link:
                    message = 'Is not a link to %s and has a delta (synchronize the packages)' % package.project.parent
                elif not package.project.is_toplevel():
                    message = 'Needs to be submitted to %s' % package.parent_project
                else:
                    # packages in a toplevel project don't necessarily have to
                    # be submitted
                    message = 'Is a link with delta (maybe submit changes to %s)' % package.parent_project

        request = _collab_find_request_to(package.name, requests_to)
        if request is not None:
            message = 'Needs to be reviewed (request id: %s)' % request.req_id

        if package.error:
            if package.error == 'not-link':
                # if package has a delta, then we already set a message above
                if not package.has_delta:
                    message = 'Is not a link to %s (make link)' % package.project.parent
            elif package.error == 'not-link-not-in-parent':
                message = 'Is not a link, and is not in %s (maybe submit it)' % package.project.parent
            elif package.error == 'not-in-parent':
                message = 'Broken link: does not exist in %s' % package.parent_project
            elif package.error == 'need-merge-with-parent':
                message = 'Broken link: requires a manual merge with %s' % package.parent_project
            elif package.error == 'not-real-devel':
                message = 'Should not exist: %s' % package.error_details
            elif package.error == 'parent-without-devel':
                message = 'No devel project set for parent (%s/%s)' % (package.parent_project, package.parent_package)
            else:
                if package.error_details:
                    message = 'Unknown error (%s): %s' % (package.error, package.error_details)
                else:
                    message = 'Unknown error (%s)' % package.error

        if message:
            lines.append((project, package.name, message))


    for (package, parent_project, parent_package) in prj.missing_packages:
        message = 'Does not exist, but is devel package for %s/%s' % (parent_project, parent_package)
        lines.append((project, package, message))


    lines.sort()

    return lines


#######################################################################


def _collab_todoadmin(apiurl, projects, include_upstream):
    lines = []

    for project in projects:
        project_lines = _collab_todoadmin_internal(apiurl, project, include_upstream)
        lines.extend(project_lines)

    if len(lines) == 0:
        print('Nothing to do.')
        return

    # the first element in the tuples is the package name, so it will sort
    # the lines the right way for what we want
    lines.sort()

    # print headers
    title = ('Project', 'Package', 'Details')
    (max_project, max_package, max_details) = _collab_table_get_maxs(title, lines)
    # trim to a reasonable max
    max_project = min(max_project, 28)
    max_package = min(max_package, 48)
    max_details = min(max_details, 65)

    print_line = _collab_table_get_template(max_project, max_package, max_details)
    _collab_table_print_header(print_line, title)
    for line in lines:
        print(print_line % line)


#######################################################################


def _collab_listreserved(projects):
    try:
        reserved_packages = OscCollabApi.get_reserved_packages(projects)
    except OscCollabWebError as e:
        print(e.msg, file=sys.stderr)
        return

    if len(reserved_packages) == 0:
        print('No package reserved.')
        return

    # print headers
    # if changing the order here, then we need to change __getitem__ of
    # Reservation in the same way
    title = ('Project', 'Package', 'Reserved by')
    (max_project, max_package, max_username) = _collab_table_get_maxs(title, reserved_packages)
    # trim to a reasonable max
    max_project = min(max_project, 28)
    max_package = min(max_package, 48)
    max_username = min(max_username, 28)

    print_line = _collab_table_get_template(max_project, max_package, max_username)
    _collab_table_print_header(print_line, title)

    for reservation in reserved_packages:
        if reservation.user:
            print(print_line % (reservation.project, reservation.package, reservation.user))


#######################################################################


def _collab_isreserved(projects, packages, no_devel_project = False):
    for package in packages:
        try:
            reservation = OscCollabApi.is_package_reserved(projects, package, no_devel_project = no_devel_project)
        except OscCollabWebError as e:
            print(e.msg, file=sys.stderr)
            continue

        if not reservation:
            print('Package %s is not reserved.' % package)
        else:
            if reservation.project not in projects or reservation.package != package:
                print('Package %s in %s (devel package for %s) is reserved by %s.' % (reservation.package, reservation.project, package, reservation.user))
            else:
                print('Package %s in %s is reserved by %s.' % (package, reservation.project, reservation.user))


#######################################################################


def _collab_reserve(projects, packages, username, no_devel_project = False):
    for package in packages:
        try:
            reservation = OscCollabApi.reserve_package(projects, package, username, no_devel_project = no_devel_project)
        except OscCollabWebError as e:
            print(e.msg, file=sys.stderr)
            continue

        if reservation.project not in projects or reservation.package != package:
            print('Package %s in %s (devel package for %s) reserved for 36 hours.' % (reservation.package, reservation.project, package))
        else:
            print('Package %s reserved for 36 hours.' % package)
        print('Do not forget to unreserve the package when done with it:')
        print('    osc %s unreserve %s' % (_osc_collab_alias, package))


#######################################################################


def _collab_unreserve(projects, packages, username, no_devel_project = False):
    for package in packages:
        try:
            OscCollabApi.unreserve_package(projects, package, username, no_devel_project = no_devel_project)
        except OscCollabWebError as e:
            print(e.msg, file=sys.stderr)
            continue

        print('Package %s unreserved.' % package)


#######################################################################


def _collab_listcommented(projects):
    try:
        commented_packages = OscCollabApi.get_commented_packages(projects)
    except OscCollabWebError as e:
        print(e.msg, file=sys.stderr)
        return

    if len(commented_packages) == 0:
        print('No package commented.')
        return

    # print headers
    # if changing the order here, then we need to change __getitem__ of
    # Comment in the same way
    title = ('Project', 'Package', 'Commented by', 'Comment')
    (max_project, max_package, max_username, max_comment) = _collab_table_get_maxs(title, commented_packages)
    # trim to a reasonable max
    max_project = min(max_project, 28)
    max_package = min(max_package, 48)
    max_username = min(max_username, 28)
    max_comment = min(max_comment, 65)

    print_line = _collab_table_get_template(max_project, max_package, max_username, max_comment)
    _collab_table_print_header(print_line, title)

    for comment in commented_packages:
        if comment.user:
            print(print_line % (comment.project, comment.package, comment.user, comment.firstline))


#######################################################################


def _collab_comment(projects, packages, no_devel_project = False):
    for package in packages:
        try:
            comment = OscCollabApi.get_package_comment(projects, package, no_devel_project = no_devel_project)
        except OscCollabWebError as e:
            print(e.msg, file=sys.stderr)
            continue

        if not comment:
            print('Package %s is not commented.' % package)
        else:
            if comment.date:
                date_str = ' on %s' % comment.date
            else:
                date_str = ''

            if comment.project not in projects or comment.package != package:
                print('Package %s in %s (devel package for %s) is commented by %s%s:' % (comment.package, comment.project, package, comment.user, date_str))
                print(comment.indent())
            else:
                print('Package %s in %s is commented by %s%s:' % (package, comment.project, comment.user, date_str))
                print(comment.indent())


#######################################################################


def _collab_commentset(projects, package, username, comment, no_devel_project = False):
    try:
        comment = OscCollabApi.set_package_comment(projects, package, username, comment, no_devel_project = no_devel_project)
    except OscCollabWebError as e:
        print(e.msg, file=sys.stderr)
        return

    if comment.project not in projects or comment.package != package:
        print('Comment on package %s in %s (devel package for %s) set.' % (comment.package, comment.project, package))
    else:
        print('Comment on package %s set.' % package)
    print('Do not forget to unset comment on the package when done with it:')
    print('    osc %s commentunset %s' % (_osc_collab_alias, package))


#######################################################################


def _collab_commentunset(projects, packages, username, no_devel_project = False):
    for package in packages:
        try:
            OscCollabApi.unset_package_comment(projects, package, username, no_devel_project = no_devel_project)
        except OscCollabWebError as e:
            print(e.msg, file=sys.stderr)
            continue

        print('Comment on package %s unset.' % package)


#######################################################################


def _collab_setup_internal(apiurl, username, pkg, ignore_reserved = False, no_reserve = False, no_devel_project = False, no_branch = False):
    if not no_devel_project:
        initial_pkg = pkg
        while pkg.devel_project:
            previous_pkg = pkg
            try:
                pkg = OscCollabApi.get_package_details(pkg.devel_project, pkg.devel_package or pkg.name)
            except OscCollabWebError as e:
                pkg = None

            if not pkg:
                print('Cannot find information on %s/%s (development package for %s/%s). You can use --nodevelproject to ignore the development package.' % (previous_pkg.project.name, previous_pkg.name, initial_pkg.project.name, initial_pkg.name), file=sys.stderr)
                break

        if not pkg:
            return (False, None, None)

        if initial_pkg != pkg:
            print('Using development package %s/%s for %s/%s.' % (pkg.project.name, pkg.name, initial_pkg.project.name, initial_pkg.name))

    project = pkg.project.name
    package = pkg.name

    checkout_dir = package

    # Is it reserved? Note that we have already looked for the devel project,
    # so we force the project/package here.
    try:
        reservation = OscCollabApi.is_package_reserved((project,), package, no_devel_project = True)
        if reservation:
            reserved_by = reservation.user
        else:
            reserved_by = None
    except OscCollabWebError as e:
        print(e.msg, file=sys.stderr)
        return (False, None, None)

    # package already reserved, but not by us
    if reserved_by and reserved_by != username:
        if not ignore_reserved:
            print('Package %s is already reserved by %s.' % (package, reserved_by))
            return (False, None, None)
        else:
            print('WARNING: package %s is already reserved by %s.' % (package, reserved_by))
    # package not reserved
    elif not reserved_by and not no_reserve:
        try:
            # Note that we have already looked for the devel project, so we
            # force the project/package here.
            OscCollabApi.reserve_package((project,), package, username, no_devel_project = True)
            print('Package %s has been reserved for 36 hours.' % package)
            print('Do not forget to unreserve the package when done with it:')
            print('    osc %s unreserve %s' % (_osc_collab_alias, package))
        except OscCollabWebError as e:
            print(e.msg, file=sys.stderr)
            if not ignore_reserved:
                return (False, None, None)

    if not no_branch:
        # look if we already have a branch, and if not branch the package
        try:
            expected_branch_project = 'home:%s:branches:%s' % (username, project)
            show_package_meta(apiurl, expected_branch_project, package)
            branch_project = expected_branch_project
            branch_package = package
            # it worked, we already have the branch
        except HTTPError as e:
            if e.code != 404:
                print('Error while checking if package %s was already branched: %s' % (package, e.msg), file=sys.stderr)
                return (False, None, None)

            # We had a 404: it means the branched package doesn't exist yet
            (branch_project, branch_package) = OscCollabObs.branch_package(project, package, no_devel_project)
            if not branch_project or not branch_package:
                print('Error while branching package %s: incomplete reply from build service' % (package,), file=sys.stderr)
                return (False, None, None)

            if package != branch_package:
                print('Package %s has been branched in %s/%s.' % (package, branch_project, branch_package))
            else:
                print('Package %s has been branched in project %s.' % (branch_package, branch_project))
    else:
            branch_project = project
            branch_package = package

    checkout_dir = branch_package

    # check out the branched package
    if os.path.exists(checkout_dir):
        # maybe we already checked it out before?
        if not os.path.isdir(checkout_dir):
            print('File %s already exists but is not a directory.' % checkout_dir, file=sys.stderr)
            return (False, None, None)
        elif not is_package_dir(checkout_dir):
            print('Directory %s already exists but is not a checkout of a Build Service package.' % checkout_dir, file=sys.stderr)
            return (False, None, None)

        obs_package = filedir_to_pac(checkout_dir)
        if obs_package.name != branch_package or obs_package.prjname != branch_project:
            print('Directory %s already exists but is a checkout of package %s from project %s.' % (checkout_dir, obs_package.name, obs_package.prjname), file=sys.stderr)
            return (False, None, None)

        if _collab_osc_package_pending_commit(obs_package):
            print('Directory %s contains some uncommitted changes.' % (checkout_dir,), file=sys.stderr)
            return (False, None, None)

        # update the package
        try:
            # we specify the revision so that it gets expanded
            # the logic comes from do_update in commandline.py
            rev = None
            if obs_package.islink() and not obs_package.isexpanded():
                rev = obs_package.linkinfo.xsrcmd5
            elif obs_package.islink() and obs_package.isexpanded():
                rev = show_upstream_xsrcmd5(apiurl, branch_project, branch_package)

            obs_package.update(rev)
            print('Package %s has been updated.' % branch_package)
        except Exception as e:
            message = 'Error while updating package %s: ' % branch_package
            _collab_exception_print(e, message)
            return (False, None, None)

    else:
        # check out the branched package
        try:
            # disable package tracking: the current directory might not be a
            # project directory
            # Rationale: for new contributors, checking out in the current
            # directory is easier as it hides some complexity. However, this
            # results in possibly mixing packages from different projects,
            # which makes package tracking not work at all.
            old_tracking = conf.config['do_package_tracking']
            conf.config['do_package_tracking'] = _collab_get_config_bool(apiurl, 'collab_do_package_tracking', default = False)
            checkout_package(apiurl, branch_project, branch_package, expand_link=True)
            conf.config['do_package_tracking'] = old_tracking
            print('Package %s has been checked out.' % branch_package)
        except Exception as e:
            message = 'Error while checking out package %s: ' % branch_package
            _collab_exception_print(e, message)
            return (False, None, None)

    # remove old helper files
    for file in os.listdir(checkout_dir):
        for helper in _osc_collab_helpers:
            if file == helper:
                path = os.path.join(checkout_dir, file)
                os.unlink(path)
                break

    return (True, branch_project, branch_package)


#######################################################################


def _collab_get_package_with_valid_project(projects, package):
    try:
        pkg = OscCollabApi.get_package_details(projects, package)
    except OscCollabWebError as e:
        pkg = None

    if pkg is None or pkg.project is None or not pkg.project.name:
        print('Cannot find an appropriate project containing %s. You can use --project to override your project settings.' % package, file=sys.stderr)
        return None

    return pkg


#######################################################################


def _print_comment_after_setup(pkg, no_devel_project):
    comment = OscCollabApi.get_package_comment(pkg.project.name, pkg.name, no_devel_project = no_devel_project)
    if comment:
        if comment.date:
            date_str = ' on %s' % comment.date
        else:
            date_str = ''

        print('Note the comment from %s%s on this package:' % (comment.user, date_str))
        print(comment.indent())


#######################################################################


def _collab_setup(apiurl, username, projects, package, ignore_reserved = False, ignore_comment = False, no_reserve = False, no_devel_project = False, no_branch = False):
    pkg = _collab_get_package_with_valid_project(projects, package)
    if not pkg:
        return
    project = pkg.project.name

    (setup, branch_project, branch_package) = _collab_setup_internal(apiurl, username, pkg, ignore_reserved, no_reserve, no_devel_project, no_branch)
    if not setup:
        return
    print('Package %s has been prepared for work.' % branch_package)

    if not ignore_comment:
        _print_comment_after_setup(pkg, no_devel_project)


#######################################################################


def _collab_download_internal(url, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    parsed_url = urlparse(url)
    basename = os.path.basename(parsed_url.path)
    if not basename:
        # FIXME: workaround until we get a upstream_basename property for each
        # package (would be needed for upstream hosted on sf, anyway).
        # Currently needed for mkvtoolnix.
        for field in parsed_url.query.split('&'):
            try:
                (key, value) = field.split('=', 1)
            except ValueError:
                value = field
            if value.endswith('.gz') or value.endswith('.tgz') or value.endswith('.bz2'):
                basename = os.path.basename(value)

    if not basename:
        raise OscCollabDownloadError('Cannot download %s: no basename in URL.' % url)

    dest_file = os.path.join(dest_dir, basename)
    # we download the file again if it already exists. Maybe the upstream
    # tarball changed, eg. We could add an option to avoid this, but I feel
    # like it won't happen a lot anyway.
    if os.path.exists(dest_file):
        os.unlink(dest_file)

    try:
        fin = urlopen(url)
    except HTTPError as e:
        raise OscCollabDownloadError('Cannot download %s: %s' % (url, e.msg))

    fout = open(dest_file, 'wb')

    while True:
        try:
            bytes = fin.read(500 * 1024)
            if len(bytes) == 0:
                break
            fout.write(bytes)
        except HTTPError as e:
            fin.close()
            fout.close()
            os.unlink(dest_file)
            raise OscCollabDownloadError('Error while downloading %s: %s' % (url, e.msg))

    fin.close()
    fout.close()

    return dest_file


#######################################################################


def _collab_extract_diff_internal(directory, old_tarball, new_tarball):
    def _cleanup(old, new, tmpdir):
        if old:
            old.close()
        if new:
            new.close()
        shutil.rmtree(tmpdir)

    def _lzma_hack(filename, tmpdir):
        if not filename.endswith('.xz'):
            return filename

        dest = os.path.join(tmpdir, os.path.basename(filename))
        shutil.copyfile(filename, dest)
        subprocess.call(['xz', '-d', dest])

        return dest[:-3]

    # we need to make sure it's safe to extract the file
    # see the warning in http://www.python.org/doc/lib/tarfile-objects.html
    def _can_extract_with_trust(name):
        if not name:
            return False
        if name[0] == '/':
            return False
        if name[0] == '.':
            # only accept ./ if the first character is a dot
            if len(name) == 1 or name[1] != '/':
                return False

        return True

    def _extract_files(tar, path, whitelist):
        if not tar or not path or not whitelist:
            return

        for tarinfo in tar:
            if not _can_extract_with_trust(tarinfo.name):
                continue
            # we won't accept symlinks or hard links. It sounds weird to have
            # this for the files we're interested in.
            if not tarinfo.isfile():
                continue
            basename = os.path.basename(tarinfo.name)
            if not basename in whitelist:
                continue
            tar.extract(tarinfo, path)

    def _diff_files(old, new, dest):
        if not new:
            return (False, False)
        if not old:
            shutil.copyfile(new, dest)
            return (True, False)

        old_f = open(old)
        old_lines = old_f.readlines()
        old_f.close()
        new_f = open(new)
        new_lines = new_f.readlines()
        new_f.close()

        diff = difflib.unified_diff(old_lines, new_lines)
        # diff is a generator, so we can't know if it's empty or not until we
        # iterate over it. So if it's empty, we'll create an empty file, and
        # remove it afterwards.

        dest_f = open(dest, 'w')

        # We first write what we consider useful and then write the complete
        # diff for reference.
        # This works because a well-formed NEWS/ChangeLog will only have new
        # items added at the top, and therefore the useful diff is the addition
        # at the top. This doesn't work for configure.{ac,in}, but that's fine.
        # We need to cache the first lines, though, since diff is a generator
        # and we don't have direct access to lines.

        i = 0
        pass_one_done = False
        cached = []

        for line in diff:
            # we skip the first three lines of the diff
            if not pass_one_done and i == 0 and line[:3] == '---':
                cached.append(line)
                i = 1
            elif not pass_one_done and i == 1 and line[:3] == '+++':
                cached.append(line)
                i = 2
            elif not pass_one_done and i == 2 and line[:2] == '@@':
                cached.append(line)
                i = 3
            elif not pass_one_done and i == 3 and line[0] == '+':
                cached.append(line)
                dest_f.write(line[1:])
            elif not pass_one_done:
                # end of pass one: we write a note to help the user, and then
                # write the cache
                pass_one_done = True

                note = '# Note by osc %s: here is the complete diff for reference.' % _osc_collab_alias
                header = ''
                for i in range(len(note)):
                    header += '#'

                dest_f.write('\n')
                dest_f.write('%s\n' % header)
                dest_f.write('%s\n' % note)
                dest_f.write('%s\n' % header)
                dest_f.write('\n')
                for cached_line in cached:
                    dest_f.write(cached_line)
                dest_f.write(line)
            else:
                dest_f.write(line)

        dest_f.close()

        if not cached:
            os.unlink(dest)
            return (False, False)

        return (True, True)


    # FIXME: only needed until we switch to python >= 3.3
    lzma_hack = not hasattr(tarfile.TarFile, 'xzopen')

    tmpdir = tempfile.mkdtemp(prefix = 'osc-collab-')

    old = None
    new = None

    if old_tarball and os.path.exists(old_tarball):
        try:
            if lzma_hack:
                old_tarball = _lzma_hack(old_tarball, tmpdir)
            old = tarfile.open(old_tarball)
        except tarfile.TarError:
            pass
    else:
        # this is not fatal: we can provide the
        # NEWS/ChangeLog/configure.{ac,in} from the new tarball without a diff
        pass

    if new_tarball and os.path.exists(new_tarball):
        new_tarball_basename = os.path.basename(new_tarball)
        try:
            if lzma_hack:
                new_tarball = _lzma_hack(new_tarball, tmpdir)
            new = tarfile.open(new_tarball)
        except tarfile.TarError as e:
            _cleanup(old, new, tmpdir)
            raise OscCollabDiffError('Error when opening %s: %s' % (new_tarball_basename, e))
    else:
        _cleanup(old, new, tmpdir)
        raise OscCollabDiffError('Cannot extract useful diff between tarballs: no new tarball.')

    # make sure we have at least a subdirectory in tmpdir, since we'll extract
    # files from two tarballs that might conflict
    old_dir = os.path.join(tmpdir, 'old')
    new_dir = os.path.join(tmpdir, 'new')

    try:
        if old:
            err_tarball = os.path.basename(old_tarball)
            _extract_files (old, old_dir, ['NEWS', 'ChangeLog', 'configure.ac', 'configure.in', 'meson.build', 'meson_options.txt'])

        err_tarball = new_tarball_basename
        _extract_files (new, new_dir, ['NEWS', 'ChangeLog', 'configure.ac', 'configure.in', 'meson.build', 'meson_options.txt'])
    except (tarfile.ReadError, EOFError):
        _cleanup(old, new, tmpdir)
        raise OscCollabDiffError('Cannot extract useful diff between tarballs: %s is not a valid tarball.' % err_tarball)

    if old:
        old.close()
        old = None
    if new:
        new.close()
        new = None

    # find toplevel NEWS/ChangeLog/configure.{ac,in} in the new tarball
    if not os.path.exists(new_dir):
        _cleanup(old, new, tmpdir)
        raise OscCollabDiffError('Cannot extract useful diff between tarballs: no relevant files found in %s.' % new_tarball_basename)

    new_dir_files = os.listdir(new_dir)
    if len(new_dir_files) != 1:
        _cleanup(old, new, tmpdir)
        raise OscCollabDiffError('Cannot extract useful diff between tarballs: unexpected file hierarchy in %s.' % new_tarball_basename)

    new_subdir = os.path.join(new_dir, new_dir_files[0])
    if not os.path.isdir(new_subdir):
        _cleanup(old, new, tmpdir)
        raise OscCollabDiffError('Cannot extract useful diff between tarballs: unexpected file hierarchy in %s.' % new_tarball_basename)

    new_news = os.path.join(new_subdir, 'NEWS')
    if not os.path.exists(new_news) or not os.path.isfile(new_news):
        new_news = None
    new_changelog = os.path.join(new_subdir, 'ChangeLog')
    if not os.path.exists(new_changelog) or not os.path.isfile(new_changelog):
        new_changelog = None
    new_configure = os.path.join(new_subdir, 'configure.ac')
    if not os.path.exists(new_configure) or not os.path.isfile(new_configure):
        new_configure = os.path.join(new_subdir, 'configure.in')
        if not os.path.exists(new_configure) or not os.path.isfile(new_configure):
            new_configure = None
    new_meson = os.path.join(new_subdir, 'meson.build')
    if not os.path.exists(new_meson) or not os.path.isfile(new_meson):
        new_meson = None
    new_mesonopt = os.path.join(new_subdir, 'meson_options.txt')
    if not os.path.exists(new_mesonopt) or not os.path.isfile(new_mesonopt):
        new_mesonopt = None

    if not new_news and not new_changelog and not new_configure and not new_meson and not new_mesonopt:
        _cleanup(old, new, tmpdir)
        raise OscCollabDiffError('Cannot extract useful diff between tarballs: no relevant files found in %s.' % new_tarball_basename)

    # find toplevel NEWS/ChangeLog/configure.{ac,in} in the old tarball
    # not fatal
    old_news = None
    old_changelog = None
    old_configure = None
    old_meson = None
    old_mesonopt = None

    if os.path.exists(old_dir):
        old_dir_files = os.listdir(old_dir)
    else:
        old_dir_files = []

    if len(old_dir_files) == 1:
        old_subdir = os.path.join(old_dir, old_dir_files[0])
        if os.path.isdir(old_subdir):
            old_news = os.path.join(old_subdir, 'NEWS')
            if not os.path.exists(old_news) or not os.path.isfile(old_news):
                old_news = None
            old_changelog = os.path.join(old_subdir, 'ChangeLog')
            if not os.path.exists(old_changelog) or not os.path.isfile(old_changelog):
                old_changelog = None
            old_configure = os.path.join(old_subdir, 'configure.ac')
            if not os.path.exists(old_configure) or not os.path.isfile(old_configure):
                old_configure = os.path.join(old_subdir, 'configure.in')
                if not os.path.exists(old_configure) or not os.path.isfile(old_configure):
                    old_configure = None
            old_meson = os.path.join(old_subdir, 'meson.build')
            if not os.path.exists(old_meson) or not os.path.isfile(old_meson):
                old_meson = None
            old_mesonopt = os.path.join(old_subdir, 'meson_options.txt')
            if not os.path.exists(old_mesonopt) or not os.path.isfile(old_mesonopt):
                old_mesonopt = None

    # Choose the most appropriate prefix for helper files, based on the alias
    # that was used by the user
    helper_prefix = _osc_collab_helper_prefixes[0]
    for prefix in _osc_collab_helper_prefixes:
        if _osc_collab_alias in prefix:
            helper_prefix = prefix
            break

    # do the diff
    news = os.path.join(directory, helper_prefix + 'NEWS')
    (news_created, news_is_diff) = _diff_files(old_news, new_news, news)
    changelog = os.path.join(directory, helper_prefix + 'ChangeLog')
    (changelog_created, changelog_is_diff) = _diff_files(old_changelog, new_changelog, changelog)
    configure = os.path.join(directory, helper_prefix + 'configure')
    (configure_created, configure_is_diff) = _diff_files(old_configure, new_configure, configure)
    meson = os.path.join(directory, helper_prefix + 'meson')
    (meson_created, meson_is_diff) = _diff_files(old_meson, new_meson, meson)
    mesonopt = os.path.join(directory, helper_prefix + 'meson_options')
    (mesonopt_created, mesonopt_is_diff) = _diff_files(old_mesonopt, new_mesonopt, mesonopt)

    # Note: we make osc ignore those helper file we created by modifying
    # the exclude list of osc.core. See the top of this file.

    _cleanup(old, new, tmpdir)

    return (news, news_created, news_is_diff, changelog, changelog_created, changelog_is_diff, configure, configure_created, configure_is_diff, meson, meson_created, meson_is_diff, mesonopt, mesonopt_created, mesonopt_is_diff)


#######################################################################


def _collab_subst_defines(s, defines):
    '''Replace macros like %{version} and %{name} in strings. Useful
       for sources and patches '''
    for key in defines.keys():
        if s.find(key) != -1:
            value = defines[key]
            s = s.replace('%%{%s}' % key, value)
            s = s.replace('%%%s' % key, value)
    return s


def _collab_update_spec(spec_file, upstream_url, upstream_version):
    if not os.path.exists(spec_file):
        print('Cannot update %s: no such file.' % os.path.basename(spec_file), file=sys.stderr)
        return (False, None, None, False)
    elif not os.path.isfile(spec_file):
        print('Cannot update %s: not a regular file.' % os.path.basename(spec_file), file=sys.stderr)
        return (False, None, None, False)

    re_spec_header_with_version = re.compile('^(# spec file for package \S*) \(Version \S*\)(.*)', re.IGNORECASE)
    re_spec_define = re.compile('^%define\s+(\S*)\s+(\S*)', re.IGNORECASE)
    re_spec_name = re.compile('^Name:\s*(\S*)', re.IGNORECASE)
    re_spec_version = re.compile('^(Version:\s*)(\S*)', re.IGNORECASE)
    re_spec_release = re.compile('^(Release:\s*)\S*', re.IGNORECASE)
    re_spec_source = re.compile('^(Source0?:\s*)(\S*)', re.IGNORECASE)
    re_spec_prep = re.compile('^%prep', re.IGNORECASE)

    defines = {}
    old_source = None
    old_version = None
    define_in_source = False

    fin = open(spec_file, 'r')
    (fdout, tmp) = tempfile.mkstemp(dir = os.path.dirname(spec_file))

    # replace version and reset release
    while True:
        line = fin.readline()
        if len(line) == 0:
            break

        match = re_spec_prep.match(line)
        if match:
            os.write(fdout, line.encode('utf-8'))
            break

        match = re_spec_header_with_version.match(line)
        if match:
            # We drop the "(Version XYZ)" part of the header
            write_line = '%s%s\n' % (match.group(1), match.group(2))
            os.write(fdout, write_line.encode('utf-8'))
            continue

        match = re_spec_define.match(line)
        if match:
            defines[match.group(1)] = _collab_subst_defines(match.group(2), defines)
            os.write(fdout, line.encode('utf-8'))
            continue

        match = re_spec_name.match(line)
        if match:
            defines['name'] = match.group(1)
            os.write(fdout, line.encode('utf-8'))
            continue

        match = re_spec_version.match(line)
        if match:
            defines['version'] = match.group(2)
            old_version = _collab_subst_defines(match.group(2), defines)
            write_line = '%s%s\n' % (match.group(1), upstream_version)
            os.write(fdout, write_line.encode('utf-8'))
            continue

        match = re_spec_release.match(line)
        if match:
            write_line = '%s0\n' % match.group(1)
            os.write(fdout, write_line.encode('utf-8'))
            continue

        match = re_spec_source.match(line)
        if match:
            old_source = os.path.basename(match.group(2))

            if upstream_url:
                non_basename = os.path.dirname(upstream_url)
                new_source = os.path.basename(upstream_url)
                # Use _name in favor of name, as if _name exists, it's for a
                # good reason
                for key in [ '_name', 'name', 'version' ]:
                    if key in defines:
                        if key == 'version':
                            new_source = new_source.replace(upstream_version, '%%{%s}' % key)
                        else:
                            new_source = new_source.replace(defines[key], '%%{%s}' % key)

                # Only use the URL as source if the basename looks like the
                # real name of the file.
                # If '?' is in the basename, then we likely have some dynamic
                # page to download the file, which means the wrong basename.
                # For instance:
                # download.php?package=01&release=61&file=01&dummy=gwenhywfar-4.1.0.tar.gz
                if '?' not in new_source:
                    write_line = '%s%s/%s\n' % (match.group(1), non_basename, new_source)
                    os.write(fdout, write_line.encode('utf-8'))
                    continue

            os.write(fdout, line.encode('utf-8'))
            continue

        os.write(fdout, line.encode('utf-8'))

    # wild read/write to finish quickly
    while True:
        bytes = fin.read(10 * 1024)
        if len(bytes) == 0:
            break
        os.write(fdout, bytes.encode('utf-8'))

    fin.close()
    os.close(fdout)

    os.rename(tmp, spec_file)

    if old_source and old_source.find('%') != -1:
        for key in defines.keys():
            if old_source.find(key) != -1:
                old_source = old_source.replace('%%{%s}' % key, defines[key])
                old_source = old_source.replace('%%%s' % key, defines[key])
                if key not in [ 'name', '_name', 'version' ]:
                    define_in_source = True

    return (True, old_source, old_version, define_in_source)


#######################################################################


def _collab_update_changes(changes_file, upstream_version, email):
    if not os.path.exists(changes_file):
        print('Cannot update %s: no such file.' % os.path.basename(changes_file), file=sys.stderr)
        return False
    elif not os.path.isfile(changes_file):
        print('Cannot update %s: not a regular file.' % os.path.basename(changes_file), file=sys.stderr)
        return False

    (fdout, tmp) = tempfile.mkstemp(dir = os.path.dirname(changes_file))

    old_lc_time = locale.setlocale(locale.LC_TIME)
    old_tz = os.getenv('TZ')
    locale.setlocale(locale.LC_TIME, 'C')
    os.putenv('TZ', 'UTC')

    os.write(fdout, b'-------------------------------------------------------------------\n')
    write_line = '%s - %s\n' % (time.strftime("%a %b %e %H:%M:%S %Z %Y"), email)
    os.write(fdout, write_line.encode('utf-8'))
    os.write(fdout, b'\n')
    write_line = '- Update to version %s:\n' % upstream_version
    os.write(fdout, write_line.encode('utf-8'))
    os.write(fdout, b'  + \n')
    os.write(fdout, b'\n')

    locale.setlocale(locale.LC_TIME, old_lc_time)
    if old_tz:
        os.putenv('TZ', old_tz)
    else:
        os.unsetenv('TZ')

    fin = open(changes_file, 'r')
    while True:
        bytes = fin.read(10 * 1024)
        if len(bytes) == 0:
            break
        os.write(fdout, bytes.encode('utf-8'))
    fin.close()
    os.close(fdout)

    os.rename(tmp, changes_file)

    return True


#######################################################################


def _collab_quilt_package(spec_file):
    def _cleanup(null, tmpdir):
        null.close()
        shutil.rmtree(tmpdir)

    null = open('/dev/null', 'w')
    tmpdir = tempfile.mkdtemp(prefix = 'osc-collab-')


    # setup with quilt
    sourcedir = os.path.dirname(os.path.realpath(spec_file))
    popen = subprocess.Popen(['quilt', 'setup', '-d', tmpdir, '--sourcedir', sourcedir, spec_file], stdout = null, stderr = null)
    retval = popen.wait()

    if retval != 0:
        _cleanup(null, tmpdir)
        print('Cannot apply patches: \'quilt setup\' failed.', file=sys.stderr)
        return False


    # apply patches for all subdirectories
    for directory in os.listdir(tmpdir):
        dir = os.path.join(tmpdir, directory)

        if not os.path.isdir(dir):
            continue

        # there's no patch, so just continue
        if not os.path.exists(os.path.join(dir, 'patches')):
            continue

        popen = subprocess.Popen(['quilt', 'push', '-a', '-q'], cwd = dir, stdout = null, stderr = null)
        retval = popen.wait()

        if retval != 0:
            _cleanup(null, tmpdir)
            print('Cannot apply patches: \'quilt push -a\' failed.', file=sys.stderr)
            return False


    _cleanup(null, tmpdir)

    return True


#######################################################################


def _collab_update(apiurl, username, email, projects, package, ignore_reserved = False, ignore_comment = False, no_reserve = False, no_devel_project = False, no_branch = False):
    if len(projects) == 1:
        project = projects[0]

        try:
            pkg = OscCollabApi.get_package_details(project, package)
        except OscCollabWebError as e:
            print(e.msg, file=sys.stderr)
            return
    else:
        pkg = _collab_get_package_with_valid_project(projects, package)
        if not pkg:
            return
        project = pkg.project.name

    # check that the project is up-to-date wrt parent project
    if pkg.parent_more_recent():
        print('Package %s is more recent in %s (%s) than in %s (%s). Please synchronize %s first.' % (package, pkg.parent_project, pkg.parent_version, project, pkg.version, project))
        return

    # check that an update is really needed
    if not pkg.upstream_version:
        print('No information about upstream version of package %s is available. Assuming it is not up-to-date.' % package)
    elif pkg.upstream_version == '--':
        print('Package %s has no upstream.' % package)
        return
    elif pkg.devel_project and pkg.needs_update() and not no_devel_project and not pkg.devel_needs_update():
        if not pkg.devel_package or pkg.devel_package == package:
            print('Package %s is already up-to-date in its development project (%s).' % (package, pkg.devel_project))
        else:
            print('Package %s is already up-to-date in its development project (%s/%s).' % (package, pkg.devel_project, pkg.devel_package))
        return
    elif not pkg.needs_update():
        print('Package %s is already up-to-date.' % package)
        return

    (setup, branch_project, branch_package) = _collab_setup_internal(apiurl, username, pkg, ignore_reserved, no_reserve, no_devel_project, no_branch)
    if not setup:
        return

    package_dir = branch_package

    # edit the version tag in the .spec files
    # not fatal if fails
    spec_file = os.path.join(package_dir, package + '.spec')
    if not os.path.exists(spec_file) and package != branch_package:
        spec_file = os.path.join(package_dir, branch_package + '.spec')
    (updated, old_tarball, old_version, define_in_source) = _collab_update_spec(spec_file, pkg.upstream_url, pkg.upstream_version)
    if old_tarball:
        old_tarball_with_dir = os.path.join(package_dir, old_tarball)
    else:
        old_tarball_with_dir = None

    if old_version and old_version == pkg.upstream_version:
        if no_branch:
            print('Package %s is already up-to-date (the database might not be up-to-date).' % branch_package)
        else:
            print('Package %s is already up-to-date (in your branch only, or the database is not up-to-date).' % branch_package)
        return

    if define_in_source:
        print('WARNING: the Source tag in %s is using some define that might not be valid anymore.' % spec_file)
    if updated:
        print('%s has been prepared.' % os.path.basename(spec_file))

    # warn if there are other spec files which might need an update
    for file in os.listdir(package_dir):
        if file.endswith('.spec') and file != os.path.basename(spec_file):
            print('WARNING: %s might need a manual update.' % file)


    # start adding an entry to .changes
    # not fatal if fails
    changes_file = os.path.join(package_dir, package + '.changes')
    if not os.path.exists(changes_file) and package != branch_package:
        changes_file = os.path.join(package_dir, branch_package + '.changes')
    if _collab_update_changes(changes_file, pkg.upstream_version, email):
        print('%s has been prepared.' % os.path.basename(changes_file))

    # warn if there are other spec files which might need an update
    for file in os.listdir(package_dir):
        if file.endswith('.changes') and file != os.path.basename(changes_file):
            print('WARNING: %s might need a manual update.' % file)


    # download the upstream tarball
    # fatal if fails
    if not pkg.upstream_url:
        print('Cannot download latest upstream tarball for %s: no URL defined.' % package, file=sys.stderr)
        return

    print('Looking for the upstream tarball...')
    try:
        upstream_tarball = _collab_download_internal(pkg.upstream_url, package_dir)
    except OscCollabDownloadError as e:
        print(e.msg, file=sys.stderr)
        return

    if not upstream_tarball:
        print('No upstream tarball downloaded for %s.' % package, file=sys.stderr)
        return
    else:
        upstream_tarball_basename = os.path.basename(upstream_tarball)
        # same file as the old one: oops, we don't want to do anything weird
        # there
        if upstream_tarball_basename == old_tarball:
            old_tarball = None
            old_tarball_with_dir = None
        print('%s has been downloaded.' % upstream_tarball_basename)


    # check integrity of the downloaded file
    # fatal if fails (only if md5 exists)
    # TODO


    # extract NEWS & ChangeLog from the old + new tarballs, and do a diff
    # not fatal if fails
    print('Extracting useful diff between tarballs (NEWS, ChangeLog, configure.{ac,in})...')
    try:
        (news, news_created, news_is_diff, changelog, changelog_created, changelog_is_diff, configure, configure_created, configure_is_diff, meson, meson_created, meson_is_diff, mesonopt, mesonopt_created, mesonopt_is_diff) = _collab_extract_diff_internal(package_dir, old_tarball_with_dir, upstream_tarball)
    except OscCollabDiffError as e:
        print(e.msg, file=sys.stderr)
    else:
        if news_created:
            news_basename = os.path.basename(news)
            if news_is_diff:
                print('NEWS between %s and %s is available in %s' % (old_tarball, upstream_tarball_basename, news_basename))
            else:
                print('Complete NEWS of %s is available in %s' % (upstream_tarball_basename, news_basename))
        else:
            print('No NEWS information found.')

        if changelog_created:
            changelog_basename = os.path.basename(changelog)
            if changelog_is_diff:
                print('ChangeLog between %s and %s is available in %s' % (old_tarball, upstream_tarball_basename, changelog_basename))
            else:
                print('Complete ChangeLog of %s is available in %s' % (upstream_tarball_basename, changelog_basename))
        else:
            print('No ChangeLog information found.')

        if configure_created:
            configure_basename = os.path.basename(configure)
            if configure_is_diff:
                print('Diff in configure.{ac,in} between %s and %s is available in %s' % (old_tarball, upstream_tarball_basename, configure_basename))
            else:
                print('Complete configure.{ac,in} of %s is available in %s' % (upstream_tarball_basename, configure_basename))
        else:
            print('No configure.{ac,in} information found (tarball is probably not using autotools).')

        if meson_created:
            meson_basename = os.path.basename(meson)
            if meson_is_diff:
                print('Diff in meson.build between %s and %s is available in %s' % (old_tarball, upstream_tarball_basename, meson_basename))
            else:
                print('Complete meson.build of %s is available in %s' % (upstream_tarball_basename, meson_basename))
        else:
            print('No meson.build information found (tarball is probably not using meson).')

        if mesonopt_created:
            mesonopt_basename = os.path.basename(mesonopt)
            if mesonopt_is_diff:
                print('Diff in meson_options.txt between %s and %s is available in %s' % (old_tarball, upstream_tarball_basename, mesonopt_basename))
            else:
                print('Complete meson_options.txt of %s is available in %s' % (upstream_tarball_basename, mesonopt_basename))
        else:
            print('No meson_options.txt information found (tarball is probably not using meson or the build has no options).')


    # try applying the patches with rpm quilt
    # not fatal if fails
    if _collab_is_program_in_path('quilt'):
        print('Running quilt...')
        if _collab_quilt_package(spec_file):
            print('Patches still apply.')
        else:
            print('WARNING: make sure that all patches apply before submitting.')
    else:
        print('quilt is not available.')
        print('WARNING: make sure that all patches apply before submitting.')


    # 'osc add newfile.tar.bz2' and 'osc del oldfile.tar.bz2'
    # not fatal if fails
    osc_package = filedir_to_pac(package_dir)

    if old_tarball_with_dir:
        if os.path.exists(old_tarball_with_dir):
            osc_package.delete_file(old_tarball, force=True)
            print('%s has been removed from the package.' % old_tarball)
        else:
            print('WARNING: the previous tarball could not be found. Please manually remove it.')
    else:
        print('WARNING: the previous tarball could not be found. Please manually remove it.')

    osc_package.addfile(upstream_tarball_basename)
    print('%s has been added to the package.' % upstream_tarball_basename)


    print('Package %s has been prepared for the update.' % branch_package)
    print('After having updated %s, you can use \'osc build\' to start a local build or \'osc %s build\' to start a build on the build service.' % (os.path.basename(changes_file), _osc_collab_alias))

    if not ignore_comment:
        _print_comment_after_setup(pkg, no_devel_project)

    # TODO add a note about checking if patches are still needed, buildrequires
    # & requires


#######################################################################


def _collab_forward(apiurl, user, projects, request_id, no_supersede = False):
    try:
        int_request_id = int(request_id)
    except ValueError:
        print('%s is not a valid request id.' % (request_id), file=sys.stderr)
        return

    request = OscCollabObs.get_request(request_id)
    if request is None:
        return

    dest_package = request.target_package
    dest_project = request.target_project

    if dest_project not in projects:
        if len(projects) == 1:
            print('Submission request %s is for %s and not %s. You can use --project to override your project settings.' % (request_id, dest_project, projects[0]), file=sys.stderr)
        else:
            print('Submission request %s is for %s. You can use --project to override your project settings.' % (request_id, dest_project), file=sys.stderr)
        return

    if request.state != 'new':
        print('Submission request %s is not new.' % request_id, file=sys.stderr)
        return

    try:
        pkg = OscCollabApi.get_package_details((dest_project,), dest_package)
        if not pkg or not pkg.parent_project:
            print('No parent project for %s/%s.' % (dest_project, dest_package), file=sys.stderr)
            return
    except OscCollabWebError as e:
        print('Cannot get parent project of %s/%s.' % (dest_project, dest_package), file=sys.stderr)
        return

    try:
        devel_project = show_develproject(apiurl, pkg.parent_project, pkg.parent_package)
    except HTTPError as e:
        print('Cannot get development project for %s/%s: %s' % (pkg.parent_project, pkg.parent_package, e.msg), file=sys.stderr)
        return

    if devel_project != dest_project:
        print('Development project for %s/%s is %s, but package has been submitted to %s.' % (pkg.parent_project, pkg.parent_package, devel_project, dest_project), file=sys.stderr)
        return

    if not OscCollabObs.change_request_state(request_id, 'accepted', 'Forwarding to %s' % pkg.parent_project):
        return

    # TODO: cancel old requests from request.dst_project to parent project

    result = create_submit_request(apiurl,
                                   dest_project, dest_package,
                                   pkg.parent_project, pkg.parent_package,
                                   request.description + ' (forwarded request %s from %s)' % (request_id, request.by))

    print('Submission request %s has been forwarded to %s (request id: %s).' % (request_id, pkg.parent_project, result))

    if not no_supersede:
        for old_id in OscCollabObs.supersede_old_requests(user, pkg.parent_project, pkg.parent_package, result):
            print('Previous submission request %s has been superseded.' % old_id)


#######################################################################


def _collab_osc_package_pending_commit(osc_package):
    # ideally, we could use osc_package.todo, but it's not set by default.
    # So we just look at all files.
    for filename in osc_package.filenamelist + osc_package.filenamelist_unvers:
        status = osc_package.status(filename)
        if status in ['A', 'M', 'D']:
            return True

    return False


def _collab_osc_package_commit(osc_package, msg):
    osc_package.commit(msg)
    # See bug #436932: Package.commit() leads to outdated internal data.
    osc_package.update_datastructs()


#######################################################################


def _collab_package_set_meta(apiurl, project, package, meta, error_msg_prefix = ''):
    if error_msg_prefix:
        error_str = error_msg_prefix + ': %s'
    else:
        error_str = 'Cannot set metadata for %s in %s: %%s' % (package, project)

    (fdout, tmp) = tempfile.mkstemp()
    os.write(fdout, meta)
    os.close(fdout)

    meta_url = make_meta_url('pkg', (quote_plus(project), quote_plus(package)), apiurl)

    failed = False
    try:
        http_PUT(meta_url, file=tmp)
    except HTTPError as e:
        print(error_str % e.msg, file=sys.stderr)
        failed = True

    os.unlink(tmp)
    return not failed


def _collab_enable_build(apiurl, project, package, meta, repos, archs):
    if len(archs) == 0:
        return (True, False)

    package_node = ET.XML(meta)
    meta_xml = ET.ElementTree(package_node)

    build_node = package_node.find('build')
    if not build_node:
        build_node = ET.Element('build')
        package_node.append(build_node)

    enable_found = {}
    for repo in repos:
        enable_found[repo] = {}
        for arch in archs:
            enable_found[repo][arch] = False

    # remove disable before adding enable
    for node in build_node.findall('disable'):
        repo = node.get('repository')
        arch = node.get('arch')

        if repo and repo not in repos:
            continue
        if arch and arch not in archs:
            continue

        build_node.remove(node)

    for node in build_node.findall('enable'):
        repo = node.get('repository')
        arch = node.get('arch')

        if repo and repo not in repos:
            continue
        if arch and arch not in archs:
            continue

        if repo and arch:
            enable_found[repo][arch] = True
        elif repo:
            for arch in enable_found[repo].keys():
                enable_found[repo][arch] = True
        elif arch:
            for repo in enable_found.keys():
                enable_found[repo][arch] = True
        else:
            for repo in enable_found.keys():
                for arch in enable_found[repo].keys():
                    enable_found[repo][arch] = True

    for repo in repos:
        for arch in archs:
            if not enable_found[repo][arch]:
                node = ET.Element('enable', { 'repository': repo, 'arch': arch})
                build_node.append(node)

    all_true = True
    for repo in enable_found.keys():
        for value in enable_found[repo].values():
            if not value:
                all_true = False
                break

    if all_true:
        return (True, False)

    meta = ET.tostring(package_node)

    if _collab_package_set_meta(apiurl, project, package, meta, 'Error while enabling build of package on the build service'):
        return (True, True)
    else:
        return (False, False)


def _collab_get_latest_package_rev_built(apiurl, project, repo, arch, package, verbose_error = True):
    url = makeurl(apiurl, ['build', project, repo, arch, package, '_history'])

    try:
        history = http_GET(url)
    except HTTPError as e:
        if verbose_error:
            print('Cannot get build history: %s' % e.msg, file=sys.stderr)
        return (False, None, None)

    try:
        root = ET.parse(history).getroot()
    except SyntaxError:
        history.close ()
        return (False, None, None)

    max_time = 0
    rev = None
    srcmd5 = None

    for node in root.findall('entry'):
        t = int(node.get('time'))
        if t <= max_time:
            continue

        srcmd5 = node.get('srcmd5')
        rev = node.get('rev')

    history.close ()

    return (True, srcmd5, rev)


def _collab_print_build_status(build_state, header, error_line, hint = False):
    def get_str_repo_arch(repo, arch, show_repos):
        if show_repos:
            return '%s/%s' % (repo, arch)
        else:
            return arch

    print('%s:' % header)

    repos = build_state.keys()
    if not repos or len(repos) == 0:
        print('  %s' % error_line)
        return

    repos_archs = []

    for repo in repos:
        archs = build_state[repo].keys()
        for arch in archs:
            repos_archs.append((repo, arch))
            one_result = True

    if len(repos_archs) == 0:
        print('  %s' % error_line)
        return

    show_hint = False
    show_repos = len(repos) > 1
    repos_archs.sort()

    max_len = 0
    for (repo, arch) in repos_archs:
        l = len(get_str_repo_arch(repo, arch, show_repos))
        if l > max_len:
            max_len = l

    # 4: because we also have a few other characters (see left variable)
    format = '%-' + str(max_len + 4) + 's%s'
    for (repo, arch) in repos_archs:
        if not build_state[repo][arch]['scheduler'] and build_state[repo][arch]['result'] in ['failed']:
            show_hint = True

        left = '  %s: ' % get_str_repo_arch(repo, arch, show_repos)
        if build_state[repo][arch]['result'] in ['unresolved', 'broken', 'blocked', 'finished', 'signing'] and build_state[repo][arch]['details']:
            status = '%s (%s)' % (build_state[repo][arch]['result'], build_state[repo][arch]['details'])
        else:
            status = build_state[repo][arch]['result']

        if build_state[repo][arch]['scheduler']:
            status = '%s (was: %s)' % (build_state[repo][arch]['scheduler'], status)

        print(format % (left, status))

    if show_hint and hint:
        for (repo, arch) in repos_archs:
            if build_state[repo][arch]['result'] == 'failed':
                print('You can see the log of the failed build with: osc buildlog %s %s' % (repo, arch))


def _collab_build_get_results(apiurl, project, repos, package, archs, srcmd5, rev, state, error_counter, verbose_error):
    try:
        results = show_results_meta(apiurl, project, package=package)
        if len(results) == 0:
            if verbose_error:
                print('Error while getting build results of package on the build service: empty results', file=sys.stderr)
            error_counter += 1
            return (True, False, error_counter, state)

        # reset the error counter
        error_counter = 0
    except (HTTPError, BadStatusLine) as e:
        if verbose_error:
            print('Error while getting build results of package on the build service: %s' % e, file=sys.stderr)
        error_counter += 1
        return (True, False, error_counter, state)

    res_root = ET.XML(b''.join(results))
    detailed_results = {}
    repos_archs = []

    for node in res_root.findall('result'):

        repo = node.get('repository')
        # ignore the repo if it's not one we explicitly use
        if not repo in repos:
           continue

        arch = node.get('arch')
        # ignore the archs we didn't explicitly enabled: this ensures we care
        # only about what is really important to us
        if not arch in archs:
            continue

        scheduler_state = node.get('state')
        scheduler_dirty = node.get('dirty') == 'true'

        status_node = node.find('status')
        try:
            status = status_node.get('code')
        except:
            # code can be missing when package is too new:
            status = 'unknown'

        try:
            details = status_node.find('details').text
        except:
            details = None

        if not repo in detailed_results:
            detailed_results[repo] = {}
        detailed_results[repo][arch] = {}
        detailed_results[repo][arch]['status'] = status
        detailed_results[repo][arch]['details'] = details
        detailed_results[repo][arch]['scheduler_state'] = scheduler_state
        detailed_results[repo][arch]['scheduler_dirty'] = scheduler_dirty
        repos_archs.append((repo, arch))

    # evaluate the status: do we need to give more time to the build service?
    # Was the build successful?
    bs_not_ready = False
    do_not_wait_for_bs = False
    build_successful = True

    # A bit paranoid, but it seems it happened to me once...
    if len(repos_archs) == 0:
        bs_not_ready = True
        build_successful = False
        if verbose_error:
            print('Build service did not return any information.', file=sys.stderr)
        error_counter += 1

    for (repo, arch) in repos_archs:
        # first look at the state of the scheduler
        scheduler_state = detailed_results[repo][arch]['scheduler_state']
        scheduler_dirty = detailed_results[repo][arch]['scheduler_dirty']
        if detailed_results[repo][arch]['scheduler_dirty']:
            scheduler_active = 'waiting for scheduler'
        elif scheduler_state in ['unknown', 'scheduling']:
            scheduler_active = 'waiting for scheduler'
        elif scheduler_state in ['blocked']:
            scheduler_active = 'blocked by scheduler'
        else:
            # we don't care about the scheduler state
            scheduler_active = ''

        need_rebuild = False
        value = detailed_results[repo][arch]['status']

        # the scheduler is working, or the result has changed since last time,
        # so we won't trigger a rebuild
        if scheduler_active or state[repo][arch]['result'] != value:
            state[repo][arch]['rebuild'] = -1

        # build is done, but not successful
        if scheduler_active or value not in ['succeeded', 'excluded']:
            build_successful = False

        # we just ignore the status if the scheduler is active, since we know
        # we need to wait for the build service
        if scheduler_active:
            bs_not_ready = True

        # build is happening or will happen soon
        elif value in ['scheduled', 'building', 'dispatching', 'finished', 'signing']:
            bs_not_ready = True

        # sometimes, the scheduler forgets about a package in 'blocked' state,
        # so we have to force a rebuild
        elif value in ['blocked']:
            bs_not_ready = True
            need_rebuild = True

        # build has failed for an architecture: no need to wait for other
        # architectures to know that there's a problem
        elif value in ['failed', 'unresolved', 'broken']:
            do_not_wait_for_bs = True

        # 'disabled' => the build service didn't take into account
        # the change we did to the meta yet (eg).
        elif value in ['unknown', 'disabled']:
            bs_not_ready = True
            need_rebuild = True

        # build is done, but is it for the latest version?
        elif value in ['succeeded']:
            # check that the build is for the version we have
            (success, built_srcmd5, built_rev) = _collab_get_latest_package_rev_built(apiurl, project, repo, arch, package, verbose_error)

            if not success:
                detailed_results[repo][arch]['status'] = 'succeeded, but maybe not up-to-date'
                error_counter += 1
                # we don't know what's going on, so we'll contact the build
                # service again
                bs_not_ready = True
            else:
                # reset the error counter
                error_counter = 0

                #FIXME: "revision" seems to not have the same meaning for the
                # build history and for the local package. See bug #436781
                # (bnc). So, we just ignore the revision for now.
                #if (built_srcmd5, built_rev) != (srcmd5, rev):
                if built_srcmd5 != srcmd5:
                    need_rebuild = True
                    detailed_results[repo][arch]['status'] = 'rebuild needed'

        if not scheduler_active and need_rebuild and state[repo][arch]['rebuild'] == 0:
            bs_not_ready = True

            print('Triggering rebuild for %s as of %s' % (arch, time.strftime('%X (%x)', time.localtime())))

            try:
                rebuild(apiurl, project, package, repo, arch)
                # reset the error counter
                error_counter = 0
            except (HTTPError, BadStatusLine) as e:
                if verbose_error:
                    print('Cannot trigger rebuild for %s: %s' % (arch, e), file=sys.stderr)
                error_counter += 1

        state[repo][arch]['scheduler'] = scheduler_active
        state[repo][arch]['result'] = detailed_results[repo][arch]['status']
        state[repo][arch]['details'] = detailed_results[repo][arch]['details']

        # Update the timeout data
        if scheduler_active:
            pass
        if state[repo][arch]['result'] in ['blocked']:
            # if we're blocked, maybe the scheduler forgot about us, so
            # schedule a rebuild every 60 minutes. The main use case is when
            # you leave the plugin running for a whole night.
            if state[repo][arch]['rebuild'] <= 0:
                state[repo][arch]['rebuild-timeout'] = 60
                state[repo][arch]['rebuild'] = state[repo][arch]['rebuild-timeout']

            # note: it's correct to decrement even if we start with a new value
            # of timeout, since if we don't, it adds 1 minute (ie, 5 minutes
            # instead of 4, eg)
            state[repo][arch]['rebuild'] = state[repo][arch]['rebuild'] - 1
        elif state[repo][arch]['result'] in ['unknown', 'disabled', 'rebuild needed']:
            # if we're in this unexpected state, force the scheduler to do
            # something
            if state[repo][arch]['rebuild'] <= 0:
                # we do some exponential timeout until 60 minutes. We skip
                # timeouts of 1 and 2 minutes since they're quite short.
                if state[repo][arch]['rebuild-timeout'] > 0:
                    state[repo][arch]['rebuild-timeout'] = min(60, state[repo][arch]['rebuild-timeout'] * 2)
                else:
                    state[repo][arch]['rebuild-timeout'] = 4
                state[repo][arch]['rebuild'] = state[repo][arch]['rebuild-timeout']

            # note: it's correct to decrement even if we start with a new value
            # of timeout, since if we don't, it adds 1 minute (ie, 5 minutes
            # instead of 4, eg)
            state[repo][arch]['rebuild'] = state[repo][arch]['rebuild'] - 1
        else:
            # else, we make sure we won't manually trigger a rebuild
            state[repo][arch]['rebuild'] = -1
            state[repo][arch]['rebuild-timeout'] = -1

    if do_not_wait_for_bs:
        bs_not_ready = False

    return (bs_not_ready, build_successful, error_counter, state)


def _collab_build_wait_loop(apiurl, project, repos, package, archs, srcmd5, rev):
    # seconds we wait before looking at the results on the build service
    check_frequency = 60
    max_errors = 10

    build_successful = False
    print_status = False
    error_counter = 0
    last_check = 0

    state = {}
    # When we want to trigger a rebuild for this repo/arch.
    # The initial value is 1 since we don't want to trigger a rebuild the first
    # time when the state is 'disabled' since the state might have changed very
    # recently (if we updated the metadata ourselves), and the build service
    # might have an old build that it can re-use instead of building again.
    for repo in repos:
        state[repo] = {}
        for arch in archs:
            state[repo][arch] = {}
            state[repo][arch]['rebuild'] = -1
            state[repo][arch]['rebuild-timeout'] = -1
            state[repo][arch]['scheduler'] = ''
            state[repo][arch]['result'] = 'unknown'
            state[repo][arch]['details'] = ''

    print("Building on %s..." % ', '.join(repos))
    print("You can press enter to get the current status of the build.")

    # It's important to start the loop by downloading results since we might
    # already have successful builds, and we don't want to wait to know that.

    try:

        while True:
            # get build status if we don't have a recent status
            now = time.time()
            if now - last_check >= 58:
                # 58s since sleep() is not 100% precise and we don't want to miss
                # one turn
                last_check = now

                (need_to_continue, build_successful, error_counter, state) = _collab_build_get_results(apiurl, project, repos, package, archs, srcmd5, rev, state, error_counter, print_status)

                # just stop if there are too many errors
                if error_counter > max_errors:
                    print('Giving up: too many consecutive errors when contacting the build service.', file=sys.stderr)
                    break

            else:
                # we didn't download the results, so we want to continue anyway
                need_to_continue = True

            if print_status:
                header = 'Status as of %s [checking the status every %d seconds]' % (time.strftime('%X (%x)', time.localtime(last_check)), check_frequency)
                _collab_print_build_status(state, header, 'no results returned by the build service')

            if not need_to_continue:
                break


            # and now wait for input/timeout
            print_status = False

            # wait check_frequency seconds or for user input
            now = time.time()
            if now - last_check < check_frequency:
                wait = check_frequency - (now - last_check)
            else:
                wait = check_frequency

            res = select.select([sys.stdin], [], [], wait)

            # we have user input
            if len(res[0]) > 0:
                print_status = True
                # empty sys.stdin
                sys.stdin.readline()


    # we catch this exception here since we might need to revert some metadata
    except KeyboardInterrupt:
        print('')
        print('Interrupted: not waiting for the build to finish. Cleaning up...')

    return (build_successful, state)


#######################################################################


def _collab_autodetect_repo(apiurl, project):
    try:
        meta_lines = show_project_meta(apiurl, project)
        meta = b''.join(meta_lines)
    except HTTPError:
        return None

    try:
        root = ET.XML(meta)
    except SyntaxError:
        return None

    repos = []
    for node in root.findall('repository'):
        name = node.get('name')
        if name:
            repos.append(name)

    if not repos:
        return None

    # This is the list of repositories we prefer, the first one being the
    # preferred one.
    #  + snapshot/standard is what openSUSE:Factory uses, and some other
    #    projects might use this too (snapshot is like standard, except that
    #    packages won't block before getting built).
    #  + openSUSE_Factory is the usual repository for devel projects.
    #  + openSUSE-Factory is a variant of the one above (typo in some project
    #    config?)
    for repo in [ 'snapshot', 'standard', 'openSUSE_Factory', 'openSUSE-Factory' ]:
        if repo in repos:
            return repo

    # No known repository? We try to use the last one named openSUSE* (last
    # one because we want the most recent version of openSUSE).
    opensuse_repos = [ repo for repo in repos if repo.startswith('openSUSE') ]
    if len(opensuse_repos) > 0:
        opensuse_repos.sort(reverse = True)
        return opensuse_repos[0]

    # Still no solution? Let's just take the first one...
    return repos[0]


#######################################################################


def _collab_build_internal(apiurl, osc_package, repos, archs):
    project = osc_package.prjname
    package = osc_package.name

    if '!autodetect!' in repos:
        print('Autodetecting the most appropriate repository for the build...')
        repos.remove('!autodetect!')
        repo = _collab_autodetect_repo(apiurl, project)
        if repo:
            repos.append(repo)

    if len(repos) == 0:
        print('Error while setting up the build: no usable repository.', file=sys.stderr)
        return False

    repos.sort()
    archs.sort()

    # check that build is enabled for this package in this project, and if this
    # is not the case, enable it
    try:
        meta_lines = show_package_meta(apiurl, project, package)
    except HTTPError as e:
        print('Error while checking if package is set to build: %s' % e.msg, file=sys.stderr)
        return False

    meta = b''.join(meta_lines)
    (success, changed_meta) = _collab_enable_build(apiurl, project, package, meta, repos, archs)
    if not success:
        return False

    # loop to periodically check the status of the build (and eventually
    # trigger rebuilds if necessary)
    (build_success, build_state) = _collab_build_wait_loop(apiurl, project, repos, package, archs, osc_package.srcmd5, osc_package.rev)

    if not build_success:
        _collab_print_build_status(build_state, 'Status', 'no status known: osc got interrupted?', hint=True)

    # disable build for package in this project if we manually enabled it
    # (we just reset to the old settings)
    if changed_meta:
        _collab_package_set_meta(apiurl, project, package, meta, 'Error while resetting build settings of package on the build service')

    return build_success


#######################################################################


def _collab_build(apiurl, user, projects, msg, repos, archs):
    try:
        osc_package = filedir_to_pac('.')
    except oscerr.NoWorkingCopy as e:
        print(e, file=sys.stderr)
        return

    project = osc_package.prjname
    package = osc_package.name

    committed = False

    # commit if there are local changes
    if _collab_osc_package_pending_commit(osc_package):
        if not msg:
            msg = edit_message()
        _collab_osc_package_commit(osc_package, msg)
        committed = True

    build_success = _collab_build_internal(apiurl, osc_package, repos, archs)

    if build_success:
        print('Package successfully built on the build service.')


#######################################################################


def _collab_build_submit(apiurl, user, projects, msg, repos, archs, forward = False, no_unreserve = False, no_supersede = False):
    try:
        osc_package = filedir_to_pac('.')
    except oscerr.NoWorkingCopy as e:
        print(e, file=sys.stderr)
        return

    project = osc_package.prjname
    package = osc_package.name

    # do some preliminary checks on the package/project: it has to be
    # a branch of a development project
    if not osc_package.islink():
        print('Package is not a link.', file=sys.stderr)
        return

    parent_project = osc_package.linkinfo.project
    if not parent_project in projects:
        if len(projects) == 1:
            print('Package links to project %s and not %s. You can use --project to override your project settings.' % (parent_project, projects[0]), file=sys.stderr)
        else:
            print('Package links to project %s. You can use --project to override your project settings.' % parent_project, file=sys.stderr)
        return

    if not project.startswith('home:%s:branches' % user):
        print('Package belongs to project %s which does not look like a branch project.' % project, file=sys.stderr)
        return

    if project != 'home:%s:branches:%s' % (user, parent_project):
        print('Package belongs to project %s which does not look like a branch project for %s.' % (project, parent_project), file=sys.stderr)
        return


    # get the message that will be used for commit & request
    if not msg:
        msg = edit_message(footer='This message will be used for the commit (if necessary) and the request.\n')

    committed = False

    # commit if there are local changes
    if _collab_osc_package_pending_commit(osc_package):
        _collab_osc_package_commit(osc_package, msg)
        committed = True

    build_success = _collab_build_internal(apiurl, osc_package, repos, archs)

    # if build successful, submit
    if build_success:
        result = create_submit_request(apiurl,
                                       project, package,
                                       parent_project, package,
                                       msg)

        print('Package submitted to %s (request id: %s).' % (parent_project, result))

        if not no_supersede:
            for old_id in OscCollabObs.supersede_old_requests(user, parent_project, package, result):
                print('Previous submission request %s has been superseded.' % old_id)

        if forward:
            # we volunteerly restrict the project list to parent_project for
            # self-consistency and more safety
            _collab_forward(apiurl, user, [ parent_project ], result, no_supersede = no_supersede)

        if not no_unreserve:
            try:
                reservation = OscCollabApi.is_package_reserved((parent_project,), package, no_devel_project = True)
                if reservation and reservation.user == user:
                    _collab_unreserve((parent_project,), (package,), user, no_devel_project = True)
            except OscCollabWebError as e:
                print(e.msg, file=sys.stderr)
    else:
        print('Package was not submitted to %s' % parent_project)


#######################################################################


# TODO
# Add a commit method.
# This will make some additional checks:
#   + if we used update, we can initialize a list of patches/sources
#     before any change. This way, on the commit, we can look if the
#     remaining files are still referenced in the .spec, and if not
#     complain if the file hasn't been removed from the directory.
#     We can also complain if a file hasn't been added with osc add,
#     while it's referenced.
#   + complain if the lines in .changes are too long


#######################################################################


# Unfortunately, as of Python 2.5, ConfigParser does not know how to
# preserve a config file: it removes comments and reorders stuff.
# This is a dumb function to append a value to a section in a config file.
def _collab_add_config_option(section, key, value):
    global _osc_collab_osc_conffile

    conffile = _osc_collab_osc_conffile

    if not os.path.exists(conffile):
        lines = [ ]
    else:
        fin = open(conffile, 'r')
        lines = fin.readlines()
        fin.close()

    (fdout, tmp) = tempfile.mkstemp(prefix = os.path.basename(conffile), dir = os.path.dirname(conffile))

    in_section = False
    added = False
    empty_line = False

    valid_sections = [ '[' + section + ']' ]
    if section.startswith('http'):
        if section.endswith('/'):
            valid_sections.append('[' + section[:-1] + ']')
        else:
            valid_sections.append('[' + section + '/]')

    for line in lines:
        if line.rstrip() in valid_sections:
            in_section = True
        # key was not in the section: let's add it
        elif line[0] == '[' and in_section and not added:
            if not empty_line:
                os.write(fdout, b'\n')
            write_line = '%s = %s\n\n' % (key, value)
            os.write(fdout, write_line.encode('utf-8'))
            added = True
            in_section = False
        elif line[0] == '[' and in_section:
            in_section = False
        # the section/key already exists: we replace
        # 'not added': in case there are multiple sections with the same name
        elif in_section and not added and line.startswith(key):
            index = line.find('=')
            if line[:index].rstrip() == key:
                line = '%s= %s\n' % (line[:index], value)
                added = True

        os.write(fdout, line.encode('utf-8'))

        empty_line = line.strip() == ''

    if not added:
        if not empty_line:
            os.write(fdout, b'\n')
        if not in_section:
            write_line = '[%s]\n' % (section,)
            os.write(fdout, write_line.encode('utf-8'))
        write_line = '%s = %s\n' % (key, value)
        os.write(fdout, write_line.encode('utf-8'))

    os.close(fdout)
    os.rename(tmp, conffile)


#######################################################################


def _collab_get_compatible_apiurl_for_config(config, apiurl):
    if apiurl is None:
        return None

    if config.has_section(apiurl):
        return apiurl

    # first try adding/removing a trailing slash to the API url
    if apiurl.endswith('/'):
        apiurl = apiurl[:-1]
    else:
        apiurl = apiurl + '/'

    if config.has_section(apiurl):
        return apiurl

    # old osc (0.110) was adding the host to the tuple without the http
    # part, ie just the host
    apiurl = urlparse(apiurl).netloc

    if apiurl and config.has_section(apiurl):
        return apiurl

    return None


def _collab_get_config_parser():
    global _osc_collab_config_parser
    global _osc_collab_osc_conffile

    if _osc_collab_config_parser is not None:
        return _osc_collab_config_parser

    conffile = _osc_collab_osc_conffile
    _osc_collab_config_parser = configparser.SafeConfigParser()
    _osc_collab_config_parser.read(conffile)
    return _osc_collab_config_parser


def _collab_get_config(apiurl, key, default = None):
    config = _collab_get_config_parser()
    if not config:
        return default

    apiurl = _collab_get_compatible_apiurl_for_config(config, apiurl)
    if apiurl and config.has_option(apiurl, key):
        return config.get(apiurl, key)
    elif config.has_option('general', key):
        return config.get('general', key)
    else:
        return default


def _collab_get_config_bool(apiurl, key, default = None):
    value = _collab_get_config(apiurl, key, default)
    if type(value) == bool:
        return value

    if value.lower() in [ 'true', 'yes' ]:
        return True
    try:
        return int(value) != 0
    except:
        pass
    return False

def _collab_get_config_list(apiurl, key, default = None):
    def split_items(line):
        items = line.split(';')
        # remove all empty items
        while True:
            try:
                items.remove('')
            except ValueError:
                break
        return items

    line = _collab_get_config(apiurl, key, default)

    items = split_items(line)
    if not items and default:
        if type(default) == str:
            items = split_items(default)
        else:
            items = default
    return items


#######################################################################


def _collab_migrate_gnome_config(apiurl):
    for key in [ 'archs', 'apiurl', 'email', 'projects' ]:
        if _collab_get_config(apiurl, 'collab_' + key) is not None:
            continue
        elif not ('gnome_' + key) in conf.config:
            continue
        _collab_add_config_option(apiurl, 'collab_' + key, conf.config['gnome_' + key])

    # migrate repo to repos
    if _collab_get_config(apiurl, 'collab_repos') is None and 'gnome_repo' in conf.config:
        _collab_add_config_option(apiurl, 'collab_repos', conf.config['gnome_repo'] + ';')


#######################################################################


def _collab_ensure_email(apiurl):
    email = _collab_get_config(apiurl, 'email')
    if email:
        return email
    email = _collab_get_config(apiurl, 'collab_email')
    if email:
        return email

    email =  raw_input('E-mail address to use for .changes entries: ')
    if email == '':
        return 'EMAIL@DOMAIN'

    _collab_add_config_option(apiurl, 'collab_email', email)

    return email


#######################################################################


def _collab_parse_arg_packages(packages):
    def remove_trailing_slash(s):
        if s.endswith('/'):
            return s[:-1]
        return s

    if type(packages) == str:
        return remove_trailing_slash(packages)
    elif type(packages) in [ list, tuple ]:
        return [ remove_trailing_slash(package) for package in packages ]
    else:
        return packages


#######################################################################


@cmdln.alias('gnome')
@cmdln.option('-A', '--apiurl', metavar='URL',
              dest='apiurl',
              help='url to use to connect to the database (different from the build service server)')
@cmdln.option('--xs', '--exclude-submitted', action='store_true',
              dest='exclude_submitted',
              help='do not show submitted packages in the output')
@cmdln.option('--xr', '--exclude-reserved', action='store_true',
              dest='exclude_reserved',
              help='do not show reserved packages in the output')
@cmdln.option('--xc', '--exclude-commented', action='store_true',
              dest='exclude_commented',
              help='do not show commented packages in the output')
@cmdln.option('--xd', '--exclude-devel', action='store_true',
              dest='exclude_devel',
              help='do not show packages that are up-to-date in their development project in the output')
@cmdln.option('--ic', '--ignore-comments', action='store_true',
              dest='ignore_comments',
              help='ignore the comments')
@cmdln.option('--ir', '--ignore-reserved', action='store_true',
              dest='ignore_reserved',
              help='ignore the reservation state of the package if necessary')
@cmdln.option('--iu', '--include-upstream', action='store_true',
              dest='include_upstream',
              help='include reports about missing upstream data')
@cmdln.option('--nr', '--no-reserve', action='store_true',
              dest='no_reserve',
              help='do not reserve the package')
@cmdln.option('--ns', '--no-supersede', action='store_true',
              dest='no_supersede',
              help='do not supersede requests to the same package')
@cmdln.option('--nu', '--no-unreserve', action='store_true',
              dest='no_unreserve',
              help='do not unreserve the package')
@cmdln.option('--nodevelproject', action='store_true',
              dest='no_devel_project',
              help='do not use development project of the packages')
@cmdln.option('--nobranch', action='store_true',
              dest='no_branch',
              help='do not branch the package in your home project')
@cmdln.option('-m', '--message', metavar='TEXT',
              dest='msg',
              help='specify log message TEXT')
@cmdln.option('-f', '--forward', action='store_true',
              dest='forward',
              help='automatically forward to parent project if successful')
@cmdln.option('--no-details', action='store_true',
              dest='no_details',
              help='do not show more details')
@cmdln.option('--details', action='store_true',
              dest='details',
              help='show more details')
@cmdln.option('--project', metavar='PROJECT', action='append',
              dest='projects', default=[],
              help='project to work on (default: openSUSE:Factory)')
@cmdln.option('--repo', metavar='REPOSITORY', action='append',
              dest='repos', default=[],
              help='build repositories to build on (default: automatic detection)')
@cmdln.option('--arch', metavar='ARCH', action='append',
              dest='archs', default=[],
              help='architectures to build on (default: i586 and x86_64)')
@cmdln.option('--nc', '--no-cache', action='store_true',
              dest='no_cache',
              help='ignore data from the cache')
@cmdln.option('-v', '--version', action='store_true',
              dest='version',
              help='show version of the plugin')
def do_collab(self, subcmd, opts, *args):
    """${cmd_name}: Various commands to ease collaboration on the openSUSE Build Service.

    A tutorial and detailed documentation are available at:
      http://en.opensuse.org/openSUSE:Osc_Collab

    "todo" (or "t") will list the packages that need some action.

    "todoadmin" (or "ta") will list the packages from the project that need
    to be submitted to the parent project, and various other errors or tasks.

    "listreserved" (or "lr") will list the reserved packages.

    "isreserved" (or "ir") will look if a package is reserved.

    "reserve" (or "r") will reserve a package so other people know you're
    working on it.

    "unreserve" (or "u") will remove the reservation you had on a package.

    "listcommented" (or "lc") will list the commented packages.

    "comment" (or "c") will look if a package is commented.

    "commentset" (or "cs") will add to a package a comment you want to share
    with other people.

    "commentunset" (or "cu") will remove the comment you set on a package.

    "setup" (or "s") will prepare a package for work (possibly reservation,
    branch, checking out, etc.). The package will be checked out in the current
    directory.

    "update" (or "up") will prepare a package for update (possibly reservation,
    branch, checking out, download of the latest upstream tarball, .spec
    edition, etc.). The package will be checked out in the current directory.

    "forward" (or "f") will forward a request to the project to parent project.
    This includes the step of accepting the request first.

    "build" (or "b") will commit the local changes of the package in
    the current directory and wait for the build to succeed on the build
    service.

    "buildsubmit" (or "bs") will commit the local changes of the package in
    the current directory, wait for the build to succeed on the build service
    and if the build succeeds, submit the package to the development project.

    Usage:
        osc collab todo [--exclude-submitted|--xs] [--exclude-reserved|--xr] [--exclude-commented|--xc] [--exclude-devel|--xd] [--ignore-comments|--ic] [--details|--no-details] [--project=PROJECT]
        osc collab todoadmin [--include-upstream|--iu] [--project=PROJECT]

        osc collab listreserved
        osc collab isreserved [--nodevelproject] [--project=PROJECT] PKG [...]
        osc collab reserve [--nodevelproject] [--project=PROJECT] PKG [...]
        osc collab unreserve [--nodevelproject] [--project=PROJECT] PKG [...]

        osc collab listcommented
        osc collab comment [--nodevelproject] [--project=PROJECT] PKG [...]
        osc collab commentset [--nodevelproject] [--project=PROJECT] PKG COMMENT
        osc collab commentunset [--nodevelproject] [--project=PROJECT] PKG [...]

        osc collab setup [--ignore-reserved|--ir] [--ignore-comments|--ic] [--no-reserve|--nr] [--nodevelproject] [--nobranch] [--project=PROJECT] PKG
        osc collab update [--ignore-reserved|--ir] [--ignore-comments|--ic] [--no-reserve|--nr] [--nodevelproject] [--nobranch] [--project=PROJECT] PKG

        osc collab forward [--no-supersede|--ns] [--project=PROJECT] ID

        osc collab build [--message=TEXT|-m=TEXT] [--repo=REPOSITORY] [--arch=ARCH]
        osc collab buildsubmit [--forward|-f] [--no-supersede|--ns] [--no-unreserve|--nu] [--message=TEXT|-m=TEXT] [--repo=REPOSITORY] [--arch=ARCH]
    ${cmd_option_list}
    """

    # uncomment this when profiling is needed
    #self.ref = time.time()
    #print("%.3f - %s" % (time.time()-self.ref, 'start'))

    global _osc_collab_alias
    global _osc_collab_osc_conffile

    _osc_collab_alias = self.lastcmd[0]

    if opts.version:
        print(OSC_COLLAB_VERSION)
        return

    cmds = ['todo', 't', 'todoadmin', 'ta', 'listreserved', 'lr', 'isreserved', 'ir', 'reserve', 'r', 'unreserve', 'u', 'listcommented', 'lc', 'comment', 'c', 'commentset', 'cs', 'commentunset', 'cu', 'setup', 's', 'update', 'up', 'forward', 'f', 'build', 'b', 'buildsubmit', 'bs']
    if not args or args[0] not in cmds:
        raise oscerr.WrongArgs('Unknown %s action. Choose one of %s.' % (_osc_collab_alias, ', '.join(cmds)))

    cmd = args[0]

    # Check arguments validity
    if cmd in ['listreserved', 'lr', 'listcommented', 'lc', 'todo', 't', 'todoadmin', 'ta', 'build', 'b', 'buildsubmit', 'bs']:
        min_args, max_args = 0, 0
    elif cmd in ['setup', 's', 'update', 'up', 'forward', 'f']:
        min_args, max_args = 1, 1
    elif cmd in ['commentset', 'cs']:
        min_args, max_args = 1, 2
    elif cmd in ['isreserved', 'ir', 'reserve', 'r', 'unreserve', 'u', 'comment', 'c', 'commentunset', 'cu']:
        min_args = 1
        max_args = sys.maxsize
    else:
        raise RuntimeError('Unknown command: %s' % cmd)

    if len(args) - 1 < min_args:
        raise oscerr.WrongArgs('Too few arguments.')
    if len(args) - 1 > max_args:
        raise oscerr.WrongArgs('Too many arguments.')

    if opts.details and opts.no_details:
        raise oscerr.WrongArgs('--details and --no-details cannot be used at the same time.')

    apiurl = conf.config['apiurl']
    user = conf.config['user']

    # See get_config() in osc/conf.py and postoptparse() in
    # osc/commandline.py
    if self.options.conffile:
        conffile = self.options.conffile
    else:
        conffile = conf.identify_conf()
    _osc_collab_osc_conffile = os.path.expanduser(conffile)

    _collab_migrate_gnome_config(apiurl)
    email = _collab_ensure_email(apiurl)

    if opts.apiurl:
        collab_apiurl = opts.apiurl
    else:
        collab_apiurl = _collab_get_config(apiurl, 'collab_apiurl')

    if len(opts.projects) != 0:
        projects = opts.projects
    else:
        projects = _collab_get_config_list(apiurl, 'collab_projects', 'openSUSE:Factory')

    if len(opts.repos) != 0:
        repos = opts.repos
    else:
        repos = _collab_get_config_list(apiurl, 'collab_repos', '!autodetect!')

    if len(opts.archs) != 0:
        archs = opts.archs
    else:
        archs = _collab_get_config_list(apiurl, 'collab_archs', 'i586;x86_64;')

    details = _collab_get_config_bool(apiurl, 'collab_details', False)
    if details and opts.no_details:
        details = False
    elif not details and opts.details:
        details = True

    OscCollabApi.init(collab_apiurl)
    OscCollabCache.init(opts.no_cache)
    OscCollabObs.init(apiurl)

    # Do the command
    if cmd in ['todo', 't']:
        _collab_todo(apiurl, projects, details, opts.ignore_comments, opts.exclude_commented, opts.exclude_reserved, opts.exclude_submitted, opts.exclude_devel)

    elif cmd in ['todoadmin', 'ta']:
        _collab_todoadmin(apiurl, projects, opts.include_upstream)

    elif cmd in ['listreserved', 'lr']:
        _collab_listreserved(projects)

    elif cmd in ['isreserved', 'ir']:
        packages = _collab_parse_arg_packages(args[1:])
        _collab_isreserved(projects, packages, no_devel_project = opts.no_devel_project)

    elif cmd in ['reserve', 'r']:
        packages = _collab_parse_arg_packages(args[1:])
        _collab_reserve(projects, packages, user, no_devel_project = opts.no_devel_project)

    elif cmd in ['unreserve', 'u']:
        packages = _collab_parse_arg_packages(args[1:])
        _collab_unreserve(projects, packages, user, no_devel_project = opts.no_devel_project)

    elif cmd in ['listcommented', 'lc']:
        _collab_listcommented(projects)

    elif cmd in ['comment', 'c']:
        packages = _collab_parse_arg_packages(args[1:])
        _collab_comment(projects, packages, no_devel_project = opts.no_devel_project)

    elif cmd in ['commentset', 'cs']:
        packages = _collab_parse_arg_packages(args[1])
        if len(args) - 1 == 1:
            comment = edit_message()
        else:
            comment = args[2]
        _collab_commentset(projects, packages, user, comment, no_devel_project = opts.no_devel_project)

    elif cmd in ['commentunset', 'cu']:
        packages = _collab_parse_arg_packages(args[1:])
        _collab_commentunset(projects, packages, user, no_devel_project = opts.no_devel_project)

    elif cmd in ['setup', 's']:
        package = _collab_parse_arg_packages(args[1])
        _collab_setup(apiurl, user, projects, package, ignore_reserved = opts.ignore_reserved, ignore_comment = opts.ignore_comments, no_reserve = opts.no_reserve, no_devel_project = opts.no_devel_project, no_branch = opts.no_branch)

    elif cmd in ['update', 'up']:
        package = _collab_parse_arg_packages(args[1])
        _collab_update(apiurl, user, email, projects, package, ignore_reserved = opts.ignore_reserved, ignore_comment = opts.ignore_comments, no_reserve = opts.no_reserve, no_devel_project = opts.no_devel_project, no_branch = opts.no_branch)

    elif cmd in ['forward', 'f']:
        request_id = args[1]
        _collab_forward(apiurl, user, projects, request_id, no_supersede = opts.no_supersede)

    elif cmd in ['build', 'b']:
        _collab_build(apiurl, user, projects, opts.msg, repos, archs)

    elif cmd in ['buildsubmit', 'bs']:
        _collab_build_submit(apiurl, user, projects, opts.msg, repos, archs, forward = opts.forward, no_unreserve = opts.no_unreserve, no_supersede = opts.no_supersede)

    else:
        raise RuntimeError('Unknown command: %s' % cmd)
