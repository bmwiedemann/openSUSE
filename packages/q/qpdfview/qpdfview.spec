#
# spec file for package qpdfview
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


%define pver 0.5

Name:           qpdfview
Version:        0.5.0
Release:        0
Summary:        Tabbed document viewer in Qt
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            https://launchpad.net/qpdfview
Source:         https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{pver}.tar.gz
Source1:        https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{pver}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  cups-devel
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(poppler-qt5)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-plugin-pdf
Requires:       libqt5_sql_backend
Recommends:     %{name}-lang
Suggests:       %{name}-plugin-djvu
Suggests:       %{name}-plugin-image
Suggests:       %{name}-plugin-ps

%description
qpdfview uses Poppler for PDF support, libspectre for PS support,
DjVuLibre for DjVu support, CUPS for printing support and the Qt
toolkit for its interface.

Current features include:
 * Outline, properties and thumbnail panes.
 * Scale, rotate and fit.
 * Fullscreen and presentation views.
 * Continuous and multiple-page layouts.
 * Search for text.
 * Configurable tool bars.
 * Configurable keyboard shortcuts.
 * Persistent per-file settings.
 * SyncTeX support.
 * Rudimentary annotation support.
 * Rudimentary form support.
 * Support for PostScript and DjVu documents.

%package plugin-djvu
Summary:        qpdfview plugin: DjVu documents
Group:          Productivity/Office/Other
Requires:       %{name}

%description plugin-djvu
This plugin is required to read DjVu documents
(*.djvu files) with the qpdfview document viewer.

%package plugin-image
Summary:        qpdfview plugin: Image files
Group:          Productivity/Office/Other
Requires:       %{name}

%description plugin-image
This plugin is required to read Image files
(*.tiff files) with the qpdfview document viewer.

%package plugin-pdf
Summary:        qpdfview plugin: PDF documents
Group:          Productivity/Office/Other
Requires:       %{name}

%description plugin-pdf
This plugin is required to read PDF documents
(*.pdf files) with the qpdfview document viewer.

%package plugin-ps
Summary:        qpdfview plugin: PostScript documents
Group:          Productivity/Office/Other
Requires:       %{name}

%description plugin-ps
This plugin is required to read PostScript documents
(*.ps files) with the qpdfview document viewer.

%lang_package

%prep
%autosetup -p1 -n %{name}-%{pver}

%build
%global _libqt5_qmake %{_libqt5_qmake} -makefile %{name}.pro
%{_libqt5_bindir}/lrelease translations/*.ts
%qmake5 PLUGIN_INSTALL_PATH=%{_libdir}/%{name}
%make_build

%install
%qmake5_install
%fdupes %{buildroot}
%find_lang %{name} --with-qt

%if 0%{?suse_version} && 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc CHANGES CONTRIBUTORS README TODO
%{_bindir}/%{name}
%dir %{_libdir}/%{name}/
%dir %{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_datadir}/metainfo/qpdfview.appdata.xml

%files plugin-djvu
%{_libdir}/%{name}/libqpdfview_djvu.so

%files plugin-image
%{_libdir}/%{name}/libqpdfview_image.so

%files plugin-pdf
%{_libdir}/%{name}/libqpdfview_pdf.so

%files plugin-ps
%{_libdir}/%{name}/libqpdfview_ps.so

%files lang -f %{name}.lang
%lang(ast) %{_datadir}/%{name}/%{name}_ast.qm
%lang(nds) %{_datadir}/%{name}/%{name}_nds.qm
%if 0%{?sle_version} < 159000
%lang(ber) %{_datadir}/%{name}/%{name}_ber.qm
%lang(rue) %{_datadir}/%{name}/%{name}_rue.qm
%lang(zgh) %{_datadir}/%{name}/%{name}_zgh.qm
%endif
%doc %{_datadir}/%{name}/help*.html

%changelog
