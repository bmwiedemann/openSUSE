#
# spec file for package xorg-scripts
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xorg-scripts
%define _name   scripts
Version:        1.0.1
Release:        0
Summary:        Miscellaneous scripts for X
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{_name}-%{version}.tar.bz2
Patch0:         u_Add-ssh-support-to-xon.patch
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(x11)
# This was part of the xorg-x11 package up to version 7.6
Conflicts:      xorg-x11 <= 7.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains miscellaneous scripts for X, like xon, a script
to start an X program on a remote machine.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install
# fdo35866
rm %{buildroot}%{_bindir}/{fontname.sh,fontprop.sh,xauth_switch_to_sun-des-1}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/xon
%{_mandir}/man1/xon.1x%{?ext_man}

%changelog
