#
# spec file for package lv2
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


%define asciidocs 1

Name:           lv2
Version:        1.18.10
Release:        0
Summary:        Plugin standard for audio systems
License:        ISC
Group:          System/Libraries
URL:            https://lv2plug.in/
Source0:        https://lv2plug.in/spec/lv2-%{version}.tar.xz
# Patch to use default docdir for documentation
Patch0:         001-lv2-docdir.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-Markdown
BuildRequires:  python3-lxml
BuildRequires:  python3-rdflib
BuildRequires:  serdi
BuildRequires:  sord
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.18.0
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile) >= 1.0.0

%if %{asciidocs} == 1
# Documentation build requirements.
BuildRequires:  asciidoc
BuildRequires:  codespell
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  python3-Pygments
%endif

%description
LV2 is a portable plugin standard for audio systems, similar in scope to LADSPA,
VST, AU, and others. It defines a C API for code and a format for data files
which collectively describe a plugin. LV2 consists of a simple core (roughly
equivalent in power to LADSPA) which can be extended to support more advanced
functionality. This allows the interface to be "grown" to accommodate the needs
of real software as they arise.

LV2 is both a stable interface and a forward-moving project: there is a stable
set of "official" extensions in use while new functionality is actively
developed. Anyone can extend LV2, which allows developers to try out new ideas
and ensure they work in practice. Good extensions are vetted by the community
and included in the official distribution so they can be relied on to be widely
supported. This open development model means developers can always scratch their
itch without a central authority getting in the way. The current stable release
includes most functionality required by modern plugins, including:

  * Audio, control, "control voltage" (audio-rate control), and event
    (e.g. MIDI) input and output
  * Expressive open-ended port metadata, including:
    - "Meaningful" controls (e.g. gain or envelope attack) allowing intelligent
      host control or UI generation
    - Control units (e.g. Hz, octaves, dB)
    - Multi-channel port groups (e.g. stereo, 5.1 surround, ambisonics
  * Embeddable GUIs in any toolkit, with support for a full plugin/UI split
    (including network transparency in capable hosts)
  * Ability to bundle any files (e.g. samples or impulses) with plugins
  * Presets (bundled and/or user saved)
  * Plugin state saving and restoring
  * Host-managed logging
  * Non-realtime plugin worker methods (simple and portable host-managed
    threading)
  * Message-based plugin communication, allowing plugins/UIs to have advanced
    interfaces without host support or specifications getting in the way
  * Transport awareness, both real time and tempo time (bars, beats, etc-.)

LV2 has graceful compatibility "baked in": for example, a simple amplifier
plugin might have audio in/out with a gain control, and function in any host.
The same plugin could have a fancy GUI and transport awareness which optionally
work in hosts that support these features. Conversely, hosts know not to load
plugins that require features it does not support.

See the specification index for complete documentation. If you are a host or
plugin author and need missing functionality, please file a ticket or let us
know your requirements on  the mailing list. LV2 is a community project that
depends on your feedback to improve - unknown requirements are unmet
requirements!

%package        devel
Summary:        Development files for LV2
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
# It actually replaces the old lv2core-devel package. But since the versioning
# went crazy (from 6.0 to 1.0.0) and nothing actually ever required it better to
# avoid the provides/obsoletes. We may want to split this and create a new
# lv2core-devel package in the future (but we need a rpm depenency extractor for
# LV2 bundles).
#Provides:       lv2core-devel
#Obsoletes:      lv2core-devel

%description    devel
LV2 is a plugin standard for audio systems, similar in scope to LADSPA,
VST, AU, and others. It defines a C API for code and a format for data files
which collectively describe a plugin. LV2 consists of a core (roughly
equivalent in power to LADSPA) which can be extended to support more
functionality. This allows the interface to be "grown" to accommodate the needs
of real software as they arise.

LV2 is both a stable interface and a forward-moving project: there is a stable
set of "official" extensions in use while new functionality is actively
developed. Most functionality required by modern plugins is available, including:

  * Audio, control, "control voltage" (audio-rate control), and event
    (e.g. MIDI) input and output
  * Expressive open-ended port metadata, including:
    - "Meaningful" controls (e.g. gain or envelope attack) allowing intelligent
      host control or UI generation
    - Control units (e.g. Hz, octaves, dB)
    - Multi-channel port groups (e.g. stereo, 5.1 surround, ambisonics
  * Embeddable GUIs in any toolkit, with support for a full plugin/UI split
    (including network transparency in capable hosts)
  * Ability to bundle any files (e.g. samples or impulses) with plugins
  * Presets (bundled and/or user saved)
  * Plugin state saving and restoring
  * Host-managed logging
  * Non-realtime plugin worker methods (simple and portable host-managed
    threading)
  * Message-based plugin communication, allowing plugins/UIs to have advanced
    interfaces without host support or specifications getting in the way
  * Transport awareness, both real time and tempo time (bars, beats, etc-.)

%package        examples
Summary:        LV2 example plugins
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Requires:       %{name} = %{version}

%description    examples
LV2 is a plugin standard for audio systems, similar in scope to LADSPA,
VST, AU, and others. It defines a C API for code and a format for data files
which collectively describe a plugin. LV2 consists of a core (roughly
equivalent in power to LADSPA) which can be extended to support more
functionality.
This package contains LV2 example plugins.

%if %{asciidocs} == 1
%package        docs
Summary:        LV2 documentation
Group:          Documentation/Other
BuildArch:      noarch
Requires:       %{name} = %{version}

%description    docs
LV2 is a plugin standard for audio systems, similar in scope to LADSPA,
VST, AU, and others. It defines a C API for code and a format for data files
which collectively describe a plugin. LV2 consists of a core (roughly
equivalent in power to LADSPA) which can be extended to support more
functionality.
This package contains the LV2 API documentation.
%endif

%prep
%setup -q
%autopatch -p0

%build
%meson -D old_headers=true \
%if %{asciidocs} == 1
  -D docs=enabled \
%endif
%meson_build

%install
%meson_install

%fdupes -s %{buildroot}%{_includedir}

sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' %{buildroot}%{_bindir}/lv2specgen.py

%files
%defattr(0644,root,root,0755)
%doc NEWS README.md
%license COPYING
%attr(0755,root,root) %{_bindir}/lv2_validate
%{_libdir}/lv2/
%exclude %{_libdir}/lv2/eg-amp.lv2/
%exclude %{_libdir}/lv2/eg-metro.lv2/
%exclude %{_libdir}/lv2/eg-midigate.lv2/
%exclude %{_libdir}/lv2/eg-sampler.lv2/
%exclude %{_libdir}/lv2/eg-scope.lv2/

%files devel
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/lv2specgen.py
%{_datadir}/lv2specgen
%{_includedir}/lv2.h
%{_includedir}/lv2/
%{_libdir}/pkgconfig/lv2.pc

%files examples
%defattr(0644,root,root,0755)
%{_libdir}/lv2/eg-amp.lv2/
%{_libdir}/lv2/eg-metro.lv2/
%{_libdir}/lv2/eg-midigate.lv2/
%{_libdir}/lv2/eg-sampler.lv2/
%{_libdir}/lv2/eg-scope.lv2/

%if %{asciidocs} == 1
%files docs
%defattr(0644,root,root,0755)
%doc %{_defaultdocdir}/lv2/ns
%doc %{_defaultdocdir}/lv2/c
%doc %{_defaultdocdir}/lv2/style
%endif

%changelog
