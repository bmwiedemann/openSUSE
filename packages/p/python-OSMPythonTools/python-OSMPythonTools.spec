#
# spec file for package python-OSMPythonTools
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


%define modname OSMPythonTools
%{?sle15_python_module_pythons}
Name:           python-OSMPythonTools
Version:        0.3.5
Release:        0
Summary:        A library to access OpenStreetMap related services
License:        GPL-3.0-only
URL:            https://github.com/mocnik-science/osm-python-tools
Source:         https://github.com/mocnik-science/osm-python-tools/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-beautifulsoup4
Requires:       python-geojson
Requires:       python-lxml
Requires:       python-numpy
Requires:       python-pandas
Requires:       python-ujson
Requires:       python-xarray
BuildArch:      noarch
%python_subpackages

%description
A library to access OpenStreetMap related services

%prep
%autosetup -p1 -n osm-python-tools-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Unfortunately, most tests access particular APIs over the net.

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*-info

%changelog
