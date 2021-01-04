#
# spec file for package python-folium
#
# Copyright (c) 2021 SUSE LLC
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


%define skip_python2 1
%define modname folium
Name:           python-folium
Version:        0.11.0
Release:        0
Summary:        Make beautiful maps with Leafletjs and Python
License:        MIT
URL:            https://github.com/python-visualization/folium
# PYPI TARBALLS DONT HAVE THE test DIR
Source:         https://github.com/python-visualization/folium/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 0001-assert-bounds-within-reasonable-machine-precision.patch -- gh#python-visualization/folium#1432 Fix float bounds assertion on 32bit platform
Patch0:         0001-assert-bounds-within-reasonable-machine-precision.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 2.9}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module branca >= 0.3.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
# /SECTION
Requires:       python-Jinja2 >= 2.9
Requires:       python-branca >= 0.3.0
Requires:       python-numpy
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
Folium is a python library to make beautiful maps with Leafletsjs. Folium
builds on the data wrangling strengths of the Python ecosystem and the mapping
strengths of the Leaflet.js library. Manipulate your data in Python, then
visualize it in a Leaflet map via folium.

%prep
%autosetup -p1 -n folium-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_json_request REQUIRES NETWORK ACCESS
%pytest -k 'not test_json_request'

%files %{python_files}
%doc CHANGES.txt README.rst
%license LICENSE.txt
%{python_sitelib}/%{modname}/
%{python_sitelib}/%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
