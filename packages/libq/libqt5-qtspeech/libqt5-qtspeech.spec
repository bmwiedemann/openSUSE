#
# spec file for package libqt5-qtspeech
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


%define qt5_snapshot 1
%define libname libQt5TextToSpeech5
%define base_name libqt5
%define real_version 5.15.8
%define so_version 5.15.8
%define tar_version qtspeech-everywhere-src-%{version}
Name:           libqt5-qtspeech
Version:        5.15.8+kde1
Release:        0
Summary:        Qt 5 Speech Addon
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         %{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  libspeechd-devel
BuildRequires:  xz
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif

%description
Qt is a set of libraries for developing applications.

The module enables a Qt application to support accessibility features
such as text-to-speech, which is useful for end-users who are visually
challenged or cannot access the application for whatever reason.

%prep
%autosetup -p1 -n %{tar_version}
%if 0%{?suse_version} < 1330
# work around wrong include directory specification in speech-dispatcher's pkgconfig file in Leap 42.x
sed -i "s|libspeechd.h|speech-dispatcher/libspeechd.h|" src/plugins/tts/speechdispatcher/qtexttospeech_speechd.*
%endif

%package -n %{libname}
Summary:        Qt 5 Speech Addon
Group:          System/Libraries
%requires_eq    libQt5Core5

%description -n %{libname}
Qt is a set of libraries for developing applications.

The module enables a Qt application to support accessibility features
such as text-to-speech, which is useful for end-users who are visually
challenged or cannot access the application for whatever reason.

%package plugin-speechd
Summary:        Qt5 Speech Module - Speech Dispatcher support
Group:          System/Libraries
Requires:       %{libname} = %{version}
Supplements:    (speech-dispatcher and %{libname})

%description plugin-speechd
This plugin adds support for using speech-dispatcher for speech synthesis
with the Qt5 Speech module.

%package devel
Summary:        Development files for the Qt5 Speech library
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}

%description devel
You need this package if you want to compile programs with qtspeech.

%package examples
Summary:        Qt5 Speech examples
Group:          Development/Libraries/X11
License:        BSD-3-Clause

%description examples
Examples for the libqt5-qtspeech module.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5
%make_jobs

%install
%qmake5_install

# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%files -n %{libname}
%license LICENSE.*
%{_libqt5_libdir}/libQt5TextToSpeech.so.*
%dir %{_libqt5_plugindir}/texttospeech/

%files plugin-speechd
%{_libqt5_plugindir}/texttospeech/libqtexttospeech_speechd.so
%dir %{_libqt5_libdir}/cmake/Qt5TextToSpeech/
%{_libqt5_libdir}/cmake/Qt5TextToSpeech/Qt5TextToSpeech_QTextToSpeechPluginSpeechd.cmake

%files devel
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_*.pri
%{_libqt5_includedir}/Qt*
%dir %{_libqt5_libdir}/cmake/Qt5TextToSpeech/
%{_libqt5_libdir}/cmake/Qt5TextToSpeech/Qt5TextToSpeechConfig.cmake
%{_libqt5_libdir}/cmake/Qt5TextToSpeech/Qt5TextToSpeechConfigVersion.cmake
%{_libqt5_libdir}/libQt5TextToSpeech.prl
%{_libqt5_libdir}/libQt5TextToSpeech.so
%{_libqt5_libdir}/pkgconfig/Qt5TextToSpeech.pc

%files examples
%{_libqt5_examplesdir}/

%changelog
