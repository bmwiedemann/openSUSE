#
# spec file for package xinit
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xinit
Version:        1.4.1
Release:        0
Summary:        X Window System initializer
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:        xinit.tar.bz2
Source2:        keygen.c
Source3:        keygen.1
Patch0:         xinit.diff
Patch1:         xinit-client-session.patch
Patch2:         xinit-suse.patch
Patch3:         xinit-tolerant-hostname-changes.patch
Patch4:         xinit-nolonger-unset-dbus-session.patch
# needed for patch0
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
Requires:       setxkbmap
Requires:       xauth
Requires:       xmodmap
Requires:       xrdb
Requires:       xsetroot
%if 0%{?suse_version} > 1320
Requires:       xterm-bin
%else
Requires:       xterm
%endif
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The xinit program is used to start the X Window System server and a
first client program on systems that are not using a display manager
such as xdm or in environments that use multiple window systems.
When this first client exits, xinit will kill the X server and then
terminate.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
# needed for patch0
autoreconf -fi

%build
%configure
make %{?_smp_mflags}
%{__cc} %{optflags} -o keygen %{SOURCE2}

%install
%make_install
install -m 0644 %{SOURCE3} %{buildroot}%{_mandir}/man1
install -m 0711 keygen %{buildroot}%{_bindir}/keygen
pushd %{buildroot}
tar xf %{SOURCE1}
popd
install -D %{buildroot}%{_sysconfdir}/X11/xinit/xinitrc %{buildroot}%{_sysconfdir}/skel/.xinitrc.template

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README.md
%config %{_sysconfdir}/X11/xinit/
%config %{_sysconfdir}/X11/Xresources
%config %{_sysconfdir}/skel/.xinitrc.template
%{_bindir}/keygen
%{_bindir}/startx
%{_bindir}/xinit
%{_mandir}/man1/keygen.1%{?ext_man}
%{_mandir}/man1/startx.1%{?ext_man}
%{_mandir}/man1/xinit.1%{?ext_man}

%changelog
