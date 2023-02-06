#
# spec file for package pax-utils
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


Name:           pax-utils
Version:        1.3.7
Release:        0
Summary:        Tools to Check ELF Files for Security Relevant Properties
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://wiki.gentoo.org/wiki/Hardened/PaX_Utilities
# Git-Clone:    https://gitweb.gentoo.org/proj/pax-utils.git
Source:         https://ftp.halifax.rwth-aachen.de/gentoo/distfiles/pax-utils-%{version}.tar.xz
# backports
# openSUSE patches
Patch20:        pax-utils-handle-lib64.patch
BuildRequires:  libcap-devel
BuildRequires:  meson
BuildRequires:  xmlto
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tools to check ELF files for security relevant properties such as
non-executable stack.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%defattr(-,root,root)
%license COPYING
%doc README.md TODO BUGS
%{_bindir}/*
%{_mandir}/man1/*

%changelog
