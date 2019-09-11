#
# spec file for package python-pysvn
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pysvn
Version:        1.9.6
Release:        0
Summary:        Highlevel Subversion Python Bindings
License:        Apache-1.1
Group:          Development/Libraries/Python
URL:            http://pysvn.tigris.org
Source0:        http://pysvn.barrys-emacs.org/source_kits/pysvn-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pycxx-devel}
BuildRequires:  %{python_module xml}
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
%setup -q -n pysvn-%{version}

%build
export CFLAGS="%{optflags}"
%{python_expand cp -r Source Source-%{$python_bin_suffix}
pushd Source-%{$python_bin_suffix}
$python setup.py backport
$python setup.py configure \
    --enable-debug --verbose --fixed-module-name --norpath \
    --pycxx-dir=%{$python_sysconfig_path include}/ --pycxx-src-dir=%{_datadir}/python%{$python_bin_suffix}/CXX
sed -i -e 's@-Wall -fPIC -fexceptions -frtti@%{optflags} -fPIC -frtti@' Makefile
make %{?_smp_mflags}
popd
}

%install
%{python_expand mkdir -p %{buildroot}/%{$python_sitearch}/pysvn
pushd Source-%{$python_bin_suffix}
cp pysvn/{__init__.py,_pysvn*.so} %{buildroot}/%{$python_sitearch}/pysvn
$python -m compileall -d %{$python_sitearch} %{buildroot}/%{$python_sitearch}/pysvn
$python -O -m compileall -d %{$python_sitearch} %{buildroot}/%{$python_sitearch}/pysvn
popd
}
rm -f Docs/generate_cpp_docs_from_html_docs.py

%check
cd Tests
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} PYTHON=$python make %{?_smp_mflags} || :

%files %{python_files}
%license LICENSE.txt
%doc Docs Examples
%{python_sitearch}/*

%changelog
