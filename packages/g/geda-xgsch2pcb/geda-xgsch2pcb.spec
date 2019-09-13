#
# spec file for package geda-xgsch2pcb
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           geda-xgsch2pcb
Version:        0.1.3
Release:        0
Summary:        Graphical Frontend for gsch2pcb
License:        GPL-2.0
Group:          Productivity/Scientific/Electronics
Url:            http://www.geda.seul.org/tools/xgsch2pcb/index.html
Source0:        http://geda.seul.org/dist/%{name}-%{version}.tar.gz
BuildRequires:  dbus-1-devel
BuildRequires:  dbus-1-python
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  python-gobject2-devel
BuildRequires:  python-gtk
BuildRequires:  update-desktop-files
Requires:       geda-utils
Requires:       pcb
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
xgsch2pcb provides an intuitive, user-friendly graphical interface to
gsch2pcb.
gsch2pcb is a command-line tool, part of the gEDA suite, which is used
to generate and update a PCB layout. It works with schematics created
by gschem, part of the gEDA suite, and layouts created by pcb, a
PCB layout system commonly used with gEDA.

%prep
%setup -q
# pass desktop file validation
sed -i 's/x-geda-gsch2pcb-project/x-geda-gsch2pcb-project;/' data/geda-xgsch2pcb.desktop.in

%build
%configure --disable-update-desktop-database
make

%install
%make_install
%suse_update_desktop_file -r %{name} Education Engineering

%find_lang %{name}
%fdupes -s %{buildroot}%{_libdir}/%{name}/

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/*
%{_datadir}/icons/*
%{_datadir}/applications/%{name}.desktop

%changelog
