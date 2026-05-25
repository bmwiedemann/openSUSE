#
# spec file for package python-pyzstd
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


%{?sle15_python_module_pythons}
Name:           python-pyzstd
Version:        0.19.1
Release:        0
Summary:        Python bindings to Zstandard (zstd) compression library
License:        BSD-3-Clause
URL:            https://github.com/Rogdham/pyzstd
Source:         https://files.pythonhosted.org/packages/source/p/pyzstd/pyzstd-%{version}.tar.gz
BuildRequires:  %{python_module backports.zstd >= 1.0.0 if %python-base < 3.14}
BuildRequires:  %{python_module devel >= 3.10}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module typing_extensions >= 4.13.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-backports.zstd >= 1.0.0 if python-base < 3.14)
Requires:       (python-typing_extensions >= 4.13.2 if python-base < 3.13)
BuildArch:      noarch
%python_subpackages

%description
Pyzstd module provides classes and functions for compressing and decompressing data,
using Facebook's Zstandard (or zstd as short name) algorithm.

The API is similar to Python's bz2/lzma/zlib modules.

%prep
%setup -q -n pyzstd-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pyzstd
%{python_sitelib}/pyzstd-%{version}.dist-info

%changelog
