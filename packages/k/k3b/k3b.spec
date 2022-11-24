#
# spec file for package k3b
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


%bcond_without released
%bcond_without ffmpeg
%bcond_without lame
%bcond_without mad
Name:           k3b
Version:        22.08.3
Release:        0
Summary:        CD/DVD/Blu-ray Burning Application by KDE
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/CD/Record
URL:            https://apps.kde.org/k3b
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
# PATCH-FIX-OPENSUSE
Patch0:         Don-t-suggest-to-install-libburn.patch
# PATCH-FIX-OPENSUSE
Patch1:         0001-Revert-Enable-the-k3b-helper-by-default.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-remove-unnecessary-and-incorrect-version-check.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  flac-devel
BuildRequires:  libdvdread-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libvorbis-devel
BuildRequires:  musepack-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Cddb)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5JobWidgets)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5NotifyConfig)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  pkgconfig(taglib)
Requires:       %{_bindir}/cdrdao
Requires:       %{_bindir}/cdrecord
Requires:       %{_bindir}/mkisofs
Requires:       %{_bindir}/readcd
Requires:       dvd+rw-tools
Requires(post): hicolor-icon-theme
Requires(post): shared-mime-info
Requires(postun): hicolor-icon-theme
Requires(postun): shared-mime-info
Recommends:     %{_bindir}/normalize
Recommends:     %{_bindir}/sox
Recommends:     %{_bindir}/transcode
Recommends:     vcdimager
Provides:       kde4-k3b = 4.2.2.svn951754
Obsoletes:      k3b-codecs
Obsoletes:      kde4-k3b < 4.2.2.svn951754
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
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package contain files needed for development with k3b.

%lang_package

%prep
%autosetup -p1

%build
CXXFLAGS="%{optflags} -fno-strict-aliasing"
%cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
%cmake_build

%install
%kf5_makeinstall -C build
%if %{with released}
  %find_lang %{name} --with-man --all-name
  %{kf5_find_htmldocs}
%endif

%suse_update_desktop_file -r org.kde.k3b Qt KDE AudioVideo DiscBurning

%fdupes -s %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%doc ChangeLog FAQ.txt PERMISSIONS.txt README.txt
%{_kf5_knsrcfilesdir}/k3btheme.knsrc
%dir %{_kf5_plugindir}/k3b_plugins/
%dir %{_kf5_plugindir}/k3b_plugins/kcms
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/kf5/kio/
%dir %{_kf5_servicesdir}/ServiceMenus
%dir %{_kf5_sharedir}/konqsidebartng
%dir %{_kf5_sharedir}/konqsidebartng/virtual_folders
%dir %{_kf5_sharedir}/konqsidebartng/virtual_folders/services
%dir %{_kf5_sharedir}/solid
%dir %{_kf5_sharedir}/solid/actions
%doc %lang(en) %{_kf5_htmldir}/en/k3b/
%{_kf5_applicationsdir}/org.kde.k3b.desktop
%{_kf5_appstreamdir}/org.kde.k3b.appdata.xml
%{_kf5_bindir}/k3b
%{_kf5_iconsdir}/hicolor/*/apps/k3b.*
%{_kf5_iconsdir}/hicolor/*/mimetypes/application-x-k3b.*
%{_kf5_kxmlguidir}/k3b
%{_kf5_libdir}/libk3bdevice.so.*
%{_kf5_libdir}/libk3blib.so.*
%{_kf5_notifydir}/k3b.notifyrc
%{_kf5_plugindir}/k3b_plugins/k3b*.so
%{_kf5_plugindir}/k3b_plugins/kcms/kcm_k3b*.so
%{_kf5_plugindir}/kf5/kio/videodvd.so
%{_kf5_servicesdir}/ServiceMenus/k3b_*.desktop
%{_kf5_servicetypesdir}/k3bplugin.desktop
%{_kf5_sharedir}/k3b
%{_kf5_sharedir}/konqsidebartng/virtual_folders/services/videodvd.desktop
%{_kf5_sharedir}/mime/packages/x-k3b.xml
%{_kf5_sharedir}/solid/actions/k3b_*.desktop

%files devel
%{_includedir}/k3b*.h
%{_kf5_libdir}/libk3bdevice.so
%{_kf5_libdir}/libk3blib.so

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
