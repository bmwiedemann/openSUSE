#
# spec file for package scummvm
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


%bcond_with faad
%bcond_without libmpeg2
%bcond_without mad
Name:           scummvm
Version:        2.9.1
Release:        0
Summary:        Interpreter for several adventure games
License:        GPL-3.0-or-later
Group:          Amusements/Games/Other
URL:            https://www.scummvm.org/
Source:         https://www.scummvm.org/frs/scummvm/%{version}/scummvm-%{version}.tar.xz
BuildRequires:  desktop-file-utils
BuildRequires:  discord-rpc-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
%if 0%{?suse_version} > 1500
BuildRequires:  libieee1284-devel
%endif
%if 0%{?suse_version} >= 1600
BuildRequires:  pkgconfig(libopenmpt) >= 0.7
%endif
BuildRequires:  libjpeg-devel
BuildRequires:  libmpcdec-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa) >= 0.9
BuildRequires:  pkgconfig(flac) >= 1.0.1
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libmikmod)
BuildRequires:  pkgconfig(libpng) >= 1.2.8
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(sonivox)
BuildRequires:  pkgconfig(theoradec) >= 1.0
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(vpx)
BuildRequires:  pkgconfig(zlib)
Suggests:       %{name}-extra
Suggests:       %{name}-tools
%if %{with faad}
BuildRequires:  pkgconfig(faad2)
%endif
%if %{with mad}
BuildRequires:  pkgconfig(mad)
%endif
%if %{with libmpeg2}
BuildRequires:  pkgconfig(libmpeg2) >= 0.4.0
%endif
%ifarch %{ix86}
BuildRequires:  nasm
%endif
BuildRequires:  fdupes
BuildRequires:  fribidi-devel
BuildRequires:  giflib-devel
BuildRequires:  libX11-devel
BuildRequires:  liba52-devel
BuildRequires:  libcurl-devel
BuildRequires:  libspeechd-devel
BuildRequires:  pkgconfig(SDL2_net)

%description
ScummVM is an interpreter that will play graphic adventure games written for
LucasArts' SCUMM virtual machine (such as Day of the Tentacle and
Monkey Island), Sierra's AGI adventures (such as early King's Quest and
Space Quest games), Adventure Soft's Simon the Sorcerer 1, 2 and Feeble Files,
Revolution Software's Beneath a Steel Sky and Broken Sword 1, 2 and 2.5,
Interactive Binary Illusions' Flight of the Amazon Queen,
Coktel Vision's Gobliiins, Wyrmkeep's Inherit the Earth, Westwood's
Legend of Kyrandia, and various others.

%package extra
Summary:        Extra engines for ScummVM
Group:          Amusements/Games/Other
Requires:       %{name} = %{version}

%description extra
lastexpress and toltecs engines for ScummVM.
These engines are in a worse state, but allow to play extra games.

%prep
%setup -q

# build the endianness test without optimization otherwise gcc is too smart
# and optimize everything away, making the test fail
sed -i '/tmp_endianness_check.cpp/ s/$CXXFLAGS/$CXXFLAGS -fno-lto -O0/' configure
%if 0%{?suse_version} < 1600
#allow to use liba52 from svn
sed -i '/a52_init/s@(0)@()@' configure
sed -i '/a52_init/s@(0)@()@' audio/decoders/ac3.cpp
%endif

%build
# scummvm relies on -gsplit-dwarf which is incompatible with -flto
%define _lto_cflags %{nil}

# No rpm configure because scummvm's configure isn't a real configure and thus
# doesn't understand some of the options %%configure passes.
CXXFLAGS="%{optflags}" ; export CXXFLAGS ; \
./configure --prefix=%{_prefix} \
            --bindir=%{_bindir} \
            --datarootdir=%{_datadir} \
            --mandir=%{_mandir} \
            --libdir=%{_libdir} \
            --docdir=%{_docdir}/%{name} \
            --enable-release \
            --enable-verbose-build \
            --enable-plugins \
            --enable-engine-dynamic=lastexpress \
            --enable-engine-dynamic=wintermute \
            --enable-opl2lpt

# Subengines are not included even as dynamic since I don't want to touch the main engines
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_docdir}/%{name}/COPYING*
%fdupes %{buildroot}%{_datadir}/scummvm

%files
%defattr(0644,root,root,0755)
%license COPYING*
%attr(0755,-,-) %{_bindir}/scummvm
%{_datadir}/scummvm
%{_mandir}/man6/scummvm.6%{?ext_man}
%{_datadir}/applications/org.scummvm.scummvm.desktop
%{_datadir}/metainfo/org.scummvm.scummvm.metainfo.xml
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/org.scummvm.scummvm.xpm
%{_docdir}/%{name}

%files extra
%defattr(0644,root,root,0755)
%{_libdir}/scummvm

%changelog
