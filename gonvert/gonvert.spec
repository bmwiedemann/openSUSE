#
# spec file for package gonvert
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           gonvert
Version:        0.2.38
Release:        0
License:        GPL-2.0+
Summary:        Conversion utility that allows conversion between many units
Url:            http://www.unihedron.com/projects/gonvert/index.php
Group:          Productivity/Scientific/Math
Source:         http://www.unihedron.com/projects/gonvert/downloads/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE gonvert-desktopfile.patch -- Fix Name, GenericName, Icon and Categories
Patch0:         gonvert.desktop.patch
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
Requires:       python-gtk
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
gonvert is a conversion utility that allows conversion between many
units, like CGS, Ancient, and Imperial, with many categories, such as
length, mass, and numbers. All converted values are shown at once as
you type. It is easy to add and change your own units.

%prep
%setup -q

# SED-FIX-OPENSUSE -- Fix paths
sed -i -e 's|/usr/local|/usr|;
           s|$(datadir)/doc|$(datadir)/doc/packages|
           s|$(datadir)/gnome/apps/Utilities|$(datadir)/applications|' Makefile

%patch0

# Remove not needed files
rm -f doc/INSTALL

%build
make

%install
%make_install

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%defattr(-,root,root,0755)
%{_bindir}/gonvert
%doc %{_datadir}/doc/packages/%{name}
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-icon_alternative.png
%{_datadir}/pixmaps/%{name}.png

%changelog
