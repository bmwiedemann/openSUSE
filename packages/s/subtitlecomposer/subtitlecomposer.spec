#
# spec file for package subtitlecomposer
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


Name:           subtitlecomposer
Version:        0.7.1
Release:        0
Summary:        A text-based subtitle editor
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://invent.kde.org/multimedia/subtitlecomposer
Source0:        https://download.kde.org/stable/subtitlecomposer/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/subtitlecomposer/%{name}-%{version}.tar.xz.sig
Source2:        subtitlecomposer.keyring
# PATCH-FIX-UPSTREAM subtitlecomposer-ARM_GLES.patch
Patch0:         subtitlecomposer-ARM_GLES.patch
# PATCH-FIX-UPSTREAM subtitlecomposer-fix_empty_lines_crash.patch
Patch1:         subtitlecomposer-fix_empty_lines_crash.patch
# PATCH-FIX-UPSTREAM Fix build with ffmpeg 5
Patch2:         0001-Fix-compilation-with-ffmpeg5-63.patch
# PATCH-FIX-UPSTREAM Fix video player
Patch3:         0001-VideoPlayer-Fix-usage-of-deprecated-removed-AVCodec-.patch
# PATCH-FIX-UPSTREAM
Patch4:         0001-Use-non-deprecated-ffmpeg-api.patch
BuildRequires:  cmake >= 3.10
BuildRequires:  extra-cmake-modules
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Auth)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Kross)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat) >= 57.83.100
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(openal)
%if 0%{?suse_version} > 1500
%ifnarch ppc64 s390x
BuildRequires:  pkgconfig(pocketsphinx) >= 5
%endif
%endif

%description
A text-based subtitles editor that supports basic operations. It supports
SubRip (SRT), MicroDVD, SSA/ASS, MPlayer, TMPlayer and YouTube captions, and
has speech Recognition using PocketSphinx.

%lang_package

%prep
%autosetup -p1

# We build kross-interpreters without python support anyway, so we can
# remove the python examples to remove an useless dependency on python2
rm src/scripting/examples/*.py

# Fix shebang
sed -i '1s|%{_bindir}/env ruby|%{_bindir}/ruby|' \
       src/scripting/examples/*.rb

# Fix shebang in newly created files
sed -i 's,#!/usr/bin/env ruby,#!%{_bindir}/ruby,' \
       src/scripting/scriptsmanager.cpp

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

# Fix permissions
chmod 755 %{buildroot}%{_kf5_appsdir}/%{name}/scripts/*.rb
# Fix rpmlint error (devel-file-in-non-devel-package) and install header files as doc (since they are installed just for help)
mkdir files_for_doc
cp -a %{buildroot}%{_kf5_appsdir}/%{name}/scripts/api/ files_for_doc/
rm -rf %{buildroot}%{_kf5_appsdir}/%{name}/scripts/api/
# Point to the correct path of the header files directory (doc)
perl -pi -e "s|'api'|'%{_docdir}/subtitlecomposer/api'|" %{buildroot}%{_kf5_appsdir}/%{name}/scripts/README

%find_lang %{name}

%{kf5_post_install}

%files
%doc ChangeLog README.md files_for_doc/api
%license LICENSE
%config(noreplace) %{_kf5_configdir}/%{name}rc
%dir %{_kf5_iconsdir}/hicolor/256x256
%dir %{_kf5_iconsdir}/hicolor/256x256/apps
%{_kf5_applicationsdir}/org.kde.%{name}.desktop
%{_kf5_appsdir}/%{name}/
%{_kf5_appstreamdir}/org.kde.%{name}.appdata.xml
%{_kf5_bindir}/%{name}
%{_kf5_iconsdir}/hicolor/*/*/*
%{_kf5_kxmlguidir}/%{name}/
%{_kf5_sharedir}/mime/packages/%{name}.xml
%if 0%{?suse_version} > 1500
%ifnarch ppc64 s390x
%{_kf5_libdir}/%{name}/
%endif
%endif

%files lang -f %{name}.lang

%changelog
