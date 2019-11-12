#
# spec file for package kaccounts-integration
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kaccounts-integration
Version:        19.08.3
Release:        0
Summary:        KDE Accounts Providers
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kcmutils-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdeclarative-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kwallet-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  libaccounts-glib-devel
BuildRequires:  libaccounts-qt5-devel
BuildRequires:  libsignon-qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
Recommends:     %{name}-lang
Recommends:     kaccounts-providers

%description
Small system to administer web accounts for the sites
and services across the KDE desktop, including: Google,
Facebook, Owncloud, IMAP, Jabber and others.

%package -n libkaccounts1
Summary:        KDE Accounts Providers - System Library
Group:          System/Libraries
Recommends:     %{name}

%description -n libkaccounts1
Small system to administer web accounts for the sites
and services across the KDE desktop, including: Google,
Facebook, Owncloud, IMAP, Jabber and others.

%package devel
Summary:        KDE Accounts Providers - Development Files
Group:          Development/Libraries/KDE
Requires:       kcoreaddons-devel
Requires:       libaccounts-qt5-devel
Requires:       libkaccounts1 = %{version}
Requires:       libsignon-qt5-devel
Requires:       pkgconfig(Qt5Core) >= 5.2.0
Requires:       pkgconfig(libaccounts-glib)

%description devel
Small system to administer web accounts for the sites
and services across the KDE desktop, including: Google,
Facebook, Owncloud, IMAP, Jabber and others. Devel files.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post   -n libkaccounts1 -p /sbin/ldconfig
%postun -n libkaccounts1 -p /sbin/ldconfig

%files
%license COPYING*
%{_kf5_plugindir}/
%{_kf5_qmldir}/
%{_kf5_servicesdir}/

%files -n libkaccounts1
%license COPYING*
%{_kf5_libdir}/libkaccounts.so.*

%files devel
%license COPYING*
%{_kf5_cmakedir}/KAccounts/
%{_kf5_libdir}/libkaccounts.so
%{_kf5_prefix}/include/KAccounts/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
