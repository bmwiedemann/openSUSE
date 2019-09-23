#
# spec file for package nautilus-share
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


%define         nautilusextdir %(pkg-config --variable=extensiondir libnautilus-extension)

Name:           nautilus-share
Version:        0.7.3
Release:        0
Summary:        Nautilus plugin for sharing directories over SMB
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Samba
Url:            http://git.gnome.org/nautilus-share
Source:         http://download.gnome.org/sources/nautilus-share/0.7/%{name}-%{version}.tar.bz2
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  nautilus-devel
BuildRequires:  translation-update-upstream
Requires:       samba >= 3.0.23
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
translation-update-upstream

%build
autoreconf -f -i
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, root)
%doc AUTHORS COPYING README
%{_datadir}/nautilus-share/
%{nautilusextdir}/*.so

%files lang -f %{name}.lang

%changelog
