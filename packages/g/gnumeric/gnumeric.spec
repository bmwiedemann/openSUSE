#
# spec file for package gnumeric
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


Name:           gnumeric
Version:        1.12.54
Release:        0
Summary:        Spreadsheet Application
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Productivity/Office/Spreadsheets
URL:            http://www.gnumeric.org/
Source0:        https://download.gnome.org/sources/gnumeric/1.12/%{name}-%{version}.tar.xz
Source1:        gnumeric-rpmlintrc

BuildRequires:  bison
BuildRequires:  docbook-dtds
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libgsf-devel
BuildRequires:  pkgconfig
# Disable python3-devel BR for now, not supported yet.
#BuildRequires:  python3-devel
BuildRequires:  pkgconfig(gio-2.0) >= 2.38.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.38.0
# Introspection disabled, need to pass --enable-introspection to configure if we want it.
#BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.0.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.38.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.8.7
BuildRequires:  pkgconfig(libgda-6.0) >= 6.0.0
BuildRequires:  pkgconfig(libgda-ui-6.0) >= 6.0.0
BuildRequires:  pkgconfig(libgoffice-0.10) >= 0.10.51
BuildRequires:  pkgconfig(libgsf-1) >= 1.14.33
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4.12
BuildRequires:  pkgconfig(pango) >= 1.24.0
BuildRequires:  pkgconfig(pangocairo) >= 1.24.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.0.0
Recommends:     %{name}-doc
Recommends:     ghostscript-fonts-std
Recommends:     liberation-fonts
# gnumeric uses a ghelp: URI to launch the help application. Let's recommend to have an app that can handle it (bnc#719679)
Recommends:     mimehandler(x-scheme-handler/ghelp)
Provides:       gnumeric2 = %{version}
Obsoletes:      gnumeric2 < %{version}
%{perl_requires}
%{?libperl_requires}

%description
Gnumeric is a spreadsheet application with advanced features and
analytics.  It aims to minimize the cost of transition from proprietary
spreadsheets by offering a familiar look and feature set.  In addition
to read and write support for all versions of Microsoft Excel
(including reading encrypted files), there is also support for many
other formats including:

*Applix 4 and 5 *DIF *Lotus-123 (wk1, wk2, wk3) *OpenOffice.org (Oasis)
*PlanPerfect (pln) *Psion5 *Quattro Pro (wb1, wb2, wb3) *SYLK
*XBase/DB3

Text formats, such as comma or tab separated values, HTML, XHTML, and
Latex, are supported and there are powerful assistants to handle custom
needs.

Gnumeric is part of the GNOME project.

%package doc
Summary:        Documentation files for Gnumeric
Group:          Documentation/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
Gnumeric is a spreadsheet application with advanced features and
analytics.  It aims to minimize the cost of transition from proprietary
spreadsheets by offering a familiar look and feature set.  In addition
to read and write support for all versions of Microsoft Excel
(including reading encrypted files), there is also support for many
other formats including:

*Applix 4 and 5 *DIF *Lotus-123 (wk1, wk2, wk3) *OpenOffice.org (Oasis)
*PlanPerfect (pln) *Psion5 *Quattro Pro (wb1, wb2, wb3) *SYLK
*XBase/DB3

Text formats, such as comma or tab separated values, HTML, XHTML, and
Latex, are supported and there are powerful assistants to handle custom
needs.

Gnumeric is part of the GNOME project.

%package devel
Summary:        Spreadsheet Application
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description devel
Gnumeric is a spreadsheet application with advanced features and
analytics.  It aims to minimize the cost of transition from proprietary
spreadsheets by offering a familiar look and feature set.  In addition
to read and write support for all versions of Microsoft Excel
(including reading encrypted files), there is also support for many
other formats including:

*Applix 4 and 5 *DIF *Lotus-123 (wk1, wk2, wk3) *OpenOffice.org (Oasis)
*PlanPerfect (pln) *Psion5 *Quattro Pro (wb1, wb2, wb3) *SYLK
*XBase/DB3

Text formats, such as comma or tab separated values, HTML, XHTML, and
Latex, are supported and there are powerful assistants to handle custom
needs.

Gnumeric is part of the GNOME project.

%lang_package

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
	--disable-static \
#	--enable-pdfdocs \
	%{nil}
%make_build

%install
%make_install
# FIXME: Build as root modifies system!
%find_lang %{name} %{?no_lang_C}
%find_lang %{name}-%{version} %{?no_lang_C} %{name}.lang
%find_lang %{name}-%{version}-functions %{?no_lang_C} %{name}.lang
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_datadir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING COPYING-gpl2 COPYING-gpl3
%doc AUTHORS BEVERAGES BUGS HACKING MAINTAINERS NEWS README ChangeLog
%{_bindir}/*
%{_libdir}/*.so
%dir %{_libdir}/gnumeric
%dir %{_libdir}/gnumeric/*[^t]
%dir %{_libdir}/gnumeric/*/plugins
%dir %{_libdir}/gnumeric/*/plugins/*
%{_libdir}/gnumeric/*/plugins/*/*.so
%{_libdir}/gnumeric/*/plugins/*/*.xml
#%%{_libdir}/gnumeric/*/plugins/*/*.py
%{_libdir}/gnumeric/*/plugins/*/*.pl
#%%{_libdir}/gnumeric/*/plugins/gnome-glossary/glossary-po-header
%{_libdir}/goffice/*/plugins/gnumeric/
%{_datadir}/applications/gnumeric.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnumeric.dialogs.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnumeric.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gnumeric.plugin.gschema.xml
%{_datadir}/gnumeric/
%{_datadir}/icons/hicolor/*/apps/gnumeric.*
%{_datadir}/metainfo/gnumeric.appdata.xml
%{_mandir}/man?/*%{ext_man}

%files doc
%doc %{_datadir}/help/C/%{name}

%files devel
%{_includedir}/libspreadsheet-*/
%{_libdir}/pkgconfig/libspreadsheet-*.pc

%files lang -f %{name}.lang

%changelog
