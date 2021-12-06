#
# spec file for package xpenguins
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


Name:           xpenguins
Version:        3.2.1
Release:        0
Summary:        Cute little penguins that walk along the tops of your windows
License:        GPL-2.0-or-later
Group:          Amusements/Toys/Background
URL:            http://xpenguins.seul.org/
Source:         https://sourceforge.net/projects/xpenguins/files/xpenguins-%{version}.tar.gz
Source1:        README.openSUSE
Source2:        %{name}-stop.desktop
Source3:        %{name}-stop.png
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)

%description
This program animates a friendly family of penguins on your root
window. They drop in from the top of the screen, walk along the tops of
your windows, up the sides of your windows, up the side of the screen,
and sometimes even levitate with their genetically-modified
go-go-gadget 'copter ability.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
cp %{SOURCE3} %{buildroot}%{_datadir}/pixmaps
%suse_update_desktop_file    %{name} Amusement
%suse_update_desktop_file -i %{name}-stop Amusement
%fdupes %{buildroot}

%files
%license COPYING
%doc README* AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/xpenguins
%{_mandir}/man1/xpenguins.1%{?ext_man}
%{_datadir}/xpenguins
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/pixmaps/%{name}-stop.png
%{_datadir}/applications/*.desktop

%changelog
