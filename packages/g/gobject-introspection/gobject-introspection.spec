#
# spec file for package gobject-introspection
#
# Copyright (c) 2023 SUSE LLC
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


Name:           gobject-introspection
Version:        1.76.0
Release:        0
# FIXME: Find a way to identify if we need python3-gobject or python-gobject from gi-find-deps.sh.
Summary:        GObject Introspection Tools
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/GObjectIntrospection

Source0:        https://download.gnome.org/sources/gobject-introspection/1.76/%{name}-%{version}.tar.xz
# gi-find-deps.sh is a rpm helper for Provides and Requires. Script creates typelib()-style Provides/Requires.
Source1:        gi-find-deps.sh
Source2:        gobjectintrospection.attr
Source3:        gobject-introspection-typelib.template
Source98:       baselibs.conf
Source99:       %{name}-rpmlintrc

BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.55.3
BuildRequires:  pkgconfig
BuildRequires:  python3-Mako
BuildRequires:  python3-Markdown
BuildRequires:  python3-devel
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.75.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libffi) >= 3.0.0
# gi-find-deps makes use of 'file' to identify the types.
Requires:       file
Requires:       libgirepository-1_0-1 = %{version}
# gi-find-deps uses the enhanced grep variant in order to do multi-line matching (for pkg.requires(..))
Requires:       pcre2-tools
Requires:       python3-xml
Requires:       python(abi) = %{python3_version}

%description
The goal of the project is to describe the APIs and collect them in
a uniform, machine readable format.

%package -n libgirepository-1_0-1
Summary:        GObject Introspection Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       girepository-1_0 >= %{version}

%description -n libgirepository-1_0-1
The goal of the project is to describe the APIs and collect them in
a uniform, machine readable format.

%package -n girepository-1_0
Summary:        Base GObject Introspection Bindings
License:        LGPL-2.1-or-later
Group:          System/Libraries
Requires:       libgirepository-1_0-1 >= %{version}
# Provide typelib() symbols based on gobject-introspection-typelib.template
# The template is checked during install if it matches the installed *.typelib files.
%(cat %{SOURCE3} | awk '{ print "Provides: " $0}')

%description -n girepository-1_0
The goal of the project is to describe the APIs and collect them in
a uniform, machine readable format.

%package devel
Summary:        GObject Introspection Development Files
# Note: the devel package requires the binaries, not just the library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       libffi-devel
Requires:       libgirepository-1_0-1 = %{version}

%description devel
The goal of the project is to describe the APIs and collect them in
a uniform, machine readable format.

%prep
%autosetup -p1

%build
%meson \
	-Dcairo=enabled \
	-Ddoctool=enabled \
	-Dgtk_doc=true \
	-Dpython='%{_bindir}/python3' \
	%{nil}
%meson_build

%check
%meson_test

%install
%meson_install
install -D %{SOURCE1} %{buildroot}%{_rpmconfigdir}/gi-find-deps.sh
install -D %{SOURCE2} -m 0644 %{buildroot}%{_rpmconfigdir}/fileattrs/gobjectintrospection.attr
# comparing, if we provide all the symbols expected.
ls %{buildroot}%{_libdir}/girepository-1.0/*.typelib | bash %{SOURCE1} -P > gobject-introspection-typelib.installed
diff -s %{SOURCE3} gobject-introspection-typelib.installed
%fdupes %{buildroot}
# fixup shebangs in files installed to /usr/bin
sed -i "s|%{_bindir}/env python|%{_bindir}/python|" %{buildroot}%{_bindir}/*

%ldconfig_scriptlets -n libgirepository-1_0-1

%files
%license COPYING COPYING.GPL
%doc NEWS README.rst TODO
%{_bindir}/g-ir-annotation-tool
%{_bindir}/g-ir-compiler
%{_bindir}/g-ir-doc-tool
%{_bindir}/g-ir-generate
%{_bindir}/g-ir-inspect
%{_bindir}/g-ir-scanner
%{_mandir}/man1/g-ir-compiler.1%{?ext_man}
%{_mandir}/man1/g-ir-generate.1%{?ext_man}
%{_mandir}/man1/g-ir-scanner.1%{?ext_man}
%{_mandir}/man1/g-ir-doc-tool.1%{?ext_man}
%{_datadir}/aclocal/introspection.m4
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gir-1.0/gir-1.2.rnc
# We don't include directly %%{_libdir}/gobject-introspection since there might
# be files there in the future that belong to the library package
%dir %{_libdir}/gobject-introspection
%{_libdir}/gobject-introspection/giscanner/
# We explicitly list the content of the directory that is of interest to us,
# since there might be files there in the future that belong to the library
# package
%dir %{_datadir}/gobject-introspection-1.0
%{_datadir}/gobject-introspection-1.0/Makefile.introspection
%{_datadir}/gobject-introspection-1.0/tests/
%{_datadir}/gobject-introspection-1.0/gdump.c
%{_rpmconfigdir}/gi-find-deps.sh
%{_rpmconfigdir}/fileattrs/gobjectintrospection.attr

%files -n libgirepository-1_0-1
%license COPYING.LGPL
# We own this directory here instead of devel to make sure other packages do
# not have to own it
%dir %{_datadir}/gir-1.0
%{_libdir}/libgirepository-1.0.so.*
%dir %{_libdir}/girepository-1.0

%files -n girepository-1_0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/gi/
%{_includedir}/gobject-introspection-1.0/
%{_libdir}/libgirepository-1.0.so
%{_libdir}/pkgconfig/gobject-introspection-1.0.pc
%{_libdir}/pkgconfig/gobject-introspection-no-export-1.0.pc

%changelog
