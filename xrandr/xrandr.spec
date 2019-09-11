#
# spec file for package xrandr
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xrandr
Version:        1.5.0
Release:        0
Summary:        Primitive command line interface to RandR extension
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
# PATCH-FEATURE-UPSTREAM xrandr-print-outputs-per-provider.patch federico@suse.com - Make the --listproviders option also print which outputs are supported by each provider
Patch1:         xrandr-print-outputs-per-provider.patch
Patch2:         U_xrandr_suppress-misleading-indentation-warning.patch
Patch3:         U_xrandr_add-filter-flag.patch
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xrandr) >= 1.3
BuildRequires:  pkgconfig(xrender)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Currently required in order to make use of RANDR 1.4 enhancements
# which have been implemented by the following drivers: intel,
# radeon, nouveau, modesetting and nvidia
Supplements:    xorg-x11-server

%description
Xrandr is used to set the size, orientation and/or reflection of
the outputs for a screen. It can also set the screen size.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
# do not ship xkeystone, see fdo#35984
rm %{buildroot}%{_bindir}/xkeystone

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/xrandr
%{_mandir}/man1/xrandr.1%{?ext_man}

%changelog
