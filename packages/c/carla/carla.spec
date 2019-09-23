#
# spec file for package carla
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


%define __provides_exclude_from ^%{_libdir}/carla/jack/.*.so.0$

Name:           carla
Version:        2.0.0+git20190321.20cc5244
Release:        0
Summary:        An audio plugin host
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
ExclusiveArch:  x86_64
Url:            http://kxstudio.linuxaudio.org/Applications:Carla
Source:         Carla-%{version}.tar.xz
Patch1:         carla-systemlibs.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  fdupes
BuildRequires:  file-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkg-config
BuildRequires:  python3-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-rdflib
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vorbisenc)
# for extra native plugins
BuildRequires:  non-ntk-fluid
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(libprojectM)
BuildRequires:  pkgconfig(mxml)
BuildRequires:  pkgconfig(zlib)
# for plugin GUIs
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(x11)
# for extra samplers support
BuildRequires:  pkgconfig(fluidsynth)

Requires:       python3-base
Requires:       python3-qt5

%description
Carla is an audio plugin host, with support for many audio drivers
and plugin formats. It features automation of parameters via MIDI CC
and full OSC control. It currently supports LADSPA, DSSI, LV2, VST2/3
and AU plugin formats, plus GIG, SF2 and SFZ sounds banks.
It futher supports bridging Window plugins using Wine.

%package devel
Summary:        Header files to access Carla's API
Group:          Development/Libraries/C and C++
BuildRequires:  pkg-config

%description devel
This package contains header files needed when writing software using
Carla's several APIs.

%package vst
Summary:        CarlaRack and CarlaPatchbay VST plugins
Group:          Productivity/Multimedia/Sound/Utilities

%description vst
This package contanis Carla VST plugins, including CarlaPatchbayFX,
CarlaPatchbay, CarlaRackFX, and CarlaRack.

%prep
%setup -q -n Carla-%{version}
%patch1 -p1

%build
export CXXFLAGS="%{optflags}"
export CFLAGS="%{optflags}"

# list build configuration, no need for optflags or -j
make features

# bulding with high -j numbers often results in build failures, thus we're disabling _smp_flags for now 
make \
%ifnarch %ix86 x86_64
	BASE_OPTS= \
%endif
	--trace

%install
make install DESTDIR=%{buildroot} PREFIX="%{_prefix}" LIBDIR="%{_libdir}"
# Move arch depended files (wrong installed)
mv %{buildroot}%{_datadir}/carla/resources/zynaddsubfx-ui %{buildroot}%{_libdir}/carla
ln -s %{_libdir}/carla/zynaddsubfx-ui %{buildroot}%{_datadir}/carla/resources/zynaddsubfx-ui
# flags
for file in carla carla-control carla-jack-multi carla-jack-single carla-patchbay carla-rack carla_app.py carla_backend.py carla_backend_qt.py carla_config.py carla_control.py carla_database.py carla_host.py carla_shared.py carla_skin.py carla_utils.py carla_widgets.py carla_settings.py externalui.py ladspa_rdf.py patchcanvas.py patchcanvas_theme.py resources_rc.py; do
	chmod +x "%{buildroot}%{_datadir}/carla/$file"
done
# SUSE specific
%if 0%{?suse_version}
 %suse_update_desktop_file -r carla AudioVideo Music
 %suse_update_desktop_file -r carla-control AudioVideo Music
 %fdupes -s %{buildroot}%{_datadir}
%endif

%files
%defattr(-,root,root)
%doc INSTALL.md README.md doc
%{_bindir}/*
%dir %{_libdir}/carla
%{_libdir}/carla/*
%dir %{_libdir}/lv2
%dir %{_libdir}/lv2/carla.lv2
%{_libdir}/lv2/carla.lv2/*
%dir %{_datadir}/carla
%{_datadir}/carla/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/
%{_datadir}/mime/packages/carla.xml

%files vst
%defattr(-,root,root)
%dir %{_libdir}/vst
%dir %{_libdir}/vst/carla.vst
%{_libdir}/vst/carla.vst/*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/carla
%{_includedir}/carla/*
%{_libdir}/pkgconfig/*

%changelog
