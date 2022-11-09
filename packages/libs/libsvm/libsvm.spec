#
# spec file for package libsvm
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


%define libname libsvm3
%define fileversion 3.3

Summary:        A Library for Support Vector Machines
License:        BSD-3-Clause
Group:          Development/Languages/Other
Name:           libsvm
Version:        3.30
Release:        0
URL:            https://www.csie.ntu.edu.tw/~cjlin/libsvm/
Source0:        https://www.csie.ntu.edu.tw/~cjlin/libsvm/%{name}-%{fileversion}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  gcc-c++
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  ncurses-devel
BuildRequires:  python-rpm-macros

%description
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

%package -n svm-tools
Summary:        A set of tools to use with libsvm
Group:          Development/Languages/C and C++

%description -n svm-tools
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

%package -n %{libname}
Summary:        A Library for Support Vector Machines
Group:          System/Libraries

%description -n %{libname}
LIBSVM is an integrated software for support vector classification,
(C-SVC, nu-SVC), regression (epsilon-SVR, nu-SVR) and distribution
estimation (one-class SVM). It supports multi-class classification.

%package	devel
Summary:        C headers for developing programs with libsvm
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
# VPP provides a libsvm.so installed in _libdir as well
Conflicts:      vpp-devel

%description	devel
This package contains the libraries and header files needed for
developing applications with libsvm.

%package -n %{python_prefix}-svm
Summary:        Python bindings for libsvm
Group:          Development/Languages/Python
Requires:       gnuplot
Requires:       svm-tools = %{version}
Provides:       python-svm = %{version}-%{release}
Obsoletes:      python-svm < %{version}-%{release}
BuildArch:      noarch

%description -n %{python_prefix}-svm
This package contains the Python bindings for libsvm.

%package java
Summary:        Java bindings for libsvm
Group:          Development/Libraries/Java
Requires:       %{libname} = %{version}
Requires:       java >= 1.6.0
Requires:       javapackages-tools
Requires(post): javapackages-tools
Requires(postun):javapackages-tools
BuildArch:      noarch

%description java
This package contains the Java bindings for libsvm.

%prep
%setup -q -n %{name}-%{fileversion}

%build
# We can't override CFLAGS, we have to patch the Makefile.
sed -i '
    s/^CFLAGS = .*$/CFLAGS = %{optflags} -Wall -Wconversion -fPIC/g
    s/$(CXX) $${SHARED_LIB_FLAG}/$(CXX) %{optflags} $${SHARED_LIB_FLAG}/g
' Makefile
make %{_smp_mflags} all lib
rm -f java/libsvm.jar
make -C java

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/libsvm
mkdir -p %{buildroot}%{python_sitelib}/svm

install -m 755 svm-train %{buildroot}%{_bindir}
install -m 755 svm-scale %{buildroot}%{_bindir}
install -m 755 svm-predict %{buildroot}%{_bindir}
install -m 755 ./tools/checkdata.py %{buildroot}%{_bindir}/svm-checkdata
install -m 755 ./tools/grid.py %{buildroot}%{_bindir}/svm-grid
install -m 755 ./tools/subset.py %{buildroot}%{_bindir}/svm-subset
install -m 755 ./tools/easy.py %{buildroot}%{_bindir}/svm-easy
install -m 644 svm.h %{buildroot}%{_includedir}/libsvm/
install -m 755 libsvm.so.3 %{buildroot}%{_libdir}
ln -s %{_libdir}/libsvm.so.3 %{buildroot}%{_libdir}/libsvm.so
mv ./python/README README-python
mv ./tools/README README-python-tools

# Don't use env in shebangs, and prefer the default Python.
# (https://www.python.org/dev/peps/pep-0394/#for-python-runtime-distributors)
sed -i '1s|/usr/bin/env *|%{_bindir}/|;1s|/usr/bin/python$|%{_bindir}/python%python_bin_suffix|' \
    %{buildroot}%{_bindir}/svm-*

install -m 644 -t %{buildroot}%{python_sitelib}/svm ./python/libsvm/*.py

# Remove unnecessary shebangs.
sed -i '/^#!\/usr\/bin\/env .*$/ d' %{buildroot}%{python_sitelib}/svm/*

install -m 755 ./java/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n svm-tools
%doc FAQ.html README
%{_bindir}/svm-train
%{_bindir}/svm-scale
%{_bindir}/svm-predict

%files -n %{libname}
%license COPYRIGHT
%{_libdir}/libsvm.so.3

%files devel
%{_includedir}/libsvm
%{_libdir}/libsvm.so

%files -n %{python_prefix}-svm
%doc README-python README-python-tools
%{_bindir}/svm-checkdata
%{_bindir}/svm-grid
%{_bindir}/svm-subset
%{_bindir}/svm-easy
%{python_sitelib}/svm

%files java
%{_javadir}/%{name}.jar

%changelog
