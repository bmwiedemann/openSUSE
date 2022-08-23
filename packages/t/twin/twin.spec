#
# spec file for package twin
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2012-2022 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           twin
Version:        0.9.0+17
Release:        0
Summary:        Textmode WINdow environment
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://github.com/cosmos72/twin
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  gpm-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)
Recommends:     gpm

%description
Twin is a text-mode window environment. It supports mouse and multiple
windows, has a built-in terminal emulator and window manager, and can
serve as display for client applications. Its retro look-and-feel comes
with very modern features: it is best described as a VNC-like server,
that can use a variety of displays - all with mouse support: from a
plain text terminal, to a Linux console, to a full kde, gnome or X11
desktop.

%package -n libtstl1
Version:        0.9.0+17
Release:        0
Summary:        Server library for twin

%description -n libtstl1
Server library for twin

%package -n libtutf1
Version:        0.9.0+17
Release:        0
Summary:        Unicode/Charset conversion library for twin
Provides:       libTutf1 = %{version}-%{release}
Obsoletes:      libTutf1 = 1.0.0

%description -n libtutf1
Unicode <-> charset conversion routines for twin.

%package -n libtutf-devel
Version:        0.9.0+17
Release:        0
Summary:        Unicode/Charset conversion library for twin
Requires:       libtutf1 = %{version}
Provides:       libTutf-devel = %{version}-%{release}
Obsoletes:      libTutf-devel = 1.0.0

%description -n libtutf-devel
Unicode <-> charset conversion routines for twin.

%package -n libtw1
Version:        0.9.0+17
Release:        0
Summary:        Main library for twin
Provides:       libTw5 = %{version}-%{release}
Obsoletes:      libTw5 = 5.0.0

%description -n libtw1
Main library for twin

%package -n libtw-devel
Version:        0.9.0+17
Release:        0
Summary:        Main library for twin
Requires:       libtstl1 = %{version}
Requires:       libtw1 = %{version}
Provides:       libTw-devel = %{version}-%{release}
Obsoletes:      libTw-devel = 5.0.0

%description -n libtw-devel
Development files for twin main library.

%prep
%autosetup -p1

%build
%configure --enable-wm=yes \
           --enable-wm-rc=yes \
           --enable-term=yes \
           --enable-hw-tty=yes \
           --enable-hw-tty-linux=yes \
           --enable-hw-tty-twterm=yes \
           --enable-hw-tty-termcap=yes \
           --enable-hw-x11=yes \
           --enable-hw-xft=yes \
           --enable-hw-twin=yes \
           --enable-hw-display=yes \
           --enable-static=no
make %{?_smp_mflags}

%install
%make_install
# Clean up
find %{buildroot}%{_libdir} -name '*.a' -type f -delete -print
find %{buildroot} -type f -name "*.la" -delete -print
# Remove installed files as we package as %%docs
pushd %{buildroot}%{_datadir}/twin/
rm BUGS Changelog.txt COPYING COPYING.LIB INSTALL README README.porting
popd

%post -n libtstl1 -p /sbin/ldconfig
%postun -n libtstl1 -p /sbin/ldconfig

%post -n libtw1 -p /sbin/ldconfig
%postun -n libtw1 -p /sbin/ldconfig

%post -n libtutf1 -p /sbin/ldconfig
%postun -n libtutf1 -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB
%doc BUGS Changelog.txt README README.porting TODO/*
%{_bindir}/tw*
%{_sbindir}/twdm
%{_libdir}/twin
%{_datadir}/twin
%{_mandir}/man1/twin.1%{?ext_man}

%files -n libtstl1
%{_libdir}/libtstl.so.*

%files -n libtutf1
%{_libdir}/libtutf.so.*

%files -n libtutf-devel
%{_includedir}/Tutf
%{_libdir}/libtutf.so

%files -n libtw1
%{_libdir}/libtw.so.*

%files -n libtw-devel
%{_includedir}/Tw
%{_libdir}/libtw.so
%{_libdir}/libtstl.so

%changelog
