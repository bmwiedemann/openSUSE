#
# spec file for package nulloy
#
# Copyright (c) 2022 SUSE LLC
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


%define rev 0.9.5
#https://github.com/nulloy/nulloy/archive/refs/tags/0.9.5.tar.gz

Name:           nulloy
Version:        0.9.5
Release:        0
Summary:        Music player with a Waveform Progress Bar
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Players
URL:            http://nulloy.com
Source:         https://github.com/nulloy/nulloy/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Patch0:         reproducible.patch
#Patch1:         nulloy-QPainterPath-patch
BuildRequires:  clang
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
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
BuildRequires:  pkgconfig(libvlc)
BuildRequires:  pkgconfig(taglib)
Recommends:     %{name}-gstreamer
Recommends:     %{name}-taglib
Recommends:     %{name}-vlc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Nulloy is a opensource, simple and clean music player with a Waveform
Progressbar. It is written in C++ using QT.

%package taglib
Summary:        Taglib plugin for %{name}
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description taglib
This package contains the taglib plugin for %{name} - a music player
with a Waveform Progressbar.

%package gstreamer
Summary:        Gstreamer plugin for %{name}
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}
Recommends:     gstreamer-plugins-good

%description gstreamer
This package contains the gstreamer playback plugin for %{name} - a lightweight
music player with a Waveform Progressbar.

%package vlc
Summary:        VLC plugin for %{name}
Group:          Productivity/Multimedia/Sound/Players
Requires:       %{name} = %{version}

%description vlc
This package contains the vlc playback plugin for %{name} - a lightweight
music player with a Waveform Progressbar.

%prep
%setup -qn %{name}-%{rev}
%autopatch -p1

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
	--vlc \
	--libdir "%{_lib}" \
	--gstreamer-tagreader

make %{?_smp_mflags}

%install
CFLAGS="%{optflags}" \
CXXFLAGS="%{optflags}" \
QMAKE=qmake-qt5 \
LRELEASE=lrelease-qt5 \
./configure \
	--no-update-check \
	--prefix %{buildroot}%{_prefix} \
	--vlc \
	--libdir "%{_lib}" \
	--gstreamer-tagreader

%makeinstall
cp -v .tmp/nulloy.svg %{buildroot}%{_datadir}/icons/hicolor/*/apps/
%suse_update_desktop_file %{name}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog THANKS
%license LICENSE.GPL3
%{_bindir}/nulloy
%{_datadir}/applications/nulloy.desktop
%{_datadir}/icons/hicolor/*/apps/nulloy.svg
%{_datadir}/nulloy
%dir %{_libdir}/nulloy
%dir %{_libdir}/nulloy/plugins

%files taglib
%defattr(-,root,root)
%{_libdir}/nulloy/plugins/libplugin_taglib.so

%files gstreamer
%defattr(-,root,root)
%{_libdir}/nulloy/plugins/libplugin_gstreamer.so

%files vlc
%defattr(-,root,root)
%{_libdir}/nulloy/plugins/libplugin_vlc.so

%changelog
