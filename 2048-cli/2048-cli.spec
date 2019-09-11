#
# spec file for package 2048-cli
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


Name:           2048-cli
Version:        0.9.1+git.20181118
Release:        0
Summary:        A CLI version of the "2048" game
License:        MIT
Group:          Amusements/Games/Strategy/Other
URL:            https://github.com/tiehuis/2048-cli
#Git-Clone:     https://github.com/tiehuis/2048-cli.git
Source:         %{name}-%{version}.tar.xz
Patch0:         2048-cli-use-proper-gettext-header.patch
Patch1:         2048-cli-link-against-correct-curses-lib.patch
BuildRequires:  ncurses-devel

%description
2048 is a mathematics-based puzzle game where the player has to slide
tiles on a grid to combine them and create a tile with the number 2048.
The player has to merge the similar number tiles (2n) by moving the arrow
keys in four different directions. When two tiles with the same number
touch, they will merge into one.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{optflags} $(pkg-config --cflags ncurses)"
make curses %{?_smp_mflags}

%install
install -Dpm 0755 2048 %{buildroot}%{_bindir}/2048-cli
install -Dpm 0644 man/2048.6 %{buildroot}%{_mandir}/man6/2048-cli.6

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{?ext_man}

%changelog
