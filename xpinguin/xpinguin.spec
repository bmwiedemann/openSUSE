#
# spec file for package xpinguin
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xpinguin
BuildRequires:  imake
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)
Summary:        The 'Logo' of Linux 2.0
License:        GPL-2.0+
Group:          Amusements/Toys/Graphics
Version:        1.0.2
Release:        0
Source:         xpinguin.tar.gz
Source1:        xpinguin.png
Source2:        xpinguin.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Based on xteddy -- really cute ;-)



Authors:
--------
    Stefan Gustavson <stefang@isy.liu.se>
    Jens Poenisch <J.Poenisch@wirtschaft.tu-chemnitz.de>

%prep
%setup -n xpinguin
ln -s xpinguin.1 xpinguin.man
xmkmf -a

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install install.man
rm -f   $RPM_BUILD_ROOT/usr/X11R6/man/man1/xpinguin.1x.gz
%suse_update_desktop_file -i xpinguin Amusement

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%_bindir/xpinguin
%_mandir/man1/xpinguin.1x.gz
/usr/share/applications/xpinguin.desktop
/usr/share/pixmaps/xpinguin.png

%changelog
