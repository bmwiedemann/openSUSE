#
# spec file for package giada
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 Packman Team <packman@links2linux.de>
# Copyright (c) 2012 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           giada
Version:        0.15.4
Release:        0
Summary:        Sampler Audio Tool
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://giadamusic.com
Source0:        https://github.com/monocasual/giada/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        giada.svg
Source2:        %{name}.changes
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fltk-devel
%if 0%{?suse_version} >= 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc7-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  portaudio-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(jansson) >= 2.7
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(rtmidi) >= 2.1.0
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)

%description
Giada is an audio tool for DJs and live performers. Up to 32 samples
may be loaded or recorded, and may be played in single mode (drum
machine) or loop mode (sequencer). The keyboard can be used to
control this.

%prep
%setup -q

%build
export CXX=g++
test -x "$(type -p g++-7)" && export CXX=g++-7 OBJCXX=g++-7
./autogen.sh
%configure --target=linux
make %{?_smp_mflags}

%install
%make_install

install -Dm 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%suse_update_desktop_file -c %{name} %{name} "Sampler Audio Tool" %{name} %{name} AudioVideo Audio Sequencer

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun
%endif

%files
%doc ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
