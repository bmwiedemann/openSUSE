#
# spec file for package python-agate-dbf
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


%{?sle15_python_module_pythons}
Name:           python-agate-dbf
Version:        0.2.3
Release:        0
Summary:        Read support for dbf files for agate
License:        MIT
URL:            http://agate-dbf.readthedocs.org/
# https://github.com/wireservice/agate-dbf/issues/4
Source:         https://github.com/wireservice/agate-dbf/archive/%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module agate >= 1.5.0}
BuildRequires:  %{python_module dbfread >= 2.0.5}
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-agate >= 1.5.0
Requires:       python-dbfread >= 2.0.5
BuildArch:      noarch

%python_subpackages

%description
Agate-dbf adds read support for dbf files to agate.

%prep
%setup -q -n agate-dbf-%{version}
sed -i -e '/^#!\//, 1d' agatedbf/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license COPYING
%{python_sitelib}/agatedbf
%{python_sitelib}/agate_dbf-%{version}.dist-info

%changelog
