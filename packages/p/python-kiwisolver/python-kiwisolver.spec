#
# spec file for package python-kiwisolver
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-kiwisolver
Version:        1.3.1
Release:        0
Summary:        An implementation of the Cassowary constraint solver
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/nucleic/kiwi
Source:         https://github.com/nucleic/kiwi/archive/%{version}.tar.gz
BuildRequires:  %{python_module cppy >= 1.1.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Kiwi is a C++ implementation of the Cassowary constraint solving
algorithm. Kiwi is an implementation of the algorithm based on the
seminal Cassowary paper, but it is not a refactoring of the original
C++ solver. Kiwi ranges from 10x to 500x faster processing than the
original Cassowary solver with the same input set, with typical use
cases gaining a 40x improvement. Memory savings are consistently >5x.

In addition to the C++ solver, Kiwi ships with hand-rolled Python bindings.

%prep
%setup -q -n kiwi-%{version}
# Fix wrong-file-end-of-line-encoding
dos2unix LICENSE README.rst releasenotes.rst

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE
%doc README.rst releasenotes.rst
%{python_sitearch}/*

%changelog
