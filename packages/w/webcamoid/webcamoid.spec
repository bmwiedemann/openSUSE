#
# spec file for package webcamoid
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


Name:           webcamoid
Version:        8.7.1
Release:        0
Summary:        Webcam applet for Plasma
License:        GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://webcamoid.github.io/
Source:         https://github.com/hipersayanX/Webcamoid/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf5-filesystem
BuildRequires:  libqt5-linguist
BuildRequires:  perl-Text-Markdown
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.9
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.9
BuildRequires:  pkgconfig(Qt5Qml) >= 5.9
BuildRequires:  pkgconfig(Qt5QuickControls2) >= 5.9
BuildRequires:  pkgconfig(Qt5Svg) >= 5.9
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.9
BuildRequires:  pkgconfig(Qt5Xml) >= 5.9
BuildRequires:  pkgconfig(libavcodec) >= 58.7.100
BuildRequires:  pkgconfig(libavdevice) >= 57.0.0
BuildRequires:  pkgconfig(libavformat) >= 58.0.102
BuildRequires:  pkgconfig(libavutil) >= 56.6.100
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libswscale) >= 5.0.101
BuildRequires:  pkgconfig(libv4l2)
Provides:       plasmoid-webcamoid = %{version}
Obsoletes:      plasmoid-webcamoid < %{version}

%description
Webcam applet for Plasma.

Features:
* Take pictures with the webcam.
* Record videos.
* Manages multiple webcams.
* Play/Stop capture, this saves resources while the applet is not in use.
* Written in C++.
* Qt based software.
* Custom controls for each webcam.
* Popup applet support (you can embed Webcamoid in the panel).
* +50 video effects available.
* Effects with live previews.
* Translated to many languages.
* Stand alone installation mode (use it as a normal program).
* Use custom network and local files as capture devices.
* Capture from desktop.

%package devel
Summary:        Development headers and libraries for Webcamoid
Group:          Development/Libraries/C and C++
Requires:       plasmoid-webcamoid = %{version}

%description devel
Development headers and libraries for Webcamoid.
Avkys library provides a wide range of plugins for audio and
video playing, recording, capture, and processing.

%prep
%setup -q -n webcamoid-%{version}

%build
%qmake5 \
    Webcamoid.pro \
    LIBDIR=%{_libdir} \
    USE3DPARTYLIBS=0 \
    LICENSEDIR=%{_defaultdocdir}/webcamoid \
    INSTALLDEVHEADERS=1 \
    QMAKE_LRELEASE=%{_bindir}/lrelease-qt5 \
    INSTALLQMLDIR=%{_kf5_qmldir}

make %{?_smp_mflags}

# generate help file
Markdown.pl --html4 README.md > README.html

%install
%qmake5_install

%{kf5_post_install}

%fdupes %{buildroot}%{_datadir}

desktop-file-edit %{buildroot}%{_kf5_applicationsdir}/webcamoid.desktop --remove-category=KDE --add-category=Video --add-category=Player

rm -rf %{buildroot}%{_datadir}/licenses/
rm -rf %{buildroot}%{_datadir}/doc/

%post
/sbin/ldconfig
%icon_theme_cache_post
%desktop_database_post

%postun
/sbin/ldconfig
%icon_theme_cache_postun
%desktop_database_postun

%files
%doc AUTHORS ChangeLog README.html THANKS
%license COPYING
%{_bindir}/%{name}
%{_kf5_applicationsdir}/%{name}.desktop
%{_libdir}/libavkys.so.*
%{_libdir}/avkys
%{_libdir}/avkys/*.so
%{_kf5_qmldir}/AkQml
%{_kf5_qmldir}/AkQml/libAkQml.so
%{_kf5_qmldir}/AkQml/qmldir
%{_kf5_mandir}/man1/%{name}.1%{ext_man}
%{_kf5_iconsdir}/hicolor

%files devel
%{_libdir}/libavkys.so
%{_includedir}/avkys
%{_includedir}/avkys/*.h

%changelog
