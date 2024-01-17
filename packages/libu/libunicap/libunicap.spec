#
# spec file for package libunicap
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


%define _use_internal_dependency_generator 0
%{expand:%%define prev__find_provides %{__find_provides}}
%define __find_provides sh %{SOURCE1} %{prev__find_provides}
%{expand:%%define prev__find_requires %{__find_requires}}
%define __find_requires sh %{SOURCE1} %{prev__find_requires}

Name:           libunicap
Version:        0.9.12
Release:        0
Summary:        Library to access different kinds of (video) capture devices
License:        GPL-2.0-or-later
Group:          Hardware/Camera
URL:            http://www.unicap-imaging.org/
Source0:        %{name}-%{version}.tar.bz2
Source1:        libunicap-filter.sh
Source2:        baselibs.conf
# PATCH-FIX-OPENSUSE openSUSE puts the videodev headers somewhere different in 12.1
Patch1:         libunicap-0.9.12-find_videodev.patch
# PATCH-FIX-UPSTREAM uses the reserved keyword "private" https://bugs.launchpad.net/unicap/+bug/656229
Patch2:         libunicap_0912_fixPrivate.patch
# PATCH-FIX-UPSTREAM libunicap-udev.patch bnc726471 https://bugs.launchpad.net/unicap/+bug/959626 sbrabec@suse.cz -- port rules to the new udev
Patch3:         libunicap-udev.patch
Patch4:         unicap-implicit-fortify-decl.patch
# Patches from Fedora:
Patch5:         libunicap-0.9.12-gcc10.patch
Patch8:         libunicap-0.9.12-arraycmp.patch
Patch9:         libunicap-0.9.12-datadirname.patch
Patch10:        libunicap-bz641623.patch
Patch12:        libunicap-0.9.12-memerrs.patch
BuildRequires:  alsa-lib-devel
BuildRequires:  gettext
BuildRequires:  gtk-doc >= 1.4
BuildRequires:  intltool
BuildRequires:  libogg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libraw1394)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(udev)
%if 0%{?suse_version} >= 1210
BuildRequires:  libv4l-devel >= 0.8.4
%else
BuildRequires:  kernel-devel
BuildRequires:  libv4l-devel
%endif
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d
%description
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
The included ucil library provides easy to use functions to render text
and graphic overlays onto video images.

%package -n libunicap2

Summary:        Library to access different kinds of (video) capture devices
Group:          Hardware/Camera
Provides:       unicap = %{version}
Obsoletes:      unicap < %{version}

%description -n libunicap2
Unicap provides a uniform interface to video capture devices. It allows
applications to use any supported video capture device via a single API.
The included ucil library provides easy to use functions to render text
and graphic overlays onto video images.

%package devel

Summary:        Development files for the unicap library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libunicap2 = %{version}

%description devel
This package includes header files and libraries necessary for
developing programs which use the unicap, unicapgtk, and ucil libraries. It
contains the API documentation of the library, too.

%prep
%setup -q -n %{name}-%{version}
%autopatch -p1
%build
mkdir -p m4
autoreconf -fiv
intltoolize --force
%configure --disable-rpath --disable-static --enable-gtk-doc-html=no --enable-libv4l
make %{?_smp_mflags}

%install
%make_install
# Don't install any static .a and libtool .la files
rm -f %{buildroot}%{_libdir}/{,unicap2/cpi/}*.{a,la}

%find_lang unicap

%post   -n libunicap2 -p /sbin/ldconfig

%postun -n libunicap2 -p /sbin/ldconfig

%files -n libunicap2 -f unicap.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/*.so.*
%{_libdir}/unicap2
%{_udevrulesdir}/50-euvccam.rules

%files devel
%defattr(-,root,root)
%{_datadir}/gtk-doc/html/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/unicap

%changelog
