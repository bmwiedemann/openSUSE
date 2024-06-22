#
# spec file for package ksystemstats6
#
# Copyright (c) 2024 SUSE LLC
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


%define kf6_version 6.2.0
%define qt6_version 6.6.0

%define rname ksystemstats
%bcond_without released
Name:           ksystemstats6
Version:        6.1.0
Release:        0
# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Plugin based system monitoring daemon
# Actually (GPL-2.0-only OR GPL-3.0-only OR LicenseRef-KDE-Accepted-GPL) AND CC0-1.0 AND BSD-3-Clause AND BSD-2-Clause
License:        BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 3.16
# For %%check
BuildRequires:  dbus-1
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  libsensors4-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NetworkManagerQt) >= %{kf6_version}
BuildRequires:  cmake(KF6Solid) >= %{kf6_version}
BuildRequires:  cmake(KSysGuard) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libudev)
Conflicts:      ksysguard5 < 5.21.80
Provides:       ksystemstats5 = %{version}
Obsoletes:      ksystemstats5 < %{version}
Obsoletes:      ksystemstats5-lang < %{version}
%systemd_ordering

%description
KSystemStats is a daemon that collects statistics about the running system.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_TESTING:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang ksystemstats_plugins %{name}.lang

%check
dbus-run-session cmake --build %{__kf6_builddir} -t test

%preun
%{systemd_user_preun plasma-ksystemstats.service}

%post
%{systemd_user_post plasma-ksystemstats.service}

%postun
%{systemd_user_postun plasma-ksystemstats.service}

%files
%license LICENSES/*
%{_kf6_bindir}/ksystemstats
%{_kf6_bindir}/kstatsviewer
%dir %{_kf6_plugindir}/ksystemstats/
%{_kf6_plugindir}/ksystemstats/ksystemstats_plugin_{cpu,disk,gpu,lmsensors,memory,network,osinfo,power}.so
%{_kf6_sharedir}/dbus-1/services/org.kde.ksystemstats1.service
%{_userunitdir}/plasma-ksystemstats.service

%files lang -f %{name}.lang

%changelog
