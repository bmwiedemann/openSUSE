#
# spec file for package python-siphash24
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
Name:           python-siphash24
Version:        1.8
Release:        0
Summary:        Streaming-capable SipHash-1-3 and SipHash-2-4 implementation
License:        Apache-2.0 OR LGPL-2.1-or-later
URL:            https://github.com/dnicolodi/python-siphash24
Source0:        https://files.pythonhosted.org/packages/source/s/siphash24/siphash24-%{version}.tar.gz
# The meson build pulls these two c-util libraries as git wrap
# subprojects (statically linked); provide them offline.
Source1:        https://github.com/c-util/c-siphash/archive/refs/tags/v1.1.0.tar.gz#/c-siphash-1.1.0.tar.gz
Source2:        https://github.com/c-util/c-stdaux/archive/refs/tags/v1.5.0.tar.gz#/c-stdaux-1.5.0.tar.gz
BuildRequires:  %{python_module Cython >= 3.1.0}
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module meson-python >= 0.18.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  meson >= 1.0.0
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
%python_subpackages

%description
A Python wrapper for the SipHash-1-3 and SipHash-2-4 pseudo-random
functions, providing a streaming-capable interface compatible with
the hashlib hash objects of the Python standard library.

%prep
%autosetup -p1 -n siphash24-%{version}
# Place the wrap subprojects so meson uses them instead of fetching
# from git at configure time.
tar -xf %{SOURCE1} -C subprojects
tar -xf %{SOURCE2} -C subprojects
mv subprojects/c-siphash-1.1.0 subprojects/libcsiphash-1
mv subprojects/c-stdaux-1.5.0 subprojects/libcstdaux-1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch test.py

%files %{python_files}
%license LICENSES/Apache-2.0.txt LICENSES/LGPL-2.1-or-later.txt
%doc README.rst CHANGELOG.rst
%{python_sitearch}/siphash24*.so
%{python_sitearch}/siphash24-%{version}.dist-info

%changelog
