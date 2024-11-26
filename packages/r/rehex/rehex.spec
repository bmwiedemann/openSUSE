#
# spec file for package rehex
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           rehex
Version:        0.62.1
Release:        0
Summary:        Reverse Engineers' Hex Editor
License:        GPL-2.0-only
URL:            https://github.com/solemnwarning/rehex
Source0:        https://github.com/solemnwarning/rehex/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         rehex-0.62.1-Build-with-Botan-3.patch
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libunistring-devel
BuildRequires:  lua-busted
BuildRequires:  perl-Template-GD
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  zip
BuildRequires:  pkgconfig(capstone)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(lua)
%if 0%{?suse_version} > 1600
BuildRequires:  pkgconfig(botan-3)
%else
BuildRequires:  pkgconfig(botan-2)
%endif
BuildRequires:  wxWidgets-devel

%description
A hex heditor with a number of features for analysing and annotating
binary file formats.

Current features include:

    Large file support (tested up to 1 TiB)
    Decoding of integer/floating point value types
    Disassembly of machine code
    Highlighting and annotation of ranges of bytes

%prep
%autosetup -p1
dos2unix README.md

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"
%make_build prefix=%{_prefix} libdir=%{_libdir}

%install
%make_install prefix=%{_prefix} libdir=%{_libdir}
%suse_update_desktop_file -r %{name} "Development;Debugger;"

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/rehex
%{_datadir}/rehex/rehex.htb

%changelog
