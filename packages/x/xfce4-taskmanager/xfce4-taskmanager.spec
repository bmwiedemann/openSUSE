#
# spec file for package xfce4-taskmanager
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


Name:           xfce4-taskmanager
Version:        1.2.2
Release:        0
Summary:        Simple Taskmanager for the Xfce Desktop Environment
License:        GPL-2.0-or-later
Group:          System/Monitoring
Url:            http://goodies.xfce.org/projects/applications/xfce4-taskmanager
Source:         http://archive.xfce.org/src/apps/xfce4-taskmanager/1.2/%{name}-%{version}.tar.bz2
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.2.0
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.2
BuildRequires:  pkgconfig(xmu) >= 1.1.2
# uses exo-open
Requires:       exo-tools
Recommends:     %{name}-lang = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
xfce4-taskmanager is a simple taskmanager for the Xfce desktop environment. It
can display window and icon names in a tree view, columns can be reordered, and
CPU and memory usage are displayed as a graph.

%lang_package

%prep
%setup -q

%build
%configure \
	--enable-gtk3
make %{?_smp_mflags} V=1

%install
%make_install

%suse_update_desktop_file -r %{name} GTK System Monitor

%find_lang %{name} %{?no_lang_C}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc AUTHORS NEWS README THANKS
%license COPYING
%{_bindir}/xfce4-taskmanager
%{_datadir}/applications/xfce4-taskmanager.desktop
%{_datadir}/icons/hicolor/*/*/xc_crosshair.png
%{_datadir}/icons/hicolor/*/*/xc_crosshair.svg

%files lang -f %{name}.lang

%changelog
