#
# spec file for package python-folium
#
# Copyright (c) 2025 SUSE LLC
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


%define modname folium
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-folium%{psuffix}
Version:        0.19.4
Release:        0
Summary:        Make beautiful maps with Leafletjs and Python
License:        MIT
URL:            https://github.com/python-visualization/folium
# PyPI does not have an sdist, plus we need the tests from GitHub.
Source0:        https://github.com/python-visualization/folium/archive/v%{version}.tar.gz#/folium-%{version}-gh.tar.gz
BuildRequires:  %{python_module base > 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module Jinja2 >= 2.9}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module branca >= 0.6.0}
BuildRequires:  %{python_module folium = %{version}}
BuildRequires:  %{python_module geopandas}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module xyzservices}
# No working chromedriver
#BuildRequires:  %%{python_module selenium}
#BuildRequires:  %%{python_module nbconvert}
%endif
Requires:       python-Jinja2 >= 2.9
Requires:       python-branca >= 0.6.0
Requires:       python-numpy
Requires:       python-requests
Requires:       python-xyzservices
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
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%if !%{with test}
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# no working chromedriver for selenium
ignoretests="--ignore tests/selenium"
# requires network access
donttest="test_json_request or test_timedynamic_geo_json"
# also uses selenium
donttest="$donttest or test__repr_png_is_bytes or test_valid_png or test_valid_png_size"
# no proj database backend running
donttest="$donttest or test_choropleth_geopandas"
%pytest -k "not ($donttest)" $ignoretests
%endif

%if !%{with test}
%files %{python_files}
%doc CHANGES.txt README.rst
%license LICENSE.txt
%{python_sitelib}/folium/
%{python_sitelib}/folium-%{version}.dist-info/
%endif

%changelog
