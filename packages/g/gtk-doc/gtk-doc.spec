#
# spec file for package gtk-doc
#
# Copyright (c) 2019 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "doc"
%bcond_without  doc
%define psuffix -manual
%else
%bcond_with     doc
%endif

Name:           gtk-doc%{?psuffix}
Version:        1.32
Release:        0
%if "%{flavor}" == ""
Summary:        GTK+ Documentation Generator
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/SGML
%else
Summary:        Manual for Gtkdoc
License:        GFDL-1.1-or-later
Group:          Documentation/HTML
%endif
URL:            http://www.gtk.org/gtk-doc/
# When updating this package, please don't forget to update the gtk-doc.m4 Source in glib2.
Source0:        https://download.gnome.org/sources/gtk-doc/1.32/gtk-doc-%{version}.tar.xz

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libtool
BuildRequires:  libxml2-tools
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  sgml-skel
%if %{with doc}
BuildRequires:  fdupes
BuildRequires:  yelp-tools
# gtk-doc-manual was split from the main package
Provides:       gtk-doc:%{_datadir}/help/C/gtk-doc-manual/index.docbook
Conflicts:      gtk-doc < %{version}-%{release}
Conflicts:      gtk-doc-lang < %{version}-%{release}
%else
BuildRequires:  xsltproc
Requires:       docbook-xsl-stylesheets
Requires:       docbook_4
Requires:       glib2-devel
Requires:       libxml2-tools
Requires:       python3-pygments
Requires:       xsltproc
Recommends:     gtk-doc-manual
# Old for <= 10.2 & CODE10
Provides:       gtkdoc = %{version}
Obsoletes:      gtkdoc
%endif

%if "%{flavor}" == ""
%description
Gtkdoc is a set of Python scripts that generates API reference
documentation in e.g DocBook, HTML or PDF format.  It can extract
documentation from source code comments in a manner similar to
Java-doc.  It is used to generate the documentation for GLib,
Gtk+, and GNOME.

%else
%description
User manual for Gtkdoc
%endif

%package mkpdf
Summary:        Gtkdoc PDF Generator
Supplements:    packageand(gtk-doc:dblatex)
Requires:       %{name} = %{version}
Requires:       dblatex

%description mkpdf
PDF generator for Gtkdoc.

%lang_package -n gtk-doc-manual

%prep
%autosetup -p1 -n gtk-doc-%{version}

%build
autoreconf
%configure PYTHON=%{_bindir}/python3 \
  DBLATEX=%{_bindir}/dblatex
make %{?_smp_mflags}

%install
%if "%{flavor}" == ""
%make_install
mkdir -p %{buildroot}%{_datadir}/gtk-doc/html
%endif

%if %{with doc}
%make_install -C help
%fdupes %{buildroot}%{_datadir}/help/[a-z]*
%find_lang gtk-doc-manual %{?no_lang_C}
%endif

%if "%{flavor}" == ""
%files
%license COPYING
%doc AUTHORS NEWS README TODO
%{_bindir}/gtkdoc-*
%{_bindir}/gtkdocize
%exclude %{_bindir}/gtkdoc-mkpdf
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/gtk-doc.m4
%{_datadir}/gtk-doc/
%exclude %{_datadir}/gtk-doc/python/gtkdoc/mkpdf*
%{_datadir}/pkgconfig/gtk-doc.pc
%dir %{_datadir}/cmake
%dir %{_datadir}/cmake/GtkDoc
%{_datadir}/cmake/GtkDoc/GtkDocConfig.cmake
%{_datadir}/cmake/GtkDoc/GtkDocConfigVersion.cmake
%{_datadir}/cmake/GtkDoc/GtkDocScanGObjWrapper.cmake

%files mkpdf
%{_bindir}/gtkdoc-mkpdf
%{_datadir}/gtk-doc/python/gtkdoc/mkpdf*
%endif

%if %{with doc}
%files -n gtk-doc-manual
%license COPYING-DOCS
%doc %{_datadir}/help/C/gtk-doc-manual

%files -n gtk-doc-manual-lang -f gtk-doc-manual.lang
%endif

%changelog
