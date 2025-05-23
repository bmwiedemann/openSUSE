#
# spec file for package libpwquality
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


%if 0%{?suse_version} >= 1550
%define _secconfdir /usr/lib/security
%else
%define _secconfdir %{_sysconfdir}/security
%endif
%define libname libpwquality1

Name:           libpwquality
Version:        1.4.5
Release:        0
Summary:        Library for password quality checking and generating random passwords
License:        BSD-3-Clause OR GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/libpwquality/libpwquality
Source:         %{url}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM - Fix installation of python bindings using setuptools. loosely based on commit 7b5e0f00
Patch0:         libpwquality-fix-python-install.patch

BuildRequires:  cracklib-devel
BuildRequires:  gettext-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(python3)

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

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}
%if 0%{?suse_version} >= 1550
mkdir -p %{buildroot}/%{_secconfdir}
mv %{buildroot}/%{_sysconfdir}/security/pwquality.conf %{buildroot}/%{_secconfdir}/pwquality.conf
%endif

%if 0%{?suse_version} > 1550
%pre -n %{libname}
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in security/pwquality.conf; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans -n %{libname}
# Migration to /usr/lib, restore just created .rpmsave
for i in security/pwquality.conf; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

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
%if 0%{?suse_version} >= 1550
%dir %{_secconfdir}
%{_secconfdir}/pwquality.conf
%else
%config(noreplace) %{_secconfdir}/pwquality.conf
%endif
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

%files -n python3-pwquality
%{python3_sitearch}/pwquality*

%files lang -f libpwquality.lang

%changelog
