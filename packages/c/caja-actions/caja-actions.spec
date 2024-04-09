#
# spec file for package caja-actions
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


%define _version 1.28

Name:           caja-actions
Version:        1.28.0
Release:        0
Summary:        Launch through the Caja file manager popup menu of selected files
License:        GPL-2.0-or-later
URL:            https://mate-desktop.org/
Group:          Productivity/File utilities
Source0:        https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  filesystem
BuildRequires:  mate-common
BuildRequires:  hicolor-icon-theme
BuildRequires:  itstool
BuildRequires:  yelp-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(libcaja-extension) > %{_version}

%description
Caja-actions is an extension for Caja file manager which allows the user to add
arbitrary program to be launched through the Caja file manager popup menu of
selected files.

%package -n caja-extension-actions-menu
Summary:        A plugin which takes care of displaying actions in Caja context menus
Group:          Productivity/File utilities
Requires:       caja >= %{_version}

%description -n caja-extension-actions-menu
caja-extension-actions-menu is a plugin which takes care of displaying actions
in Caja context menus

%package -n caja-extension-actions-tracker
Summary:        A plugin which tracks the current Caja selection
Group:          Productivity/File utilities
Requires:       caja >= %{_version}

%description -n caja-extension-actions-tracker
caja-extension-actions-tracker is a plugin which tracks the current Caja
selection, and sends it in response to a DBus request.

%package doc
Summary:       Documents of caja-actions
Group:         Documentation/HTML
BuildArch:     noarch

%description doc
This package provides help documents for caja-actions

%package devel
Summary:       Development tools for caja-actions
Group:         Development/Libraries/Other
BuildArch:     noarch

%description devel
The caja-actions-devel package contains the header files caja-actions.

%lang_package

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm %{buildroot}%{_datadir}/doc/caja-actions/INSTALL

%find_lang %{name}
%fdupes %{buildroot}%{_datadir}

%files
%doc AUTHORS NEWS README
%license COPYING
%{_bindir}/%{name}-*
%{_datadir}/applications/cact.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_libexecdir}/%{name}
%{_libdir}/%{name}

%files -n caja-extension-actions-menu
%{_libdir}/caja/extensions-2.0/libcaja-actions-menu.so

%files -n caja-extension-actions-tracker
%{_libdir}/caja/extensions-2.0/libcaja-actions-tracker.so

%files doc
%{_datadir}/help/*/*
%{_datadir}/doc/%{name}

%files devel
%doc AUTHORS NEWS README
%license COPYING
%{_includedir}/%{name}

%files lang -f %{name}.lang

%changelog

