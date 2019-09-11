#
# spec file for package python-bcolz
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%ifarch %{ix86} x86_64
%bcond_without tests
%else
%bcond_with tests
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-bcolz
Version:        1.2.1
Release:        0
Summary:        Columnar and compressed data containers
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.com/Blosc/bcolz
Source:         https://files.pythonhosted.org/packages/source/b/bcolz/bcolz-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 0.22}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module numpy-devel >= 1.8}
BuildRequires:  %{python_module setuptools > 18.0}
BuildRequires:  %{python_module setuptools_scm > 1.5.4}
BuildRequires:  %{python_module xml}
BuildRequires:  blosc-devel >=  1.8.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%if %{with tests}
BuildRequires:  python-mock
%endif
Requires:       python-numpy >= 1.8
Requires:       python-xml
Recommends:     python-numexpr >= 2.5.2
Recommends:     python-pandas
Recommends:     python-tables
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %{ix86} x86_64
%python_subpackages

%description
The bcolz package provides columnar and compressed data containers.
Column storage allows for efficiently querying tables with a large
number of columns.  It also allows for cheap addition and removal of
column.  In addition, bcolz objects are compressed by default for
reducing memory/disk I/O needs.  The compression process is carried
out internally by Blosc, a high-performance compressor that is
optimized for binary data.

%prep
%setup -q -n bcolz-%{version}

%build
export CFLAGS="%{optflags}"
export BLOSC_DIR=%{_includedir}
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with tests}
%check
# %%python_exec setup.py test
pushd docs
%{python_expand export PYTHONPATH="%{buildroot}%{$python_sitearch}"
$python -c "import bcolz; bcolz.test()"
}
popd
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc ANNOUNCE.rst README.rst RELEASE_NOTES.rst THANKS.rst
%license LICENSES/*
%{python_sitearch}/bcolz
%{python_sitearch}/bcolz-%{version}-py*.egg-info

%changelog
