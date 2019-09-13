#
# spec file for package python-tables
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-tables
Version:        3.5.2
Release:        0
Summary:        Hierarchical datasets for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/PyTables/PyTables
Source0:        https://files.pythonhosted.org/packages/source/t/tables/tables-%{version}.tar.gz
Patch0:         Never-use-the-msse2-flag-explicitly.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
# Python 3 version needs mock too for some reason
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module numexpr >= 2.5.2}
BuildRequires:  %{python_module numpy-devel >= 1.8.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.9.0}
BuildRequires:  blosc-devel >= 1.4.1
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel >= 1.8.4
BuildRequires:  libbz2-devel
BuildRequires:  lzo-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx >= 1.1
BuildRequires:  python3-jupyter_ipython
BuildRequires:  python3-numpydoc
BuildRequires:  python3-sphinx_rtd_theme
Requires:       python-numexpr >= 2.5.2
Requires:       python-numpy >= 1.8.1
Requires:       python-six >= 1.9.0
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
Group:          Development/Languages/Python
Provides:       %{python_module tables-doc = %{version}}

%description -n %{name}-doc
Documentation and help files for %{name}

%prep
%setup -q -n tables-%{version}
%patch0 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
pushd doc
export PYTHONPATH=%{buildroot}%{python3_sitearch}
make html
popd

%fdupes doc/build/html
%fdupes examples/

%check
pushd LICENSES
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitearch}
$python -B -m tables.tests.test_all
}
popd

%files %{python_files}
%doc README.rst RELEASE_NOTES.txt THANKS
%license LICENSE.txt
%license LICENSES/*
%python3_only %{_bindir}/pt2to3
%python3_only %{_bindir}/ptdump
%python3_only %{_bindir}/ptrepack
%python3_only %{_bindir}/pttree
%{python_sitearch}/tables/
%{python_sitearch}/tables-%{version}-py*.egg-info

%files -n %{name}-doc
%license LICENSE.txt
%license LICENSES/*
%doc doc/build/html/
%doc examples/

%changelog
