#
# spec file for package python-agate-excel
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-agate-excel
Version:        0.4.2
Release:        0
Summary:        Read support for Excel files (xls and xlsx) for agate
License:        MIT
URL:            https://github.com/wireservice/agate-excel
Source:         https://github.com/wireservice/agate-excel/archive/%{version}.tar.gz
BuildRequires:  %{python_module agate >= 1.5.0}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module olefile}
BuildRequires:  %{python_module openpyxl >= 2.3.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xlrd >= 0.9.4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-agate >= 1.5.0
Requires:       python-numpy
Requires:       python-olefile
Requires:       python-openpyxl >= 2.3.0
Requires:       python-xlrd >= 0.9.4
BuildArch:      noarch
%python_subpackages

%description
Agate-excel adds read support for Excel files (xls and xlsx)
to agate.

%prep
%autosetup -p1 -n agate-excel-%{version}

sed -i -e '/^#!\//, 1d' agateexcel/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.rst README.rst
%license COPYING
%{python_sitelib}/agateexcel
%{python_sitelib}/agate_excel-%{version}.dist-info

%changelog
