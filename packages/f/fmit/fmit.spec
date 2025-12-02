#
# spec file for package fmit
#
# Copyright (c) 2025 SUSE LLC
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


Name:           fmit
Version:        1.3.3
Release:        0
Summary:        A free musical instrument tuner
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://gillesdegottex.github.io/fmit
Source:         https://github.com/gillesdegottex/fmit/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fmit-correct-appdata-dir.patch badshah400@gmail.com -- install appdata file to the correct dir (/usr/share/metainfo instead of /usr/share/appdata)
Patch0:         fmit-correct-appdata-dir.patch
BuildRequires:  appstream-glib
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  itstool
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(portaudio-2.0)
Recommends:     %{name}-lang
ExclusiveArch:  i586 x86_64

%description
fmit is a free musical instrument tuner. It works with JACK, Alsa,
OSS and PortAudio audio input devices. It currently has the
following features:-
* Error history
* Volume history
* Statistics
* Tunning scales
* (Werckmeister III, Kirnberger III, Diatonic and Meantone)
* Microtonal tuning (with Scala file support)
* Harmonic ratios
* Wave shape
* Discrete Fourier Transform view

%lang_package

%prep
%autosetup -p1

%build
lrelease6 %{name}.pro
%qmake6 PREFIX=%{_prefix} \
        CONFIG+="acs_alsa acs_jack acs_portaudio"
%qmake6_build

%install
%qmake6_install

%find_lang %{name} --with-qt

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%license COPYING_GPL.txt COPYING_LGPL.txt
%doc README.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/translations
%{_datadir}/metainfo/*.appdata.xml

%files lang -f %{name}.lang
%dir %{_datadir}/%{name}/translations

%changelog
