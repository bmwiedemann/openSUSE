#
# spec file for package input-pad
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define libinput_paddir %{_libdir}/%{name}-1.1
%define moduledir       %{_libdir}/%{name}-1.1/modules
%define kbduidir        %{_libdir}/%{name}-1.1/modules/kbdui
%define xkeysenddir     %{_libdir}/%{name}-1.1/modules/xkeysend
%define build_xtest    (0%{?suse_version} > 1210)
Name:           input-pad
Version:        1.1.0
Release:        0
Summary:        On-screen Input Pad to Send Characters with Mouse
License:        LGPL-2.0-or-later
URL:            https://github.com/fujiwarat/input-pad
Source0:        https://github.com/fujiwarat/input-pad/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  swig
BuildRequires:  pkgconfig(eek-0.90)
BuildRequires:  pkgconfig(eek-gtk-0.90)
BuildRequires:  pkgconfig(eek-xkl-0.90)
BuildRequires:  pkgconfig(eekboard-0.90)
BuildRequires:  pkgconfig(gail)
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-broadway-3.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.37
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gobject-introspection-no-export-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-broadway-3.0)
BuildRequires:  pkgconfig(gtk+-unix-print-2.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)
BuildRequires:  pkgconfig(libxklavier) >= 4.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.0
Requires:       python3-gobject
Obsoletes:      python-input-pad
%if 0%{?suse_version} > 1210
BuildRequires:  pkgconfig(xkbfile)
%endif
%if %{build_xtest}
BuildRequires:  pkgconfig(xtst)
%endif

%description
The input pad is a tool to send a character on a button to text applications.

%package devel
Summary:        Development tools for input-pad
Requires:       %{name} = %{version}-%{release}

%description devel
The input-pad-devel package contains the header files.

%if %{build_xtest}
%package xtest
Summary:        Input Pad with XTEST extension
Requires:       %{name} = %{version}-%{release}

%description xtest
The input-pad-xtest package contains the XTEST extension module.
%endif

%package eek
Summary:        Input Pad with eekboard extension
Requires:       %{name} = %{version}-%{release}

%description eek
The input-pad-eek package contains the eekboard extension module.

%prep
%setup -q

%build
%configure    --enable-pygobject2         \
              --enable-eek                \
%if %{build_xtest}
             --enable-xtest              \
%endif
             --disable-static

%make_build

%install
make install DESTDIR=%{buildroot} INSTALL='install -p'

if [ ! -d %{buildroot}%{kbduidir} ] ; then
    mkdir -p %{buildroot}%{kbduidir}
fi
if [ ! -d %{buildroot}%{xkeysenddir} ] ; then
    mkdir -p %{buildroot}%{xkeysenddir}
fi

find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_libdir}/*.a
%if %{build_xtest}
rm -f %{buildroot}%{xkeysenddir}/*.la
rm -f %{buildroot}%{xkeysenddir}/*.a
%endif
rm -f %{buildroot}%{kbduidir}/*.la
rm -f %{buildroot}%{kbduidir}/*.a

%find_lang %{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%{_bindir}/input-pad
%dir %{libinput_paddir}
%dir %{moduledir}
%dir %{xkeysenddir}
%dir %{kbduidir}
%{_libdir}/libinput-pad-*.so.*
%{_libdir}/girepository-1.0/InputPad-1.1.typelib
%{_datadir}/%{name}
%{_datadir}/pixmaps/input-pad.png
%{_mandir}/man1/input-pad.1%{?ext_man}

%files devel
%{_includedir}/%{name}-1.1
%{_libdir}/libinput-pad-*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/InputPad-1.1.gir

%if %{build_xtest}
%files xtest
%{xkeysenddir}/libinput-pad-xtest-gdk.so
%endif

%files eek
%{kbduidir}/libinput-pad-eek-gtk.so

%changelog
