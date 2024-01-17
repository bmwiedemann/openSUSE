#
# spec file for package peksystray
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           peksystray
Version:        0.4.0
Release:        0
Summary:        A system tray "notification area" dockapp
License:        GPL-2.0-only
Group:          System/GUI/Other
Url:            http://peksystray.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/peksystray/peksystray/%{version}/peksystray-%{version}.tar.bz2
Patch0:         peksystray-0.4.0-xcheck.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(x11)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A very simple and light implementation of a system tray for any window
manager supporting docking, conforming to the System Tray Freedesktop
standard.

Peksystray provides a window where icons will automatically add up
depending on the requests from the applications. Both the size of the
window and the size of the icons can be selected by the user. If the
window is full, it can automatically display another window in order
to display more icons.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -f -i
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%{_bindir}/peksystray

%changelog
