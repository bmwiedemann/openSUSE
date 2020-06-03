#
# spec file for package qtractor
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


Name:           qtractor
Version:        0.9.14
Release:        0
Summary:        An Audio/MIDI multi-track sequencer
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            http://qtractor.org/
#https://github.com/rncbc/qtractor/archive/qtractor_0_9_10.zip
Source0:        https://downloads.sourceforge.net/project/qtractor/qtractor/%{version}/qtractor-%{version}.tar.gz
# PATCH-{FIX}-{OPENSUSE} qtractor-powerpc.patch dvaleev@suse.com -- Fix build on ppc
Patch2:         qtractor-powerpc.patch
BuildRequires:  alsa-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dssi-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  ladspa-devel
BuildRequires:  libjack-devel
BuildRequires:  liblo-devel
BuildRequires:  libqt5-linguist
BuildRequires:  librubberband-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel >= 1.0.11
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(mad)
BuildRequires:  pkgconfig(shared-mime-info)
Requires:       jack

%description
Qtractor is an Audio/MIDI multi-track sequencer application
written in C++ around the Qt4 toolkit using Qt Designer.

The initial target platform will be Linux, where the Jack Audio
Connection Kit (JACK) for audio, and the Advanced Linux Sound
Architecture (ALSA) for MIDI, are the main infrastructures to
evolve as a fairly-featured Linux Desktop Audio Workstation GUI,
specially dedicated to the personal home-studio.

%prep
%setup -q
%patch2

%build
%configure
make %{?_smp_mflags}

%install
%make_install
mv %{buildroot}%{_libdir}/qtractor/qtractor_plugin_scan %{buildroot}%{_bindir}

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post
%mime_database_post
%desktop_database_post

%postun
%desktop_database_postun
%mime_database_postun
%icon_theme_cache_postun
%endif

%files
%doc AUTHORS ChangeLog README TODO
%license COPYING
%dir %{_datadir}/metainfo/
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%{_bindir}/%{name}
%{_bindir}/qtractor_plugin_scan
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/*/*/apps/%{name}.*
%{_datadir}/icons/*/*/mimetypes/application-x-%{name}-*.*
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/%{name}.1%{ext_man}
%{_mandir}/man1/qtractor.fr.1%{ext_man}
%{_datadir}/%{name}/translations/*

%changelog
