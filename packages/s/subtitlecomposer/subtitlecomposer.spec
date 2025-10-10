#
# spec file for package subtitlecomposer
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


# Arbitrary versions, upstream never bumped the default ones
%define kf6_version 6.15
%define qt6_version 6.8
#
Name:           subtitlecomposer
Version:        0.8.2
Release:        0
Summary:        A text-based subtitle editor
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://invent.kde.org/multimedia/subtitlecomposer
Source0:        https://download.kde.org/stable/subtitlecomposer/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/subtitlecomposer/%{name}-%{version}.tar.xz.sig
Source2:        subtitlecomposer.keyring
# PATCH-FIX-UPSTREAM https://invent.kde.org/multimedia/subtitlecomposer/-/merge_requests/48
Patch0:        use-pocketsphinx-5.0.0-api.patch
# PATCH-FIX-UPSTREAM
Patch1:         0001-Include-libavcodec-avfft.h-only-when-AUDIO_VISUALIZA.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Fix-build-with-Qt-6.10.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  qt6-widgets-private-devel >= %{qt6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF6Codecs) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6OpenGLWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat) >= 59.27.100
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(openssl)
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

%build
%cmake_kf6 \
  -DBUILD_WITH_QT6:BOOL=TRUE \
  -DQT_MAJOR_VERSION:STRING=6

%qt6_build

%install
%qt6_install

# Fix rpmlint error (devel-file-in-non-devel-package) and install header files as doc (since they are installed just for help)
mkdir files_for_doc
cp -a %{buildroot}%{_kf6_appsdir}/subtitlecomposer/scripts/api/ files_for_doc/
rm -r %{buildroot}%{_kf6_appsdir}/subtitlecomposer/scripts/api/
# Point to the correct path of the header files directory (doc)
perl -pi -e "s|'api'|'%{_docdir}/subtitlecomposer/api'|" %{buildroot}%{_kf6_appsdir}/subtitlecomposer/scripts/README

%find_lang %{name}

%files
%doc ChangeLog README.md files_for_doc/api
%license LICENSE
%config(noreplace) %{_kf6_configdir}/subtitlecomposerrc
%dir %{_kf6_iconsdir}/hicolor/256x256
%dir %{_kf6_iconsdir}/hicolor/256x256/apps
%{_kf6_applicationsdir}/org.kde.subtitlecomposer.desktop
%{_kf6_appsdir}/subtitlecomposer/
%{_kf6_appstreamdir}/org.kde.subtitlecomposer.appdata.xml
%{_kf6_bindir}/subtitlecomposer
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_sharedir}/mime/packages/subtitlecomposer.xml
%if 0%{?suse_version} > 1500
%ifnarch ppc64 s390x
%{_kf6_libdir}/subtitlecomposer/
%endif
%endif

%files lang -f %{name}.lang

%changelog
