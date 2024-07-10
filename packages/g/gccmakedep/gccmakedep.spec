#
# spec file for package gccmakedep
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


Name:           gccmakedep
Version:        1.0.4
Release:        0
Summary:        Utility to list the resource database of an X application
License:        MIT
Group:          Development/Tools/Building
URL:            https://xorg.freedesktop.org/
Source0:        https://www.x.org/releases/individual/util/%{name}-%{version}.tar.xz
# This was part of the xorg-x11-util-devel package up to version 7.6
Conflicts:      xorg-x11-util-devel <= 7.6
BuildArch:      noarch

%description
The gccmakedep program calls 'gcc -M' to output makefile rules
describing the dependencies of each sourcefile, so that make knows
which object files must be recompiled when a dependency has changed.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc ChangeLog
%{_bindir}/gccmakedep
%{_mandir}/man1/gccmakedep.1%{?ext_man}

%changelog
