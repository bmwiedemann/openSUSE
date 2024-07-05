#
# spec file for package okular
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           okular
Version:        24.05.2
Release:        0
Summary:        Document Viewer
# GPL-3.0+ license used by a runtime plugin
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://okular.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FEATURE-OPENSUSE
Patch1000:      0001-Inform-users-about-the-okular-spectre-package.patch
# Disabled upstream
# BuildRequires:  chmlib-devel
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libdjvulibre-devel
BuildRequires:  libepub-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmarkdown-devel
BuildRequires:  libtiff-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel >= %{qt6_version}
BuildRequires:  cmake(KExiv2Qt6)
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Bookmarks) >= %{kf6_version}
BuildRequires:  cmake(KF6Completion) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6Crash) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Parts) >= %{kf6_version}
BuildRequires:  cmake(KF6Pty) >= %{kf6_version}
BuildRequires:  cmake(KF6Purpose) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6ThreadWeaver) >= %{kf6_version}
BuildRequires:  cmake(KF6Wallet) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(QMobipocket6)
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6TextToSpeech) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(poppler-qt6) >= 22.02.0
BuildRequires:  pkgconfig(zlib)
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
Requires:       kf6-kirigami-imports >= %{kf6_version}
Requires:       kirigami-addons6

%description mobile
Document viewing program; supports document in PDF, PS and
many other formats. This contains the UI targeted at mobile devices with a
touch screen.

%package devel
Summary:        Development files for the Okular document viewer
Requires:       %{name} = %{version}
Requires:       cmake(KF6Config) >= %{kf6_version}
Requires:       cmake(KF6CoreAddons) >= %{kf6_version}
Requires:       cmake(KF6XmlGui) >= %{kf6_version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6PrintSupport) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
Obsoletes:      okular5-devel < %{version}
Provides:       okular5-devel = %{version}

%description devel
Document viewing program; supports document in various formats

%lang_package

%prep
%autosetup -p1 -n okular-%{version}

# No technical reason for requiring cmake 3.22
sed -i 's#3.22#3.20#' CMakeLists.txt

%build
%ifarch ppc64
%define _lto_cflags %{nil}
%endif
%cmake_kf6 -DBUILD_TESTING=OFF -DOKULAR_UI=both
%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --with-man --all-name

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc %lang(en) %{_kf6_htmldir}/en/*/
%doc %{_kf6_mandir}/man1/okular.*
# %%{_kf6_applicationsdir}/okularApplication_chm.desktop
%{_kf6_applicationsdir}/okularApplication_comicbook.desktop
%{_kf6_applicationsdir}/okularApplication_djvu.desktop
%{_kf6_applicationsdir}/okularApplication_dvi.desktop
%{_kf6_applicationsdir}/okularApplication_epub.desktop
%{_kf6_applicationsdir}/okularApplication_fax.desktop
%{_kf6_applicationsdir}/okularApplication_fb.desktop
%{_kf6_applicationsdir}/okularApplication_kimgio.desktop
%{_kf6_applicationsdir}/okularApplication_md.desktop
%{_kf6_applicationsdir}/okularApplication_mobi.desktop
%{_kf6_applicationsdir}/okularApplication_pdf.desktop
%{_kf6_applicationsdir}/okularApplication_tiff.desktop
%{_kf6_applicationsdir}/okularApplication_txt.desktop
%{_kf6_applicationsdir}/okularApplication_xps.desktop
%{_kf6_applicationsdir}/org.kde.okular.desktop
# %%{_kf6_appstreamdir}/org.kde.okular-chm.metainfo.xml
%{_kf6_appstreamdir}/org.kde.okular-comicbook.metainfo.xml
%{_kf6_appstreamdir}/org.kde.okular-djvu.metainfo.xml
%{_kf6_appstreamdir}/org.kde.okular-dvi.metainfo.xml
%{_kf6_appstreamdir}/org.kde.okular-epub.metainfo.xml
%{_kf6_appstreamdir}/org.kde.okular-fax.metainfo.xml
%{_kf6_appstreamdir}/org.kde.okular-fb.metainfo.xml
%{_kf6_appstreamdir}/org.kde.okular-kimgio.metainfo.xml
%{_kf6_appstreamdir}/org.kde.okular-md.metainfo.xml
%{_kf6_appstreamdir}/org.kde.okular-mobipocket.metainfo.xml
%{_kf6_appstreamdir}/org.kde.okular-poppler.metainfo.xml
%{_kf6_appstreamdir}/org.kde.okular-tiff.metainfo.xml
%{_kf6_appstreamdir}/org.kde.okular-txt.metainfo.xml
%{_kf6_appstreamdir}/org.kde.okular-xps.metainfo.xml
%{_kf6_appstreamdir}/org.kde.okular.appdata.xml
%{_kf6_bindir}/okular
%{_kf6_configkcfgdir}/gssettings.kcfg
%{_kf6_configkcfgdir}/okular.kcfg
%{_kf6_configkcfgdir}/okular_core.kcfg
%{_kf6_configkcfgdir}/pdfsettings.kcfg
%{_kf6_debugdir}/okular.categories
%{_kf6_iconsdir}/hicolor/*/*/okular.*
%{_kf6_libdir}/libOkular6Core.so.*
%{_kf6_plugindir}/kf6/parts/okularpart.so
# %%{_kf6_plugindir}/kf6/kio/kio_msits.so
%dir %{_kf6_plugindir}/okular_generators/
# %%{_kf6_plugindir}/okular_generators/okularGenerator_chmlib.so
%{_kf6_plugindir}/okular_generators/okularGenerator_comicbook.so
%{_kf6_plugindir}/okular_generators/okularGenerator_djvu.so
%{_kf6_plugindir}/okular_generators/okularGenerator_dvi.so
%{_kf6_plugindir}/okular_generators/okularGenerator_epub.so
%{_kf6_plugindir}/okular_generators/okularGenerator_fax.so
%{_kf6_plugindir}/okular_generators/okularGenerator_fb.so
%{_kf6_plugindir}/okular_generators/okularGenerator_kimgio.so
%{_kf6_plugindir}/okular_generators/okularGenerator_md.so
%{_kf6_plugindir}/okular_generators/okularGenerator_mobi.so
%{_kf6_plugindir}/okular_generators/okularGenerator_poppler.so
%{_kf6_plugindir}/okular_generators/okularGenerator_tiff.so
%{_kf6_plugindir}/okular_generators/okularGenerator_txt.so
%{_kf6_plugindir}/okular_generators/okularGenerator_xps.so
%{_kf6_sharedir}/kconf_update/okular.upd
%{_kf6_sharedir}/okular/

%files spectre
%{_kf6_applicationsdir}/okularApplication_ghostview.desktop
%{_kf6_appstreamdir}/org.kde.okular-spectre.metainfo.xml
%{_kf6_plugindir}/okular_generators/okularGenerator_ghostview.so

%files mobile
%license LICENSES/*
%{_kf6_bindir}/okularkirigami
%{_kf6_qmldir}/org/kde/okular/
%{_kf6_applicationsdir}/org.kde.okular.kirigami.desktop
# Can use a wildcard here, for non-mobile it's already expanded above
%{_kf6_applicationsdir}/org.kde.mobile.okular_*.desktop
%{_kf6_appstreamdir}/org.kde.okular.kirigami.appdata.xml

%files devel
%{_includedir}/okular/
%{_kf6_cmakedir}/Okular6/
%{_kf6_libdir}/libOkular6Core.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/*/

%changelog
