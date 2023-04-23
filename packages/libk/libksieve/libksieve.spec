#
# spec file for package libksieve
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


%define soversion 5
%bcond_without released
Name:           libksieve
Version:        23.04.0
Release:        0
Summary:        Sieve and Managesieve support library for KDE PIM applications
License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextEditTextToSpeech)
BuildRequires:  cmake(KPim5IdentityManagement)
BuildRequires:  cmake(KPim5IMAP)
BuildRequires:  cmake(KPim5Libkdepim)
BuildRequires:  cmake(KPim5MailTransport)
BuildRequires:  cmake(KPim5Mime)
BuildRequires:  cmake(KF5PimCommon)
BuildRequires:  cmake(KPim5TextEdit)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64

%description
This package contains the libksieve library, which is used to support
the Sieve server-side mail filtering protocol in KDE PIM applications.

%package -n libksieve%{soversion}
Summary:        Sieve and Managesieve support library for KDE PIM applications
Requires:       libksieve = %{version}
# Before 21.08.3, the libraries were in libksieve
Conflicts:      libksieve < 21.08.3

%description -n libksieve%{soversion}
This package contains the libksieve library, which is used to support
the Sieve server-side mail filtering protocol in KDE PIM applications.

%package devel
Summary:        Development package for libksieve
Requires:       libksieve%{soversion} = %{version}

%description devel
This package contains development headers of libksieve.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%ldconfig_scriptlets -n libksieve%{soversion}

%files
%{_kf5_debugdir}/libksieve.categories
%{_kf5_debugdir}/libksieve.renamecategories
%{_kf5_knsrcfilesdir}/ksieve_script.knsrc
%{_kf5_sharedir}/sieve/

%files -n libksieve%{soversion}
%license LICENSES/*
%{_kf5_libdir}/libKPim5KManageSieve.so.*
%{_kf5_libdir}/libKPim5KSieve.so.*
%{_kf5_libdir}/libKPim5KSieveUi.so.*

%files devel
%dir %{_includedir}/KPim5
%dir %{_includedir}/KF5
%{_includedir}/KF5/KSieve/
%{_includedir}/KPim5/KManageSieve/
%{_includedir}/KPim5/KSieveUi/
%{_kf5_cmakedir}/KF5LibKSieve/
%{_kf5_cmakedir}/KPim5LibKSieve/
%{_kf5_libdir}/libKPim5KManageSieve.so
%{_kf5_libdir}/libKPim5KSieve.so
%{_kf5_libdir}/libKPim5KSieveUi.so
%{_kf5_mkspecsdir}/qt_KManageSieve.pri
%{_kf5_mkspecsdir}/qt_KSieveUi.pri

%files lang -f %{name}.lang

%changelog
