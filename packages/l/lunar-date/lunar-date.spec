#
# spec file for package lunar-date
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define _libver 3_0
%define _libpkg lib%{name}-%{_libver}-1
Name:           lunar-date
Version:        3.2.0
Release:        0
Summary:        Chinese Lunar calendar library
License:        LGPL-2.1-or-later
URL:            https://github.com/yetist/lunar-date
Source:         https://github.com/yetist/lunar-date/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gi-docgen
BuildRequires:  meson >= 1.0.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(vapigen)

%package -n %{_libpkg}
Summary:        Chinese Lunar calendar library
Recommends:     %{name}-lang
Provides:       locale(patterns-gnome-gnome:zh_CN;zh_SG;zh_TW;zh_HK)
Provides:       locale(patterns-mate-mate:zh_CN;zh_SG;zh_TW;zh_HK)
Provides:       locale(patterns-xfce-xfce:zh_CN;zh_SG;zh_TW;zh_HK)

%package -n typelib-1_0-LunarDate-%{_libver}
Summary:        Chinese Lunar calendar introspection bindings
Provides:       locale(patterns-gnome-gnome:zh_CN;zh_SG;zh_TW;zh_HK)
Provides:       locale(patterns-mate-mate:zh_CN;zh_SG;zh_TW;zh_HK)
Provides:       locale(patterns-xfce-xfce:zh_CN;zh_SG;zh_TW;zh_HK)

%package devel
Summary:        Chinese Lunar calendar library development files
Requires:       %{_libpkg} = %{version}
Requires:       typelib-1_0-LunarDate-%{_libver} = %{version}

%package doc
Summary:        Chinese Lunar calendar library Documents
BuildArch:      noarch

%description
Library to support date conversion from/to chinese lunar calendar

%description -n %{_libpkg}
Library to support date conversion from/to chinese lunar calendar

%description -n typelib-1_0-LunarDate-%{_libver}
Introspection bindings for Chinese Lunar calendar for use in Gnome Shell

%description devel
Development files for Chinese Lunar calendar library

%description doc
Documents for Chinese Lunar calendar library

%lang_package

%prep
%setup -q

%build
%meson -Ddocs=true \
       -Dintrospection=true \
       -Dvapi=true \
       -Dtests=true \
       %{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%post -n %{_libpkg} -p /sbin/ldconfig
%postun -n %{_libpkg} -p /sbin/ldconfig

%files
%doc AUTHORS NEWS README.md
%license COPYING
%{_bindir}/lunar-date
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/org.chinese.Lunar.Date.service

%files lang -f %{name}.lang

%files -n %{_libpkg}
%{_libdir}/*.so.*

%files -n typelib-1_0-LunarDate-%{_libver}
%{_libdir}/girepository-1.0/*.typelib

%files doc
%{_datadir}/doc/%{name}/

%files devel
%{_includedir}/%{name}-*
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir
%{_libdir}/pkgconfig/*.pc
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*

%changelog
