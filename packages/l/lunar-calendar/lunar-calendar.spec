#
# spec file for package lunar-calendar
#
# Copyright (c) 2020 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
%define   commit          f91a880e9dbf4ad28fbe9cda2cb899106c25ef97
#%define   shortcommit     %(c=%{commit}; echo ${c:0:7})
%define   shortcommit     f91a880
%define   sover           1

Summary:        Chinese Lunar calendar
Name:           lunar-calendar
Version:        3.0.0+git20191124.%{shortcommit}
Release:        0
License:        GPL-2.0+
Group:          System/I18n/Chinese
Url:            https://github.com/yetist/lunar-calendar
# Source0:        https://github.com/yetist/lunar-calendar/archive/v%{version}/%{name}-%{version}.tar.gz
Source0:        https://github.com/yetist/lunar-calendar/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        %{name}.sh
Source2:        %{name}.csh
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lunar-date-3.0)
Requires:       lib%{name}-3_0-%{sover} = %{version}-%{release}


%description
This is the traditional Chinese calendar application.

%package -n lib%{name}-3_0-%{sover}
Summary:        The lunar-calendar libraries
Group:          System/Libraries

%description -n lib%{name}-3_0-%{sover}
This package contains the libraries for lunar-calendar.

%package gtk3-module
Summary:        The lunar-calendar libraries -- GTK+ 3 Module
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}-%{release}
Provides:       locale(patterns-gnome-gnome:zh_CN;zh_SG;zh_TW;zh_HK)
Provides:       locale(patterns-mate-mate:zh_CN;zh_SG;zh_TW;zh_HK)
Provides:       locale(patterns-xfce-xfce:zh_CN;zh_SG;zh_TW;zh_HK)

%description gtk3-module
This package contains a GTK+ 3 module of lunar-calendar. Calendar applications 
base on GTK3 can display Chinese Lunar calendar by this module.

%package -n typelib-1_0-LunarCalendar-3_0
Summary:        Introspection bindings for lunar-calendar
Group:          System/Libraries
Requires:       %{name} = %{version}-%{release}

%description -n typelib-1_0-LunarCalendar-3_0
This package contains the introspection bindings for the lunar-calendar library.

%package doc
Summary:        Lunar calendar Documents
Group:          Documentation/Other
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
Documents for lunar-calendar

%package devel
Summary:        Development tools for ibus
Group:          Development/Libraries/C and C++
Requires:       lib%{name}-3_0-%{sover} = %{version}-%{release}

%description devel
The lunar-calendar-devel package contains the header files and developer
docs for lunar-calendar.

%{lang_package}

%prep
%setup -q -n %{name}-%{commit}

%build
%meson -Denable_gtk_modules=true \
       -Denable_gtk_doc=true \
       -Dwith_introspection=true \
       -Dwith_vala=true \
       -Denable_tests=true \
       %{nil}
%meson_build

%install
%meson_install
install -d %{buildroot}%{_sysconfdir}/profile.d/
install -m0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d/
install -m0755 %{SOURCE2} %{buildroot}%{_sysconfdir}/profile.d/

%fdupes %{buildroot}
%find_lang %{name}

%post -n lib%{name}-3_0-%{sover} -p /sbin/ldconfig

%postun -n lib%{name}-3_0-%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc NEWS README.md
%license COPYING

%files gtk3-module
%defattr(-,root,root,-)
%{_libdir}/gtk-3.0/modules/liblunar-calendar-module.so
%config %{_sysconfdir}/profile.d/%{name}.sh
%config %{_sysconfdir}/profile.d/%{name}.csh

%files lang -f %{name}.lang

%files -n lib%{name}-3_0-%{sover}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}*.so.*

%files -n typelib-1_0-LunarCalendar-3_0
%defattr(-,root,root,-)
%{_libdir}/girepository-1.0/*.typelib

%files doc
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/%{name}

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}-3.0
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib%{name}*.so
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*
%{_datadir}/gir-1.0/LunarCalendar-3.0.gir


%changelog
