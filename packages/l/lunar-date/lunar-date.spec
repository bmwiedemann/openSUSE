#
# spec file for package lunar-date
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


%define _libver 3_0
%define _libpkg lib%{name}-%{_libver}-1

Summary:        Chinese Lunar calendar library
License:        GPL-2.0-or-later
Group:          System/I18n/Chinese
Name:           lunar-date
Version:        2.9.3
Release:        0
URL:            https://github.com/yetist/lunar-date
Source:         https://github.com/yetist/lunar-date/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(vapigen)

%package -n %{_libpkg}
Summary:        Chinese Lunar calendar library
Group:          System/I18n/Chinese
Recommends:     %{name}-lang

%package -n typelib-1_0-LunarDate-%{_libver}
Summary:        Chinese Lunar calendar introspection bindings
Group:          System/I18n/Chinese

%package devel
Summary:        Chinese Lunar calendar library development files
Group:          Development/Libraries/C and C++
Requires:       %{_libpkg} = %{version}
Requires:       typelib-1_0-LunarDate-%{_libver} = %{version}

%package doc
Summary:        Chinese Lunar calendar library Documents
Group:          Documentation/Other
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

%{lang_package}

%prep
%setup -q

%build
%meson -Denable_gtk_doc=true \
       -Dwith_introspection=true \
       -Dwith_vala=true \
       -Denable_tests=true \
       %{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%post -n %{_libpkg} -p /sbin/ldconfig

%postun -n %{_libpkg} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS NEWS README.md
%license COPYING
%{_bindir}/lunar-date
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/org.chinese.Lunar.Date.service

%files lang -f %{name}.lang

%files -n %{_libpkg}
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files -n typelib-1_0-LunarDate-%{_libver}
%defattr(-,root,root,-)
%{_libdir}/girepository-1.0/*.typelib

%files doc
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/%{name}

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}-*
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir
%{_libdir}/pkgconfig/*.pc
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*

%changelog
