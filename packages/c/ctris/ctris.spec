#
# spec file for package ctris
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           ctris
Version:        0.43
Release:        0
Summary:        Console based Tetris clone
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Arcade
URL:            https://github.com/0xminik/ctris
#Git-Clone:     https://github.com/0xminik/ctris.git
Source:         https://github.com/0xminik/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ncurses-devel

%description
A colorized, small and flexible Tetris clone for the console.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install BINDIR="%{buildroot}%{_bindir}"

%files
%license COPYING
%doc AUTHORS README TODO
%{_mandir}/man6/ctris.6%{?ext_man}
%{_bindir}/ctris

%changelog
