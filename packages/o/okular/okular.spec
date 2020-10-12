#
# spec file for package okular
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           okular
Version:        20.08.2
Release:        0
Summary:        Document Viewer
# GPL-3.0+ license used by a runtime plugin
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE
Patch1000:      0001-Inform-users-about-the-okular-spectre-package-in-the.patch
BuildRequires:  chmlib-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  freetype2-devel
BuildRequires:  kf5-filesystem
BuildRequires:  libdjvulibre-devel
BuildRequires:  libepub-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmarkdown-devel
BuildRequires:  libpoppler-qt5-devel
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
Recommends:     %{name}-lang
Suggests:       %{name}-spectre
Obsoletes:      okular5 < %{version}
Provides:       okular5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
Document viewing program; supports document in PDF, PS and
many other formats.

%package spectre
Summary:        PostScript support for the Okular document viewer
Group:          Productivity/Office/Other
Requires:       %{name} = %{version}-%{release}

%description spectre
Document viewing program; supports document in PDF, PS and
many other formats. This package contains the plugins required
to display PostScript documents and images.

%package devel
Summary:        Development files for the Okular document viewer
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
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
%cmake_kf5 -d build -- -DBUILD_TESTING=ON -DOKULAR_UI=desktop
%cmake_build

%install
%make_install -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif

rm -rfv %{buildroot}/%{_kf5_applicationsdir}/org.kde.mobile*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_debugdir}/okular.categories
%dir %{_kf5_htmldir}
%dir %{_kf5_htmldir}/en
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
%{_kf5_applicationsdir}/okularApplication_ooo.desktop
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
%{_kf5_appstreamdir}/org.kde.okular-ooo.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-plucker.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-poppler.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-tiff.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-txt.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular-xps.metainfo.xml
%{_kf5_appstreamdir}/org.kde.okular.appdata.xml
%{_kf5_bindir}/okular
%{_kf5_configkcfgdir}/
%{_kf5_iconsdir}/hicolor/*/*/okular.*
%{_kf5_kxmlguidir}/
%{_kf5_libdir}/libOkular5Core.so.*
%dir %{_kf5_plugindir}/okular/
%dir %{_kf5_plugindir}/okular/generators/
%{_kf5_plugindir}/okularpart.so
%{_kf5_plugindir}/kio_msits.so
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
%{_kf5_plugindir}/okular/generators/okularGenerator_ooo.so
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
%{_kf5_servicesdir}/okularOoo.desktop
%{_kf5_servicesdir}/okularPlucker.desktop
%{_kf5_servicesdir}/okularPoppler.desktop
%{_kf5_servicesdir}/okularTiff.desktop
%{_kf5_servicesdir}/okularTxt.desktop
%{_kf5_servicesdir}/okularXps.desktop
%{_kf5_servicesdir}/okular_part.desktop
%{_kf5_servicesdir}/ms-its.protocol
%{_kf5_servicetypesdir}/okularGenerator.desktop
%{_kf5_sharedir}/kconf_update
%{_kf5_sharedir}/okular

%files spectre
%license COPYING*
%{_kf5_applicationsdir}/okularApplication_ghostview.desktop
%{_kf5_appstreamdir}/org.kde.okular-spectre.metainfo.xml
%{_kf5_plugindir}/okular/generators/okularGenerator_ghostview.so
%{_kf5_servicesdir}/okularGhostview.desktop

%files devel
%license COPYING*
%{_kf5_cmakedir}/Okular5/
%{_kf5_libdir}/libOkular5Core.so
%{_kf5_prefix}/include/okular/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
