#
# spec file for package qrustyquake
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


Name:           qrustyquake
Version:        1.0.0
Release:        0
Summary:        Quake using software rendering with modern maps and mods support
License:        GPL-3.0-or-later
URL:            https://github.com/cyanbun96/qrustyquake
Source:         https://github.com/cyanbun96/qrustyquake/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(sdl3-mixer)

%description

A modernized SDL3-based WinQuake port (software rendering only) aimed at faithfulness
to the original while being compatible with most modern maps and mods.

The Quake data files are required.
Either launch qrustyquake in a directory containing the id1 folder
containing game data, or start qrustyquake with the -basedir command-line option
with for argument the path of the directory containing the id1 directory.

%prep
%autosetup

%build
%make_build RELEASE_FLAGS="%{optflags}" -C src

%install
install -m755 -Dt %{buildroot}%{_bindir} src/qrustyquake

%files
%license LICENSE
%doc README.md
%{_bindir}/qrustyquake

%changelog
