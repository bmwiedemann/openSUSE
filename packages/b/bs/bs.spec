#
# spec file for package bs
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


Name:           bs
Version:        2.13
Release:        0
Summary:        Battleships solitaire game with a color interface
License:        BSD-2-Clause
Group:          Amusements/Games/Strategy/Turn Based
URL:            http://www.catb.org/~esr/bs/
Source0:        http://www.catb.org/~esr/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  hicolor-icon-theme
BuildRequires:  ncurses-devel
BuildRequires:  update-desktop-files

%description
The classic game of Battleships against the computer. Uses character-cell
graphics with a visual point-and-shoot interface. If you're using an xterm
under Linux the mouse will work.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install
%suse_update_desktop_file %{name}

%files
%license COPYING
%doc NEWS.adoc README
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{?ext_man}
%{_datadir}/appdata/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/

%changelog
