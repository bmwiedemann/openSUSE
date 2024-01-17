#
# spec file for package libcapi20
#
# Copyright (c) 2021 SUSE LLC
# Copyright (C) 2020 B1 Systems GmbH, Vohburg, Germany
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           libcapi20
Version:        3.27
Release:        0
Summary:        Library for the Common ISDN Application Programming Interface
License:        LGPL-2.1-or-later
Group:          Hardware/ISDN
Source:         libcapi20-3.27.tar.xz
Source9:        baselibs.conf
URL:            https://github.com/leggewie-DM/libcapi20

%description
libcapi handles requests from CAPI-driven applications such as fax
systems via active and passive ISDN cards.

%package -n libcapi20-3
Summary:        Library for the Common ISDN Application Programming Interface
License:        LGPL-2.1-or-later
Group:          System/Libraries
Provides:       capi4linux = 2011.8.29
Obsoletes:      capi4linux < 2011.8.29

%description -n libcapi20-3
libcapi handles requests from CAPI-driven applications such as fax
systems via active and passive ISDN cards.

%package devel
Summary:        Header files for the Common ISDN API library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Provides:       capi4linux-devel = 2011.8.29
Obsoletes:      capi4linux-devel < 2011.8.29
Requires:       libcapi20-3 = %version

%description devel
This package provides files needed for development of CAPI-aware
software.

%prep
%autosetup

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
# This package failed when testing with -Wl,-as-needed being default.
# So we disable it here, if you want to retest, just delete this comment and the line below.
export SUSE_ASNEEDED=0
%configure
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la
rm -f "%buildroot/%_libdir"/capi/*.la
rm -f "%buildroot/%_libdir"/*.a

%post -n libcapi20-3 -p /sbin/ldconfig
%postun -n libcapi20-3 -p /sbin/ldconfig

%files
%license debian/copyright
%doc debian/libcapi20-3.README.Debian
%doc README

%files -n libcapi20-3
%license COPYING.LIB
%_libdir/libcapi20.so.3*
%exclude %_libdir/capi/*.so
%_libdir/capi/

%files devel
%license COPYING COPYING.LIB
%_includedir/capi20.h
%_includedir/capicmd.h
%_includedir/capiutils.h
%_includedir/capi_debug.h
%_includedir/capi_mod.h
%_libdir/libcapi20.so
%_libdir/pkgconfig/capi20.pc
%_libdir/capi/*.so

%changelog
