#
# spec file for package python-tlv8
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-tlv8
Version:        0.10.0
Release:        0
Summary:        Python module to handle type-length-value (TLV) encoded data
License:        Apache-2.0
URL:            https://github.com/jlusiardi/tlv8_python
# pypi tarball does not contain tests directory
Source:         https://github.com/jlusiardi/tlv8_python/archive/v%{version}.tar.gz#/tlv8-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Python module to handle type-length-value (TLV) encoded data 8-bit type, 8-bit length, and N-byte value as described within the Apple HomeKit Accessory Protocol Specification Non-Commercial Version Release R2.

%prep
%setup -q -n tlv8_python-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%{python_sitelib}/tlv8
%{python_sitelib}/tlv8-%{version}.dist-info/

%changelog
