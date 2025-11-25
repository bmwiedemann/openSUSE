#
# spec file for package python-tables
#
# Copyright (c) 2025 SUSE LLC and contributors
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define psuffix %{nil}
%bcond_with test
%else
%define psuffix -%{flavor}
%bcond_without test
%if "%{flavor}" != "test-py311"
%define skip_python311 1
%endif
%if "%{flavor}" != "test-py312"
%define skip_python312 1
%endif
%if "%{flavor}" != "test-py313"
%define skip_python313 1
%endif
%if "%{flavor}" != "test-py314"
%define skip_python314 1
%endif
# Skip all empty test flavors: last one is for sle15_python_module_pythons
%if "%{shrink:%pythons}" == "" || ( "%pythons" == "python311" && 0%{?skip_python311} )
ExclusiveArch:  donotbuild
%define python_module() %flavor-not-enabled-in-buildset-for-suse-%{?suse_version}
%endif
%endif

Name:           python-tables%{psuffix}
Version:        3.10.2
Release:        0
Summary:        Hierarchical datasets for Python
License:        BSD-3-Clause
URL:            https://github.com/PyTables/PyTables
Source0:        https://files.pythonhosted.org/packages/source/t/tables/tables-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#PyTables/PyTables#1256
Patch0:         support-numexpr-2.13.0.patch
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  python-rpm-macros
%if ! %{with test}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numexpr >= 2.6.2}
BuildRequires:  %{python_module numpy-devel >= 1.20}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module py-cpuinfo}
BuildRequires:  %{python_module setuptools >= 61}
BuildRequires:  %{python_module typing-extensions >= 4.4.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  blosc-devel >= 1.21.1
BuildRequires:  blosc2-devel >= 2.11
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  libbz2-devel
BuildRequires:  lzo-devel
%else
# with test
BuildRequires:  %{python_module tables = %{version}}
%endif
Requires:       python-blosc2 >= 2.3
Requires:       python-numexpr >= 2.6.2
# See gh#PyTables/PyTables#1083
Requires:       python-numpy >= 1.20
Requires:       python-packaging
Requires:       python-py-cpuinfo
Requires:       python-typing-extensions >= 4.4.0
# boo#1196682
%requires_eq    hdf5
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
