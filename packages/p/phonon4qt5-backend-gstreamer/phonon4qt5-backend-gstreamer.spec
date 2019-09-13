#
# spec file for package phonon4qt5-backend-gstreamer
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define filename phonon-backend-gstreamer
%define _phonon4qt5_version 4.10.60
%bcond_without lang
Name:           phonon4qt5-backend-gstreamer
Version:        4.10.0
Release:        0
Summary:        Phonon Multimedia Platform Abstraction
License:        LGPL-2.1-only OR LGPL-3.0-only
Group:          System/GUI/KDE
URL:            https://phonon.kde.org/
Source:         https://download.kde.org/stable/phonon/%{filename}/%{version}/%{filename}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  kf5-filesystem
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  cmake(Phonon4Qt5) >= %{_phonon4qt5_version}
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
Requires:       libphonon4qt5 >= %{_phonon4qt5_version}
Supplements:    packageand(gstreamer-plugins-base:phonon4qt5)
# the icons were in phonon-backend-gstreamer previously
Conflicts:      phonon-backend-gstreamer < 4.9.1
Obsoletes:      phonon4qt5-backend-gstreamer-0_10 < %{version}
Provides:       phonon4qt5-backend = %{version}
Provides:       phonon4qt5-backend-gstreamer = %{version}
Provides:       phonon4qt5-backend-gstreamer-0_10 = %{version}

%description
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%lang_package

%prep
%setup -q -n phonon-backend-gstreamer-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build

%if %{with lang}
  %find_lang phonon_gstreamer %{name}.lang --with-qt
%endif

%files
%license COPYING*
%dir %{_kf5_plugindir}/phonon4qt5_backend
%{_kf5_plugindir}/phonon4qt5_backend/phonon_gstreamer.so
%{_kf5_iconsdir}/hicolor/*/apps/phonon-gstreamer.*

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
