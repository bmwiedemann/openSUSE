#
# spec file for package twin
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Malcolm J Lewis <malcolmlewis@opensuse.org>
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
Version:        0.8.0
Release:        0
Summary:        Textmode WINdow environment
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://sourceforge.net/projects/twin/
Source0:        https://github.com/cosmos72/twin/archive/v0.8.0.tar.gz
Source1:        twin-rpmlintrc
BuildRequires:  ncurses-devel
BuildRequires:  zlib-devel
Recommends:     gpm
BuildRequires:  gpm-devel
BuildRequires:  libXpm-devel

%description
Twin is a text-mode window environment. It supports mouse and multiple
windows, has a built-in terminal emulator and window manager, and can
serve as display for client applications. Its retro look-and-feel comes
with very modern features: it is best described as a VNC-like server,
that can use a variety of displays - all with mouse support: from a
plain text terminal, to a Linux console, to a full kde, gnome or X11
desktop.

%package -n libTutf1
Version:        1.0.0
Summary:        Unicode/Charset conversion library for twin

%description -n libTutf1
Unicode <-> charset conversion routines for twin.

%package -n libTutf-devel
Version:        1.0.0
Requires:       libTutf1 = %{version}
Summary:        Unicode/Charset conversion library for twin

%description -n libTutf-devel
Unicode <-> charset conversion routines for twin.

%package -n libTw5
Version:        5.0.0
Summary:        Main library for twin

%description -n libTw5
Main library for twin

%package -n libTw-devel
Version:        5.0.0
Summary:        Main library for twin
Requires:       libTw5 = %{version}

%description -n libTw-devel
Development files for twins main library.

%prep
%setup -q

%build
%configure --enable-tt=yes \
           --enable-hw-tty=yes \
	   --enable-hw-tty-linux=yes \
	   --enable-hw-tty-twterm=yes \
	   --enable-hw-tty-termcap=yes \
	   --enable-hw-x11=yes \
	   --enable-hw-gfx=yes \
	   --enable-hw-twin=yes \
	   --enable-hw-display=yes \
	   --enable-ext=yes \
	   --enable-ext-tt=yes \
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

%post -n libTw5 -p /sbin/ldconfig
%postun -n libTw5 -p /sbin/ldconfig

%post -n libTutf1 -p /sbin/ldconfig
%postun -n libTutf1 -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB
%doc BUGS Changelog.txt README README.porting TODOS/*
%{_bindir}/tw*
%{_sbindir}/twdm
%{_libdir}/twin
%{_datadir}/twin
%{_mandir}/man1/twin.1%{?ext_man}

%files -n libTutf1
%{_libdir}/libTutf.so.*

%files -n libTutf-devel
%{_includedir}/Tutf
%{_libdir}/libTutf.so

%files -n libTw5
%{_libdir}/libTw.so.*

%files -n libTw-devel
%{_includedir}/Tw
%{_libdir}/libTw.so

%changelog
