#
# spec file for package libmateweather
#
# Copyright (c) 2020 SUSE LLC
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


%define sover   1
%define _version 1.24
Name:           libmateweather
Version:        1.24.1
Release:        0
Summary:        MATE Weather
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  timezone >= 2016g
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
%glib2_gsettings_schema_requires

%description
libmateweather is a library to access weather information from
online services for numerous locations.

%lang_package

%package -n mateweather-common
Summary:        MATE Weather common files
BuildArch:      noarch

%description -n mateweather-common
libmateweather is a library to access weather information from
online services for numerous locations.

%package devel
Summary:        MATE Weather development files
Requires:       %{name}%{sover} = %{version}
Requires:       mateweather-common = %{version}

%description devel
libmateweather is a library to access weather information from
online services for numerous locations.

%package -n %{name}%{sover}
Summary:        MATE Weather shared libraries
Requires:       mateweather-common
Recommends:     %{name}-lang
Provides:       %{name} = %{version}
Obsoletes:      python-mateweather < %{version}

%description -n %{name}%{sover}
libmateweather is a library to access weather information from
online services for numerous locations.

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --enable-locations-compression \
  --disable-static
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{name}%{sover} -p /sbin/ldconfig

%postun -n %{name}%{sover} -p /sbin/ldconfig

%files lang -f %{name}.lang

%files -n %{name}%{sover}
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/*.so.%{sover}*

%files -n mateweather-common
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/mate/
%{_datadir}/%{name}/

%files devel
%license COPYING
%doc AUTHORS NEWS README
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/mateweather.pc
%{_datadir}/gtk-doc/html/%{name}/

%changelog
