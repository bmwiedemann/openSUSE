#
# spec file for package pulseaudio-qt
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%flavor" == "qt6"
%define pkg_suffix 6
%define qt6 1
%define kf6_version 6.0.0
%define qt6_version 6.6.0
%define library_name libKF6PulseAudioQt5
%else
ExclusiveArch: do_not_build
%endif

%define rname pulseaudio-qt
%bcond_without released
Name:           pulseaudio-qt%{?pkg_suffix}
Version:        1.7.0
Release:        0
Summary:        Qt bindings for PulseAudio
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/pulseaudio-qt/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/pulseaudio-qt/%{rname}-%{version}.tar.xz.sig
Source2:        pulseaudio-qt.keyring
%endif
BuildRequires:  pkgconfig
%if 0%{?qt6}
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
%endif
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpulse)

%description
Pulseaudio-Qt is a library providing Qt bindings to PulseAudio.

%package -n %{library_name}
Summary:        Qt bindings for PulseAudio

%description -n %{library_name}
Pulseaudio-Qt is a library providing Qt bindings to PulseAudio.

%package devel
Summary:        Development files for pulseaudio-qt, Qt bindings for PulseAudio
Requires:       %{library_name} = %{version}
%if 0%{?qt6}
Requires:       cmake(Qt6Core) >= %{qt6_version}
%endif

%description devel
Development files for pulseaudio-qt, a library providing Qt bindings to
PulseAudio.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%if 0%{?qt6}
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE
%kf6_build
%endif

%install
%if 0%{?qt6}
%kf6_install
%endif

%ldconfig_scriptlets -n %{library_name}

%files -n %{library_name}
%license LICENSES/*
%if 0%{?qt6}
%{_kf6_libdir}/libKF6PulseAudioQt.so.*
%endif

%files devel
%if 0%{?qt6}
%doc %{_kf6_qchdir}/KF6PulseAudioQt.*
%{_kf6_cmakedir}/KF6PulseAudioQt/
%{_kf6_includedir}/KF6PulseAudioQt/
%{_kf6_includedir}/pulseaudioqt_version.h
%{_kf6_libdir}/libKF6PulseAudioQt.so
%{_kf6_pkgconfigdir}/KF6PulseAudioQt.pc
%endif

%changelog
