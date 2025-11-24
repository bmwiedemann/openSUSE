#
# spec file for package qpdfview
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


%define pver 0.5

Name:           qpdfview
Version:        0.5.0
Release:        0
Summary:        Tabbed document viewer in Qt
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            https://launchpad.net/qpdfview
Source:         %{url}/trunk/%{version}/+download/%{name}-%{pver}.tar.gz
Source1:        %{url}/trunk/%{version}/+download/%{name}-%{pver}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
%if 0%{?suse_version} >= 1699
BuildRequires:  pkgconfig(cups)
%else
BuildRequires:  cups-devel
%endif
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(poppler-qt6)
BuildRequires:  pkgconfig(synctex)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-plugin-pdf
Requires:       qt6-sql-sqlite
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
%{_qt6_bindir}/lrelease %{name}.pro
%qmake6 %{name}.pro \
    PLUGIN_INSTALL_PATH=%{_libdir}/%{name}
%qmake6_build

%install
%qmake6_install
%fdupes %{buildroot}
%find_lang %{name} --with-qt

%files
%license COPYING
%doc CHANGES CONTRIBUTORS README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_datadir}/metainfo/%{name}.appdata.xml
%dir %{_datadir}/%{name}
%doc %{_datadir}/%{name}/help.html

%files plugin-djvu
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}_djvu.so

%files plugin-image
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}_image.so

%files plugin-pdf
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}_pdf.so

%files plugin-ps
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}_ps.so

%files lang -f %{name}.lang
%if 0%{?sle_version}
%{_datadir}/%{name}/%{name}_???.qm
%endif
%doc %{_datadir}/%{name}/help_*.html

%changelog
