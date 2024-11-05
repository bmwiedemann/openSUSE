#
# spec file for package xpinguin
#
# Copyright (c) 2024 SUSE LLC
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


Name:           xpinguin
Version:        1.0.2
Release:        0
Summary:        The 'Logo' of Linux 2.0
License:        GPL-2.0-or-later
Group:          Amusements/Toys/Graphics
Source:         xpinguin.tar.gz
Source1:        xpinguin.png
Source2:        xpinguin.desktop
Patch1:         0001-Fix-to-compile-with-gcc-14.2.1.patch
BuildRequires:  imake
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xpm)

%description
Based on xteddy -- really cute ;-)

%prep
%autosetup -n xpinguin
ln -s xpinguin.1 xpinguin.man
xmkmf -a

%build
%make_build CC="cc %{optflags}"

%install
%make_install install.man
rm -f   %{buildroot}%{_prefix}/X11R6/man/man1/xpinguin.1x.gz
%suse_update_desktop_file -i xpinguin Amusement

%files
%{_bindir}/xpinguin
%{_mandir}/man1/xpinguin.1x.gz
%{_datadir}/applications/xpinguin.desktop
%{_datadir}/pixmaps/xpinguin.png

%changelog
