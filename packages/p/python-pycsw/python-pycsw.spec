#
# spec file for package python-pycsw
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
%define         skip_python36 1
Name:           python-pycsw
Version:        2.6.1
Release:        0
Summary:        OGC CSW server implementation written in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://pycsw.org/
# Use the GitHub archive instead of pypi because it has the test suite
Source:         https://github.com/geopython/pycsw/archive/refs/tags/%{version}.tar.gz#/pycsw-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM pycsw-pr671-rm-json-encoding.patch -- gh#geopython/pycsw#671
Patch0:         https://github.com/geopython/pycsw/pull/671.patch#/pycsw-pr671-rm-json-encoding.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-OWSLib >= 0.16.0
Requires:       python-Shapely >= 1.5.17
Requires:       python-geolinks >= 0.2.0
Requires:       python-lxml >= 3.6.2
Requires:       python-pyproj >= 1.9.5.1
Requires:       python-xmltodict >= 0.10.2
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module apipkg}
BuildRequires:  %{python_module OWSLib >= 0.16.0}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module Shapely >= 1.5.17}
BuildRequires:  %{python_module geolinks >= 0.2.0}
BuildRequires:  %{python_module lxml >= 3.6.2}
BuildRequires:  %{python_module pyproj >= 1.9.5.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module xmltodict >= 0.10.2}
# /SECTION
%python_subpackages

%description
PyCSW implements clause 10 (HTTP protocol binding (Catalogue Services
for the Web, CSW)) of the OpenGIS Catalogue Service Implementation
Specification, version 2.0.2.  The  project  is  certified  OGC
Compliant,  and  is  an  OGC  Reference  Implementation. PyCSW allows
for the publishing and discovery of geospatial metadata. Existing
repositories of geospatial metadata can be exposed via OGC:CSW 2.0.2.

%prep
%autosetup -p1 -n pycsw-%{version}
# remove extra mock
sed -i 's/import mock/from unittest import mock/' tests/unittests/test_{wsgi,util}.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pycsw-admin.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# online connection to demo.pycsw.org
donttest="(GetRecords and distributedsearch)"
# pyproj database context missing
donttest+=" or (default_post_GetRecords-filter-bbox-reproject)"
# many fail, not tested in upstream CI either
donttest+=" or (functional and harvesting)"
%pytest -ra -k "not ($donttest)"

%post
%python_install_alternative pycsw-admin.py

%postun
%python_uninstall_alternative pycsw-admin.py

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/pycsw-admin.py
%{python_sitelib}/*

%changelog
