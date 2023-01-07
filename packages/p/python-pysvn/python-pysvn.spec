#
# spec file for package python-pysvn
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


%define packagename pysvn
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pysvn
Version:        1.9.20
Release:        0
Summary:        Highlevel Subversion Python Bindings
License:        Apache-1.1
Group:          Development/Libraries/Python
URL:            https://pysvn.sourceforge.io/
Source0:        https://sourceforge.net/projects/pysvn/files/pysvn/V%{version}/pysvn-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pycxx-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libapr1-devel
BuildRequires:  libcom_err-devel
BuildRequires:  libcom_err2
BuildRequires:  libexpat-devel
BuildRequires:  neon-devel
BuildRequires:  python-rpm-macros
BuildRequires:  subversion-devel
Requires:       neon
Requires:       subversion
%python_subpackages

%description
pysvn is a set of highlevel Python bindings to Subversion. pysvn
enables tools to be written in Python that use Subversion.

Features:
 * Supports all svn client features
 * Supports svn transaction features required to write svn pre-commit
   hooks
 * Python like interface
 * Documentation and examples provided
 * No need to understand the Subversion C API

%prep
%setup -q -n %{packagename}-%{version}

%{python_expand # python_build and python_install not applicable: not the standard setuptools workflow
# copy pristine dirs to flavor specific directory (shuffled by python_expand)
mkdir -p build
cp -r Builder Docs Examples Kit Patches Source Tests build/
}

rm -r Builder Docs Examples Kit Patches Source Tests
# Remove bundled libs
rm -rf Import

%build
export CFLAGS="%{optflags}"
%{python_expand #
pushd build/Source
$python setup.py configure --enable-debug --verbose --fixed-module-name --norpath

sed -i -e 's@-Wall -fPIC -fexceptions -frtti@%{optflags} -fPIC -frtti@' Makefile
%make_build
popd
}

%install
%{python_expand #
install -d -m 755 %{buildroot}%{$python_sitearch}/%{packagename}
install -p -m 644 build/Source/pysvn/__init__.py %{buildroot}%{$python_sitearch}/%{packagename}
install -p -m 755 build/Source/pysvn/_pysvn.so %{buildroot}%{$python_sitearch}/%{packagename}

mkdir -p pkgdoc-%{$python_bin_suffix}
cp -r build/Docs build/Examples pkgdoc-%{$python_bin_suffix}

%fdupes %{buildroot}%{$python_sitearch}
}

%check
%{python_expand #
pushd build/Tests
# the tests expect a valid answer from locale.getdefaultlocale()
# C.UTF-8 does not work. Use en_US.utf-8.
# The test have not been test in parallel, use one core for now.
export LC_ALL=en_US.UTF-8
PYTHONPATH=%{buildroot}%{$python_sitearch} make -j1
popd
}

%files %{python_files}
%license LICENSE.txt
%doc pkgdoc-%{python_bin_suffix}/Docs pkgdoc-%{python_bin_suffix}/Examples
%{python_sitearch}/%{packagename}

%changelog
