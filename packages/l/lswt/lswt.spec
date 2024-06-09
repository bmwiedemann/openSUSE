#
# spec file for package lswt
#
# Copyright (c) 2024 SUSE LLC
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


Name:           lswt
Version:        2.0.0
Release:        0
Summary:        Wayland toplevel lister
License:        GPL-3.0-only
Group:          System/X11/Utilities
URL:            https://git.sr.ht/~leon_plickat/lswt
Source:         %{name}-%{version}.tar.zst
Patch0:         Makefile.patch
BuildRequires:  scdoc >= 1.9.2
BuildRequires:  pkgconfig(wayland-client)

%description
A program to list Wayland toplevels.

Requires the Wayland server to implement the foreign-toplevel-management-unstable-v1
protocol extension.

%prep
%autosetup

%build
%make_build

%install
%make_install

%files
%license LICENSE
%doc README
%{_bindir}/lswt
%{_mandir}/man1/lswt.1.gz
%{_datadir}/bash-completion/completions/lswt

%changelog
