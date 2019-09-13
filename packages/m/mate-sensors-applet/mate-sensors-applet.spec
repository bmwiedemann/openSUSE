#
# spec file for package mate-sensors-applet
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


%define soname  libmate-sensors-applet-plugin
%define sover   0
%define _version 1.23
Name:           mate-sensors-applet
Version:        1.23.0
Release:        0
Summary:        MATE Desktop panel applet to display sensor readings
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  itstool
BuildRequires:  libsensors4-devel
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libatasmart)
BuildRequires:  pkgconfig(libmatepanelapplet-4.0) >= %{_version}
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(xext)

%description
MATE Sensors Applet is an applet for the MATE Panel to display
readings from hardware sensors, including CPU temperature, fan
speeds and voltage readings under Linux.

%package -n mate-applet-sensors
Summary:        MATE Desktop panel applet to display sensor readings
Group:          System/GUI/Other
Requires:       mate-panel >= %{_version}
Recommends:     libXNVCtrl
Recommends:     mate-applet-sensors-lang
# mate-sensors-applet was last used in openSUSE Leap 42.1.
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
Obsoletes:      %{name}-lang < %{version}

%description -n mate-applet-sensors
MATE Sensors Applet is an applet for the MATE Panel to display
readings from hardware sensors, including CPU temperature, fan
speeds and voltage readings under Linux.

%lang_package -n mate-applet-sensors

%package -n mate-applet-sensors-devel
Summary:        Development files for mate-sensors-applet
Group:          Development/Libraries/Other
Requires:       %{soname}%{sover} = %{version}
# mate-sensors-applet-devel was last used in openSUSE Leap 42.1.
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}

%description -n mate-applet-sensors-devel
MATE Sensors Applet is an applet for the MATE Panel to display
readings from hardware sensors, including CPU temperature, fan
speeds and voltage readings under Linux.

%package -n %{soname}%{sover}
Summary:        MATE Desktop sensors applet shared libraries
Group:          Development/Libraries/C and C++

%description -n %{soname}%{sover}
MATE Sensors Applet is an applet for the MATE Panel to display
readings from hardware sensors, including CPU temperature, fan
speeds and voltage readings under Linux.

%prep
%autosetup -p1

%build
export LDFLAGS='-ldl'
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static                    \
  --libexecdir=%{_libexecdir}/%{name}
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}/%{_datadir}/help

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%if 0%{?suse_version} < 1500
%post -n mate-applet-sensors
%icon_theme_cache_post

%postun -n mate-applet-sensors
%icon_theme_cache_postun
%endif

%files -n mate-applet-sensors
%license COPYING
%doc NEWS README
%{_libexecdir}/%{name}/
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%dir %{_datadir}/mate-panel/
%dir %{_datadir}/mate-panel/applets/
%{_datadir}/mate-panel/applets/org.mate.applets.SensorsApplet.mate-panel-applet
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/help/C/mate-sensors-applet
%{_datadir}/icons/hicolor/*/*/%{name}*.png
%{_datadir}/pixmaps/%{name}/

%files -n mate-applet-sensors-lang -f %{name}.lang

%files -n %{soname}%{sover}
%{_libdir}/%{soname}.so.%{sover}*

%files -n mate-applet-sensors-devel
%{_includedir}/%{name}/
%{_libdir}/%{soname}.so

%changelog
