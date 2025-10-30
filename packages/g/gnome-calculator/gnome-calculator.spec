#
# spec file for package gnome-calculator
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define sover 2-1_0_1
%define gcisover 1-0_0_0

Name:           gnome-calculator
Version:        49.1.1
Release:        0
Summary:        A GNOME Calculator Application
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://wiki.gnome.org/Apps/Calculator
Source0:        %{name}-%{version}.tar.zst
BuildSystem:    meson
BuildOption:    -Ddisable-introspection=true

BuildRequires:  blueprint-compiler
BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson >= 0.52.0
BuildRequires:  mpc-devel
BuildRequires:  mpfr-devel
BuildRequires:  vala
BuildRequires:  valadoc
BuildRequires:  valadoc-doclet-devhelp
BuildRequires:  rpm_macro(meson_buildrequires)

%description
A GNOME calculator package based on calctool and MP library.

%package -n gnome-shell-search-provider-gnome-calculator
Summary:        GNOME Calculator -- Search Provider for GNOME Shell
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}
Supplements:    (gnome-shell and %{name})

%description -n gnome-shell-search-provider-gnome-calculator
This package contains a search provider to enable GNOME Shell to get
search results from GNOME Calculator.

%package -n libgcalc-%{sover}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n libgcalc-%{sover}
This package contains a shared library for %{name}.

%package -n libgci-%{gcisover}
Summary:        GNOME Calculator Library GTK Interface
Group:          System/Libraries

%description -n libgci-%{gcisover}
This package contains a shared library for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       libgcalc-%{sover} = %{version}
Requires:       libgci-%{gcisover} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%lang_package

%generate_buildrequires
%meson_buildrequires

%install -a
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%check
%ifnarch %ix86 %arm
%meson_test
%else
echo Test ignored on 32bit architectures, see https://gitlab.gnome.org/GNOME/gnome-calculator/-/issues/503
%endif

%ldconfig_scriptlets -n libgcalc-%{sover}
%ldconfig_scriptlets -n libgci-%{gcisover}

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}
%{_bindir}/gnome-calculator
%{_bindir}/gcalccmd
%{_datadir}/metainfo/org.gnome.Calculator.metainfo.xml
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
%{_libdir}/libgcalc-2.so.*

%files -n libgci-%{gcisover}
%{_libdir}/libgci-1.so.*

%files devel
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books
%{_datadir}/devhelp/books/GCalc-2/
%{_datadir}/devhelp/books/GCi-1/
%{_includedir}/gcalc-2/
%{_includedir}/gci-2/
%{_libdir}/libgcalc-2.so
%{_libdir}/pkgconfig/gcalc-2.pc
%{_libdir}/pkgconfig/gci-1.pc
%{_libdir}/libgci-1.so
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/GCalc-2.gir
%{_datadir}/gir-1.0/GCi-1.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gcalc-2.*
%{_datadir}/vala/vapi/gci-1.*

%files lang -f %{name}.lang

%changelog
