#
# spec file for package dia
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


Name:           dia
Version:        0.97.3
Release:        0
Summary:        A Diagram Creation Program
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://wiki.gnome.org/Dia
Source0:        https://download.gnome.org/sources/dia/0.97/%{name}-%{version}.tar.xz
Source1:        font-test-japanese.dia
Source2:        font-test-czech.dia
Source3:        font-test-german-euro.dia
Source4:        dia.appdata.xml
# PATCH-FIX-UPSTREAM dia-intltool-0.51.patch bgo#737255 dimstar@opensuse.org -- Fix installation of locales with intltool 0.51
Patch0:         dia-intltool-0.51.patch
# PATCH-FIX-OPENSUSE dia-0.92.2-no-strict-aliasing.patch
Patch3:         dia-0.92.2-no-strict-aliasing.patch
# PATCH-FIX-OPENSUSE dia-remove-datetime.patch vuntz@novell.com -- Do not put date/time in the compiled binary (needed for build-compare)
Patch17:        dia-remove-datetime.patch
# PATCH-FIX-UPSTREAM dia-libemf-64bit.patch bgo#675495 sbrabec@suse.cz -- Fix build with libEMF on 64-bit platforms.
Patch20:        dia-libemf-64bit.patch
# PATCH-FIX-OPENSUSE dia-enable-html-doc.patch mgorse@suse.com -- Always enable html docs if xsltproc present.
Patch23:        dia-enable-html-doc.patch
# PATCH-FIX-OPENSUSE dia-configure-c99.patch boo#1224536 mjambor@suse.cz -- Fix configure issue with GCC 14, from https://src.fedoraproject.org/rpms/dia/c/0a14169fc36b959598074065678e0126830317f8?branch=rawhide
Patch30:        dia-configure-c99.patch
# PATCH-FIX-UPSTREAM dia-0.97.3-get_data_size.patch boo#1224536 mjambor@suse.cz -- One of upstream patches for -Wincompatible-pointer-types
Patch31:        dia-0.97.3-get_data_size.patch
# PATCH-FIX-UPSTREAM dia-0.97.3-const-ft_vector.patch boo#1224536 mjambor@suse.cz -- One of upstream patches for -Wincompatible-pointer-types
Patch32:        dia-0.97.3-const-ft_vector.patch
# PATCH-FIX-UPSTREAM dia-0.97.3-g_test_add_data_func_1.patch boo#1224536 mjambor@suse.cz -- One of upstream patches for -Wincompatible-pointer-types
Patch33:        dia-0.97.3-g_test_add_data_func_1.patch
# PATCH-FIX-UPSTREAM dia-0.97.3-g_test_add_data_func_2.patch boo#1224536 mjambor@suse.cz -- One of upstream patches for -Wincompatible-pointer-types
Patch34:        dia-0.97.3-g_test_add_data_func_2.patch

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libEMF-devel
BuildRequires:  libtool
BuildRequires:  libxslt-tools
BuildRequires:  pkgconfig
BuildRequires:  swig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdk-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libart-2.0)
BuildRequires:  pkgconfig(libexslt)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(pango)
Requires:       ghostscript-fonts-std
Requires:       xdg-utils

%description
Dia is designed to be much like the commercial program 'Visio.' It can
be used to draw many different kinds of diagrams. It has special
objects to help draw entity relationship diagrams, UML diagrams, SADT,
flowcharts, network diagrams, and simple circuits. It is possible to
add support for new shapes by writing simple XML files, and using a
subset of SVG to draw the shape.

Dia can load and save diagrams to a custom XML format (gzipped by
default to save space), can export diagrams to EPS, PNG, CGM, or SVG
formats, and can print diagrams (including ones that span multiple
pages).

%lang_package

%prep
%setup -q
%patch -P 0 -p1
%patch -P 3
%patch -P 17 -p1
%patch -P 20 -p1
%patch -P 23 -p1
%patch -P 30 -p1
%patch -P 31 -p1
%patch -P 32 -p1
%patch -P 33 -p1
%patch -P 34 -p1

cp $RPM_SOURCE_DIR/font-test*dia .

%build
autoreconf -f -i
intltoolize --force
%configure\
	--disable-static\
	--disable-gnome\
	--with-cairo\
	--with-swig \
	--docdir=%{_docdir}/%{name}
make  VERBOSE=1 %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file -r -N Dia -C "" -G "Diagram Editor" dia Office FlowChart
%find_lang %{name} %{?no_lang_C}
# No need for mime-info-to-mime, application/x-dia-diagram is defined in freedesktop.org.xml
rm -r %{buildroot}%{_datadir}/mime-info
rm samples/Makefile* samples/*png
if [ -f %{buildroot}%{_datadir}/appdata/dia.appdata.xml ]; then
  echo "Please remove the added dia.appdata.xml file from the sources - the tarball installs it"
  false
else
  mkdir -p %{buildroot}%{_datadir}/appdata
  cp %{SOURCE4} %{buildroot}%{_datadir}/appdata/
fi

%fdupes %{buildroot}%{_datadir}

%files
%doc AUTHORS ChangeLog KNOWN_BUGS NEWS README TODO
%license COPYING
%{_bindir}/*
%{_libdir}/dia
%dir %{_datadir}/appdata
%{_datadir}/appdata/dia.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dia
%{_datadir}/icons/hicolor/*/apps/dia.*
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/en/
%dir %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/html/en
# EXAMPLES FOR THE (eu,fr,pl) LANGS ARE ALL SYMLINKED TO en
%doc %{_docdir}/%{name}/*/examples
%{_mandir}/man1/*.*

%files lang -f %{name}.lang
%exclude %{_docdir}/%{name}/AUTHORS
%exclude %{_docdir}/%{name}/COPYING
%exclude %{_docdir}/%{name}/ChangeLog
%exclude %{_docdir}/%{name}/KNOWN_BUGS
%exclude %{_docdir}/%{name}/NEWS
%exclude %{_docdir}/%{name}/README
%exclude %{_docdir}/%{name}/TODO
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/html
%exclude %{_docdir}/%{name}/en
%doc %{_docdir}/%{name}/*
%exclude %{_docdir}/%{name}/html/en
%exclude %{_docdir}/%{name}/*/examples
%doc %{_docdir}/%{name}/html/*
%{_mandir}/fr/man1/*.*

%changelog
