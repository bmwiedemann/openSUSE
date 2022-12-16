#
# spec file for package cracklib
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


Name:           cracklib
Version:        2.9.8
Release:        0
Summary:        Library to crack passwords using dictionaries
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/cracklib/cracklib
Source:         https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Source2:        baselibs.conf
# PATCH-FIX-OPENSUSE (should be upstreamed)
# Remove support for broken 64bit indexes from magic entry [bnc#106007]
Patch1:         0001-cracklib-magic.diff
# PATCH-FIX-OPENSUSE Hide non-public functions
Patch2:         0002-cracklib-2.9.2-visibility.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gzip
BuildRequires:  libtool
BuildRequires:  zlib-devel
Requires:       cracklib-dict

%description
CrackLib tests passwords to determine whether they match
certainsecurity-oriented characteristics. You can use CrackLib to
stopusers from choosing passwords that are too simple.This package
contains a full dictionary file used by cracklib.

%package devel
Summary:        Header files and libraries for developing apps which will use CrackLib
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libcrack2 = %{version}
Provides:       cracklib:%{_includedir}/crack.h

%description devel
The cracklib-devel package contains the header files and libraries
needed to develop programs that use the CrackLib functions to to
determine whether passwords match certain security-oriented
characteristics.

%package -n libcrack2
Summary:        Library to crack passwords using dictionaries
Group:          System/Libraries
Requires:       cracklib >= %{version}

%description -n libcrack2
CrackLib tests passwords to determine whether they match
certain security-oriented characteristics. You can use CrackLib to
stopusers from choosing passwords that are too simple.This package
contains a full dictionary file used by cracklib.

%package dict-small
Summary:        Small dictionary for cracklib, a password checking library
Group:          System/Libraries
Conflicts:      cracklib-dict-full
Provides:       cracklib-dict

%description dict-small
CrackLib tests passwords to determine whether they match certain
security-oriented characteristics. You can use CrackLib to stop users
from choosing passwords that are easy to guess.

This package contains a small dictionay file used by cracklib.

%prep
%autosetup -p0

%build
AUTOPOINT=true autoreconf -fi
%configure \
	--enable-hidden-symbols \
	--disable-static
%make_build
#make -C po update-po

%install
mkdir -p %{buildroot}%{_prefix}/lib
%make_install
# libtool is broken by design, remove this *.la files ...
rm %{buildroot}/%{_libdir}/libcrack.la
# set executable
chmod 755 ./util/cracklib-format
# Adjust path in comment
sed "s,%{_libexecdir}/cracklib_dict,%{_datadir}/cracklib/pw_dict,g" lib/crack.h > %{buildroot}/%{_includedir}/crack.h
./util/cracklib-format ./dicts/cracklib-small | \
./util/cracklib-packer %{buildroot}/%{_datadir}/cracklib/pw_dict
ln -s cracklib-format %{buildroot}/%{_sbindir}/mkdict
ln -s cracklib-packer %{buildroot}/%{_sbindir}/packer
rm -f %{buildroot}/%{_datadir}/cracklib/cracklib-small
ln -sf %{_datadir}/cracklib/pw_dict.hwm %{buildroot}%{_prefix}/lib/cracklib_dict.hwm
ln -sf %{_datadir}/cracklib/pw_dict.pwd %{buildroot}%{_prefix}/lib/cracklib_dict.pwd
ln -sf %{_datadir}/cracklib/pw_dict.pwi %{buildroot}%{_prefix}/lib/cracklib_dict.pwi
#
# using zip'ed dict takes too long for a check. But the support
# for this is still in the lib.
#
#gzip $RPM_BUILD_ROOT/%{_datadir}/cracklib/pw_dict.pwd
#ln -sf %{_datadir}/cracklib/pw_dict.pwd.gz $RPM_BUILD_ROOT/usr/lib/cracklib_dict.pwd.gz
%find_lang %{name}
%ifnarch ppc64
nm -C -D %{buildroot}%{_libdir}/libcrack.so.2 | grep ' T '
%endif

%check
sed -i 's:\(util/cracklib-check\):\1 %{buildroot}%{_prefix}/lib/cracklib_dict:' Makefile
%make_build test

%post -n libcrack2 -p /sbin/ldconfig
%postun -n libcrack2 -p /sbin/ldconfig

%files -n libcrack2
%{_libdir}/libcrack.so.2
%{_libdir}/libcrack.so.2.*

%files -f %{name}.lang
%license COPYING.LIB
%license README-LICENSE
%doc README README-WORDS NEWS README-DAWG AUTHORS
%{_sbindir}/create-cracklib-dict
%{_sbindir}/mkdict
%{_sbindir}/packer
%{_sbindir}/cracklib-check
%{_sbindir}/cracklib-format
%{_sbindir}/cracklib-packer
%{_sbindir}/cracklib-unpacker
%dir %{_datadir}/cracklib
%{_datadir}/cracklib/cracklib.magic
%{_prefix}/lib/cracklib_dict.hwm
%{_prefix}/lib/cracklib_dict.pwd
%{_prefix}/lib/cracklib_dict.pwi

%files devel
%{_includedir}/crack.h
%{_includedir}/packer.h
%{_libdir}/libcrack.so

%files dict-small
%{_datadir}/cracklib/pw_dict.hwm
%{_datadir}/cracklib/pw_dict.pwd
%{_datadir}/cracklib/pw_dict.pwi

%changelog
