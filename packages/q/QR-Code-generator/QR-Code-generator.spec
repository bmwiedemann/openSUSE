#
# spec file for package QR-Code-generator
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
%define libcname libqrcodegen1
%define libcppname libqrcodegencpp1
Name:           QR-Code-generator
Version:        1.5.0
Release:        0
Summary:        QR Code generator library
License:        MIT
URL:            https://github.com/nayuki/QR-Code-generator
Source:         https://github.com/nayuki/QR-Code-generator/archive/v%{version}.tar.gz
Patch0:         cflags.patch
Patch2:         0002-Make-use-of-fPIC-parameter-when-building.patch
Patch3:         0003-Generate-both-shared-and-static-libraries.patch
Patch4:         0004-Create-install-targets-for-C-and-CPP.patch
Patch5:         0005-Rename-cpp-library-to-qrcodegencpp-to-avoid-conflict.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This project aims to be the best, clearest QR Code generator library in multiple languages.
The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation comments.

%if 0%{?suse_version} < 1500
# this is hack to make rpm happy as %python_subpackage does not work
%package -n python-%{name}
Summary:        QR Code generator python bindings

%description -n python-%{name}
QR Code generator python2 bindings
%endif

%package devel
Summary:        Development files for QR code generator
Requires:       %{libcname}
Requires:       %{libcppname}
Provides:       qrcodegen-devel

%description devel
Development files, headers/libs for QR code generator

%package -n %{libcname}
Summary:        QR Code generator library

%description -n %{libcname}
C QR Code generator library

%package -n %{libcppname}
Summary:        QR Code generator library

%description -n %{libcppname}
C++ QR Code generator library

%prep
%setup -q
%autopatch -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
pushd c
make -j1
popd
pushd cpp
make -j1
popd
pushd python
%python_build
popd

%install
pushd c
%make_install LIBDIR=%{buildroot}%{_libdir}
popd
pushd cpp
%make_install LIBDIR=%{buildroot}%{_libdir}
popd
pushd python
%python_install
popd
rm -rf %{buildroot}%{_libdir}/*.a

%post -n %{libcname} -p /sbin/ldconfig
%postun -n %{libcname} -p /sbin/ldconfig
%post -n %{libcppname} -p /sbin/ldconfig
%postun -n %{libcppname} -p /sbin/ldconfig

%files %{python_files}
%license Readme.markdown
%{python_sitelib}/*

%files -n QR-Code-generator-devel
%{_includedir}/*
%{_libdir}/*.so

%files -n %{libcname}
%license Readme.markdown
%{_libdir}/libqrcodegen.so.*

%files -n %{libcppname}
%license Readme.markdown
%{_libdir}/libqrcodegencpp.so.*

%changelog
