#
# spec file for package nbsdgames
#
# Copyright (c) 2022 SUSE LLC
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


Name:           nbsdgames
Version:        5
Release:        0
Summary:        A collection of text-based games
License:        CC0-1.0
Group:          Amusements/Games/Other
URL:            https://github.com/abakh/nbsdgames
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  ncurses-devel
BuildRequires:  update-desktop-files

%description
A new collection of console games inspired by the classic bsd-games collection.

%prep
%setup -q

%build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
make install GAMES_DIR=%{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man6
make manpages MAN_DIR=%{buildroot}%{_mandir}/man6

install -D nbsdgames.desktop %{buildroot}%{_datadir}/applications/nbsdgames.desktop
install -D nbsdgames.svg %{buildroot}%{_datadir}/pixmaps/nbsdgames.svg
chmod -x %{buildroot}%{_datadir}/pixmaps/nbsdgames.svg
%suse_update_desktop_file %{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_mandir}/man6/*.6%{?ext_man}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/nbsdgames.svg

%changelog
