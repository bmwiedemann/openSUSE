#
# spec file for package malcontent
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


Name:           malcontent
Version:        0.12.0
Release:        0
Summary:        Parental control system
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://gitlab.freedesktop.org/pwithnall/malcontent
Source:         https://tecnocode.co.uk/downloads/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  itstool
BuildRequires:  meson >= 0.50.0
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(accountsservice) >= 0.6.39
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(glib-2.0) >= 2.54.2
BuildRequires:  pkgconfig(glib-testing-0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(polkit-gobject-1)

%description
Libmalcontent implements parental controls support which can be
used by applications to filter or limit the access of child
accounts to inappropriate content.

%lang_package

%package -n libmalcontent-0-0
Summary:        Malcontent system library
Requires:       malcontent >= %{version}

%description -n libmalcontent-0-0
Libmalcontent implements parental controls support which can be
used by applications to filter or limit the access of child
accounts to inappropriate content.

%package -n typelib-1_0-Malcontent-0
Summary:        Introspection bindings for the malcontent system library

%description -n typelib-1_0-Malcontent-0
Libmalcontent implements parental controls support which can be
used by applications to filter or limit the access of child
accounts to inappropriate content.

%package -n libmalcontent-ui-1-1
Summary:        Malcontent UI library

%description -n libmalcontent-ui-1-1
Libmalcontent implements parental controls support which can be
used by applications to filter or limit the access of child
accounts to inappropriate content.

%package -n typelib-1_0-MalcontentUi-1
Summary:        Introspection bindings for the malcontent UI library

%description -n typelib-1_0-MalcontentUi-1
Libmalcontent implements parental controls support which can be
used by applications to filter or limit the access of child
accounts to inappropriate content.

%package devel
Summary:        Devel package
Requires:       libmalcontent-0-0 = %{version}
Requires:       libmalcontent-ui-1-1 = %{version}
Requires:       typelib-1_0-Malcontent-0 = %{version}
Requires:       typelib-1_0-MalcontentUi-1 = %{version}

%description devel
Libmalcontent implements parental controls support which can be
used by applications to filter or limit the access of child
accounts to inappropriate content.

%package control
Summary:        Parental Control Application
Requires:       malcontent >= %{version}

%description control
Parental Control management application for Malcontent

%prep
%autosetup -p1
sed -i 's|env python3|python3|' malcontent-client/malcontent-client.py

%build
%meson \
	-Dpamlibdir=%{_pam_moduledir}
	%{nil}
%meson_build

%install
%meson_install
# com.endlessm.ParentalControls.rules would allow 'wheel' group users access without polkit auth
# wheel is not used in openSUSE, so we simply package this file as an example %%doc file
mv %{buildroot}%{_datadir}/polkit-1/rules.d/com.endlessm.ParentalControls.rules .
%find_lang %{name}
%python3_fix_shebang

%ldconfig_scriptlets -n libmalcontent-0-0
%ldconfig_scriptlets  -n libmalcontent-ui-1-1

%files
%license COPYING
%doc NEWS README.md
%doc com.endlessm.ParentalControls.rules
%{_pam_moduledir}/pam_malcontent.so
%{_bindir}/malcontent-client
%{_mandir}/man8/malcontent-client.8%{?ext_man}
%{_datadir}/dbus-1/interfaces/com.endlessm.ParentalControls.*
%dir %{_datadir}/accountsservice
%dir %{_datadir}/accountsservice/interfaces
%{_datadir}/accountsservice/interfaces/com.endlessm.ParentalControl*
%{_datadir}/polkit-1/actions/com.endlessm.ParentalControls.policy
%{_datadir}/polkit-1/actions/org.freedesktop.MalcontentControl.policy

%files lang -f %{name}.lang

%files -n libmalcontent-0-0
%{_libdir}/libmalcontent-0.so.*

%files -n typelib-1_0-Malcontent-0
%{_libdir}/girepository-1.0/Malcontent-0.typelib

%files -n libmalcontent-ui-1-1
%{_libdir}/libmalcontent-ui-1.so.*

%files -n typelib-1_0-MalcontentUi-1
%{_libdir}/girepository-1.0/MalcontentUi-1.typelib

%files devel
%{_includedir}/%{name}-0/
%{_includedir}/%{name}-ui-1/
%{_libdir}/libmalcontent-0.so
%{_libdir}/libmalcontent-ui-1.so
%{_libdir}/pkgconfig/malcontent-0.pc
%{_libdir}/pkgconfig/malcontent-ui-1.pc
%{_datadir}/gir-1.0/Malcontent-0.gir
%{_datadir}/gir-1.0/MalcontentUi-1.gir

%files control
%{_bindir}/malcontent-control
%{_datadir}/metainfo/org.freedesktop.MalcontentControl.appdata.xml
%{_datadir}/icons/hicolor/*/apps/org.freedesktop.MalcontentControl*
%{_datadir}/applications/org.freedesktop.MalcontentControl.desktop

%changelog
