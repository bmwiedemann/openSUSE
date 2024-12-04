#
# spec file for package python-MapProxy
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%if 0%{?suse_version} >= 1550
# Restrict to primary python on Tumbleweed
%define pythons python3
%else
%{?sle15_python_module_pythons}
%endif

Name:           python-MapProxy
Version:        2.0.2
Release:        0
Summary:        Proxy for geospatial data
License:        Apache-2.0
URL:            http://mapproxy.org/
Group:          Development/Languages/Python
Source0:        https://files.pythonhosted.org/packages/source/M/MapProxy/MapProxy-%{version}.tar.gz
# test files missing in the sdist
Source1:        https://github.com/mapproxy/mapproxy/raw/%{version}/mapproxy/test/system/fixture/cache.gpkg
Source2:        https://github.com/mapproxy/mapproxy/raw/%{version}/mapproxy/test/unit/polygons/polygons.geojson
Source99:       python-MapProxy-rpmlintrc
BuildRequires:  %{python_module GDAL}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyYAML >= 3.0}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test
BuildRequires:  %{python_module Paste}
BuildRequires:  %{python_module Shapely >= 2}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module botocore}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module greenlet}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module moto}
BuildRequires:  %{python_module pyproj}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module requests}
BuildRequires:  proj
# /SECTION
Requires:       proj
Requires:       python-Pillow
Requires:       python-PyYAML >= 3.0
Recommends:     python-GDAL
Recommends:     python-Shapely >= 1.8
Provides:       python-mapproxy = %{version}-%{release}
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
MapProxy is an open source proxy for geospatial data. It caches,
accelerates and transforms data from existing map services and
serves any desktop or web GIS client.

%prep
%autosetup -p1 -n MapProxy-%{version}
# Source1 required twice
cp %{SOURCE1} mapproxy/test/system/fixture/
mkdir -p mapproxy/test/unit/fixture/
cp %{SOURCE1} mapproxy/test/unit/fixture/
cp %{SOURCE2} mapproxy/test/unit/polygons
# fix wrong interpreter in test scripts
sed -i 's/env python.*$/python3/' mapproxy/test/unit/test_client_cgi.py mapproxy/test/system/fixture/minimal_cgi.py
chmod +x mapproxy/test/system/fixture/minimal_cgi.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/mapproxy-seed
%python_clone -a %{buildroot}%{_bindir}/mapproxy-util

%check
# for local tests outside of obs
#export MAPPROXY_TEST_COUCHDB=http://127.0.0.1:5984
#export MAPPROXY_TEST_REDIS=127.0.0.1:6379
export BOTO_CONFIG=/doesnotexist
# online tests or no local server started
donttest="TestCouchDBCache"
donttest="$donttest or TestRedisCache"
donttest="$donttest or test_https_"
donttest="$donttest or mapproxy.script.export.resolve_source"
# flaky
donttest="$donttest or (TestWMS130 and test_get_map)"
# unexcpected mime type
donttest="$donttest or TestMapServerCGI"
# can't write temporary minimal script (?)
donttest="$donttest or TestCGIClient"
%pytest mapproxy -ra -k "not ($donttest)"

%post
%python_install_alternative mapproxy-seed mapproxy-util

%postun
%python_uninstall_alternative mapproxy-seed

%files %{python_files}
%doc CHANGES.txt README.rst
%license COPYING.txt LICENSE.txt
%python_alternative %{_bindir}/mapproxy-seed
%python_alternative %{_bindir}/mapproxy-util
%{python_sitelib}/mapproxy
%{python_sitelib}/MapProxy-%{version}.dist-info

%changelog
