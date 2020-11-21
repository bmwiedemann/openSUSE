#
# spec file for package kinit
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


%define _tar_path 5.75
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kinit
Version:        5.75.0
Release:        0
Summary:        Helper library to speed up start of applications on KDE workspaces
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE fpie.patch  -- add -(f)pie link flags to start_kdeinit target
Patch0:         fpie.patch
# PATCH-FIX-OPENSUSE
Patch1:         0001-Only-move-XAUTHORITY-if-it-s-temporary.patch
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libcap-devel
BuildRequires:  libcap-progs
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Crash) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DBusAddons) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5DocTools) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5I18n) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5KIO) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5Service) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{_kf5_bugfix_version}
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5DBus) >= 5.12.0
BuildRequires:  cmake(Qt5Gui) >= 5.12.0
BuildRequires:  cmake(Qt5Widgets) >= 5.12.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
%if %{with lang}
Recommends:     %{name}-lang = %{version}
%endif

%description
Kdeinit is a process launcher somewhat similar to the famous init used for
booting UNIX.

%package devel
Summary:        Helper library to speed up start of applications on KDE workspaces
Group:          Development/Libraries/KDE
Requires:       extra-cmake-modules

%description devel
Kdeinit is a process launcher somewhat similar to the famous init used for
booting UNIX. Development files.

%lang_package

%prep
%setup -q
%autopatch -p1

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %fdupes %{buildroot}

%if %{with lang}
%find_lang %{name} --with-man --all-name
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%if %{with lang}
%files lang -f %{name}.lang
%endif

%files
%license LICENSES/*
%doc README*
%{_kf5_bindir}/kdeinit5
%{_kf5_bindir}/kdeinit5_shutdown
%{_kf5_bindir}/kdeinit5_wrapper
%{_kf5_bindir}/kwrapper5
%{_kf5_libdir}/libkdeinit5_klauncher.so
%{_kf5_libexecdir}/klauncher
%{_kf5_bindir}/kshell5
%{_kf5_libexecdir}/start_kdeinit
%{_kf5_libexecdir}/start_kdeinit_wrapper
%doc %lang(en) %{_kf5_mandir}/*/kdeinit5.*
%{_kf5_debugdir}/kinit.categories
%{_kf5_debugdir}/*.renamecategories

%files devel
%{_kf5_libdir}/cmake/KF5Init/
%{_kf5_dbusinterfacesdir}/kf5_org.kde.KLauncher.xml

%changelog
