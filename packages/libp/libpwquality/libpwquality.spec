#
# spec file for package libpwquality
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


%define _secconfdir %{_sysconfdir}/security
%define libname libpwquality1
%bcond_without python2

Name:           libpwquality
Version:        1.4.5
Release:        0
Summary:        Library for password quality checking and generating random passwords
License:        BSD-3-Clause OR GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libpwquality/libpwquality
Source:         %{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf

BuildRequires:  cracklib-devel
BuildRequires:  gettext-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(python3)
%if %{with python2}
BuildRequires:  pkgconfig(python2)
%endif
BuildRequires:  python-rpm-macros

%description
libpwquality is a library for password quality checks and generation
of random passwords that pass the checks.

%lang_package

%package -n %{libname}
Summary:        Library for password quality checking and generating random passwords
Group:          System/Libraries
Requires:       cracklib-dict >= 2.8
Recommends:     cracklib-dict-full >= 2.8
# To make lang package installable
Provides:       %{name}

%description -n %{libname}
libpwquality is a library for password quality checks and generation
of random passwords that pass the checks.

%package tools
Summary:        Tools from libpequality, a library for password quality checking
Group:          Productivity/Security

%description tools
libpwquality is a library for password quality checks and generation
of random passwords that pass the checks.

This package contains simple tools that use libpwquality.

%package devel
Summary:        Development files for libpwquality, a library for password quality checking
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       pkgconfig

%description devel
libpwquality is a library for password quality checks and generation
of random passwords that pass the checks.

This package provides files needed for development of applications
using the libpwquality library.

%package -n pam_pwquality
Summary:        PAM module to disallow weak new passwords
Group:          System/Libraries
Requires:       pam
Requires(post): pam-config
Requires(postun):pam-config

%description -n pam_pwquality
The pam_pwquality PAM module can be used instead of pam_cracklib to
disallow weak new passwords when user's login password is changed.

%package -n python2-pwquality
Summary:        Python bindings for libpwquality
Group:          Development/Libraries/Python
Provides:       python-pwquality = %{version}-%{release}
Obsoletes:      python-pwquality < %{version}-%{release}

%description -n python2-pwquality
libpwquality is a library for password quality checks and generation
of random passwords that pass the checks.

This package provides Python bindings for the libpwquality library.

%package -n python3-pwquality
Summary:        Python 3 bindings for libpwquality
Group:          Development/Libraries/Python
Provides:       python-pwquality = %{version}-%{release}
Obsoletes:      python-pwquality < %{version}-%{release}

%description -n python3-pwquality
libpwquality is a library for password quality checks and generation
of random passwords that pass the checks.

This package provides Python 3 bindings for the libpwquality library.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--with-securedir=%{_pam_moduledir} \
	--with-python-binary=%{_bindir}/python3 \
	--with-pythonsitedir=%{python3_sitearch} \
	%{nil}
%if 0%{?suse_version} < 1500
make -O %{?_smp_mflags}
%else
%make_build
%endif
%if %{with python2}
pushd python
%python_build
popd
%endif

%install
%make_install
%if %{with python2}
pushd python
%python_install
popd
%endif

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%post -n pam_pwquality
# Due to boo#728586 it is necessary to duplicate this in the 32bit variant.
# So you need to edit baselibs.conf if you change this.
%{_sbindir}/pam-config -a --pwquality || :

%postun -n pam_pwquality
if [ "$1" = "0" ]; then
  %{_sbindir}/pam-config -d --pwquality || :
fi

%files -n %{libname}
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libpwquality.so.*
%config(noreplace) %{_secconfdir}/pwquality.conf
%{_mandir}/man3/pwquality.3%{?ext_man}
%{_mandir}/man5/pwquality.conf.5%{?ext_man}

%files tools
%{_bindir}/pwmake
%{_bindir}/pwscore
%{_mandir}/man1/pwmake.1%{?ext_man}
%{_mandir}/man1/pwscore.1%{?ext_man}

%files devel
%{_includedir}/pwquality.h
%{_libdir}/libpwquality.so
%{_libdir}/pkgconfig/pwquality.pc

%files -n pam_pwquality
%{_pam_moduledir}/pam_pwquality.so
%{_mandir}/man8/pam_pwquality.8%{?ext_man}

%if %{with python2}
%files -n python2-pwquality
%{python2_sitearch}/*
%endif

%files -n python3-pwquality
%{python3_sitearch}/*

%files lang -f libpwquality.lang

%changelog
