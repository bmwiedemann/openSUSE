#
# spec file for package xmahjongg
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


Name:           xmahjongg
Version:        3.7
Release:        0
Summary:        Colorful X solitaire MahJongg game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Board/Card
URL:            http://www.lcdf.org/xmahjongg/
Source0:        http://www.lcdf.org/xmahjongg/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
BuildRequires:  gcc-c++
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
Conflicts:      xmahjong

%description
Real Mah Jongg is a social game that originated in China thousands of
years ago. Four players, named after the four winds, take tiles from a
wall in turn. The best tiles are made of ivory and wood; they click
pleasantly when you knock them together. Computer Solitaire Mah Jongg
(xmahjongg being one of the sillier examples) is nothing like that but
it's fun, or it must be, since there are like 300 shareware versions
available for Windows. This is for X11 and it's free.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
install -D %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%suse_update_desktop_file -i %{name}

%files
%doc NEWS README
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/applications/%{name}.*
%{_mandir}/man6/%{name}.6*
%{_datadir}/%{name}

%changelog
