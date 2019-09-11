#
# spec file for package vala-panel-plugin-sntray
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


%define _rev    4c8a0c6b72a96e823f9dd1302a0280de
%define _name   xfce4-sntray-plugin
Name:           vala-panel-plugin-sntray
Version:        0.4.11
Release:        0
Summary:        StatusNotifierItem (appindicator) plugin for vala-panel
License:        LGPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://gitlab.com/vala-panel-project/xfce4-sntray-plugin
Source:         https://gitlab.com/vala-panel-project/xfce4-sntray-plugin/uploads/%{_rev}/%{_name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.6
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.36
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.14.0
BuildRequires:  pkgconfig(vala-panel) >= 0.4.50
Recommends:     %{name}-lang
%if 0%{?suse_version} >= 1500 || (0%{?sle_version} >= 120100 && 0%{?is_opensuse})
BuildRequires:  pkgconfig(libxfce4panel-2.0)
BuildRequires:  pkgconfig(libxfconf-0)
%endif

%description
StatusNotifierItem is the new D-Bus standard for system tray.

%package lang
Summary:        Languages for package vala-panel-plugin-sntray
Group:          System/Localization
Suggests:       %{name} = %{version}
Supplements:    packageand(bundle-lang-other:%{name})
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch
%if 0%{?suse_version} >= 1500 || (0%{?sle_version} >= 120100 && 0%{?is_opensuse})
Suggests:       xfce4-panel-plugin-sntray = %{version}
Supplements:    packageand(bundle-lang-other:xfce4-panel-plugin-sntray)
Provides:       xfce4-panel-plugin-sntray-lang = %{version}
Provides:       xfce4-panel-plugin-sntray-lang-all = %{version}
%endif

%description lang
Provides translations to the packages vala-panel-plugin-sntray and
xfce4-panel-plugin-sntray.

%if 0%{?suse_version} >= 1500 || (0%{?sle_version} >= 120100 && 0%{?is_opensuse})
%package -n xfce4-panel-plugin-sntray
Summary:        StatusNotifierItem (appindicator) plugin for xfce4-panel
Group:          System/GUI/XFCE
Requires:       xfce4-panel
Recommends:     xfce4-panel-plugin-sntray-lang

%description -n xfce4-panel-plugin-sntray
StatusNotifierItem is the new D-Bus standard for system tray.
%endif

%prep
%setup -q -n %{_name}-%{version}

%build
%cmake \
  -DCMAKE_SHARED_LINKER_FLAGS="" \
  -DGSETTINGS_COMPILE=OFF
make %{?_smp_mflags} V=1

%install
%cmake_install
%find_lang %{_name}
%fdupes %{buildroot}%{_datadir}/

%if 0%{?suse_version} < 1500
%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun
%endif

%files
%license LICENSE
%doc README.md
%dir %{_libdir}/vala-panel/
%dir %{_libdir}/vala-panel/applets/
%{_libdir}/vala-panel/applets/libsntray.so
%{_datadir}/vala-panel/applets/sntray.plugin
%{_datadir}/glib-2.0/schemas/org.valapanel.toplevel.sntray.gschema.xml

%files lang -f %{_name}.lang

%if 0%{?suse_version} >= 1500 || (0%{?sle_version} >= 120100 && 0%{?is_opensuse})
%files -n xfce4-panel-plugin-sntray
%license LICENSE
%doc README.md
%dir %{_libdir}/xfce4/
%dir %{_libdir}/xfce4/panel/
%dir %{_libdir}/xfce4/panel/plugins/
%{_libdir}/xfce4/panel/plugins/libsntray-xfce.so
%dir %{_datadir}/xfce4/
%dir %{_datadir}/xfce4/panel/
%dir %{_datadir}/xfce4/panel/plugins/
%{_datadir}/xfce4/panel/plugins/sntray.desktop
%endif

%changelog
