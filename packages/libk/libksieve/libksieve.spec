#
# spec file for package libksieve
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
Name:           libksieve
Version:        19.08.2
Release:        0
Summary:        Sieve and Managesieve support library for KDE PIM
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  karchive-devel
BuildRequires:  kdoctools-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kidentitymanagement-devel >= %{_kapp_version}
BuildRequires:  kio-devel
BuildRequires:  kmailtransport-devel >= %{_kapp_version}
BuildRequires:  kmime-devel
BuildRequires:  knewstuff-devel
BuildRequires:  kpimtextedit-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  libkdepim-devel
BuildRequires:  pimcommon-devel >= %{_kapp_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  pkgconfig(Qt5PrintSupport) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.6.0
BuildRequires:  pkgconfig(Qt5WebEngine) >= 5.6.0
BuildRequires:  pkgconfig(Qt5WebEngineWidgets) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.6.0
BuildRequires:  pkgconfig(Qt5Xml) >= 5.6.0
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64 mips mips64
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
This package contains the libksieve library, which is used to support
the Sieve server-side mail filtering protocol in KDE PIM applications.

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
  %{kf5_find_htmldocs}
%endif

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%package devel
Summary:        Development package for libksieve
License:        LGPL-2.1-or-later
Group:          Development/Libraries/KDE
Requires:       libksieve = %{version}

%description devel
This package contains development headers of libksieve.

%files devel
%license COPYING*
%{_kf5_includedir}/KManageSieve/
%{_kf5_includedir}/KSieveUi/
%{_kf5_includedir}/kmanagesieve/
%{_kf5_includedir}/ksieveui/
%{_kf5_includedir}/libksieve_version.h
%{_kf5_libdir}/cmake/KF5LibKSieve/
%{_kf5_libdir}/libKF5KManageSieve.so
%{_kf5_libdir}/libKF5KSieve.so
%{_kf5_libdir}/libKF5KSieveUi.so
%{_kf5_mkspecsdir}/qt_KManageSieve.pri
%{_kf5_mkspecsdir}/qt_KSieve.pri
%{_kf5_mkspecsdir}/qt_KSieveUi.pri

%files
%license COPYING*
%{_kf5_knsrcfilesdir}/ksieve_script.knsrc
%{_kf5_debugdir}/libksieve.categories
%{_kf5_debugdir}/libksieve.renamecategories
%doc %lang(en) %{_kf5_htmldir}/en/kioslave5/
%{_kf5_libdir}/libKF5KManageSieve.so.*
%{_kf5_libdir}/libKF5KSieve.so.*
%{_kf5_libdir}/libKF5KSieveUi.so.*
%{_kf5_plugindir}/kf5/kio/sieve.so
%{_kf5_servicesdir}/sieve.protocol
%{_kf5_sharedir}/sieve/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
