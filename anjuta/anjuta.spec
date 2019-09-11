#
# spec file for package anjuta
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


Name:           anjuta
Version:        3.28.0
Release:        0
Summary:        Versatile Integrated Development Environment for GNOME
License:        GPL-2.0-or-later
Group:          Development/Tools/IDE
URL:            https://wiki.gnome.org/Apps/Anjuta
Source0:        http://download.gnome.org/sources/anjuta/3.28/%{name}-%{version}.tar.xz
Source99:       %{name}-rpmlintrc
BuildRequires:  autogen
BuildRequires:  binutils-devel
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  libapr-util1-devel
BuildRequires:  libapr1-devel
BuildRequires:  libvala-devel
BuildRequires:  libxslt-devel
BuildRequires:  perl-gettext
BuildRequires:  pkgconfig
BuildRequires:  sqlite3-devel
BuildRequires:  subversion-devel
BuildRequires:  translation-update-upstream
BuildRequires:  vala
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gdl-3.0) >= 3.5.5
BuildRequires:  pkgconfig(gladeui-2.0) >= 3.12.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.34.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.6.0
BuildRequires:  pkgconfig(gtksourceview-3.0) >= 3.0.0
BuildRequires:  pkgconfig(libdevhelp-3.0) >= 3.7.5
BuildRequires:  pkgconfig(libgda-5.0) >= 5.0.0
BuildRequires:  pkgconfig(libgvc)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.23
BuildRequires:  pkgconfig(serf-1)
BuildRequires:  pkgconfig(vte-2.91)
# Directly required by anjuta:
Requires:       autoconf
Requires:       autogen
Requires:       automake
Requires:       gettext
# libgda-sqlite is needed by the symbol-db plugin. See bnc#624924.
Requires:       libgda-sqlite
Requires:       libtool
Recommends:     %{name}-lang
%ifnarch ia64 s390 s390x aarch64 ppc64le
BuildRequires:  valgrind-devel
%endif

%description
Anjuta is a versatile Integrated Development Environment (IDE) for the
GNOME desktop. It features a number of advanced programming facilities
includes project management, application wizards, an interactive
debugger, an integrated Glade UI designer, integrated Devhelp API help,
an integrated Valgrind memory profiler, an integrated gprof performance
profiler, a class generator, a powerful source editor, source browsing,
and more.

%package -n libanjuta-3-0
Summary:        Library for developing Anjuta plugins
Group:          System/Libraries

%description -n libanjuta-3-0
Anjuta is a versatile Integrated Development Environment (IDE) for the
GNOME desktop.

%package -n typelib-1_0-Anjuta-3_0
Summary:        Introspection bindings for the Anjuta plugin library
Group:          System/Libraries

%description -n typelib-1_0-Anjuta-3_0
Anjuta is a versatile Integrated Development Environment (IDE) for the
GNOME desktop.

This package provides the GObject Introspection bindings for the Anjuta
library to develop plugins.

%package -n glade-catalog-anjuta
Summary:        Glade catalog for Anjuta
Group:          Development/Tools/GUI Builders
Requires:       %{name} = %{version}
Requires:       glade
Supplements:    packageand(glade:%{name}-devel)

%description -n glade-catalog-anjuta
Anjuta is a versatile Integrated Development Environment (IDE) for the
GNOME desktop.

This package provides a catalog for Glade, to allow the use the Anjuta
widgets in Glade.

%package devel
Summary:        Development files for Anjuta plugins
Group:          Development/Libraries/C and C++
Requires:       libanjuta-3-0 = %{version}
Requires:       typelib-1_0-Anjuta-3_0 = %{version}
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}

%description devel
Anjuta is a versatile Integrated Development Environment (IDE) for the
GNOME desktop.

%lang_package

%prep
%setup -q
translation-update-upstream

%build
%configure\
        --disable-static \
        --enable-glade-catalog \
        %{nil}
make %{?_smp_mflags} V=1

%install
%make_install
# These should go to defaultdocdir.
rm -r %{buildroot}%{_datadir}/doc
%find_lang anjuta %{?no_lang_C}
%find_lang anjuta-faqs %{no_lang_C} %{name}.lang
# There's no translation for those yet. If build fails because of non-packaged
# translations, uncomment those lines.
%find_lang anjuta-build-tutorial %{?no_lang_C} anjuta.lang
#%%find_lang anjuta-faqs %{?no_lang_C} anjuta.lang
%find_lang anjuta-manual %{?no_lang_C} anjuta.lang
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}/%{_prefix}

%post -n libanjuta-3-0 -p /sbin/ldconfig
%postun -n libanjuta-3-0 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README doc/ScintillaDoc.html
%doc %{_datadir}/help/C/anjuta-build-tutorial/
%doc %{_datadir}/help/C/anjuta-faqs/
%doc %{_datadir}/help/C/anjuta-manual/
%{_bindir}/anjuta
%{_bindir}/anjuta-launcher
%{_bindir}/anjuta-tags
%{_libdir}/anjuta/
%{_datadir}/anjuta/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/anjuta.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/mime/packages/*.xml
%{_datadir}/pixmaps/anjuta/
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/mimetypes/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/icons/hicolor/scalable/mimetypes/*.svg
%{_datadir}/icons/hicolor/symbolic/apps/anjuta-symbolic.svg
%{_mandir}/man?/*%{ext_man}

%files -n libanjuta-3-0
%{_libdir}/libanjuta-3.so.*

%files -n typelib-1_0-Anjuta-3_0
%{_libdir}/girepository-1.0/Anjuta-3.0.typelib
%{_libdir}/girepository-1.0/IAnjuta-3.0.typelib

%files -n glade-catalog-anjuta
%{_libdir}/glade/modules/libgladeanjuta.so
%{_datadir}/glade/catalogs/anjuta-glade.xml

%files devel
%doc ChangeLog FUTURE TODO
# Own these directories to avoid requirement on gtk-doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%doc %{_datadir}/gtk-doc/html/libanjuta/
%{_includedir}/libanjuta-3.0/
%{_libdir}/libanjuta-3.so
%{_libdir}/pkgconfig/libanjuta-3.0.pc
%{_datadir}/gir-1.0/*.gir

%files lang -f %{name}.lang

%changelog
