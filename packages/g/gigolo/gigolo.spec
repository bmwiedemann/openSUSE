#
# spec file for package gigolo
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           gigolo
Version:        0.5.0
Release:        0
Summary:        Frontend to Manage Connections to Remote Filesystems
License:        GPL-2.0-or-later
Group:          System/Filesystems
Url:            https://git.xfce.org/apps/gigolo/
Source0:        https://archive.xfce.org/src/apps/gigolo/0.5/%{name}-%{version}.tar.bz2
Source1:        %{name}.png
BuildRequires:  ed
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gio-2.0) >= 2.16.0
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14
# uses xdg-open
Requires:       xdg-utils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Recommends:     %{name}-lang = %{version}

%description
Gigolo is a frontend to manage connections to remote filesystems using
GIO/GVFS. It allows connecting/mounting remote filesystems and manage

%lang_package

%prep
%setup -q
ed -s gigolo.desktop.in <<'EOF'
,s/^Icon=gtk-network/Icon=folder-remote/
w
EOF

%build
%configure
%make_build

%install
%make_install

# remove documentation/license files included below
rm -rf %{buildroot}%{_datadir}/doc

%suse_update_desktop_file -i %{name} System GTK Filesystem

%find_lang %{name}

%files
%license COPYING
%doc AUTHORS NEWS README THANKS TODO
%doc %{_mandir}/man1/gigolo.1*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%files lang -f %{name}.lang

%changelog
