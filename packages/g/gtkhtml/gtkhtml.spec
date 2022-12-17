#
# spec file for package gtkhtml
#
# Copyright (c) 2022 SUSE LLC
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


%define _gtkhtml_version 4.0
%define _gtkhtml_editor_version 4.0
%define _gtkhtml_api 4_0
%define _gtkhtml_editor_api 4_0
%define _gtkhtml_major 0
%define _gtkhtml_editor_major 0
Name:           gtkhtml
Version:        4.10.0
Release:        0
Summary:        Lightweight HTML rendering/printing/editing engine
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/gtkhtml/4.10/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(enchant) >= 1.1.7
BuildRequires:  pkgconfig(gail-3.0) >= 3.2.0
BuildRequires:  pkgconfig(gladeui-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.2.0
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.26.0
Requires:       gsettings-desktop-schemas

%description
GtkHTML is a lightweight HTML rendering/printing/editing engine. It
was originally based on KHTMLW, part of the KDE project, but is now
being developed independently.

%package -n libgtkhtml-%{_gtkhtml_api}-%{_gtkhtml_major}
Summary:        Lightweight HTML rendering/printing/editing engine
Group:          System/Libraries
# For the lang package to be installable
Provides:       %{name} = %{version}
Provides:       %{name}-%{_gtkhtml_api} = %{version}
Obsoletes:      %{name} < %{version}
Provides:       gtkhtml2 = %{version}
Obsoletes:      gtkhtml2 < %{version}

%description -n libgtkhtml-%{_gtkhtml_api}-%{_gtkhtml_major}
GtkHTML is a lightweight HTML rendering/printing/editing engine. It
was originally based on KHTMLW, part of the KDE project, but is now
being developed independently.

%package -n libgtkhtml-editor-%{_gtkhtml_editor_api}-%{_gtkhtml_editor_major}
Summary:        Lightweight HTML rendering/printing/editing engine
Group:          System/Libraries
Recommends:     iso-codes

%description -n libgtkhtml-editor-%{_gtkhtml_editor_api}-%{_gtkhtml_editor_major}
GtkHTML is a lightweight HTML rendering/printing/editing engine. It
was originally based on KHTMLW, part of the KDE project, but is now
being developed independently.

%package -n glade-catalog-gtkhtml
Summary:        Lightweight HTML rendering/printing/editing engine -- Catalog for Glade
Group:          Development/Tools/GUI Builders
Requires:       glade
Requires:       libgtkhtml-editor-%{_gtkhtml_editor_api}-%{_gtkhtml_editor_major} = %{version}
Supplements:    packageand(glade:%{name}-devel)

%description -n glade-catalog-gtkhtml
GtkHTML is a lightweight HTML rendering/printing/editing engine. It
was originally based on KHTMLW, part of the KDE project, but is now
being developed independently.

This package provides a catalog for Glade, to allow the use of GtkHTML
widgets in Glade.

%package devel
Summary:        Lightweight HTML rendering/printing/editing engine -- Development Files
Group:          Development/Libraries/GNOME
Requires:       libgtkhtml-%{_gtkhtml_api}-%{_gtkhtml_major} = %{version}
Requires:       libgtkhtml-editor-%{_gtkhtml_editor_api}-%{_gtkhtml_editor_major} = %{version}
Provides:       gtkhtml2-devel = %{version}
Obsoletes:      gtkhtml2-devel < %{version}

%description devel
GtkHTML is a lightweight HTML rendering/printing/editing engine. It
was originally based on KHTMLW, part of the KDE project, but is now
being developed independently.

This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package -n %{name}-%{_gtkhtml_api}

%prep
%setup -q

%build
%configure \
        --disable-static \
        --with-glade-catalog
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}-%{_gtkhtml_version}
%fdupes %{buildroot}

%post -n libgtkhtml-%{_gtkhtml_api}-%{_gtkhtml_major} -p /sbin/ldconfig
%postun -n libgtkhtml-%{_gtkhtml_api}-%{_gtkhtml_major} -p /sbin/ldconfig
%post -n libgtkhtml-editor-%{_gtkhtml_editor_api}-%{_gtkhtml_editor_major} -p /sbin/ldconfig
%postun -n libgtkhtml-editor-%{_gtkhtml_editor_api}-%{_gtkhtml_editor_major} -p /sbin/ldconfig

%files -n libgtkhtml-%{_gtkhtml_api}-%{_gtkhtml_major}
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_datadir}/gtkhtml-%{_gtkhtml_version}/
%{_libdir}/libgtkhtml-%{_gtkhtml_version}.so.*

%files -n libgtkhtml-editor-%{_gtkhtml_editor_api}-%{_gtkhtml_editor_major}
%{_libdir}/libgtkhtml-editor-%{_gtkhtml_editor_version}.so.*

%files -n %{name}-%{_gtkhtml_api}-lang -f %{name}-%{_gtkhtml_version}.lang

%files -n glade-catalog-gtkhtml
%{_libdir}/glade/modules/libglade-gtkhtml-editor.so
%{_datadir}/glade/catalogs/gtkhtml-editor.xml

%files devel
%{_bindir}/gtkhtml-editor-test
%{_includedir}/libgtkhtml-%{_gtkhtml_version}/
%{_libdir}/libgtkhtml-%{_gtkhtml_version}.so
%{_libdir}/libgtkhtml-editor-%{_gtkhtml_editor_version}.so
%{_libdir}/pkgconfig/libgtkhtml-%{_gtkhtml_version}.pc
%{_libdir}/pkgconfig/gtkhtml-editor-%{_gtkhtml_editor_version}.pc

%changelog
