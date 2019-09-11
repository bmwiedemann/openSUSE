#
# spec file for package xpenguins
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xpenguins
Version:        2.2
Release:        0
Summary:        cute little penguins that walk along the tops of your windows
License:        GPL-2.0+
Group:          Amusements/Toys/Background
Url:            http://xpenguins.seul.org/
Source:         xpenguins-%{version}.tar.bz2
Source1:        README.openSUSE
Source2:        %{name}.desktop
Source3:        %{name}-stop.desktop
Source4:        %{name}.png
Source5:        %{name}-stop.png
Patch0:         xpenguins-%{version}-typo.diff
Patch1:         xpenguins-%{version}-automake-1.13.diff
BuildRequires:  automake
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This program animates a friendly family of penguins on your root
window. They drop in from the top of the screen, walk along the tops of
your windows, up the sides of your windows, up the side of the screen,
and sometimes even levitate with their genetically-modified
go-go-gadget 'copter ability.

%prep
%setup -q
%patch0
%patch1 -p1
cp %{SOURCE1} %{SOURCE4} %{SOURCE5} .

%build
aclocal
automake -a
autoconf
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{name}.png %{name}-stop.png %{buildroot}%{_datadir}/pixmaps
%suse_update_desktop_file -i %{name} Amusement
%suse_update_desktop_file -i %{name}-stop Amusement

%files
%defattr(-,root,root)
%doc README* AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xpenguins
%doc %{_mandir}/man1/xpenguins.1*
%{_datadir}/xpenguins
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%changelog
