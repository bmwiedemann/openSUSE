#
# spec file for package nbsdgames
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        6.0.1
Release:        0
Summary:        A collection of text-based games
License:        CC0-1.0
Group:          Amusements/Games/Other
URL:            https://github.com/abakh/nbsdgames
Source:         https://github.com/abakh/nbsdgames/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ncurses-devel

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

install -m 0644 -D nbsdgames.desktop %{buildroot}%{_datadir}/applications/nbsdgames.desktop
install -D nbsdgames.svg %{buildroot}%{_datadir}/pixmaps/nbsdgames.svg
chmod -x %{buildroot}%{_datadir}/pixmaps/nbsdgames.svg

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_mandir}/man6/*.6%{?ext_man}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/nbsdgames.svg

%changelog
