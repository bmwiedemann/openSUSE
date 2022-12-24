#
# spec file for package ardour
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


%define dirbase ardour7
Name:           ardour
Version:        7.2.0
Release:        0
Summary:        Multichannel Digital Audio Workstation
# Legal: Ardour is a mix of GPL-2.0-or-later, [L]GPL-3.0-or-later and a couple copyleft
#  licensed files (BSD, WTFPL). Use GPL-3.0-only for the compiled package.
License:        GPL-3.0-only
URL:            https://ardour.org/
Source0:        Ardour-%{version}.tar.bz2
Source99:       ardour-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel >= 1.56.0
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fftw3-threads-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  graphviz
BuildRequires:  hicolor-icon-theme
BuildRequires:  itstool > 2.0.0
BuildRequires:  jack-devel
BuildRequires:  libcppunit-devel
BuildRequires:  libhidapi-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  readline-devel
BuildRequires:  rubberband-vamp
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(atkmm-1.6) >= 2.22.6
BuildRequires:  pkgconfig(aubio) >= 0.3.2
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(cairomm-1.0) >= 1.10.0
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fftw3) >= 3.3.1
BuildRequires:  pkgconfig(flac) >= 1.2.1
BuildRequires:  pkgconfig(fluidsynth) >= 1.1.6
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(giomm-2.4) >= 2.32.0
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.32.0
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24.18
BuildRequires:  pkgconfig(gtkmm-2.4) >= 2.24.2
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libart-2.0) >= 2.3.21
BuildRequires:  pkgconfig(libcurl) >= 7.25.0
BuildRequires:  pkgconfig(libexslt)
BuildRequires:  pkgconfig(liblo) >= 0.26
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libwebsockets) >= 2.0.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(lrdf)
BuildRequires:  pkgconfig(ltc)
BuildRequires:  pkgconfig(lv2) >= 1.2.0
BuildRequires:  pkgconfig(ogg) >= 1.3.0
BuildRequires:  pkgconfig(pangomm-1.4) >= 2.28.4
BuildRequires:  pkgconfig(raptor2) >= 2.0.6
BuildRequires:  pkgconfig(rasqal) >= 0.9.28
BuildRequires:  pkgconfig(redland) >= 1.0.15
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(samplerate) >= 0.1.8
BuildRequires:  pkgconfig(serd-0)
BuildRequires:  pkgconfig(sigc++-2.0) >= 2.2.10
BuildRequires:  pkgconfig(sndfile) >= 1.0.18
BuildRequires:  pkgconfig(sord-0)
BuildRequires:  pkgconfig(soundtouch) >= 1.8.0
BuildRequires:  pkgconfig(sratom-0)
BuildRequires:  pkgconfig(suil-0)
BuildRequires:  pkgconfig(taglib) >= 1.9.1
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vamp)
BuildRequires:  pkgconfig(vorbis) >= 1.3.2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
Requires:       graphviz
Requires:       lv2
%requires_ge    liblilv-0-0
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun): desktop-file-utils
Requires(postun): shared-mime-info
Recommends:     a2jmidid
Recommends:     gtk2-engine-clearlooks
Recommends:     libfftw3_threads3
Conflicts:      ardour-vst
Conflicts:      ardour2
Conflicts:      ardour2-vst
Conflicts:      ardour3
Conflicts:      ardour3vst
Conflicts:      ardour4
Conflicts:      ardour4vst
Conflicts:      ardour5
Conflicts:      ardour5vst

%description
Ardour is a multichannel hard disk recorder (HDR) and digital audio
workstation (DAW). It is capable of simultaneous recording 24 or more
channels of 32 bit audio at 48kHz. Ardour is intended to function as a
"professional" HDR system, replacing dedicated hardware solutions such
as the Mackie HDR, the Tascam 2424 and more traditional tape systems
like the Alesis ADAT series. It is also intended to provide the same
or better functionality as software systems such as ProTools,
Samplitude, Logic Audio, Nuendo and Cubase VST (we acknowledge these
and all other names as trademarks of their respective owners). It
supports MIDI Machine Control, and so can be controlled from any MMC
controller, such as the Mackie Digital 8 Bus mixer and many other
modern digital mixers.

%lang_package

%prep
%autosetup -p1 -n Ardour-%{version}
# delete not needed files
find . -name ".gitignore" -exec rm {} \;
chmod -x ./doc/*.svg
chmod -x ./doc/*.txt
# don't use python2
find . -name wscript -o -name waf -o -name '*.py' \
  | xargs sed -i -e '1{s|^#!.*python$|#!/usr/bin/python3|}'


%build
./waf configure \
   --prefix=%{_prefix} \
   --libdir=%{_libdir} \
   --includedir=%{_includedir} \
   --configdir=%{_sysconfdir} \
   --docdir=%{_docdir} \
   --docs \
   --nls \
   --internal-shared-libs \
   --with-backends=jack,alsa,dummy,pulseaudio \
   --lv2dir=%{_libdir}/%{dirbase}/LV2 \
   --lxvst \
   --freedesktop \
   --noconfirm \
   --no-phone-home \
   --optimize
./waf i18n
./waf %{?_smp_mflags}

%install
./waf --destdir=%{buildroot} install -v

# upstream installs in wrong places
install -D -m 644 -t %{buildroot}%{_datadir}/metainfo %{buildroot}%{_datadir}/appdata/ardour7.appdata.xml
rm -r %{buildroot}%{_datadir}/appdata

%suse_update_desktop_file -i ardour7 AudioVideo Recorder
%find_lang ardour7
%find_lang gtk2_ardour7
%find_lang gtkmm2ext3

# remove dupes
%fdupes -s %{buildroot}%{_datadir}

%files -f ardour7.lang -f gtk2_ardour7.lang -f gtkmm2ext3.lang
%license COPYING
%doc doc README
%dir %{_sysconfdir}/%{dirbase}
%config(noreplace) %{_sysconfdir}/%{dirbase}/*
%{_bindir}/%{dirbase}
%{_bindir}/%{dirbase}-copy-mixer
%{_bindir}/%{dirbase}-export
%{_bindir}/%{dirbase}-lua
%{_bindir}/%{dirbase}-new_empty_session
%{_bindir}/%{dirbase}-new_session
%{_datadir}/%{dirbase}/
%{_datadir}/applications/%{dirbase}.desktop
%{_datadir}/icons/hicolor/*/apps/%{dirbase}.png
%{_datadir}/metainfo/ardour7.appdata.xml
%{_datadir}/mime/packages/ardour.xml
%{_libdir}/%{dirbase}/
%exclude %{_datadir}/%{dirbase}/templates/.stub
%exclude %{_libdir}/%{dirbase}/libhidapi.a

%changelog
