#
# spec file for package lndir
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           lndir
Version:        1.0.3
Release:        0
License:        MIT
Summary:        Utility to create a shadow directory of symbolic links to another directory tree
Url:            http://xorg.freedesktop.org/
Group:          Development/Tools/Building
Source0:        http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
# This was part of the xorg-x11-util-devel package up to version 7.6
Conflicts:      xorg-x11-util-devel <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The lndir program makes a shadow copy of a directory tree, except that
the shadow is not populated with real files but instead with symbolic
links pointing at the real files in the original directory tree.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/lndir
%{_mandir}/man1/lndir.1%{?ext_man}

%changelog
