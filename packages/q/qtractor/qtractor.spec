#
# spec file for package qtractor
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


# Qt6 is the default framework in 0.9.29
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
%define qt6 1
%endif
Name:           qtractor
Version:        0.9.31
Release:        0
Summary:        An Audio/MIDI multi-track sequencer
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            https://qtractor.org/
Source0:        https://download.sourceforge.net/qtractor/qtractor-%{version}.tar.gz
BuildRequires:  alsa-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  dssi-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  ladspa-devel
BuildRequires:  libjack-devel
BuildRequires:  liblo-devel
BuildRequires:  librubberband-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel >= 1.0.11
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
%if 0%{?qt6}
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
%else
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
%endif
BuildRequires:  pkgconfig(aubio)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(suil-0)
BuildRequires:  pkgconfig(xcb)

%description
Qtractor is an Audio/MIDI multi-track sequencer application
written in C++ around the Qt toolkit.

The initial target platform will be Linux, where the Jack Audio
Connection Kit (JACK) for audio, and the Advanced Linux Sound
Architecture (ALSA) for MIDI, are the main infrastructures to
evolve as a fairly-featured Linux Desktop Audio Workstation GUI,
specially dedicated to the personal home-studio.

%prep
%setup -q

%build
%if 0%{?qt6}
%cmake_qt6
%{qt6_build}
%else
%cmake
%cmake_build
%endif

%install
%if 0%{?qt6}
%{qt6_install}
%else
%cmake_install
%endif

mv %{buildroot}%{_libdir}/qtractor/qtractor_plugin_scan %{buildroot}%{_bindir}

%files
%doc ChangeLog README
%license LICENSE
%dir %{_datadir}/metainfo/
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_bindir}/%{name}
%{_bindir}/qtractor_plugin_scan
%{_datadir}/applications/org.rncbc.qtractor.desktop
%{_datadir}/metainfo/org.rncbc.qtractor.metainfo.xml
%{_datadir}/icons/*/*/apps/org.rncbc.qtractor*
%{_datadir}/icons/*/*/mimetypes/org.rncbc.qtractor.*
%{_datadir}/mime/packages/org.rncbc.qtractor.xml
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/fr/man1/%{name}.1%{?ext_man}
%{_datadir}/%{name}/translations/*

%changelog
