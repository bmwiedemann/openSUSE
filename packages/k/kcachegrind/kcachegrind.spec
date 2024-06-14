#
# spec file for package kcachegrind
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
Name:           kcachegrind
Version:        24.05.1
Release:        0
Summary:        Frontend for Cachegrind
License:        GPL-2.0-only AND BSD-4-Clause AND GFDL-1.2-only
URL:            https://apps.kde.org/kcachegrind
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DBusAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6WidgetsAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

%description
KCachegrind is a frontend for cachegrind.

%lang_package

%prep
%autosetup -p1

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
export CXXFLAGS="%{optflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"

%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-html --all-name --with-qt

%suse_update_desktop_file org.kde.kcachegrind Development Profiling

%files
%license LICENSES/*
%doc README
%doc %lang(en) %{_kf6_htmldir}/en/kcachegrind/
%{_kf6_applicationsdir}/org.kde.kcachegrind.desktop
%{_kf6_appstreamdir}/org.kde.kcachegrind.appdata.xml
%{_kf6_bindir}/dprof2calltree
%{_kf6_bindir}/hotshot2calltree
%{_kf6_bindir}/kcachegrind
%{_kf6_bindir}/memprof2calltree
%{_kf6_bindir}/op2calltree
%{_kf6_bindir}/pprof2calltree
%{_kf6_iconsdir}/hicolor/*/*/*
%{_kf6_sharedir}/kcachegrind/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kcachegrind/

%changelog
