#
# spec file
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


%define psuffix %{nil}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test-py38"
%define psuffix -test-py38
%define skip_python39 1
%define skip_python310 1
%define skip_python311 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py39"
%define psuffix -test-py39
%define skip_python38 1
%define skip_python310 1
%define skip_python311 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py310"
%define psuffix -test-py310
%define skip_python38 1
%define skip_python39 1
%define skip_python311 1
%bcond_without test
%endif
%if "%{flavor}" == "test-py311"
%define psuffix -test-py311
%define skip_python38 1
%define skip_python39 1
%define skip_python310 1
%bcond_without test
%endif
%if "%{flavor}" == ""
%bcond_with test
%endif

Name:           python-tables%{psuffix}
Version:        3.8.0
Release:        0
Summary:        Hierarchical datasets for Python
License:        BSD-3-Clause
URL:            https://github.com/PyTables/PyTables
Source0:        https://files.pythonhosted.org/packages/source/t/tables/tables-%{version}.tar.gz
# PATCH-FIX-UPSTREAM tables-pr1000-debundled-blosc2.patch gh#PyTables/PyTables#1000
Patch0:         tables-pr1000-debundled-blosc2.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  python-rpm-macros
%if ! %{with test}
BuildRequires:  %{python_module Cython >= 0.29.21}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numexpr >= 2.6.2}
BuildRequires:  %{python_module numpy-devel >= 1.19}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module py-cpuinfo}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  blosc-devel >= 1.21.1
BuildRequires:  blosc2-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  libbz2-devel
BuildRequires:  lzo-devel
%else
# with test
BuildRequires:  %{python_module tables = %{version}}
# usage of pkg_resources in tests
BuildRequires:  %{python_module setuptools}
%endif
Requires:       python-Cython >= 0.29.21
Requires:       python-numexpr >= 2.6.2
Requires:       python-numpy >= 1.19
Requires:       python-packaging
Requires:       python-py-cpuinfo
# boo#1196682
%requires_eq    hdf5
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     bzip2
Recommends:     lzo
%python_subpackages

%description
PyTables is a package for managing hierarchical datasets and
designed to efficently cope with extremely large amounts of
data. PyTables is built on top of the HDF5 library and the
NumPy package and features an object-oriented interface
that, combined with C-code generated from Pyrex sources,
makes of it a fast, yet extremely easy to use tool for
interactively save and retrieve large amounts of data.

%prep
%autosetup -p1 -n tables-%{version}
# make sure we use the system blosc
rm -r c-blosc
# https://github.com/PyTables/PyTables/issues/1001
rm tables/libblosc2.so

%if !%{with test}
%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export PYTABLES_NO_EMBEDDED_LIBS=1
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pttree
%python_clone -a %{buildroot}%{_bindir}/ptrepack
%python_clone -a %{buildroot}%{_bindir}/ptdump
%python_clone -a %{buildroot}%{_bindir}/pt2to3
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
pushd LICENSES
export VERBOSE=TRUE
%python_exec -B -m tables.tests.test_all
popd
%endif

%post
%python_install_alternative pttree
%python_install_alternative ptrepack
%python_install_alternative ptdump
%python_install_alternative pt2to3

%postun
%python_uninstall_alternative pttree
%python_uninstall_alternative ptrepack
%python_uninstall_alternative ptdump
%python_uninstall_alternative pt2to3

%if !%{with test}
%files %{python_files}
%doc README.rst ANNOUNCE.txt THANKS
%license LICENSE.txt
%license LICENSES/*
%python_alternative %{_bindir}/pt2to3
%python_alternative %{_bindir}/ptdump
%python_alternative %{_bindir}/ptrepack
%python_alternative %{_bindir}/pttree
%{python_sitearch}/tables/
%{python_sitearch}/tables-%{version}.dist-info
%endif

%changelog
