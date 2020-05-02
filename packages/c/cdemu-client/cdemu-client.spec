#
# spec file for package cdemu-client
#
# Copyright (c) 2020 SUSE LLC
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


Name:           cdemu-client
Version:        3.2.4
Release:        0
Summary:        Command-line client to control cdemu-daemon
License:        GPL-2.0-or-later
Group:          System/Filesystems
URL:            https://cdemu.sf.net/about/client/

#Git-Clone:	git://git.code.sf.net/p/cdemu/code
Source:         https://downloads.sf.net/cdemu/%name-%version.tar.bz2
BuildRequires:  cmake >= 2.8.5
BuildRequires:  gettext-tools >= 0.15
BuildRequires:  gobject-introspection
BuildRequires:  intltool >= 0.21
BuildRequires:  python3 >= 3.4
BuildRequires:  pkgconfig(bash-completion)
Requires:       python3 >= 3.4
Requires:       python3-dbus-python
Requires:       python3-gobject
BuildArch:      noarch

%description
cdemu-client is a command-line client for controlling cdemu-daemon.

It provides a way to perform the key tasks related to controlling the
CDEmu daemon, such as loading and unloading devices, displaying
devices' status and retrieving/setting their debug masks.

%lang_package

%prep
%setup -q
sed -i "s|/usr/bin/env python3|%{_bindir}/python3|" src/cdemu

%build
cmake . \
	-DCMAKE_INSTALL_PREFIX:PATH="%_prefix" \
	-DCMAKE_INSTALL_LIBDIR:PATH="%_libdir"
make %{?_smp_mflags}

%install
%make_install
%find_lang cdemu

%files
%doc AUTHORS COPYING README
%_bindir/cdemu
%_datadir/applications/%name.desktop
%_datadir/pixmaps/%name.svg
%_datadir/bash-completion/
%_mandir/man1/cdemu.1*

%files lang -f cdemu.lang

%changelog
