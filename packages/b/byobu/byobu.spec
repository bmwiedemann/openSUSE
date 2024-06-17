#
# spec file for package byobu
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Tejas Guruswamy <tejas.guruswamy@opensuse.org>.
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


Name:           byobu
Version:        6.12
Release:        0
Summary:        Enhanced profile and configuration utilities for GNU Screen and tmux
License:        GPL-3.0-only
Group:          System/Console
URL:            https://byobu.org/
Source:         https://github.com/dustinkirkland/byobu/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
# For /usr/share/dbus-1/services/ ownership.
BuildRequires:  dbus-1-devel
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
# For env in desktop-file
Requires:       coreutils
Requires:       gawk
Requires:       gettext-runtime
Requires:       net-tools
Requires:       python3-newt
Requires:       snack
Recommends:     pastebinit
Recommends:     sensible-utils
Recommends:     tmux
Suggests:       %{name}-doc
Suggests:       screen
Suggests:       wireless-tools
BuildArch:      noarch
%{perl_requires}

%package doc
Summary:        Documentation files for byobu
Group:          Documentation/Other
Requires:       %{name}

%description
Byobu includes an enhanced profiles, convenient keybindings,
configuration utilities, and toggle-able system status
notifications for both the GNU Screen window manager and tmux
terminal multiplexer.

%description doc
Help files and changelog for %{name}.

%prep
%setup -q

%build
cp debian/changelog ChangeLog
autoreconf -i
%configure
%make_build

%install
%make_install

mkdir -p %{buildroot}%{_docdir}/
mv -f %{buildroot}%{_datadir}/doc/%{name}/ %{buildroot}%{_docdir}/%{name}/

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
ln -s ../../../../%{name}/pixmaps/%{name}.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

mkdir -p %{buildroot}%{_datadir}/applications/
rm %{buildroot}%{_datadir}/%{name}/desktop/byobu.desktop
mv %{buildroot}%{_datadir}/%{name}/desktop/byobu.desktop.old %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file -G "Screen Profiles" -r %{name} System TerminalEmulator
%fdupes %{buildroot}%{_mandir}/

sed -i 's,%{_bindir}/env python3,%{_bindir}/python3,' %{buildroot}%{_prefix}/lib/byobu/include/*.py

%files
%license COPYING
%doc README.md
%config %{_sysconfdir}/profile.d/Z97-%{name}.*sh
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_bindir}/*
%{_prefix}/lib/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*.1%{?ext_man}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/dbus-1/services/*%{name}.service

%files doc
%doc ChangeLog
%{_docdir}/%{name}/help.*.txt

%changelog
