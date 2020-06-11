#
# spec file for package libicns
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2011 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%define sover   1
Name:           libicns
Version:        0.8.1+git20190323
Release:        0
Summary:        Application for manipulation of the Mac OS icns
License:        LGPL-2.1-or-later AND LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            https://icns.sourceforge.io/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
Recommends:     unar

%description
It can read and write files from the Mac OS X icns format, as well as
read from Mac OS resource files and macbinary encoded Mac OS resource
forks. As of release 0.5.9, it can fully read and write any 128x128 and
all smaller 32-bit icons, and read support for 8-bit, 4-bit, and 1-bit
icons. If linked against Jasper, it also has full support for 256x256
and 512x512 32-bit icons with masks as alpha channels.

The package contains icns2png, png2icns and icontainer2icns.

%package -n icns-utils
Summary:        Application for manipulation of the Mac OS icns
License:        GPL-2.0-only

%description -n icns-utils
Utilities to convert to and from icns files using %{name}:
    1. png2icns: Tool to convert png icons to icns icons,
    2. icns2png: Tool to convert icns icons to png, and
    3. icontainer2icns: Tool for extracting icns files from icontainers.

%package -n %{name}%{sover}
Summary:        System libraries for %{name}
License:        LGPL-2.1-only

%description -n %{name}%{sover}
System libraries file for %{name}.

%package devel
Summary:        Development files for %{name}
License:        LGPL-2.1-only
Requires:       %{name}%{sover} = %{version}
Requires:       glibc-devel

%description devel
Libraries and header files for developing applications that use libicns.

%prep
%autosetup

%build
autoreconf -fiv
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{name}%{sover} -p /sbin/ldconfig

%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n icns-utils
%license COPYING*
%doc README ChangeLog NEWS TODO
%{_bindir}/icns2png
%{_bindir}/icnsutil
%{_bindir}/icontainer2icns
%{_bindir}/png2icns
%{_mandir}/man1/icns2png.1%{?ext_man}
%{_mandir}/man1/icnsutil.1%{?ext_man}
%{_mandir}/man1/icontainer2icns.1%{?ext_man}
%{_mandir}/man1/png2icns.1%{?ext_man}

%files -n %{name}%{sover}
%{_libdir}/%{name}.so.%{sover}*

%files devel
%doc src/apidocs.* DEVNOTES
%{_includedir}/icns.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
