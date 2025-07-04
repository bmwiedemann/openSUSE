#
# spec file for package python-py3c
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-py3c
Version:        1.4
Release:        0
Summary:        Python compatibility headers
License:        MIT
URL:            https://py3c.readthedocs.io/
Source:         https://github.com/encukou/py3c/archive/v%{version}.tar.gz#/py3c-%{version}.tar.gz
Source99:       python-py3c-rpmlintrc
# Needed for test build
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
py3c helps porting C extensions to Python 3.

It provides a guide, and a set of macros to facilitate porting
and reduce boilerplate.

%package -n py3c-devel
Summary:        Development files for py3c

%description -n py3c-devel
py3c helps porting C extensions to Python 3.

%prep
%setup -q -n py3c-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# we will use the make install to deploy includes
rm -r %{buildroot}%{_includedir}/*
%make_install prefix=%{_prefix}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd test
# Test C extension
%pyproject_wheel
%{python_expand # copy the lib and run the test
cp ./build/lib.linux*/test_py3c* ./
$python __main__.py -v
rm -f test_py3c*.so
rm -rf build
}
# Test Cpp extension
export TEST_USE_CPP="yes"
%pyproject_wheel
%{python_expand # copy the lib and run the test
cp ./build/lib.linux*/test_py3c* ./
$python __main__.py -v
rm -f test_py3c*.so
}
popd

%files %{python_files}
%doc README.rst
%license LICENSE.MIT
%{python_sitelib}/py3c-%{version}*-info

%files -n py3c-devel
%{_includedir}/py3c.h
%dir %{_includedir}/py3c
%{_includedir}/py3c/capsulethunk.h
%{_includedir}/py3c/comparison.h
%{_includedir}/py3c/compat.h
%{_includedir}/py3c/fileshim.h
%{_includedir}/py3c/py3shims.h
%{_includedir}/py3c/tpflags.h
%{_datadir}/pkgconfig/py3c.pc

%changelog
