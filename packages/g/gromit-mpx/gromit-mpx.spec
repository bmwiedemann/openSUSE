#
# spec file for package gromit-mpx
#
# Copyright (c) 2021 SUSE LLC
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


Name:           gromit-mpx
Version:        1.4
Release:        0
Summary:        A desktop annotation tool
License:        GPL-2.0-or-later
URL:            https://github.com/bk138/gromit-mpx
Source:         https://github.com/bk138/gromit-mpx/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(appindicator3-0.1) >= 0.4.92
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi) >= 1.3
Provides:       gromit = %{version}-%{release}
Obsoletes:      gromit = 20041213

%description
Gromit-MPX is a multi-pointer GTK3 port of the original Gromit desktop annotation tool.
It enables graphical annotations with several pointers at once and is A LOT faster than
its predecessor since it uses the XCOMPOSITE extension where available.

%prep
%autosetup -p1

%build
%cmake -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build

%install
%cmake_install
rm -rv %{buildroot}%{_datadir}/doc/

%files
%license COPYING
%doc AUTHORS ChangeLog *.md
%config(noreplace) %{_sysconfdir}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/net.christianbeier.Gromit-MPX.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/icons/hicolor/scalable/apps/gromit-mpx_active.svg
%{_datadir}/icons/hicolor/scalable/apps/net.christianbeier.Gromit-MPX.svg
%{_datadir}/metainfo/net.christianbeier.Gromit-MPX.appdata.xml
%{_datadir}/pixmaps/gromit-mpx_active.png

%changelog
