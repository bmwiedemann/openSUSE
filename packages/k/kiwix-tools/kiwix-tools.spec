#
# spec file for package kiwix-tools
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


Name:           kiwix-tools
Version:        3.8.2
Release:        0
Summary:        Command line Kiwix tools
License:        GPL-3.0-or-later
URL:            https://github.com/kiwix/kiwix-tools
Source:         https://mirror.download.kiwix.org/release/kiwix-tools/kiwix-tools-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig(docopt)
BuildRequires:  pkgconfig(libkiwix)
BuildRequires:  pkgconfig(libzim)

%description
The Kiwix tools is a collection of Kiwix related command line tools:
* kiwix-manage: Manage XML based library of ZIM files
* kiwix-search: Full text search in ZIM files
* kiwix-serve: HTTP daemon serving ZIM files

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc Changelog README.md
%{_bindir}/kiwix-manage
%{_bindir}/kiwix-search
%{_bindir}/kiwix-serve
%{_mandir}/man1/*
%{_mandir}/fr/man1/*

%changelog

