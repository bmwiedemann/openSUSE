#
# spec file for package d-feet
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


Name:           d-feet
Version:        0.3.14
Release:        0
Summary:        Graphical D-Bus Debugger
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            http://live.gnome.org/DFeet/
Source0:        http://download.gnome.org/sources/d-feet/0.3/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool >= 0.40.0
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.4
Recommends:     %{name}-lang
BuildArch:      noarch

%description
D-Feet is a graphical D-Bus debugger.  D-Bus is an RPC library used on
the Desktop.  D-Feet can be used to inspect D-Bus objects of running
programs and invoke methods on those objects.

%lang_package

%prep
%autosetup

%build
export PYTHON=%{_bindir}/python3
%configure \
	--libdir=/unused-in-noarch \
	--disable-tests \
	%{nil}

%install
%make_install

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%files
%license COPYING
%doc AUTHORS README
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{python3_sitelib}/dfeet/
%{_datadir}/%{name}/
%{_datadir}/applications/org.gnome.dfeet.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.dfeet.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/icons/HighContrast/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.dfeet.appdata.xml

%files lang -f %{name}.lang

%changelog
