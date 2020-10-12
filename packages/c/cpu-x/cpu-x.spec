#
# spec file for package cpu-x
#
# Copyright (c) 2020 SUSE LLC
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


Name:           cpu-x
Version:        4.0.1
Release:        0
Summary:        Hardware overview utility
License:        GPL-3.0-or-later
Group:          System/X11/Utilities
URL:            https://github.com/X0rg/CPU-X/
Source:         https://github.com/X0rg/CPU-X/archive/v%version.tar.gz
Patch1:         no-no-pie.patch
BuildRequires:  cmake
BuildRequires:  gettext-tools
BuildRequires:  nasm
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(libcpuid) >= 0.4.0
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libprocps)
BuildRequires:  pkgconfig(ncursesw)
ExclusiveArch:  %ix86 x86_64
Provides:       bundled(dmidecode) = 3.2.20200417

%description
CPU-X is a software that gathers information about CPU, motherboard
and peripherals. It is similar to CPU-Z (Windows) and can be used in
graphical mode by using GTK or in text-based mode by using NCurses. A
dump mode is present from command line.

%prep
%autosetup -p1 -n CPU-X-%version

%build
%cmake
%cmake_build

%install
%cmake_install
rm -Rf "%buildroot/%_datadir/polkit-1" "%buildroot/%_datadir/applications"
%find_lang %name

%files -f %name.lang
%_bindir/cpu-x
%_libexecdir/cpu-x*
%_datadir/bash-completion/
%_datadir/cpu-x/
%_datadir/fish/
%_datadir/icons/*
%_datadir/glib-2.0/
%_datadir/metainfo/
%_datadir/zsh/
%license COPYING

%changelog
