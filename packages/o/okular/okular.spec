#
# spec file for package okular
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


# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           okular
Version:        22.12.1
Release:        0
Summary:        Document Viewer
# GPL-3.0+ license used by a runtime plugin
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://okular.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
%if 0
# PATCH-FEATURE-OPENSUSE
# PATCH-NEEDS-REBASE DISABLED as of 2021-04-10: needs rework (underlying code changed)
Patch1000:      0001-Inform-users-about-the-okular-spectre-package-in-the.patch
%endif
BuildRequires:  chmlib-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  freetype2-devel
BuildRequires:  kf5-filesystem
BuildRequires:  libdjvulibre-devel
BuildRequires:  libepub-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmarkdown-devel
BuildRequires:  libpoppler-qt5-devel
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  libqca-qt5-devel
BuildRequires:  libspectre-devel
BuildRequires:  libtiff-devel
BuildRequires:  libzip-devel
BuildRequires:  zlib-devel
BuildRequires:  cmake(KF5Activities)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Bookmarks)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5JS)
BuildRequires:  cmake(KF5KExiv2)
BuildRequires:  cmake(KF5KHtml)
BuildRequires:  cmake(KF5Kirigami2)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Parts)
BuildRequires:  cmake(KF5Pty)
BuildRequires:  cmake(KF5Purpose)
BuildRequires:  cmake(KF5ThreadWeaver)
BuildRequires:  cmake(KF5Wallet)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Phonon4Qt5)
BuildRequires:  cmake(QMobipocket)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5TextToSpeech)
BuildRequires:  cmake(Qt5Widgets)
Suggests:       %{name}-spectre
Obsoletes:      okular5 < %{version}
Provides:       okular5 = %{version}

%description
Document viewing program; supports document in PDF, PS and
many other formats.

%package spectre
Summary:        PostScript support for the Okular document viewer
Requires:       %{name} = %{version}-%{release}

%description spectre
Document viewing program; supports document in PDF, PS and
many other formats. This package contains the plugins required
to display PostScript documents and images.

%package mobile
Summary:        Document Viewer, Mobile UI
Requires:       %{name} = %{version}-%{release}
Requires:       kirigami2

%description mobile
Document viewing program; supports document in PDF, PS and
many other formats. This contains the UI targeted at mobile devices with a
touch screen.

%package devel
Summary:        Development files for the Okular document viewer
Requires:       %{name} = %{version}
%requires_eq    libQt5Core-private-headers-devel
Requires:       cmake(KF5Config)
Requires:       cmake(KF5CoreAddons)
Requires:       cmake(KF5XmlGui)
Requires:       cmake(Qt5Core)
Requires:       cmake(Qt5PrintSupport)
Requires:       cmake(Qt5Widgets)
Obsoletes:      okular5-devel < %{version}
Provides:       okular5-devel = %{version}

%description devel
Document viewing program; supports document in various formats

%lang_package

%prep
%autosetup -p1 -n okular-%{version}

%build
%ifarch ppc64
%define _lto_cflags %{nil}
%endif
%cmake_kf5 -d build -- -DBUILD_TESTING=OFF -DOKULAR_UI=both
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name
%{kf5_find_htmldocs}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc %lang(en) %{_kf5_htmldir}/en/*/
%doc %{_kf5_mandir}/man1/okular.*
%{_kf5_applicationsdir}/okularApplication_chm.desktop
%{_kf5_applicationsdir}/okularApplication_comicbook.desktop
%{_kf5_applicationsdir}/okularApplication_djvu.desktop
%{_kf5_applicationsdir}/okularApplication_dvi.desktop
%{_kf5_applicationsdir}/okularApplication_epub.desktop
%{_kf5_applicationsdir}/okularApplication_fax.desktop
%{_kf5_applicationsdir}/okularApplication_fb.desktop
%{_kf5_applicationsdir}/okularApplication_kimgio.desktop
%{_kf5_applicationsdir}/okularApplication_md.desktop
%{_kf5_applicationsdir}/okularApplication_mobi.desktop
%{_kf5_applicationsdir}/okularApplication_pdf.desktop
%{_kf5_applicationsdir}/okularApplication_plucker.desktop
%{_kf5_applicationsdir}/okularApplication_tiff.desktop
%{_kf5_applicationsdir}/okularApplication_txt.desktop
%{_kf5_applicationsdir}/okularApplication_xps.desktop
%{_kf5_applicationsdir}/org.kde.okular.desktop
%{_kf5_appstreamdir}/org.kde.okular-chm.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-comicbook.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-djvu.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-dvi.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-epub.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-fax.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-fb.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-kimgio.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-md.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-mobipocket.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-plucker.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-poppler.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-tiff.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-txt.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-xps.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular.appdata.xml
%{_kf5_bindir}/okular
%{_kf5_configkcfgdir}/gssettings.kcfg
%{_kf5_configkcfgdir}/okular*.kcfg
%{_kf5_configkcfgdir}/pdfsettings.kcfg
%{_kf5_debugdir}/okular.categories
%{_kf5_iconsdir}/hicolor/*/*/okular.*
%{_kf5_kxmlguidir}/okular/
%{_kf5_libdir}/libOkular5Core.so.*
%dir %{_kf5_plugindir}/okular/
%dir %{_kf5_plugindir}/okular/generators/
%{_kf5_plugindir}/okularpart.so
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/kf5/kio/
%{_kf5_plugindir}/kf5/kio/kio_msits.so
%{_kf5_plugindir}/okular/generators/okularGenerator_chmlib.so
%{_kf5_plugindir}/okular/generators/okularGenerator_comicbook.so
%{_kf5_plugindir}/okular/generators/okularGenerator_djvu.so
%{_kf5_plugindir}/okular/generators/okularGenerator_dvi.so
%{_kf5_plugindir}/okular/generators/okularGenerator_epub.so
%{_kf5_plugindir}/okular/generators/okularGenerator_fax.so
%{_kf5_plugindir}/okular/generators/okularGenerator_fb.so
%{_kf5_plugindir}/okular/generators/okularGenerator_kimgio.so
%{_kf5_plugindir}/okular/generators/okularGenerator_md.so
%{_kf5_plugindir}/okular/generators/okularGenerator_mobi.so
%{_kf5_plugindir}/okular/generators/okularGenerator_plucker.so
%{_kf5_plugindir}/okular/generators/okularGenerator_poppler.so
%{_kf5_plugindir}/okular/generators/okularGenerator_tiff.so
%{_kf5_plugindir}/okular/generators/okularGenerator_txt.so
%{_kf5_plugindir}/okular/generators/okularGenerator_xps.so
%{_kf5_servicesdir}/okularChm.desktop
%{_kf5_servicesdir}/okularComicbook.desktop
%{_kf5_servicesdir}/okularDjvu.desktop
%{_kf5_servicesdir}/okularDvi.desktop
%{_kf5_servicesdir}/okularEPub.desktop
%{_kf5_servicesdir}/okularFax.desktop
%{_kf5_servicesdir}/okularFb.desktop
%{_kf5_servicesdir}/okularKimgio.desktop
%{_kf5_servicesdir}/okularMd.desktop
%{_kf5_servicesdir}/okularMobi.desktop
%{_kf5_servicesdir}/okularPlucker.desktop
%{_kf5_servicesdir}/okularPoppler.desktop
%{_kf5_servicesdir}/okularTiff.desktop
%{_kf5_servicesdir}/okularTxt.desktop
%{_kf5_servicesdir}/okularXps.desktop
%{_kf5_servicesdir}/okular_part.desktop
%{_kf5_servicetypesdir}/okularGenerator.desktop
%{_kf5_sharedir}/kconf_update
%{_kf5_sharedir}/okular/

%files spectre
%{_kf5_applicationsdir}/okularApplication_ghostview.desktop
%{_kf5_appstreamdir}/org.kde.okular-spectre.metainfo.xml
%{_kf5_plugindir}/okular/generators/okularGenerator_ghostview.so
%{_kf5_servicesdir}/okularGhostview.desktop

%files mobile
%license LICENSES/*
%{_kf5_bindir}/okularkirigami
%dir %{_kf5_qmldir}/org/
%dir %{_kf5_qmldir}/org/kde/
%{_kf5_qmldir}/org/kde/okular/
%{_kf5_applicationsdir}/org.kde.okular.kirigami.desktop
# Can use a wildcard here, for non-mobile it's already expanded above
%{_kf5_applicationsdir}/org.kde.mobile.okular_*.desktop
%{_kf5_appstreamdir}/org.kde.okular.kirigami.appdata.xml

%files devel
%{_kf5_cmakedir}/Okular5/
%{_kf5_libdir}/libOkular5Core.so
%{_kf5_prefix}/include/okular/

%files lang -f %{name}.lang

%changelog
