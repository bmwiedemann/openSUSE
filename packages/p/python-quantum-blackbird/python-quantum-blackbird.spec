#
# spec file for package python-quantum-blackbird
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


%define packagename quantum-blackbird
%define skip_python2 1
%define skip_python36 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-quantum-blackbird
Version:        0.3.0
Release:        0
Summary:        Quantum assembly language for continuous-variable quantum computation
License:        Apache-2.0
URL:            https://github.com/XanaduAI/blackbird
Source:         https://github.com/XanaduAI/blackbird/archive/v%{version}.tar.gz#/blackbird-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skip_32bit_divide_scalar_array_test.patch gh#XanaduAI/blackbird#42 mcepl@suse.com
# Skip tests failing on 32bit
Patch0:         skip_32bit_divide_scalar_array_test.patch
BuildRequires:  %{python_module antlr4-python3-runtime >= 4.8}
BuildRequires:  %{python_module networkx}
BuildRequires:  %{python_module numpy >= 1.16}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sympy}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  uuid-devel
Requires:       python-antlr4-python3-runtime >= 4.8
Requires:       python-networkx
Requires:       python-numpy >= 1.16
Requires:       python-sympy
BuildArch:      noarch
%python_subpackages

%description
Blackbird is a quantum assembly language for continuous-variable quantum
computation, that can be used to program Xanadu's quantum photonics
hardware and Strawberry Fields simulator.

%prep
%autosetup -p1 -n blackbird-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Fix E: spurious-executable-perm of README.rst
chmod 644 README.rst

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*egg-info
%{python_sitelib}/blackbird

%changelog
