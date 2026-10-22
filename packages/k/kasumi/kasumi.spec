#
# spec file for package kasumi
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


Name:           kasumi
Version:        2.7
Release:        0
Summary:        Dictionary Tool for Anthy
License:        GPL-2.0-or-later
URL:            https://github.com/fujiwarat/kasumi-unicode
Source0:        https://github.com/fujiwarat/kasumi-unicode/releases/download/%{version}/kasumi-unicode-%{version}.tar.xz
Patch1:         kasumi-gcc14-fix.patch
Patch2:         kasumi-c++14.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(anthy)
BuildRequires:  pkgconfig(gtk+-3.0)
Provides:       locale(anthy:ja)

%description
A graphical tool to edit the personal dictionary for Anthy.

%prep
%autosetup -p1 -n kasumi-unicode-%{version}

%build
libtoolize --force
autoreconf --force --install
%configure
%make_build

%install
%make_install
%suse_update_desktop_file -i %{name} System SystemSetup
%find_lang kasumi-unicode

%files -f kasumi-unicode.lang
%license COPYING
%doc AUTHORS ChangeLog INSTALL NEWS README
%{_bindir}/*
%{_datadir}/pixmaps/kasumi.png
%{_datadir}/applications/kasumi.desktop
%{_mandir}/man1/*

%changelog
