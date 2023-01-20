#
# spec file for package fish
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


Name:           fish
Version:        3.6.0
Release:        0
Summary:        The "friendly interactive shell"
License:        GPL-2.0-only
Group:          System/Shells
URL:            https://fishshell.com/
Source:         https://github.com/fish-shell/fish-shell/releases/download/%{version}/fish-%{version}.tar.xz
Source1:        https://github.com/fish-shell/fish-shell/releases/download/%{version}/fish-%{version}.tar.xz.asc
Source100:      fish.keyring
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  groff
BuildRequires:  ncurses-devel
BuildRequires:  pcre2-devel >= 10.21
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
Requires:       bc
Requires:       man
Recommends:     terminfo

%description
fish is a command line shell.
It is geared towards interactive use and its features are focused on user
friendlieness and discoverability. The language syntax is simple but
incompatible with other shell languages.

%package devel
Summary:        Devel files for the fish shell
Group:          Development/Libraries/C and C++

%description devel
This package contains development files for the fish shell.

%prep
%autosetup -p1

# fix E: env-script-interpreter
find share/tools -type f -name *.py -exec sed -i -r '1s|^#!%{_bindir}/env |#!%{_bindir}/|' {} +

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}

%install
%cmake_install

%find_lang %{name}

rm %{buildroot}/%{_datadir}/doc/fish/.buildinfo

%suse_update_desktop_file -G "Command-line interpreter" fish TerminalEmulator

%post
# Add fish to the list of allowed shells in /etc/shells
if ! grep -q '^%{_bindir}/%{name}$' %{_sysconfdir}/shells; then
	echo %{_bindir}/%{name} >>%{_sysconfdir}/shells
fi

%postun
# Remove fish from the list of allowed shells in /etc/shells
if [ "$1" = 0 ]; then
	grep -v '^%{_bindir}/%{name}$' %{_sysconfdir}/shells >%{_sysconfdir}/%{name}.tmp
	mv %{_sysconfdir}/%{name}.tmp %{_sysconfdir}/shells
fi

%files -f %{name}.lang
%dir %{_sysconfdir}/fish
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_bindir}/fish
%{_bindir}/fish_indent
%{_bindir}/fish_key_reader
%{_datadir}/doc/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*.1%{?ext_man}
%{_datadir}/applications/fish.desktop
%{_datadir}/pixmaps/fish.png

%files devel
%{_datadir}/pkgconfig/fish.pc

%changelog
