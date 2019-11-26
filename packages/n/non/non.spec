#
# spec file for package non
#
# Copyright (c) 2019 SUSE LLC
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


%define mixer_version 1.2.0
%define sequencer_version 1.9.5
%define sessman_version 1.2.0
%define timeline_version 1.2.0
Name:           non
Version:        %{timeline_version}
Release:        0
Summary:        Modular digital audio workstation
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            http://non.tuxfamily.org/
Source0:        https://github.com/original-male/non/archive/non-daw-v%{version}.tar.gz
Patch0:         non-desktop-files.patch
Patch1:         non-fix-potential-strlcat-overflow.patch
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  ladspa-devel
BuildRequires:  non-ntk-fluid
BuildRequires:  pkgconfig
BuildRequires:  python2-base
BuildRequires:  pkgconfig(jack) >= 0.103.0
BuildRequires:  pkgconfig(liblo) >= 0.26
BuildRequires:  pkgconfig(lrdf) >= 0.4.0
BuildRequires:  pkgconfig(ntk) >= 1.3.0
BuildRequires:  pkgconfig(sigc++-2.0) >= 2.0.0
BuildRequires:  pkgconfig(sndfile) >= 1.0.18
BuildRequires:  pkgconfig(x11)

%description
The Non DAW Studio is a modular system composed of four main parts:
Non Timeline, a non-destructive, non-linear audio recorder and
arranger. Non Mixer, a live mixer with effects plugin hosting and
advanced Ambisonics spatialization control. Non Sequencer, a live,
pattern based MIDI sequencer, and finally, the Non Session Manager
to tie together these applications and more into cohesive
song-level units.

%package mixer
Version:        %{mixer_version}
Release:        0
Summary:        Mixer for the Non digital audio workstation
Group:          Productivity/Multimedia/Sound/Editors and Convertors

%description mixer
The Non DAW Studio is a modular system composed of four main parts:
Non Timeline, a non-destructive, non-linear audio recorder and
arranger. Non Mixer, a live mixer with effects plugin hosting and
advanced Ambisonics spatialization control. Non Sequencer, a live,
pattern based MIDI sequencer, and finally, the Non Session Manager
to tie together these applications and more into cohesive
song-level units.

This package contains the Non Mixer.

%package sequencer
Version:        %{sequencer_version}
Release:        0
Summary:        Sequencer for the Non digital audio workstation
Group:          Productivity/Multimedia/Sound/Editors and Convertors

%description sequencer
The Non DAW Studio is a modular system composed of four main parts:
Non Timeline, a non-destructive, non-linear audio recorder and
arranger. Non Mixer, a live mixer with effects plugin hosting and
advanced Ambisonics spatialization control. Non Sequencer, a live,
pattern based MIDI sequencer, and finally, the Non Session Manager
to tie together these applications and more into cohesive
song-level units.

This package contains the Non Sequencer.

%package session-manager
Version:        %{sessman_version}
Release:        0
Summary:        Session manager for the Non digital audio workstation
Group:          Productivity/Multimedia/Sound/Editors and Convertors

%description session-manager
The Non DAW Studio is a modular system composed of four main parts:
Non Timeline, a non-destructive, non-linear audio recorder and
arranger. Non Mixer, a live mixer with effects plugin hosting and
advanced Ambisonics spatialization control. Non Sequencer, a live,
pattern based MIDI sequencer, and finally, the Non Session Manager
to tie together these applications and more into cohesive
song-level units.

This package contains the Non Session Manager.

%package timeline
Version:        %{timeline_version}
Release:        0
Summary:        Timeline for the Non digital audio workstation
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Requires:       python2-base

%description timeline
The Non DAW Studio is a modular system composed of four main parts:
Non Timeline, a non-destructive, non-linear audio recorder and
arranger. Non Mixer, a live mixer with effects plugin hosting and
advanced Ambisonics spatialization control. Non Sequencer, a live,
pattern based MIDI sequencer, and finally, the Non Session Manager
to tie together these applications and more into cohesive
song-level units.

This package contains the Non Timeline.

%prep
%setup -q -n non-non-daw-v%{timeline_version}
%autopatch -p1

sed -i "s,^#!%{_bindir}/env ,#!%{_bindir}/," timeline/bin/import-ardour-session

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
python ./waf configure \
    --prefix="%{_prefix}"  \
    --bindir="%{_bindir}"  \
    --mandir="%{_mandir}"  \
    --libdir="%{_libdir}"
python ./waf build --verbose %{?_smp_mflags}

%install
python ./waf --destdir=%{buildroot} install

%if 0%{?suse_version}
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/doc/non-* %{buildroot}%{_docdir}
%endif

%fdupes %{buildroot}

%files mixer
%license COPYING
%{_bindir}/non-midi-mapper
%{_bindir}/non-mixer
%{_bindir}/non-mixer-noui
%{_datadir}/applications/non-mixer.desktop
%{_datadir}/icons/hicolor/*/apps/non-mixer.png
%{_datadir}/pixmaps/non-mixer
%{_docdir}/non-mixer

%files sequencer
%license COPYING
%{_bindir}/non-sequencer
%{_datadir}/applications/non-sequencer.desktop
%{_datadir}/icons/hicolor/*/apps/non-sequencer.png
%{_datadir}/non-sequencer
%{_datadir}/pixmaps/non-sequencer
%{_docdir}/non-sequencer

%files session-manager
%license COPYING
%{_bindir}/jackpatch
%{_bindir}/non-session-manager
%{_bindir}/nsm-proxy
%{_bindir}/nsm-proxy-gui
%{_bindir}/nsmd
%{_datadir}/applications/non-session-manager.desktop
%{_datadir}/icons/hicolor/*/apps/non-session-manager.png
%{_datadir}/pixmaps/non-session-manager
%{_docdir}/non-session-manager

%files timeline
%license COPYING
%doc timeline/bin/import-external-sources timeline/bin/remove-unused-sources
%{_bindir}/import-ardour-session
%{_bindir}/import-ardour-session_gui
%{_bindir}/non-daw
%{_bindir}/non-timeline
%{_datadir}/applications/non-timeline.desktop
%{_datadir}/icons/hicolor/*/apps/non-timeline.png
%{_datadir}/pixmaps/non-timeline
%{_docdir}/non-timeline

%changelog
