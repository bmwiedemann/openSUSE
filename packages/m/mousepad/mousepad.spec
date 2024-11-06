#
# spec file for package mousepad
#
# Copyright (c) 2024 SUSE LLC
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


%define libname libmousepad0
Name:           mousepad
Version:        0.6.3
Release:        0
Summary:        Simple Text Editor for Xfce
License:        GPL-2.0-or-later
Group:          Productivity/Text/Editors
URL:            https://docs.xfce.org/apps/mousepad/start
Source:         https://archive.xfce.org/src/apps/mousepad/0.6/mousepad-%{version}.tar.bz2
BuildRequires:  appstream-glib
BuildRequires:  gettext >= 0.19.8
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.56.2
BuildRequires:  pkgconfig(gmodule-2.0)  >= 2.56.2
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtksourceview-4) >= 4.0.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.17.5
BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  pkgconfig(polkit-agent-1) >= 102

%description
Mousepad is a simple text editor for Xfce.

%package -n %{libname}
Summary:        Mousepad plugin provider
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n %{libname}
A plugin provider for the Mousepad text editor

%package devel
Summary:        Development files for Mousepad
Group:          Development/Libraries
Requires:       %{libname} >= %{version}

%Description devel
Development files for Mousepad plugin development

%lang_package

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

%find_lang %{name} %{?no_lang_C}

%suse_update_desktop_file org.xfce.%{name}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc AUTHORS NEWS ChangeLog README.md
%license COPYING
%{_bindir}/mousepad
%{_datadir}/applications/org.xfce.mousepad.desktop
%{_datadir}/applications/org.xfce.mousepad-settings.desktop
%{_datadir}/glib-2.0/schemas/org.xfce.mousepad.gschema.xml
%{_datadir}/glib-2.0/schemas/org.xfce.mousepad.plugins.gspell.gschema.xml
%{_datadir}/metainfo/org.xfce.%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/apps/org.xfce.mousepad.*
%{_datadir}/polkit-1/actions/org.xfce.mousepad.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_libdir}/%{name}/plugins/libmousepad-plugin-gspell.so
%{_libdir}/%{name}/plugins/libmousepad-plugin-shortcuts.so

%files -n %{libname}
%{_libdir}/libmousepad.so.*

%files devel
%{_libdir}/libmousepad.so

%files lang -f %{name}.lang

%changelog
