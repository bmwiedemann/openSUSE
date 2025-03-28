#
# spec file for package zbar
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2010 Carlos Goncalves <cgoncalves@opensuse.org>.
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


%define sover   0
%define libname lib%{name}%{sover}
Name:           zbar
Version:        0.23.93
Release:        0
Summary:        Bar code reader
License:        LGPL-2.0-or-later
URL:            https://github.com/mchehab/zbar
Source0:        https://linuxtv.org/downloads/%{name}/%{name}-%{version}.tar.bz2
Source98:       baselibs.conf
# https://github.com/mchehab/zbar/issues/277
Patch0:         https://github.com/mchehab/zbar/commit/368571ffa1a0f6cc41f708dd0d27f9b6e9409df8.patch#/zbar-pkgconfig.patch
# https://github.com/mchehab/zbar/issues/277
Patch1:         https://github.com/mchehab/zbar/commit/a549566ea11eb03622bd4458a1728ffe3f589163.patch#/zbar-configure.patch
BuildRequires:  automake
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.9.0
BuildRequires:  xmlto
BuildRequires:  pkgconfig(ImageMagick)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xv)
%lang_package

%description
ZBar reads bar codes from various sources, such as video streams,
image files and raw intensity sensors. It supports many symbologies
(types of bar codes) including EAN-13/UPC-A, UPC-E, EAN-8, Code 128,
Code 39, Interleaved 2 of 5 and QR Code.

It can be used through the standalone GUI and command-line programs,
or integrated by other programs through a library.

%package -n %{libname}
Summary:        Bar code reading library

%description -n %{libname}
ZBar reads bar codes from various sources, such as video streams,
image files and raw intensity sensors. It supports many symbologies
(types of bar codes) including EAN-13/UPC-A, UPC-E, EAN-8, Code 128,
Code 39, Interleaved 2 of 5 and QR Code.

This package provides the ZBar library.

%package -n lib%{name}-devel
Summary:        Development environment for the ZBar library
Requires:       %{libname} = %{version}

%description -n lib%{name}-devel
This package contains all necessary include files, libraries,
configuration files and development tools needed to compile and link
applications using the zbar library.

%package -n lib%{name}qt0
Summary:        ZBar Qt bindings

%description -n lib%{name}qt0
This package provides ZBar Qt bindings.

%package -n lib%{name}qt-devel
Summary:        Development environment for the ZBar Qt bindings library
Requires:       lib%{name}-devel = %{version}
Requires:       lib%{name}qt0 = %{version}

%description -n lib%{name}qt-devel
This package contains all necessary include files, libraries,
configuration files and development tools needed to compile and link
applications using the zbar-qt library.

%package -n python3-zbar
Summary:        Python3 module for ZBar

%description -n python3-zbar
This package contains the module to use ZBar from python3.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
  --docdir=%{_docdir}/%{name} \
  --disable-static \
  --without-java \
  --with-python=python3 \
  --without-gtk
%make_build

%install
%make_install
find %{buildroot} -name "*.la"  -or -name "*.a" | xargs rm -f
rm -rf %{buildroot}%{_datadir}/doc/zbar-%{version}/
rm -f %{buildroot}%{_docdir}/zbar/{COPYING,LICENSE.md,INSTALL.md}

%find_lang %{name}
# Lets wait for review first
rm -rf %{buildroot}%{_sysconfdir}/dbus-1/system.d/org.linuxtv.Zbar.conf

%ldconfig_scriptlets -n %{libname}
%ldconfig_scriptlets -n libzbarqt0

%files
%license COPYING LICENSE.md
%{_defaultdocdir}/%{name}/
%{_bindir}/zbarimg
%{_bindir}/zbarcam
%{_bindir}/zbarcam-qt
%{_mandir}/man1/*

%files lang -f %{name}.lang

%files -n %{libname}
%{_libdir}/libzbar.so.%{sover}*

%files -n lib%{name}-devel
%doc HACKING.md TODO.md
%dir %{_includedir}/%{name}
%{_includedir}/zbar.h
%{_includedir}/zbar/Exception.h
%{_includedir}/zbar/Symbol.h
%{_includedir}/zbar/Image.h
%{_includedir}/zbar/Scanner.h
%{_includedir}/zbar/Decoder.h
%{_includedir}/zbar/ImageScanner.h
%{_includedir}/zbar/Video.h
%{_includedir}/zbar/Window.h
%{_includedir}/zbar/Processor.h
%{_libdir}/libzbar.so
%{_libdir}/pkgconfig/zbar.pc

%files -n lib%{name}qt0
%{_libdir}/libzbarqt.so.%{sover}*

%files -n lib%{name}qt-devel
%{_includedir}/%{name}/QZBar*.h
%{_libdir}/libzbarqt.so
%{_libdir}/pkgconfig/zbar-qt.pc

%files -n python3-zbar
%{python3_sitearch}/zbar.so

%changelog
