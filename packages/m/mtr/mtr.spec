#
# spec file for package mtr
#
# Copyright (c) 2023 SUSE LLC
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


Name:           mtr
Version:        0.95
Release:        0
Summary:        Ping and Traceroute Network Diagnostic Tool
License:        GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
URL:            https://www.bitwizard.nl/mtr/
Source:         https://github.com/traviscross/mtr/archive/refs/tags/v%{version}.tar.gz#/mtr-%{version}.tar.gz
Source1:        xmtr.desktop
Patch1:         mtr-0.75-manmtr.patch
Patch2:         mtr-0.87-manxmtr.patch
Patch3:         mtr-fixoverflow.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk3-devel
BuildRequires:  libcap-devel
BuildRequires:  libjansson-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  update-desktop-files
Requires(post): permissions
Recommends:     bash-completion

%description
Mtr is a network diagnostic tool that combines Ping and Traceroute into
one program. This package contains the mtr version with an ncurses
interface, in other words, the text mode version is usable in a shell
(telnet or SSH session, for example).

Find the graphical version in the mtr-gtk package.

%package gtk
Summary:        Ping and Traceroute Network Diagnostic Tool
# needed for mtr-packet
Group:          Productivity/Networking/Diagnostic
Requires:       %{name} = %{version}
Requires:       xdg-utils

%description gtk
Mtr is a network diagnostic tool which combines Ping and Traceroute
into one program. This package contains mtr with a GTK interface.
You'll find the text mode version in the mtr package.

%prep
%setup -q
cp man/mtr.8.in man/xmtr.8.in
%autopatch -p1

%build
echo "%{version}" >.tarball-version
autoreconf -fvi

%configure \
	--disable-silent-rules \
	--enable-ipv6 \
	--with-json \
	--with-gtk \
	--disable-gtktest
%make_build
mv mtr xmtr
%make_build distclean
# console version
%configure \
	--disable-silent-rules \
	--enable-ipv6 \
	--with-json \
	--without-gtk
%make_build

%install
%make_install

# xmtr fun
install -m 4755 xmtr %{buildroot}%{_sbindir}
install -m 644 xmtr.8 %{buildroot}/%{_mandir}/man8
install -Dm 644 img/mtr_icon.xpm %{buildroot}%{_includedir}/X11/pixmaps/xmtr_icon.xpm
install -Dm 644 img/mtr_icon.xpm %{buildroot}%{_datadir}/pixmaps/xmtr_icon.xpm
%suse_update_desktop_file -i xmtr Network Monitor

%post
%set_permissions %{_sbindir}/mtr-packet

%verifyscript
%verify_permissions -e %{_sbindir}/mtr-packet

%files
%doc AUTHORS NEWS SECURITY TODO
%license COPYING
%{_datadir}/bash-completion/completions/mtr
%{_mandir}/man8/mtr-packet.8%{?ext_man}
%{_mandir}/man8/mtr.8%{?ext_man}
%verify(not caps) %attr(755,root,root) %{_sbindir}/mtr-packet
%attr(755,root,root) %{_sbindir}/mtr

%files gtk
%doc AUTHORS NEWS SECURITY TODO
%license COPYING
%{_mandir}/man8/xmtr.8%{?ext_man}
%attr(755,root,root) %{_sbindir}/xmtr
%{_includedir}/X11/pixmaps
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
