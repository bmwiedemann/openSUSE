#
# spec file for package audacity
#
# Copyright (c) 2026 SUSE LLC and contributors
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


# VST3 is ON by default in 4.x (opt-in in 3.x): Audacity 4 rebuilt VST3
# effects support on Linux and the SDK is rebuilt from the bundled
# sources (EXTDEPS_OVERRIDE_VST3SDK=REBUILD below), no network fetch.
%bcond_without vst3
Name:           audacity
Version:        4.0.1
Release:        0
Summary:        A Multi Track Digital Audio Editor
License:        CC-BY-3.0 AND GPL-2.0-or-later AND GPL-3.0-only
URL:            https://audacityteam.org/
Source:         https://github.com/audacity/audacity/releases/download/Audacity-%{version}/audacity-sources-%{version}.tar.xz
Source1:        audacity-extdeps-cache-%{version}.tar.xz
Source2:        audacity-license-nyquist
Patch0:         audacity-wxstring-untranslatable.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gettext
# The muse extdeps CMake machinery shells out to the git binary even for
# the offline source cache (resolve.cmake: _extdeps_populate_source).
BuildRequires:  git
# Qt tools want an UTF-8 locale
BuildRequires:  glibc-locale-base
BuildRequires:  hicolor-icon-theme
BuildRequires:  patchelf
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel
BuildRequires:  utfcpp-devel
BuildRequires:  wxWidgets-3_2-devel
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6StateMachine)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
# rapidjson ships a CMake config but no pkgconfig file, so the
# package-name dependency stays instead of a pkgconfig one.
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(alsa)
# CVE-2024-50602 fixed in expat 2.6.4; Factory ships newer, floor it.
BuildRequires:  pkgconfig(expat) >= 2.6.4
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(flac++)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lame)
BuildRequires:  pkgconfig(libmpg123)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(soundtouch)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(suil-0)
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(zix-0)
BuildRequires:  pkgconfig(zlib)
# Nothing provides libavutil without a suffix
Requires:       ffmpeg
Recommends:     %{name}-lang
# No Provides/Obsoletes audacity-plugins: the 3.x plugin modules it stood
# for (mod-script-pipe et al. under the audacity libdir) are dropped in 4.0.
# pipewire-libjack-0_3 replaces jack and when audacity loads it
# causes a sigsev See https://bugzilla.suse.com/show_bug.cgi?id=1191585
# i586: 32-bit no longer supported upstream.
# s390x, ppc64: big-endian; the au3 sample engine is little-endian only
# ("All sample block data is little endian...big endian not yet supported").
# ppc64le, riscv64: little-endian but with no Audacity 4 build on record;
# excluded until verified, re-enable with a test build.
ExcludeArch:    i586 s390x ppc64 ppc64le riscv64

%description
Audacity is a program that manipulates digital audio wave forms.
In addition to multitrack recording capabilities with effects, it
imports and exports many sound file formats, including WAV, AIFF,
AU, IRCAM, MP, and Ogg Vorbis. Wave data larger than the available
physical memory size can be edited.

%package -n libsbsms10
Summary:        Subband Sinusoidal Modeling Synthesis audio library
# No standalone sbsms in Factory: Audacity rebuilds the bundled sbsms
# 2.2.0 extdep and ships its runtime here; no -devel subpackage, the
# unversioned link is build-time only and removed at install time.

%description -n libsbsms10
Subband Sinusoidal Modeling Synthesis library for high-quality
time-stretching and pitch-shifting, rebuilt from the sources bundled
with Audacity (no standalone sbsms package in Factory).

%lang_package

%prep
%setup -q -n audacity-%{version}
# Offline extdeps source cache, see
# buildscripts/cmake/PrepareDepsSources.cmake ("offline/distro builds").
# EXTDEPS_CACHE=... is exported at build time.
mkdir -p .extdeps-cache
tar -xf %{SOURCE1} -C .extdeps-cache
%patch -P 0 -p1

%build
export EXTDEPS_CACHE="%{_builddir}/audacity-%{version}/.extdeps-cache"
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
%cmake \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo \
        -DQT_QML_NO_CACHEGEN=ON \
        -DAU4_BUILD_MODE=release \
        -DAU4_BUILD_CONFIGURATION=app \
        -DEXTDEPS_OVERRIDE_ALL=SYSTEM \
        -DEXTDEPS_OVERRIDE_SBSMS=REBUILD \
        -DEXTDEPS_OVERRIDE_VST3SDK=REBUILD \
        -DMUSE_ENABLE_UNIT_TESTS=OFF \
        -DMUSE_MODULE_UPDATE=OFF \
%if %{without vst3}
        -DAU_MODULE_EFFECTS_VST=OFF \
        -DMUSE_MODULE_VST=OFF \
%endif
        -DAU_MODULE_EFFECTS_LV2=ON \
        -DAU_USE_LIBCURL=OFF \
        -Wno-dev
%cmake_build

%install
%cmake_install
cp -f %{SOURCE2} LICENSE_NYQUIST.txt
# The bundled sbsms extdep bakes its build-tree lib dir into the binary
# as RPATH; the shipped /usr/lib64/libsbsms.so.10 is found via the
# default search path, so drop it.  No -devel subpackage: remove the
# unversioned link (build-time only, already linked).
patchelf --remove-rpath %{buildroot}%{_bindir}/%{name}
# The bundled sbsms extdep installs its licenses to a nonstandard prefix;
# relocate them with the other licenses (this also removes the stray dir).
mkdir -p %{buildroot}%{_licensedir}/%{name}-sbsms
mv %{buildroot}%{_prefix}/licenses/sbsms/COPYING %{buildroot}%{_prefix}/licenses/sbsms/LICENSE %{buildroot}%{_licensedir}/%{name}-sbsms/
rmdir %{buildroot}%{_prefix}/licenses/sbsms %{buildroot}%{_prefix}/licenses
rm %{buildroot}%{_libdir}/libsbsms.so
%find_lang %{name} --with-qt

# No "check" section: upstream unit tests compile only with
# MUSE_ENABLE_UNIT_TESTS=ON (set OFF above), so nothing runnable ships.

%ldconfig_scriptlets -n libsbsms10

%files
%doc README.md
%license LICENSE.txt LICENSE_NYQUIST.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/
# Upstream 4.x installs its data under a versioned dir
%dir %{_datadir}/audacity-4.0/
%dir %{_datadir}/audacity-4.0/locale/
%{_datadir}/audacity-4.0/locale/languages.json
%{_datadir}/audacity-4.0/workspaces/
%{_datadir}/applications/org.audacityteam.Audacity.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/metainfo/org.audacityteam.Audacity.appdata.xml
%{_datadir}/mime/packages/audacity.xml

%files -n libsbsms10
%license %{_licensedir}/%{name}-sbsms/COPYING
%license %{_licensedir}/%{name}-sbsms/LICENSE
%dir %{_licensedir}/%{name}-sbsms/
%{_libdir}/libsbsms.so.10*

%files lang -f %{name}.lang

%changelog
