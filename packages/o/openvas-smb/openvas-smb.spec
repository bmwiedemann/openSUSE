#
# spec file for package openvas-smb
#
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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

%define sover 1
Name:           openvas-smb
Version:        1.0.5
Release:        0
Summary:        SMB module for OpenVAS Scanner
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://github.com/greenbone/openvas-smb
#Git-Clone:     https://github.com/greenbone/gvm-libs.git
Source:         https://github.com/greenbone/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source98:       https://github.com/greenbone/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source99:       https://www.greenbone.net/GBCommunitySigningKey.asc#/%{name}.keyring
Patch0:         0001-Fix-heimdal-gssapi-dependencies.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libheimdal-devel >= 7.5.0
BuildRequires:  mingw32-cross-gcc
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  xmltoman
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls) >= 3.2.15
BuildRequires:  pkgconfig(popt)
Provides:       wmic
Provides:       winexe

%description
This is the smb module for the OpenVAS Scanner. It includes libraries
(openvas-wmiclient/openvas-wincmd) to interface with Microsoft Windows
Systems through the Windows Management Instrumentation API and a
winexe binary to execute processes remotely on that system.

%package -n libopenvas_wincmd%{sover}
Summary:        Support libraries for GVM
Group:          System/Libraries

%description -n libopenvas_wincmd%{sover}
The support libraries for the Greenbone Vulnerability Management framework.

%package -n libopenvas_wincmd-devel
Summary:        Development files for the OpenVAS wincmd library
Group:          Development/Libraries/C and C++
Requires:       libopenvas_wincmd%{sover} = %{version}

%description -n libopenvas_wincmd-devel
The support libraries for the Greenbone Vulnerability Management framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libopenvas_wincmd.

%package -n libopenvas_wmiclient%{sover}
Summary:        Support libraries for GVM
Group:          System/Libraries

%description -n libopenvas_wmiclient%{sover}
The support libraries for the Greenbone Vulnerability Management framework.

%package -n libopenvas_wmiclient-devel
Summary:        Development files for the OpenVAS wmiclient library
Group:          Development/Libraries/C and C++
Requires:       libopenvas_wmiclient%{sover} = %{version}

%description -n libopenvas_wmiclient-devel
The support libraries for the Greenbone Vulnerability Management framework.

This subpackage contains libraries and header files for developing
applications that want to make use of libopenvas_wmiclient.

%prep
%setup -q
%patch0 -p1
# Fix libheimdal include path
find . -name '*.[c\|h]' -print0 | xargs -0 sed -i 's|heimdal\/||g'

%build
%cmake -DCMAKE_C_FLAGS="-Wno-address -std=c11"
%make_jobs

%install
%cmake_install

%post -n libopenvas_wincmd%{sover} -p /sbin/ldconfig
%post -n libopenvas_wmiclient%{sover} -p /sbin/ldconfig
%postun -n libopenvas_wincmd%{sover} -p /sbin/ldconfig
%postun -n libopenvas_wmiclient%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc CHANGES README.md
%{_bindir}/winexe
%{_bindir}/wmic
%{_mandir}/man1/winexe.1%{?ext_man}
%{_mandir}/man1/wmic.1%{?ext_man}

%files -n libopenvas_wmiclient%{sover}
%{_libdir}/libopenvas_wmiclient.so.%{sover}*

%files -n libopenvas_wmiclient-devel
%dir %{_includedir}/openvas
%dir %{_includedir}/openvas/smb
%{_includedir}/openvas/smb/*.h
%{_libdir}/libopenvas_wmiclient.so
%{_libdir}/pkgconfig/libopenvas_wmiclient.pc

%files -n libopenvas_wincmd%{sover}
%{_libdir}/libopenvas_wincmd.so.%{sover}*

%files -n libopenvas_wincmd-devel
%{_libdir}/libopenvas_wincmd.so
%{_libdir}/pkgconfig/libopenvas_wincmd.pc

%changelog
