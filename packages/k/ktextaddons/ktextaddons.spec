#
# spec file for package ktextaddons
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define kf6_version 6.11.0
%define qt6_version 6.8.0

%bcond_without released
Name:           ktextaddons
Version:        1.8.0
Release:        0
Summary:        Various text handling addons
License:        LGPL-2.1-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/ktextaddons/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/ktextaddons/%{name}-%{version}.tar.xz.sig
# https://invent.kde.org/sysadmin/release-keyring/-/blob/master/keys/mlaurent@key1.asc?ref_type=heads
Source2:        ktextaddons.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Archive) >= %{kf6_version}
BuildRequires:  cmake(KF6ConfigWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KIO) >= %{kf6_version}
BuildRequires:  cmake(KF6Sonnet) >= %{kf6_version}
BuildRequires:  cmake(KF6SyntaxHighlighting) >= %{kf6_version}
BuildRequires:  cmake(KF6TextWidgets) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6MultimediaWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6Sql) >= %{qt6_version}
BuildRequires:  cmake(Qt6TextToSpeech) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6UiPlugin) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       qt6-sql-sqlite >= %{qt6_version}

%description
KTextAddons provides libraries to work with texts, such as grammar checks,
text to speech and translations.

%lang_package

%package -n libKF6TextAddons1
Summary:        Text addons libraries
Requires:       (ktextaddons = %{version} if kmail)
Recommends:     ktextaddons = %{version}
# translation package was renamed
Obsoletes:      ktextaddons-lang < %{version}

%description -n libKF6TextAddons1
KTextAddons provides libraries to work with texts, such as grammar checks,
text to speech and translations.

%package devel
Summary:        Development files for ktextaddons, a library for handling texts
Requires:       libKF6TextAddons1 = %{version}

%description devel
This package provides development files to use ktextaddons in other applications.

%prep
%autosetup -p1

%build
%cmake_kf6 \
  -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang %{name} --all-name

%ldconfig_scriptlets
%ldconfig_scriptlets -n libKF6TextAddons1

%files
%{_kf6_debugdir}/ktextaddons.categories
%{_kf6_debugdir}/ktextaddons.renamecategories
%{_kf6_plugindir}/kf6/translator/
%{_kf6_plugindir}/kf6/speechtotext/
%{_kf6_plugindir}/kf6/textautogeneratetext/
%{_kf6_libdir}/libtextautogenerateollama.so.*
%{_kf6_libdir}/libtextautogenerategenericnetwork.so.*
%{_kf6_libdir}/libtextautogenerate-cmark-rc-copy.so.*

%files lang -f %{name}.lang

%files -n libKF6TextAddons1
%license LICENSES/*
%{_kf6_libdir}/libKF6TextAutoCorrectionCore.so.*
%{_kf6_libdir}/libKF6TextAutoCorrectionWidgets.so.*
%{_kf6_libdir}/libKF6TextAutoGenerateText.so.*
%{_kf6_libdir}/libKF6TextCustomEditor.so.*
%{_kf6_libdir}/libKF6TextEmoticonsCore.so.*
%{_kf6_libdir}/libKF6TextEmoticonsWidgets.so.*
%{_kf6_libdir}/libKF6TextGrammarCheck.so.*
%{_kf6_libdir}/libKF6TextEditTextToSpeech.so.*
%{_kf6_libdir}/libKF6TextTranslator.so.*
%{_kf6_libdir}/libKF6TextAddonsWidgets.so.*
%{_kf6_libdir}/libKF6TextUtils.so.*
%{_kf6_libdir}/libKF6TextSpeechToText.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Text*.*
%{_kf6_cmakedir}/KF6TextAddonsWidgets/
%{_kf6_cmakedir}/KF6TextAutoCorrectionCore/
%{_kf6_cmakedir}/KF6TextAutoCorrectionWidgets/
%{_kf6_cmakedir}/KF6TextAutoGenerateText/
%{_kf6_cmakedir}/KF6TextCustomEditor/
%{_kf6_cmakedir}/KF6TextEditTextToSpeech/
%{_kf6_cmakedir}/KF6TextEmoticonsCore/
%{_kf6_cmakedir}/KF6TextEmoticonsWidgets/
%{_kf6_cmakedir}/KF6TextGrammarCheck/
%{_kf6_cmakedir}/KF6TextSpeechToText/
%{_kf6_cmakedir}/KF6TextTranslator/
%{_kf6_cmakedir}/KF6TextUtils/
%{_kf6_cmakedir}/textautogenerate-cmark-rc-copy/
%{_kf6_includedir}/TextAddonsWidgets/
%{_kf6_includedir}/TextAutoCorrectionCore/
%{_kf6_includedir}/TextAutoCorrectionWidgets/
%{_kf6_includedir}/TextAutoGenerateText/
%{_kf6_includedir}/TextCustomEditor/
%{_kf6_includedir}/TextEditTextToSpeech/
%{_kf6_includedir}/TextEmoticonsCore/
%{_kf6_includedir}/TextEmoticonsWidgets/
%{_kf6_includedir}/TextGrammarCheck/
%{_kf6_includedir}/TextSpeechToText/
%{_kf6_includedir}/TextTranslator/
%{_kf6_includedir}/TextUtils/
%{_kf6_libdir}/libKF6TextAddonsWidgets.so
%{_kf6_libdir}/libKF6TextAutoCorrectionCore.so
%{_kf6_libdir}/libKF6TextAutoCorrectionWidgets.so
%{_kf6_libdir}/libKF6TextAutoGenerateText.so
%{_kf6_libdir}/libKF6TextCustomEditor.so
%{_kf6_libdir}/libKF6TextEditTextToSpeech.so
%{_kf6_libdir}/libKF6TextEmoticonsCore.so
%{_kf6_libdir}/libKF6TextEmoticonsWidgets.so
%{_kf6_libdir}/libKF6TextGrammarCheck.so
%{_kf6_libdir}/libKF6TextSpeechToText.so
%{_kf6_libdir}/libKF6TextTranslator.so
%{_kf6_libdir}/libKF6TextUtils.so
%{_kf6_plugindir}/designer/textcustomeditor.so
%{_kf6_plugindir}/designer/texttranslatorwidgets6.so
%{_kf6_libdir}/libtextautogenerate-cmark-rc-copy.so

%changelog
