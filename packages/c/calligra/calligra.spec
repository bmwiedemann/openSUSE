#
# spec file for package calligra
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_without lang
Name:           calligra
Version:        3.2.1
Release:        0
Summary:        Libraries and Base Files for the Calligra Suite
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND GFDL-1.2-only
Group:          Productivity/Office/Suite
URL:            https://www.calligra.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE
Patch0:         0001-Revert-Chart-Depend-on-KChart-2.7.0.patch
BuildRequires:  OpenEXR-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gsl-devel
BuildRequires:  kf5-filesystem
BuildRequires:  libboost_system-devel
BuildRequires:  libeigen3-devel
BuildRequires:  libetonyek-devel
BuildRequires:  libgit2-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libodfgen-devel
BuildRequires:  libpoppler-qt5-devel
BuildRequires:  libspnav-devel
BuildRequires:  libvisio-devel
BuildRequires:  libwpd-devel
BuildRequires:  libwpg-devel
BuildRequires:  libwps-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  pstoedit
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KChart)
BuildRequires:  cmake(KF5Activities)
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5GuiAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KDELibs4Support)
BuildRequires:  cmake(KF5KHtml)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kross)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Okular5)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickWidgets)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Recommends:     %{name}-doc = %{version}
Recommends:     %{name}-lang = %{version}
Suggests:       calligra-karbon
Suggests:       calligra-plan
Suggests:       calligra-sheets
Suggests:       calligra-stage
Suggests:       calligra-words

%description
The Calligra Suite is a set of applications that allows you to easily complete
your work. The Calligra Suite is unique because not only does it consist of the
normal office applications like word processor (Words) and spreadsheet (Sheets),
but it brings you creative applications as well.

This package contains the base files and libraries for the Suite.

%package gemini
Summary:        Touched-based optimized Calligra Suite
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Office/Suite
Requires:       kirigami2
Requires:       libqt5-qtquickcontrols
# needed for Dropbox login
Recommends:     libqt5-qtwebengine

%description gemini
Touched based optimized Calligra Suite

%package devel
Summary:        The Build Enviroment from Calligra
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}

%description devel
This package contains the build environment needed to compile Calligra
applications.

%package doc
Summary:        Documentation of the Calligra Suite
License:        GFDL-1.2-only
Group:          Documentation/HTML
Requires:       %{name} = %{version}
Obsoletes:      calligra5-doc
BuildArch:      noarch

%description doc
Documentation of the Calligra Office Suite applications.

%package karbon
Summary:        Vector Drawing Application
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
Requires:       pstoedit
Obsoletes:      calligra5-karbon

%description karbon
Karbon is the vector drawing application of the Calligra Suite.

%package sheets
Summary:        Spreadsheet Application
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
Obsoletes:      calligra5-sheets

%description sheets
Sheets is the spreadsheet application of the Calligra Suite.

%package stage
Summary:        Application for Creating Presentations
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
Obsoletes:      calligra5-stage

%description stage
Stage is the presentation application of the Calligra Suite.

%package tools
Summary:        Various tools for the Calligra Suite
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
Obsoletes:      calligra5-tools

%description tools
This package contains various tools for the Calligra Suite.

%package words
Summary:        Word Processor
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
Obsoletes:      %{name}-words-common < %{version}
Provides:       %{name}-words-common = %{version}
Obsoletes:      %{name}-author < %{version}

%description words
Words is the word processor application of the Calligra Suite.

%package extras-converter
Summary:        Commandline tool for conversion
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Office/Suite

%description extras-converter
Commandline tool for conversion between any file formats for which
there is a chain of Calligra import/export filters.

%package extras-okular
Summary:        Plugin for Okular
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Office/Suite
Requires:       %{name} = %{version}
Requires:       okular
Supplements:    (%{name} and okular)

%description extras-okular
Plugins for Okular supporting files in the formats ODP, ODT, MS DOC/DOCX, MS PPT/PPTX, and WPD.

%package extras-dolphin
Summary:        Diverse plugins for Dolphin
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Office/Suite
Supplements:    (%{name} and dolphin)

%description extras-dolphin
Plugin for the Dolphin file properties dialog, displaying the
metadata of files in the ODF formats and a plugin adding a "Print"
action for several formats to the filemanager context menu and
calling the related Calligra programs.

%package extras-filemanagertemplates
Summary:        "Create New" templates for ODF files
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Office/Suite
Supplements:    kio
# the files were in extras-dolphin previously
Conflicts:      %{name}-extras-dolphin < 3.2.0

%description extras-filemanagertemplates
Templates for ODF files that show up in the "Create New" context menu
of KIO-based filemanagers (dolphin, konqueror, krusader, Plasma's folderview)
and the KDE filedialog.

%package lang
Summary:        Translations for the Calligra Suite Applications
License:        LGPL-2.1-or-later
Group:          System/Localization
Requires:       calligra = %{version}
Obsoletes:      calligra-l10n-bs < %{version}
Provides:       calligra-l10n-bs = %{version}
Obsoletes:      calligra-l10n-ca < %{version}
Provides:       calligra-l10n-ca = %{version}
Obsoletes:      calligra-l10n-caValencia < %{version}
Provides:       calligra-l10n-caValencia = %{version}
Obsoletes:      calligra-l10n-cs < %{version}
Provides:       calligra-l10n-cs = %{version}
Obsoletes:      calligra-l10n-da < %{version}
Provides:       calligra-l10n-da = %{version}
Obsoletes:      calligra-l10n-de < %{version}
Provides:       calligra-l10n-de = %{version}
Obsoletes:      calligra-l10n-el < %{version}
Provides:       calligra-l10n-el = %{version}
Obsoletes:      calligra-l10n-en_GB < %{version}
Provides:       calligra-l10n-en_GB = %{version}
Obsoletes:      calligra-l10n-es < %{version}
Provides:       calligra-l10n-es = %{version}
Obsoletes:      calligra-l10n-et < %{version}
Provides:       calligra-l10n-et = %{version}
Obsoletes:      calligra-l10n-fi < %{version}
Provides:       calligra-l10n-fi = %{version}
Obsoletes:      calligra-l10n-fr < %{version}
Provides:       calligra-l10n-fr = %{version}
Obsoletes:      calligra-l10n-gl < %{version}
Provides:       calligra-l10n-gl = %{version}
Obsoletes:      calligra-l10n-hu < %{version}
Provides:       calligra-l10n-hu = %{version}
Obsoletes:      calligra-l10n-it < %{version}
Provides:       calligra-l10n-it = %{version}
Obsoletes:      calligra-l10n-ja < %{version}
Provides:       calligra-l10n-ja = %{version}
Obsoletes:      calligra-l10n-kk < %{version}
Provides:       calligra-l10n-kk = %{version}
Obsoletes:      calligra-l10n-nb < %{version}
Provides:       calligra-l10n-nb = %{version}
Obsoletes:      calligra-l10n-nl < %{version}
Provides:       calligra-l10n-nl = %{version}
Obsoletes:      calligra-l10n-pl < %{version}
Provides:       calligra-l10n-pl = %{version}
Obsoletes:      calligra-l10n-pt < %{version}
Provides:       calligra-l10n-pt = %{version}
Obsoletes:      calligra-l10n-pt_BR < %{version}
Provides:       calligra-l10n-pt_BR = %{version}
Obsoletes:      calligra-l10n-ru < %{version}
Provides:       calligra-l10n-ru = %{version}
Obsoletes:      calligra-l10n-sk < %{version}
Provides:       calligra-l10n-sk = %{version}
Obsoletes:      calligra-l10n-sv < %{version}
Provides:       calligra-l10n-sv = %{version}
Obsoletes:      calligra-l10n-tr < %{version}
Provides:       calligra-l10n-tr = %{version}
Obsoletes:      calligra-l10n-uk < %{version}
Provides:       calligra-l10n-uk = %{version}
Obsoletes:      calligra-l10n-zh_CN < %{version}
Provides:       calligra-l10n-zh_CN = %{version}
Obsoletes:      calligra-l10n-zh_TW < %{version}
Provides:       calligra-l10n-zh_TW = %{version}

%description lang
This package contains application translations for the Calligra Suite

%prep
%setup -q
%if 0%{?suse_version} <= 1500 && 0%{?sle_version} <= 150100
%patch0 -p1
%endif
%if %pkg_vcmp kdoctools < 5.57.0
# older kdoctools versions lack the necessary support for indonesian language causing the build to fail
rm -r po/id/docs/
%endif

%build
%cmake_kf5 -d build
%make_jobs

%install
cd build
%kf5_makeinstall

# Create filelists
%create_subdir_filelist -d data -f main -v devel
%create_subdir_filelist -d devtools -f tools -v devel
%create_subdir_filelist -d extras/calligra -f main -v devel
%create_subdir_filelist -d extras/converter -f converter -v devel
%create_subdir_filelist -d extras/filemanagertemplates -f filemanagertemplates -v devel
%create_subdir_filelist -d extras/okularodpgenerator -f okular -v devel
%create_subdir_filelist -d extras/okularodtgenerator -f okular -v devel
%create_subdir_filelist -d extras/properties -f dolphin -v devel
%create_subdir_filelist -d extras/quickprint -f dolphin -v devel
%create_subdir_filelist -d extras/thumbnail -f main -v devel
%create_subdir_filelist -d filters/karbon -f karbon -v devel
%create_subdir_filelist -d filters/libmso -f main -v devel
%create_subdir_filelist -d filters/libmsooxml -f main -v devel
%create_subdir_filelist -d filters/libodf2 -f main -v devel
%create_subdir_filelist -d filters/libodfreader -f main -v devel
%create_subdir_filelist -d filters/odg -f main -v devel
%create_subdir_filelist -d filters/sheets -f sheets -v devel
%create_subdir_filelist -d filters/stage -f stage -v devel
%create_subdir_filelist -d filters/words -f words -v devel
%create_subdir_filelist -d interfaces -f main -v devel
%create_subdir_filelist -d karbon -v devel
%create_subdir_filelist -d libs -f main -v devel
%create_subdir_filelist -d pics -f main -v devel
%create_subdir_filelist -d plugins -f main -v devel
%create_subdir_filelist -d servicetypes -f main -v devel
%create_subdir_filelist -d sheets -v devel
%create_subdir_filelist -d stage -v devel
%create_subdir_filelist -d words -v devel
%create_subdir_filelist -d gemini -v devel
cd ..

# Remove doc files from filelists (packaged in calligra-doc)
sed -ri s,.*%{_datadir}/doc/kde/HTML/en/.*,, filelists/*

%suse_update_desktop_file -r org.kde.karbon     Qt KDE Graphics VectorGraphics
%suse_update_desktop_file -r org.kde.calligragemini     Qt KDE Graphics RasterGraphics
%suse_update_desktop_file -r org.kde.calligrasheets     Qt KDE Office Spreadsheet
%suse_update_desktop_file -r org.kde.calligrastage      Qt KDE Office Presentation
%suse_update_desktop_file -r org.kde.calligrawords      Qt KDE Office WordProcessor

%post
/sbin/ldconfig
%mime_database_post

%postun
/sbin/ldconfig
%mime_database_postun

%post   gemini -p /sbin/ldconfig
%postun gemini -p /sbin/ldconfig
%post   karbon -p /sbin/ldconfig
%postun karbon -p /sbin/ldconfig
%post   sheets -p /sbin/ldconfig
%postun sheets -p /sbin/ldconfig
%post   stage -p /sbin/ldconfig
%postun stage -p /sbin/ldconfig
%post   tools -p /sbin/ldconfig
%postun tools -p /sbin/ldconfig
%post   words -p /sbin/ldconfig
%postun words -p /sbin/ldconfig
%post   extras-okular -p /sbin/ldconfig
%postun extras-okular -p /sbin/ldconfig

%files -f filelists/main
%license COPYING COPYING.LIB
%doc README
%dir %{_kf5_qmldir}/org/kde
%{_kf5_qmldir}/org/kde/calligra/
%{_datadir}/calligra/
%{_kf5_iconsdir}/hicolor/
%dir %{_kf5_servicesdir}/ServiceMenus
%dir %{_kf5_servicesdir}/ServiceMenus/calligra
%dir %{_kf5_appstreamdir}
%{_kf5_applicationsdir}/calligra.desktop
%dir %{_kf5_plugindir}/calligra
%dir %{_kf5_plugindir}/calligra/devices
%dir %{_kf5_plugindir}/calligra/dockers
%dir %{_kf5_plugindir}/calligra/formatfilters
%dir %{_kf5_plugindir}/calligra/pageapptools
%dir %{_kf5_plugindir}/calligra/shapefiltereffects
%dir %{_kf5_plugindir}/calligra/shapes
%dir %{_kf5_plugindir}/calligra/textediting
%dir %{_kf5_plugindir}/calligra/textinlineobjects
%dir %{_kf5_plugindir}/calligra/tools
%dir %{_kf5_plugindir}/calligra/colorspaces
%dir %{_datadir}/color
%dir %{_datadir}/color/icc
%dir %{_datadir}/color/icc/calligra
%exclude %{_datadir}/calligra_shape_music/fonts/Emmentaler-14.ttf

%files extras-converter -f filelists/converter

%files extras-dolphin -f filelists/dolphin

%files extras-filemanagertemplates -f filelists/filemanagertemplates
%dir %{_datadir}/templates
%dir %{_datadir}/templates/.source

%files extras-okular -f filelists/okular
%{_kf5_applicationsdir}/okular*.desktop
%{_kf5_plugindir}/okular/
%{_kf5_servicesdir}/okular*.desktop

%files devel -f filelists/devel
%{_libdir}/libkookularGenerator_odt.so

%files doc
%license COPYING.DOC
%doc %lang(en) %{_kf5_htmldir}/en/calligra/

%files karbon -f filelists/karbon
%license karbon/COPYING.LIB
%doc karbon/AUTHORS karbon/CHANGES karbon/IDEAS karbon/README karbon/TODO
%exclude %{_kf5_iconsdir}
%{_datadir}/karbon/
%dir %{_kf5_kxmlguidir}/karbon
%exclude %{_datadir}/calligra
%{_kf5_plugindir}/karbon/

%files gemini -f filelists/gemini
%{_kf5_sharedir}/calligragemini/
%exclude %{_kf5_iconsdir}/hicolor
%dir %{_kf5_qmldir}/Calligra
%dir %{_kf5_qmldir}/Calligra/Gemini
%dir %{_kf5_qmldir}/Calligra/Gemini/Dropbox
%dir %{_kf5_qmldir}/Calligra/Gemini/Git
%dir %{_kf5_qmldir}/org

%files sheets -f filelists/sheets
%doc sheets/AUTHORS sheets/CHANGES sheets/README sheets/TODO
%exclude %{_datadir}/calligra
%exclude %{_kf5_iconsdir}
%{_kf5_plugindir}/calligrasheets/
%{_kf5_htmldir}/en/calligrasheets/
%{_datadir}/calligrasheets/
%{_kf5_kxmlguidir}/calligrasheets/

%files stage -f filelists/stage
%doc stage/AUTHORS stage/CHANGES stage/TODO
%exclude %{_datadir}/calligra
%exclude %{_kf5_iconsdir}
%{_kf5_plugindir}/calligrastage/
%dir %{_kf5_plugindir}/calligra/presentationeventactions
%{_kf5_htmldir}/en/calligrastage/
%exclude %{_kf5_applicationsdir}/okular*.desktop
%exclude %{_kf5_plugindir}/okular/
%exclude %{_kf5_servicesdir}/okular*.desktop
%{_datadir}/calligra_shape_music/
%{_datadir}/calligrastage/
%{_kf5_kxmlguidir}/calligrastage/

%files tools -f filelists/tools

%files words -f filelists/words
%{_kf5_applicationsdir}/org.kde.calligrawords.desktop
%{_kf5_bindir}/calligrawords
%{_kf5_libdir}/libkdeinit5_calligrawords.so
%exclude %{_kf5_iconsdir}/hicolor
%{_datadir}/calligrawords/
%{_kf5_kxmlguidir}/calligrawords/
%exclude %{_kf5_applicationsdir}/okular*.desktop
%exclude %{_kf5_plugindir}/okular/
%exclude %{_kf5_servicesdir}/okular*.desktop
%dir %{_kf5_plugindir}/calligra/parts

%if %{with lang}
%files lang
%{_datadir}/locale/
%{_kf5_htmldir}/
%exclude %{_kf5_htmldir}/en/
%endif

%changelog
