#
# spec file for package python-pybcj
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python2 1
Name:           python-pybcj
Version:        1.0.1
Release:        0
Summary:        A bcj filter library
License:        LGPL-2.1-or-later
URL:            https://codeberg.org/miurahr/pybcj
Source:         https://files.pythonhosted.org/packages/source/p/pybcj/pybcj-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.6}
BuildRequires:  %{python_module importlib_metadata if %python-base < 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 58.0}
BuildRequires:  %{python_module setuptools_scm >= 6.0.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       (python-importlib_metadata if python-base < 3.8)
# SECTION test
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
In data compression, BCJ, short for Branch-Call-Jump, refers to a technique that
improves the compression of machine code of executable binaries by replacing
relative branch addresses with absolute ones. This allows a LZMA compressor to
identify duplicate targets and archive higher compression rate.

BCJ is used in 7-zip compression utility as default filter for executable binaries.

pybcj is a python bindings with BCJ implementation by C language. The C codes are
derived from p7zip, portable 7-zip implementation. pybcj support Intel/Amd
x86/x86_64, Arm/Arm64, ArmThumb, Sparc, PPC, and IA64.

%prep
%setup -q -n pybcj-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc Changelog.rst README.rst
%license LICENSE
%{python_sitearch}/bcj
%{python_sitearch}/pybcj-%{version}.dist-info

%changelog
