#
# spec file for package gnome-calculator
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


%define sover 1-0_0_0

Name:           gnome-calculator
Version:        3.34.1
Release:        0
Summary:        A GNOME Calculator Application
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://wiki.gnome.org/Apps/Calculator
Source0:        https://download.gnome.org/sources/gnome-calculator/3.34/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  mpc-devel
BuildRequires:  mpfr-devel
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  vala
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.40
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.19.3
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.42
BuildRequires:  pkgconfig(libxml-2.0)

%description
A GNOME calculator package based on calctool and MP library.

%package -n gnome-shell-search-provider-gnome-calculator
Summary:        GNOME Calculator -- Search Provider for GNOME Shell
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}
Supplements:    packageand(gnome-shell:%{name})

%description -n gnome-shell-search-provider-gnome-calculator
This package contains a search provider to enable GNOME Shell to get
search results from GNOME Calculator.

%package -n libgcalc-%{sover}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n libgcalc-%{sover}
This package contains the shared library for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       libgcalc-%{sover} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%check
%meson_test

%post -n libgcalc-%{sover} -p /sbin/ldconfig
%postun -n libgcalc-%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}
%{_bindir}/gnome-calculator
%{_bindir}/gcalccmd
%{_datadir}/metainfo/org.gnome.Calculator.appdata.xml
%{_datadir}/applications/org.gnome.Calculator.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.calculator.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Calculator*.svg
%{_mandir}/man1/gnome-calculator.1%{?ext_man}
%{_mandir}/man1/gcalccmd.1%{?ext_man}

%files -n gnome-shell-search-provider-gnome-calculator
%{_datadir}/dbus-1/services/org.gnome.Calculator.SearchProvider.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Calculator-search-provider.ini
%{_libexecdir}/gnome-calculator-search-provider

%files -n libgcalc-%{sover}
%{_libdir}/libgcalc-1.so.*

%files devel
%dir %{_includedir}/gcalc-1
%dir %{_includedir}/gcalc-1/gcalc
%{_includedir}/gcalc-1/gcalc/gcalc.h
%{_libdir}/libgcalc-1.so
%{_libdir}/pkgconfig/gcalc-1.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GCalc-1.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gcalc-1.deps
%{_datadir}/vala/vapi/gcalc-1.vapi

%files lang -f %{name}.lang

%changelog
