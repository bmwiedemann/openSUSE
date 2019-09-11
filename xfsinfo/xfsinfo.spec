#
# spec file for package xfsinfo
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xfsinfo
Version:        1.0.6
Release:        0
Summary:        X font server information utility
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libfs)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
xfsinfo is a utility for displaying information about an X font
server. It is used to examine the capabilities of a server, the
predefined values for various parameters used in communicating between
clients and the server, and the font catalogues and alternate servers
that are available.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README.md
%{_bindir}/xfsinfo
%{_mandir}/man1/xfsinfo.1%{?ext_man}

%changelog
