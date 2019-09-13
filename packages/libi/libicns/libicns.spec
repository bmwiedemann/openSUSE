#
# spec file for package libicns
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define         libname %{name}1
Name:           libicns
Version:        0.8.1
Release:        0
Summary:        Application for manipulation of the Mac OS icns
License:        LGPL-2.1-or-later
Group:          Productivity/Graphics/Convertors
Url:            http://icns.sourceforge.net/
Source0:        http://download.sourceforge.net/icns/%{name}-%{version}.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libpng)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Group:          Productivity/Graphics/Convertors

%description -n icns-utils
Utilities to convert to and from icns files using %{name}:
    1. png2icns: Tool to convert png icons to icns icons,
    2. icns2png: Tool to convert icns icons to png, and
    3. icontainer2icns: Tool for extracting icns files from icontainers.

%package -n %{libname}
Summary:        System libraries for %{name}
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n %{libname}
System libraries file for %{name}.

%package devel
Summary:        Development files for %{name}
License:        LGPL-2.1-only
Group:          Development/Libraries/Other
Requires:       %{libname} = %{version}
Provides:       %{libname}-devel = %{version}
Requires:       glibc-devel

%description devel
Libraries and header files for developing applications that use libicns.

%prep
%setup -q

%build
%configure \
  --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n icns-utils
%defattr(-,root,root)
%doc README COPYING* ChangeLog NEWS TODO
%{_bindir}/png2icns
%{_bindir}/icns2png
%{_bindir}/icontainer2icns
%{_mandir}/man1/*.gz

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%doc src/apidocs.* DEVNOTES
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
