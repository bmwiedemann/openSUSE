#
# spec file for package ktextaddons
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


%define sonum   1
%bcond_without released
Name:           ktextaddons
Version:        1.1.0
Release:        0
Summary:        Various text handling addons
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/ktextaddons/%{name}-%{version}.tar.xz
%if %{with released}
# GPG key ACC97558AFEF335FA6455C7F02214E6A62A281BC cannot be found
# Source1:         https://download.kde.org/stable/ktextaddons/%%{name}-%%{version}.tar.xz.sig
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(Qt5Core) >= 5.15.2
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5Network) >= 5.15.2
BuildRequires:  cmake(Qt5TextToSpeech) >= 5.15.2
BuildRequires:  cmake(Qt5UiPlugin) >= 5.15.2
BuildRequires:  cmake(Qt5Widgets) >= 5.15.2

%description
KTextAddons provides libraries to work with texts, such as grammar checks,
text to speech, or translations.

%lang_package

%package -n libKF5TextAutoCorrection%{sonum}
Summary:        Text autocorrection library
License:        LGPL-2.1-or-later
Requires:       %{name} = %{version}

%description -n libKF5TextAutoCorrection%{sonum}
This package provides a library for text autocorrection.

%package -n libKF5TextEditTextToSpeech%{sonum}
Summary:        Text to speech functionality
License:        LGPL-2.0-or-later AND GPL-2.0-or-later

%description  -n libKF5TextEditTextToSpeech%{sonum}
This package provides a library for text to speech functionality.

%package -n libKF5TextGrammarCheck%{sonum}
Summary:        Text grammar checking
License:        LGPL-2.1-or-later
Requires:       %{name} = %{version}

%description -n libKF5TextGrammarCheck%{sonum}
This package provides a library for automated grammar checking.

%package -n libKF5TextTranslator%{sonum}
Summary:        Text translation library
License:        LGPL-2.1-or-later
Requires:       %{name} = %{version}

%description -n libKF5TextTranslator%{sonum}
This package provides a library for automated text translation.

%package devel
Summary:        Development files for ktextaddons, a library for handling texts
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
Requires:       libKF5TextAutoCorrection%{sonum} = %{version}
Requires:       libKF5TextEditTextToSpeech%{sonum} = %{version}
Requires:       libKF5TextGrammarCheck%{sonum} = %{version}
Requires:       libKF5TextTranslator%{sonum} = %{version}
%requires_eq    cmake(Qt5Core)
%requires_eq    cmake(Qt5Gui)
%requires_eq    cmake(Qt5Network)

%description devel
This package provides development files to use ktextaddons in other applications.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%fdupes %{buildroot}

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libKF5TextAutoCorrection%{sonum}
%ldconfig_scriptlets -n libKF5TextEditTextToSpeech%{sonum}
%ldconfig_scriptlets -n libKF5TextGrammarCheck%{sonum}
%ldconfig_scriptlets -n libKF5TextTranslator%{sonum}

%files
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/kf5/translator/
%{_kf5_plugindir}/kf5/translator/*.so

%files lang -f %{name}.lang

%files -n libKF5TextAutoCorrection%{sonum}
%{_kf5_libdir}/libKF5TextAutoCorrection.so.%{sonum}
%{_kf5_libdir}/libKF5TextAutoCorrection.so.%{sonum}.*

%files -n libKF5TextGrammarCheck%{sonum}
%{_kf5_libdir}/libKF5TextGrammarCheck.so.%{sonum}
%{_kf5_libdir}/libKF5TextGrammarCheck.so.%{sonum}.*

%files -n libKF5TextEditTextToSpeech%{sonum}
%{_kf5_libdir}/libKF5TextEditTextToSpeech.so.%{sonum}
%{_kf5_libdir}/libKF5TextEditTextToSpeech.so.%{sonum}.*

%files -n libKF5TextTranslator%{sonum}
%{_kf5_libdir}/libKF5TextTranslator.so.%{sonum}
%{_kf5_libdir}/libKF5TextTranslator.so.%{sonum}.*

%files devel
%{_kf5_cmakedir}/KF5TextAutoCorrection
%{_kf5_cmakedir}/KF5TextEditTextToSpeech
%{_kf5_cmakedir}/KF5TextGrammarCheck
%{_kf5_cmakedir}/KF5TextTranslator
%{_kf5_includedir}/TextAutoCorrection/
%{_kf5_includedir}/TextEditTextToSpeech/
%{_kf5_includedir}/TextGrammarCheck/
%{_kf5_includedir}/TextTranslator/
%{_kf5_libdir}/libKF5TextAutoCorrection.so
%{_kf5_libdir}/libKF5TextEditTextToSpeech.so
%{_kf5_libdir}/libKF5TextGrammarCheck.so
%{_kf5_libdir}/libKF5TextTranslator.so
%{_kf5_mkspecsdir}/qt_*.pri
%dir %{_kf5_plugindir}/designer/
%{_kf5_plugindir}/designer/texttranslatorwidgets5.so

%changelog
