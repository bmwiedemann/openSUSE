#
# spec file for package ksystemstats5
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2021 Fabian Vogt <fabian@ritter-vogt.de>
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
Name:           ksystemstats5
Version:        5.26.5
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Plugin based system monitoring daemon
# Actually (GPL-2.0-only OR GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL) AND CC0-1.0 AND BSD-3-Clause AND BSD-2-Clause
License:        BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/ksystemstats-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/ksystemstats-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.98.0
# TODO: This is now a hard requirement
#%ifnarch s390 s390x
BuildRequires:  libsensors4-devel
#%endif
%if 0%{?suse_version} < 1550
BuildRequires:  gcc10-PIE
BuildRequires:  gcc10-c++
%endif
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KSysGuard) >= %{_plasma5_version}
BuildRequires:  cmake(Qt5Core) >= 5.15
BuildRequires:  cmake(Qt5Test)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libudev)
# For %%check
BuildRequires:  dbus-1
Conflicts:      ksysguard5 < 5.21.80
%{systemd_ordering}

%description
KSystemStats is a daemon that collects statistics about the running system.

%lang_package

%prep
%autosetup -p1 -n ksystemstats-%{version}

%build
%if 0%{?suse_version} < 1550
  export CXX=g++-10
%endif
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON
  %cmake_build

%install
  %kf5_makeinstall -C build
%if %{with released}
  %find_lang ksystemstats_plugins %{name}.lang
%endif

%check
export CTEST_OUTPUT_ON_FAILURE=1
dbus-run-session make %{?_smp_mflags} -C build VERBOSE=1 test

%preun
%{systemd_user_preun plasma-ksystemstats.service}

%post
%{systemd_user_post plasma-ksystemstats.service}

%postun
%{systemd_user_postun plasma-ksystemstats.service}

%files
%license LICENSES/*
%{_kf5_bindir}/ksystemstats
%{_kf5_bindir}/kstatsviewer
%dir %{_kf5_plugindir}/ksystemstats/
%{_kf5_plugindir}/ksystemstats/ksystemstats_plugin_{cpu,disk,gpu,lmsensors,memory,network,osinfo,power}.so
%{_kf5_sharedir}/dbus-1/services/org.kde.ksystemstats.service
%{_userunitdir}/plasma-ksystemstats.service

%if %{with released}
%files lang -f %{name}.lang
%endif

%changelog
