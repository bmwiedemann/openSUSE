#
# spec file for package drkonqi5
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


%define kf5_version 5.58.0
%bcond_without lang
Name:           drkonqi5
# Full Plasma 5 version (e.g. 5.9.1)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.9.1 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Version:        5.20.0
Release:        0
Summary:        Helper for debugging and reporting crashes
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            http://www.kde.org/
Source:         drkonqi-%{version}.tar.xz
%if %{with lang}
Source1:        drkonqi-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
# PATCHES 100-199 are from upstream 5.16 branch
# PATCHES 200-299 and above are from upstream master/5.17+ branch
BuildRequires:  extra-cmake-modules >= 1.8.0
BuildRequires:  cmake(KF5Completion) >= %{kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5Crash) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IdleTime) >= %{kf5_version}
BuildRequires:  cmake(KF5JobWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_version}
BuildRequires:  cmake(KF5Service) >= %{kf5_version}
BuildRequires:  cmake(KF5SyntaxHighlighting) >= %{kf5_version}
BuildRequires:  cmake(KF5Wallet) >= %{kf5_version}
BuildRequires:  cmake(KF5WidgetsAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlRpcClient) >= %{kf5_version}
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.12.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
# We want useful backtraces
Recommends:     gdb
# we want symbol install support
Recommends:     ptools
Recommends:     %{name}-lang

%description
The KDE Crash Handler gives the user feedback if a program has crashed.

%lang_package

%prep
%setup -q -n drkonqi-%{version}

%build
  %cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
  %cmake_build

%install
  %kf5_makeinstall -C build

  %if %{with lang}
    %{kf5_find_lang}
  %endif

  install -p -D -m755 src/doc/examples/installdbgsymbols_suse.sh \
  %{buildroot}%{_kf5_bindir}/installdbgsymbols.sh

%files
%license COPYING
%{_kf5_bindir}/installdbgsymbols.sh
%dir %{_kf5_libdir}/libexec
%{_kf5_libdir}/libexec/drkonqi
%{_kf5_sharedir}/drkonqi/
%{_kf5_applicationsdir}/org.kde.drkonqi.desktop
%{_kf5_debugdir}/drkonqi.categories

%if %{with lang}
%files lang -f %{name}.lang
%endif

%changelog
