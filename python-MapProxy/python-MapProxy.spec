#
# spec file for package python-MapProxy
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


# Tests require a network connection
%bcond_with test

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define oldpython python
Name:           python-MapProxy
Version:        1.11.0
Release:        0
Summary:        Proxy for geospatial data
License:        Apache-2.0
Url:            http://mapproxy.org/
Group:          Development/Languages/Python
Source0:        https://files.pythonhosted.org/packages/source/M/MapProxy/MapProxy-%{version}.tar.gz
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module GDAL}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  geos-devel
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig(gdal)
BuildRequires:  pkgconfig(proj)
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module Paste}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module boto3}
BuildRequires:  %{python_module botocore}
BuildRequires:  %{python_module eventlet}
BuildRequires:  %{python_module greenlet}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module riak}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module requests}
BuildRequires:  libgeos_c1
BuildRequires:  proj
%endif
Requires:       libgeos_c1
Requires:       proj
Requires:       python-Shapely
Requires:       python-gdal
Requires:       python-lxml
Requires:       python-Pillow
Requires:       python-PyYAML
Recommends:     python-Paste
Recommends:     python-Werkzeug
Recommends:     python-boto3
Recommends:     python-botocore
Recommends:     python-eventlet
Recommends:     python-greenlet
Recommends:     python-lxml
Recommends:     python-redis
Recommends:     python-requests
Recommends:     python-riak
BuildArch:      noarch
%ifpython2
Obsoletes:      %{oldpython}-mapproxy < %{version}
Provides:       %{oldpython}-mapproxy = %{version}
%endif
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
%python_subpackages

%description
MapProxy is an open source proxy for geospatial data. It caches,
accelerates and transforms data from existing map services and
serves any desktop or web GIS client.

%prep
%setup -q -n MapProxy-%{version}
# Fix non-executable-script
sed -i -e '/^#! \//, 1d' mapproxy/test/system/fixture/cgi.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/mapproxy-seed
%python_clone -a %{buildroot}%{_bindir}/mapproxy-util

%post
%{python_install_alternative mapproxy-seed mapproxy-util}

%postun
%python_uninstall_alternative mapproxy-seed

%if %{with test}
%check
export MAPPROXY_TEST_COUCHDB=http://127.0.0.1:5984
export MAPPROXY_TEST_REDIS=127.0.0.1:6379
export BOTO_CONFIG=/doesnotexist
%python_exec setup.py test
%endif

%files %{python_files}
%doc CHANGES.txt README.rst
%license COPYING.txt LICENSE.txt 
%python_alternative %{_bindir}/mapproxy-seed
%python_alternative %{_bindir}/mapproxy-util
%{python_sitelib}/*


%changelog
