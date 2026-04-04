#
# spec file for package nulloy
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without vlc
%bcond_without taglib

Name:           nulloy
Version:        0.9.9
Release:        0
Summary:        Music player with a Waveform Progress Bar
License:        GPL-3.0-only
URL:            https://nulloy.com/
Source:         https://github.com/nulloy/nulloy/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  ImageMagick-config-7-upstream-open
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig
BuildRequires:  zip
BuildRequires:  pkgconfig(ImageMagick)
BuildRequires:  pkgconfig(Qt5Core) >= 5.6
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
%if %{with vlc}
BuildRequires:  pkgconfig(libvlc)
Recommends:     %{name}-vlc
%endif
%if %{with taglib}
BuildRequires:  pkgconfig(taglib)
Recommends:     %{name}-taglib
%endif
Recommends:     %{name}-gstreamer

%description
Nulloy is a opensource, simple and clean music player with a Waveform
Progressbar. It is written in C++ using QT.

%if %{with taglib}
%package taglib
Summary:        Taglib plugin for %{name}
Requires:       %{name} = %{version}

%description taglib
This package contains the taglib plugin for %{name} - a music player
with a Waveform Progressbar.
%endif

%package gstreamer
Summary:        Gstreamer plugin for %{name}
Requires:       %{name} = %{version}
Recommends:     gstreamer-plugins-good

%description gstreamer
This package contains the gstreamer playback plugin for %{name} - a lightweight
music player with a Waveform Progressbar.

%if %{with vlc}
%package vlc
Summary:        VLC plugin for %{name}
Requires:       %{name} = %{version}

%description vlc
This package contains the vlc playback plugin for %{name} - a lightweight
music player with a Waveform Progressbar.
%endif

%prep
%autosetup -p1

%build
# -Wno-error=return-type
# This is not an autotools configure

CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags} -Wno-error=return-type" \
QMAKE=%{_libdir}/qt5/bin/qmake \
LRELEASE=lrelease-qt5 \
./configure \
	--no-update-check \
	--prefix %{_prefix} \
%if %{with vlc}
	--vlc \
%endif
%if %{with taglib}
	--gstreamer-tagreader \
%else
	--no-taglib \
%endif
	--libdir "%{_lib}"
%make_build

%install
%make_install INSTALL_ROOT="%{buildroot}"

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc AUTHORS ChangeLog README.md THANKS
%license LICENSE.GPL3
%{_bindir}/nulloy
%{_datadir}/applications/nulloy.desktop
%{_datadir}/icons/hicolor/scalable/apps/nulloy.svg
%dir %{_datadir}/nulloy
%{_datadir}/nulloy/i18n
%{_datadir}/nulloy/skins
%dir %{_libdir}/nulloy
%dir %{_libdir}/nulloy/plugins

%if %{with taglib}
%files taglib
%{_libdir}/nulloy/plugins/libplugin_taglib.so
%endif

%files gstreamer
%{_libdir}/nulloy/plugins/libplugin_gstreamer.so

%if %{with vlc}
%files vlc
%{_libdir}/nulloy/plugins/libplugin_vlc.so
%endif

%changelog
