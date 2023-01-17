#
# spec file for package st
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2013 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           st
Version:        0.9
Release:        0
Summary:        Simple Terminal Implementation for X
License:        MIT
Group:          System/X11/Terminals
URL:            https://%{name}.suckless.org/
Source:         https://dl.suckless.org/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Patch1:         compose-buffer-overflow.patch
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-devel
Requires:       terminfo

%description
Simple and lightweight and unbloated X11 terminal.

%prep
%autosetup -p1
# terminfo entries are provided by terminfo from ncurses
sed -e "/tic .*st.info/d" -i Makefile

%build
%if 0%{?suse_version} > 1500
%{set_build_flags}
export CPPFLAGS="${CXXFLAGS}"
%else
export CPPFLAGS="%{optflags}"
export CLAGS="%{optflags}"
export LDFLAGS="${RPM_LD_FLAGS}"
%endif

%{?make_build}%{?!make_build:make -j %{?_smp_mflags}} \
    X11INC="%{_includedir}" \
    X11LIB="%{_libdir}" \
    CC="gcc"

%install
%make_install PREFIX="%{_prefix}"

install -D -m0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"
%suse_update_desktop_file -r "%{name}" System TerminalEmulator

%files
%license LICENSE
%doc FAQ README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
