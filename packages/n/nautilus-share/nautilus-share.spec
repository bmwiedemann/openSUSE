#
# spec file for package nautilus-share
#
# Copyright (c) 2021 SUSE LLC
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


%define         nautilusextdir %(pkg-config --variable=extensiondir libnautilus-extension)
Name:           nautilus-share
Version:        0.7.3
Release:        0
Summary:        Nautilus plugin for sharing directories over SMB
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Samba
URL:            https://git.gnome.org/nautilus-share
Source:         http://download.gnome.org/sources/nautilus-share/0.7/%{name}-%{version}.tar.bz2
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  nautilus-devel
Requires:       samba-client >= 3.0.23

%description
An application for the GNOME desktop integrated into Nautilus
which allows use of Nautilus shares without signing in as root.

Features:

* A new command in the Nautilus context menu
  (Menu key or right click).

* A dialog to share a directory, which allows choosing a
  name and decide on read-only/read-write status.

* Possibility to access the share settings from the Properties
  tab of a directory.

* Possibility to examine whether a share name already exists by
  typing it.

* Nautilus displays a palm icon to visually show which
  directories are shared.

%lang_package

%prep
%setup -q

%build
autoreconf -f -i
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%files
%license COPYING
%doc AUTHORS README
%{_datadir}/nautilus-share/
%{nautilusextdir}/*.so

%files lang -f %{name}.lang

%changelog
