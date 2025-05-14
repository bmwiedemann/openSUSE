#
# spec file for package python-binary
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


Name:           python-binary
Version:        1.0.0
Release:        0
License:        Apache-2.0 OR MIT
Summary:        Library to convert between binary and SI units
URL:            https://github.com/ofek/binary
Source:         https://files.pythonhosted.org/packages/source/b/binary/binary-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
# /SECTION
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
Python library to convert between and within binary (IEC) and decimal (SI) units.

%prep
%setup -q -n binary-%{version}
dos2unix README.rst

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -r %{buildroot}/%{$python_sitelib}/tests/

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE-APACHE LICENSE-MIT
%{python_sitelib}/binary
%{python_sitelib}/binary-%{version}.dist-info

%changelog
