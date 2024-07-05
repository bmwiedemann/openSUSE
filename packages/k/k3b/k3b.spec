#
# spec file for package k3b
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
%bcond_without ffmpeg
%bcond_without lame
%bcond_without mad
Name:           k3b
Version:        24.05.2
Release:        0
Summary:        CD/DVD/Blu-ray Burning Application by KDE
License:        GPL-2.0-or-later
URL:            https://apps.kde.org/k3b
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         Don-t-suggest-to-install-libburn.patch
# PATCH-FIX-OPENSUSE
Patch1:         0001-Revert-Enable-the-k3b-helper-by-default.patch
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libmusicbrainz-devel
BuildRequires:  musepack-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(KCddb6)
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Auth) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6FileMetaData) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6JobWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Notifications) >= %{kf6_version}
BuildRequires:  cmake(KF6NotifyConfig) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
%ifarch x86_64 %{x86_64} aarch64 riscv64
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
%endif
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(vorbis)
Requires:       %{_bindir}/cdrdao
Requires:       %{_bindir}/cdrecord
Requires:       %{_bindir}/mkisofs
Requires:       %{_bindir}/readcd
Requires:       dvd+rw-tools
Requires:       udisks2
Recommends:     %{_bindir}/normalize
Recommends:     %{_bindir}/sox
Recommends:     %{_bindir}/transcode
Recommends:     vcdimager
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
%endif
%if %{with lame}
BuildRequires:  libmp3lame-devel
Requires:       lame
%endif
%if %{with mad}
BuildRequires:  pkgconfig(mad)
%endif

%description
Featuring a graphical interface, k3b provides various
options for burning a CD, DVD, or BD (Blu-ray disc). Various types of
projects are supported, including audio and data, video
projects for DVD and VCD, as well as multi-session and mixed-mode discs. k3b
has the ability to erase re-writeable media, and can perform more
complicated tasks such as audiovisual encoding and decoding.

%package devel
Summary:        Development files for k3b
Requires:       k3b = %{version}

%description devel
This package contain files needed for development with k3b.

%lang_package

%prep
%autosetup -p1

%build
CXXFLAGS="%{optflags} -fno-strict-aliasing"
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name

%fdupes %{buildroot}

%ldconfig_scriptlets

%files
%license LICENSES/*
%doc README.txt
%doc %lang(en) %{_kf6_htmldir}/en/k3b/
%{_kf6_applicationsdir}/org.kde.k3b.desktop
%{_kf6_appstreamdir}/org.kde.k3b.appdata.xml
%{_kf6_bindir}/k3b
%{_kf6_debugdir}/k3b.categories
%{_kf6_iconsdir}/hicolor/*/apps/k3b.*
%{_kf6_iconsdir}/hicolor/*/mimetypes/application-x-k3b.*
%{_kf6_knsrcfilesdir}/k3btheme.knsrc
%{_kf6_libdir}/libk3bdevice.so.*
%{_kf6_libdir}/libk3blib.so.*
%{_kf6_notificationsdir}/k3b.notifyrc
%{_kf6_plugindir}/k3b_plugins/
%{_kf6_plugindir}/kf6/kio/videodvd.so
%{_kf6_sharedir}/k3b/
%dir %{_kf6_sharedir}/kio
%dir %{_kf6_sharedir}/kio/servicemenus
%{_kf6_sharedir}/kio/servicemenus/k3b_create_audio_cd.desktop
%{_kf6_sharedir}/kio/servicemenus/k3b_create_data_project.desktop
%{_kf6_sharedir}/kio/servicemenus/k3b_create_video_cd.desktop
%{_kf6_sharedir}/kio/servicemenus/k3b_write_bin_image.desktop
%{_kf6_sharedir}/kio/servicemenus/k3b_write_iso_image.desktop
# No idea if that still works
%dir %{_kf6_sharedir}/konqsidebartng
%dir %{_kf6_sharedir}/konqsidebartng/virtual_folders
%dir %{_kf6_sharedir}/konqsidebartng/virtual_folders/services
%{_kf6_sharedir}/konqsidebartng/virtual_folders/services/videodvd.desktop
%{_kf6_sharedir}/mime/packages/x-k3b.xml
%dir %{_kf6_sharedir}/solid
%dir %{_kf6_sharedir}/solid/actions
%{_kf6_sharedir}/solid/actions/k3b_*.desktop

%files devel
%{_includedir}/k3b*.h
%{_kf6_libdir}/libk3bdevice.so
%{_kf6_libdir}/libk3blib.so

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/k3b/

%changelog
