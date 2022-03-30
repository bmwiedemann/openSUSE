#
# spec file for package python-tables
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-tables
Version:        3.7.0
Release:        0
Summary:        Hierarchical datasets for Python
License:        BSD-3-Clause
URL:            https://github.com/PyTables/PyTables
Source0:        https://files.pythonhosted.org/packages/source/t/tables/tables-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numexpr >= 2.6.2}
BuildRequires:  %{python_module numpy-devel >= 1.19}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module setuptools}
BuildRequires:  blosc-devel >= 1.21.1
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  libbz2-devel
BuildRequires:  lzo-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx >= 1.1
BuildRequires:  python3-jupyter_ipython
BuildRequires:  python3-numpydoc
BuildRequires:  python3-sphinx_rtd_theme
Requires:       python-numexpr >= 2.6.2
Requires:       python-numpy >= 1.19
Requires:       python-packaging
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

%package -n %{name}-doc
Summary:        Documentation for %{name}
Provides:       %{python_module tables-doc = %{version}}

%description -n %{name}-doc
Documentation and help files for %{name}

%prep
%autosetup -p1 -n tables-%{version}
# make sure we use the system blosc
rm -r c-blosc

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
# Never use SSE2 and AVX2 because obs buildbots might support it
# but the target does not
export DISABLE_SSE2=1
export DISABLE_AVX2=1
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pttree
%python_clone -a %{buildroot}%{_bindir}/ptrepack
%python_clone -a %{buildroot}%{_bindir}/ptdump
%python_clone -a %{buildroot}%{_bindir}/pt2to3
%{python_expand #
rm %{buildroot}%{$python_sitearch}/tables/*.c
rm %{buildroot}%{$python_sitearch}/tables/tests/*.c
%fdupes %{buildroot}%{$python_sitearch}
}

pushd doc
export PYTHONPATH=%{buildroot}%{python3_sitearch}
make html
rm build/html/.buildinfo
popd
# manual copy to buildroot so we can deduplicate
mkdir -p %{buildroot}%{_docdir}/%{name}-doc/
cp -r doc/build/html %{buildroot}%{_docdir}/%{name}-doc/
cp -r examples %{buildroot}%{_docdir}/%{name}-doc/
%fdupes %{buildroot}%{_docdir}/%{name}-doc/

%check
pushd LICENSES
export VERBOSE=TRUE
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -B -m tables.tests.test_all
}
popd

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

%files %{python_files}
%doc README.rst ANNOUNCE.txt THANKS
%license LICENSE.txt
%license LICENSES/*
%python_alternative %{_bindir}/pt2to3
%python_alternative %{_bindir}/ptdump
%python_alternative %{_bindir}/ptrepack
%python_alternative %{_bindir}/pttree
%{python_sitearch}/tables/
%{python_sitearch}/tables-%{version}*-info

%files -n %{name}-doc
%license LICENSE.txt
%license LICENSES/*
%doc %{_docdir}/%{name}-doc/

%changelog
