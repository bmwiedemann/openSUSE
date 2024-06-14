#
# spec file for package libksieve
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
%define kpim6_version 6.1.1

%bcond_without released
Name:           libksieve
Version:        24.05.1
Release:        0
Summary:        Sieve and Managesieve support library for KDE PIM applications
License:        GPL-2.0-only AND LGPL-2.1-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  doxygen
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6NewStuff) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextAddonsWidgets)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextEditTextToSpeech)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KPim6IdentityManagementCore) >= %{kpim6_version}
BuildRequires:  cmake(KPim6IMAP) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Libkdepim) >= %{kpim6_version}
BuildRequires:  cmake(KPim6MailTransport) >= %{kpim6_version}
BuildRequires:  cmake(KPim6Mime) >= %{kpim6_version}
BuildRequires:  cmake(KPim6PimCommon) >= %{kpim6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6WebEngineWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# It can only build on the same platforms as Qt Webengine
ExclusiveArch:  x86_64 %{x86_64} aarch64 riscv64

%description
This package contains the libksieve library, which is used to support
the Sieve server-side mail filtering protocol in KDE PIM applications.

%package -n libksieve6
Summary:        Sieve and Managesieve support library for KDE PIM applications
Requires:       libksieve = %{version}
Obsoletes:      libksieve5 < %{version}
# Before 21.08.3, the libraries were in libksieve
Conflicts:      libksieve < 21.08.3

%description -n libksieve6
This package contains the libksieve library, which is used to support
the Sieve server-side mail filtering protocol in KDE PIM applications.

%package devel
Summary:        Development package for libksieve
Requires:       libksieve6 = %{version}
Requires:       cmake(KF6SyntaxHighlighting) >= %{kf6_version}

%description devel
This package contains development headers of libksieve.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libksieve6

%files
%{_kf6_debugdir}/libksieve.categories
%{_kf6_debugdir}/libksieve.renamecategories
%{_kf6_knsrcfilesdir}/ksieve_script.knsrc
%{_kf6_sharedir}/sieve/

%files -n libksieve6
%license LICENSES/*
%{_kf6_libdir}/libKPim6KManageSieve.so.*
%{_kf6_libdir}/libKPim6KSieve.so.*
%{_kf6_libdir}/libKPim6KSieveCore.so.*
%{_kf6_libdir}/libKPim6KSieveUi.so.*

%files devel
%doc %{_kf6_qchdir}/KPim6KManageSieve.*
%doc %{_kf6_qchdir}/KPim6KSieveCore.*
%doc %{_kf6_qchdir}/KPim6KSieveUi.*
%{_includedir}/KPim6/KManageSieve/
%{_includedir}/KPim6/KSieve/
%{_includedir}/KPim6/KSieveCore/
%{_includedir}/KPim6/KSieveUi/
%{_kf6_cmakedir}/KPim6KManageSieve/
%{_kf6_cmakedir}/KPim6KSieve/
%{_kf6_cmakedir}/KPim6KSieveCore/
%{_kf6_cmakedir}/KPim6KSieveUi/
%{_kf6_libdir}/libKPim6KManageSieve.so
%{_kf6_libdir}/libKPim6KSieve.so
%{_kf6_libdir}/libKPim6KSieveCore.so
%{_kf6_libdir}/libKPim6KSieveUi.so

%files lang -f %{name}.lang

%changelog
