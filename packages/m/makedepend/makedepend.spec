#
# spec file for package makedepend
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


Name:           makedepend
Version:        1.0.8
Release:        0
Summary:        Utility to create dependencies in makefiles
License:        MIT
Group:          Development/Tools/Building
URL:            https://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xproto) >= 7.0.17
# This was part of the xorg-x11-util-devel package up to version 7.6
Conflicts:      xorg-x11-util-devel <= 7.6

%description
The makedepend program reads each sourcefile in sequence and parses it
like a C-preprocessor so that it can correctly tell which #include
directives would be used in a compilation.

These dependencies are then written to a makefile in such a way that
make will know which object files must be recompiled when a dependency
has changed.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/makedepend
%{_mandir}/man1/makedepend.1%{?ext_man}

%changelog
