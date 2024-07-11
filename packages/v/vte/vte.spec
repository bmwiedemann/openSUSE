#
# spec file for package vte
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


%define _sover   -2_91-0
%define _apiver  2.91
%define _binver  2_91
%define _apiver4 3.91
%define _binver4 3_91
%define _name    vte

%bcond_without  gtk4_support
%bcond_with     glade_support

Name:           vte
Version:        0.76.3
Release:        0
Summary:        Terminal Emulator Library
License:        CC-BY-4.0 AND LGPL-3.0-or-later AND GPL-3.0-or-later AND MIT
Group:          Development/Libraries/GNOME
URL:            https://gitlab.gnome.org/GNOME/vte
Source:         %{_name}-%{version}.tar.zst
# PATCH-FIX-OPENSUSE vte-enable-build-flag-pie.patch yfjiang@suse.com -- enable PIE flag to be compatible with gcc default linking option
Patch0:         vte-enable-build-flag-pie.patch

# PATCH-FIX-SLE vte-revert-back-to-c++17.patch yu.daike@suse.com -- revert c++20 features back to c++17
Patch100:       vte-revert-back-to-c++17.patch

BuildRequires:  c++_compiler
BuildRequires:  fdupes
%if %{with glade_support}
BuildRequires:  glade
%endif
BuildRequires:  gobject-introspection-devel
BuildRequires:  gperf
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  (python3-dataclasses if python3-base < 3.7)
BuildRequires:  pkgconfig(fribidi) >= 1.0.0
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.72.0
BuildRequires:  pkgconfig(gnutls) >= 3.2.7
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16.0
%if %{with gtk4_support}
BuildRequires:  pkgconfig(gtk4) >= 4.14.0
%endif
BuildRequires:  pkgconfig(liblz4) >= 1.9
BuildRequires:  pkgconfig(libpcre2-8) >= 10.21
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pango) >= 1.22.0
BuildRequires:  pkgconfig(vapigen) >= 0.24
BuildRequires:  pkgconfig(zlib)

%description
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

%package -n libvte%{_sover}
Summary:        Terminal Emulator Library
# Needed to make lang package installable (and because we used to
# have a vte package earlier).
License:        LGPL-2.0-only
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libvte%{_sover}
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

%package -n typelib-1_0-Vte-%{?_binver}
Summary:        Introspection bindings for the VTE terminal emulator library
License:        LGPL-2.0-only
Group:          System/Libraries
Provides:       typelib-1_0-Vte-%{_apiver} = %{version}
Obsoletes:      typelib-1_0-Vte-%{_apiver} < %{version}

%description -n typelib-1_0-Vte-%{?_binver}
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

This package provides the GObject Introspection bindings for VTE.

%package tools
Summary:        Tools from the VTE terminal emulator package
License:        LGPL-2.0-only
Group:          System/Libraries

%description tools
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

This package provides tools using VTE.

%if %{with gtk4_support}
%package -n typelib-1_0-Vte-%{?_binver4}
Summary:        Introspection bindings for the VTE terminal emulator library
License:        LGPL-2.0-only
Group:          System/Libraries

%description -n typelib-1_0-Vte-%{?_binver4}
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

This package provides the GObject Introspection bindings for VTE.

%package tools-gtk4
Summary:        Tools from the VTE terminal emulator package
License:        LGPL-2.0-only
Group:          System/Libraries

%description tools-gtk4
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

This package provides tools using VTE.
%endif

%package devel
Summary:        Development files for the VTE terminal emulator library
License:        LGPL-2.0-only
Group:          Development/Libraries/GNOME
Requires:       libvte%{_sover} = %{version}
Requires:       typelib-1_0-Vte-%{?_binver} = %{version}
%if %{with gtk4_support}
Requires:       typelib-1_0-Vte-%{?_binver4} = %{version}
%endif
Provides:       vte-doc = %{version}
Obsoletes:      vte-doc < %{version}

%description devel
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

This package contains the files needed for building applications using
VTE.

%if %{with glade_support}
%package -n glade-catalog-vte
Summary:        Glade catalog for vte
License:        CC-BY-4.0 AND LGPL-3.0-or-later AND GPL-3.0-or-later AND MIT
Group:          Development/Tools/GUI Builders
Requires:       %{name} = %{version}
Requires:       glade
Supplements:    (glade and %{name}-devel)
BuildArch:      noarch

%description -n glade-catalog-vte
This package provides a catalog for Glade, to allow the use the vte
widgets in Glade.
%endif

%lang_package

%prep
%autosetup -n %{_name}-%{version} -N
%patch -P 0 -p1
%if 0%{?sle_version}
%patch -P 100 -p1
%endif

%build
%meson \
	-Ddocs=true \
%if %{with gtk4_support}
	-Dgtk4=true \
%endif
%if %{with glade_support}
	-Dglade=true \
%else
	-Dglade=false \
%endif
	%{nil}
%meson_build

%install
%meson_install

%find_lang vte-%{_apiver}
%fdupes %{buildroot}%{_prefix}

# Make default docdir ref openSUSE standard
mkdir -p %{buildroot}%{_docdir}/vte-%{_apiver}
%if %{with gtk4_support}
mkdir -p %{buildroot}%{_docdir}/vte-%{_apiver}-gtk4
%endif
# Move docs from upstream docdir to openSUSE docdir standard
mv %{buildroot}%{_datadir}/doc/vte-%{_apiver} %{buildroot}%{_docdir}
%if %{with gtk4_support}
mv %{buildroot}%{_datadir}/doc/vte-%{_apiver}-gtk4 %{buildroot}%{_docdir}
%endif

%ldconfig_scriptlets -n libvte%{_sover}

%files -n libvte%{_sover}
%license COPYING.CC-BY-4-0 COPYING.GPL3 COPYING.LGPL3 COPYING.XTERM
%{_libdir}/*.so.*
%config %{_sysconfdir}/profile.d/vte.sh
%config %{_sysconfdir}/profile.d/vte.csh
%dir %{_userunitdir}/vte-spawn-.scope.d
%{_userunitdir}/vte-spawn-.scope.d/defaults.conf
%{_libexecdir}/vte-urlencode-cwd

%files -n typelib-1_0-Vte-%{?_binver}
%{_libdir}/girepository-1.0/Vte-%{_apiver}.typelib

%files tools
%{_bindir}/vte-%{?_apiver}

%if %{with gtk4_support}
%files -n typelib-1_0-Vte-%{?_binver4}
%{_libdir}/girepository-1.0/Vte-%{_apiver4}.typelib

%files tools-gtk4
%{_bindir}/vte-%{?_apiver}-gtk4
%endif

%files devel
%doc AUTHORS
%doc %{_docdir}/vte-%{_apiver}/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/vte-%{_apiver}/
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/vte-%{_apiver}.vapi
%{_datadir}/vala/vapi/vte-%{_apiver}.deps

%if %{with gtk4_support}
%{_includedir}/vte-%{_apiver}-gtk4/
%doc %{_docdir}/vte-%{_apiver}-gtk4/
%{_datadir}/vala/vapi/vte-%{_apiver}-gtk4.deps
%{_datadir}/vala/vapi/vte-%{_apiver}-gtk4.vapi
%endif

%if %{with glade_support}
%files -n glade-catalog-vte
%{_datadir}/glade/catalogs/vte-%{_apiver}.xml
%{_datadir}/glade/pixmaps/hicolor/16x16/actions/widget-vte-terminal.png
%{_datadir}/glade/pixmaps/hicolor/22x22/actions/widget-vte-terminal.png
%endif

%files lang -f vte-%{_apiver}.lang

%changelog
