#
# spec file for package zynaddsubfx
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


Name:           zynaddsubfx
Version:        3.0.6
Release:        0
Summary:        A Real-Time Software Synthesizer for Linux
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
URL:            https://zynaddsubfx.sourceforge.io/
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.bz2
Patch0:         zynaddsubfx-buildflags.patch
BuildRequires:  cmake
BuildRequires:  dssi
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(fftw3l)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(mxml)
BuildRequires:  pkgconfig(ntk) >= 1.3.1001
BuildRequires:  pkgconfig(ntk_gl) >= 1.3.1001
BuildRequires:  pkgconfig(ntk_images) >= 1.3.1001
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)
Provides:       ZynAddSubFX = %{version}
Obsoletes:      ZynAddSubFX < %{version}
Requires:       %{name}-common = %{version}

%description
zynaddsubfx is a many-featured real-time software synthesizer for
Linux.	Features include polyphony and multitimbrel and microtonal
capabilities. It includes randomness of some parameters, which can make
warm sounds, like analog synthesizers.	This program has system and
insertion effects, too.

%package bash-completion
Summary:        Bash completion for ZynAddSubFX
Requires:       %{name} = %{version}
Requires:       bash

%description bash-completion
Bash command line completion support for ZynAddSubFX.

%package common
Summary:        Common files for ZynAddSubFX synthesizers
Group:          Productivity/Multimedia/Sound/Midi
Provides:       ZynAddSubFX-common = %{version}
Obsoletes:      ZynAddSubFX-common < %{version}
BuildArch:      noarch

%description common
zynaddsubfx is a many-featured real-time software synthesizer for
Linux.	Features include polyphony and multitimbrel and microtonal
capabilities. It includes randomness of some parameters, which can make
warm sounds, like analog synthesizers.	This program has system and
insertion effects, too.

These are files common to the gui and dssi,lv2 and vst plugins.

%package dssi
Summary:        Real-time software synthesizer, DSSI Plugin version
Group:          Productivity/Multimedia/Sound/Midi
Requires:       %{name}-common = %{version}-%{release}
Requires:       dssi

%description dssi
zynaddsubfx is a many-featured real-time software synthesizer for
Linux.	Features include polyphony and multitimbrel and microtonal
capabilities. It includes randomness of some parameters, which can make
warm sounds, like analog synthesizers.	This program has system and
insertion effects, too.

This package includes the DSSI zynaddsubfx synthesizer plugins.

%package lv2
Summary:        Real-time software synthesizer, LV2 Plugin version
Group:          Productivity/Multimedia/Sound/Midi
Requires:       %{name}-common = %{version}-%{release}

%description lv2
zynaddsubfx is a many-featured real-time software synthesizer for
Linux.	Features include polyphony and multitimbrel and microtonal
capabilities. It includes randomness of some parameters, which can make
warm sounds, like analog synthesizers.	This program has system and
insertion effects, too.

This package includes the LV2 zynaddsubfx synthesizer plugins.

%package vst
Summary:        Real-time software synthesizer, VST Plugin version
Group:          Productivity/Multimedia/Sound/Midi
Requires:       %{name}-common = %{version}-%{release}

%description vst
zynaddsubfx is a many-featured real-time software synthesizer for
Linux.	Features include polyphony and multitimbrel and microtonal
capabilities. It includes randomness of some parameters, which can make
warm sounds, like analog synthesizers.	This program has system and
insertion effects, too.

This package includes the VST zynaddsubfx synthesizer plugins.

%prep
%autosetup -p1

%build
%cmake \
      -DDefaultOutput=jack \
      -DNoNeonPlease:BOOL=ON \
      -DOssEnable:BOOL=FALSE \
%ifarch %{ix86} x86_64
      -DX86Build=ON \
%endif
      -DPluginLibDir:STRING=%{_lib}

pushd src/Tests/CMakeFiles
for i in `find . -name link.txt` ;do sed -i 's/--no-as-needed -lpthread/--no-as-needed -lpthread -lfltk/' ${i} ;done
popd

make %{?_smp_mflags}

%install
make -C build DESTDIR=%{buildroot} install
%suse_update_desktop_file -r %{name}-alsa AudioVideo Music
%suse_update_desktop_file -r %{name}-jack AudioVideo Music
%suse_update_desktop_file -r %{name}-jack-multi AudioVideo Music
mkdir -p %{buildroot}%{_datadir}/zynaddsubfx
cp -a instruments/examples instruments/banks %{buildroot}%{_datadir}/zynaddsubfx

# We are including these in the common package below
rm -fr %{buildroot}%{_datadir}/doc/%{name}/
#Remove defective and useless zynaddsubfx-oss.desktop
rm -f %{buildroot}%{_datadir}/applications/zynaddsubfx-oss.desktop

%files
%{_bindir}/*
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/pixmaps/zynaddsubfx.svg
%{_datadir}/pixmaps/zynaddsubfx.png

%files bash-completion
%{_datadir}/bash-completion/completions/zynaddsubfx

%files common
%license COPYING
%doc AUTHORS.txt NEWS.txt README.adoc
%{_datadir}/%{name}/

%files dssi
%{_libdir}/dssi/

%files lv2
%{_libdir}/lv2/

%files vst
%{_libdir}/vst/

%changelog
