#
# spec file for package python-tzdata
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


%{?sle15_python_module_pythons}
Name:           python-tzdata
Version:        2025.1
Release:        0
Summary:        Provider of IANA time zone data
License:        Apache-2.0
URL:            https://github.com/python/tzdata
Source:         https://files.pythonhosted.org/packages/source/t/tzdata/tzdata-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-subtests}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 40.8.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Provider of IANA time zone data

%prep
%autosetup -p1 -n tzdata-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc NEWS.md README.rst
%license licenses/LICENSE_APACHE
%{python_sitelib}/tzdata
%{python_sitelib}/tzdata-%{version}.dist-info

%changelog
