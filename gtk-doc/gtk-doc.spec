#
# spec file for package gtk-doc
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


Name:           gtk-doc
Version:        1.29
Release:        0
Summary:        GTK+ DocBook Documentation Generator
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/SGML
URL:            http://www.gtk.org/gtk-doc/
# When updating this package, please don't forget to update the gtk-doc.m4 Source in glib2.
Source0:        https://download.gnome.org/sources/gtk-doc/1.29/%{name}-%{version}.tar.xz

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libtool
BuildRequires:  libxml2-tools
BuildRequires:  openjade
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  sgml-skel
BuildRequires:  xsltproc
BuildRequires:  yelp-tools
Requires:       docbook-xsl-stylesheets
Requires:       docbook_4
Requires:       glib2-devel
Requires:       libxml2-tools
Requires:       openjade
Requires:       xsltproc
Recommends:     %{name}-lang
Recommends:     source-highlight
# Old for <= 10.2 & CODE10
Provides:       gtkdoc = %{version}
Obsoletes:      gtkdoc

%description
Gtkdoc is a set of Perl scripts that generate API reference
documentation in DocBook format.  It can extract documentation from
source code comments in a manner similar to Java-doc.  It is used to
generate the documentation for GLib, Gtk+, and GNOME.

%lang_package

%prep
%autosetup -p1

%build
%configure PYTHON=%{_bindir}/python3
make %{?_smp_mflags}

%install
%make_install
# Do not install the cmake files for now - they need more clarification (1.25)
rm -rf %{buildroot}%{_libdir}/cmake
mkdir -p %{buildroot}%{_datadir}/gtk-doc/html
mv -v doc/README doc/doc.README
%find_lang %{name}-manual %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS COPYING-DOCS ChangeLog NEWS README TODO doc/*
%{_bindir}/gtkdoc-*
%{_bindir}/gtkdocize
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/gtk-doc.m4
%{_datadir}/gtk-doc/
%{_datadir}/pkgconfig/gtk-doc.pc
%doc %{_datadir}/help/C/gtk-doc-manual/

%files lang -f %{name}-manual.lang

%changelog
