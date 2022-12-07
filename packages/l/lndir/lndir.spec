#
# spec file for package lndir
#
# Copyright (c) 2022 SUSE LLC
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


Name:           lndir
Version:        1.0.4
Release:        0
Summary:        Utility to create a shadow directory of symbolic links to another directory tree
License:        MIT
Group:          Development/Tools/Building
URL:            https://xorg.freedesktop.org/
Source0:        https://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
# This was part of the xorg-x11-util-devel package up to version 7.6
Conflicts:      xorg-x11-util-devel <= 7.6

%description
The lndir program makes a shadow copy of a directory tree, except that
the shadow is not populated with real files but instead with symbolic
links pointing at the real files in the original directory tree.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/lndir
%{_mandir}/man1/lndir.1%{?ext_man}

%changelog
