#
# spec file for package python-geomdl
#
# Copyright (c) 2020 SUSE LLC
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


%define archivename NURBS-Python
%define packagename geomdl
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-geomdl
Version:        5.2.10
Release:        0
Summary:        Object-oriented B-Spline and NURBS evaluation library
License:        MIT
URL:            https://github.com/orbingol/NURBS-Python
Source:         https://github.com/orbingol/NURBS-Python/archive/v%{version}.tar.gz#/%{archivename}-%{version}.tar.gz
BuildRequires:  %{python_module matplotlib >= 2.2.3}
BuildRequires:  %{python_module numpy >= 1.15.4}
BuildRequires:  %{python_module plotly}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib >= 2.2.3
Requires:       python-numpy >= 1.15.4
Requires:       python-plotly
BuildArch:      noarch
%python_subpackages

%description
NURBS-Python (geomdl) is a pure Python, self-contained, object-oriented
B-Spline and NURBS spline library.

%prep
%setup -q -n %{archivename}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*egg-info
%{python_sitelib}/%{packagename}

%changelog
