#
# spec file for package ffado
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


%define docs 0
%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
%define mflavor %{nil}
%else
%define mflavor -%{flavor}
%endif
%define sover 2
%define tname libffado
Name:           ffado%{mflavor}
Version:        2.4.9
Release:        0
Summary:        FireWire 1394 support for audio devices
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            http://www.ffado.org/
Source0:        http://www.ffado.org/files/%{tname}-%{version}.tgz
Source1:        baselibs.conf
# No current date and time allowed.
Patch0:         libffado-date_time.patch
# PATCH-FIX-UPSTREAM ffado-nosys.patch davejplater@gmail.com -- No import sys in SConstruct although functions are used.
Patch4:         ffado-nosys.patch
Patch5:         reproducible.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-c++-1)
BuildRequires:  pkgconfig(dbus-python)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libavc1394)
BuildRequires:  pkgconfig(libconfig++)
BuildRequires:  pkgconfig(libiec61883) >= 1.1.0
BuildRequires:  pkgconfig(libraw1394) >= 2.0.5
BuildRequires:  pkgconfig(libxml++-3.0) >= 3.0.0
%if "%{flavor}" == ""
BuildRequires:  python3-setuptools
BuildRequires:  scons >= 3.0.2
BuildRequires:  pkgconfig(dbus-1) >= 1.0
Requires:       libffado%{sover} = %{version}
Recommends:     ffado-mixer = %{version}
%endif
%if "%{flavor}" == "mixer"
BuildRequires:  doxygen
BuildRequires:  ffado = %{version}
BuildRequires:  graphviz-gnome
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-setuptools
BuildRequires:  scons
BuildRequires:  update-desktop-files
BuildRequires:  xdg-utils
BuildRequires:  xorg-x11-fonts
BuildRequires:  pkgconfig(libffado) = %{version}
%if 0%{?suse_version} == 1600 && !0%{?is_opensuse}
ExclusiveArch:  do_not_build
%endif
Requires:       ffado = %{version}
BuildArch:      noarch
%endif

%description
%if "%{flavor}" == ""
FFADO provides a generic solution to support FireWire (IEEE1394,
iLink) based (semi-)professional audio interfaces. It provides Linux
with at least the same level of functionality that is present on the
other operating systems. The range of FireWire Audio Devices
supported ranges from pure audio interfaces over mixed audio-control
devices to DSP algorithm devices.
%endif
%if "%{flavor}" == "mixer"
ffado-mixer presents a graphical application allowing a FFADO device
to be controlled. The extent of the control is determined by the
level of support for the device in FFADO and in ffado-dbus-server.
Typical controls offered by ffado-mixer include faders for the
on-board mixer, phantom power control, mode switches and so on.
%endif

%package -n ffado-devel
Summary:        Development files for ffado
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libffado%{sover} = %{version}
Requires:       pkgconfig(dbus-c++-1)
Requires:       pkgconfig(libconfig)
Obsoletes:      libffado-devel < %{version}-%{release}
Provides:       libffado-devel = %{version}-%{release}

%description -n ffado-devel
This package supplys the files necessary to develop
applications that use the FFADO libraries and API.

%package -n libffado%{sover}
Summary:        FireWire 1394 support for audio devices
Group:          System/Libraries

%description -n libffado%{sover}
This package provides the libffado shared library that
provides a unified programming interface to configure and
use all supported devices. Currently, this library is used
by the 'firewire' backends of the JACK Audio Connection Kit
sound server. This backend provides audio and MIDI support,
and is available in jackd. Access to the device internal
configuration (e.g. internal mixer) is exposed using the
ffado-dbus-server daemon. This daemon exposes the
configurable parameters of all detected devices through
DBUS. The ffadomixer application in support/mixer presents
a GUI to control these parameters (only for officially
supported devices).

%prep
%autosetup -n %{tname}-%{version} -p0

for i in `grep -rl "/usr/bin/env python"`;do sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i} ;done
for i in `grep -rl "/usr/bin/python"`;do sed -i '1s/^#!.*/#!\/usr\/bin\/python3/' ${i} ;done

%build
export EXTRA_FLAGS="-Wno-deprecated-declarations -fpermissive --std=gnu++11"
%if 0%{?gcc_version} > 5
export EXTRA_FLAGS="${EXTRA_FLAGS}  -Werror=date-time"
%endif
%ifarch %arm
export EXTRA_FLAGS="${EXTRA_FLAGS} -fPIC"
%endif
#export DBUS1_FLAGS="$DBUS1_FLAGS -lpthread"
scons %{_smp_mflags} \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir} \
  MANDIR=%{_mandir} \
  UDEVDIR=%{_udevrulesdir} \
  DETECT_USERSPACE_ENV=False \
%if "%{flavor}" == ""
  ENABLE_GENERICAVC=yes \
  ENABLE_ALL=yes \
  ENABLE_SETBUFFERSIZE_API_VER=auto \
  BUILD_TESTS=yes \
  BUILD_MIXER=False \
  ENABLE_DICE=true \
%endif
%if "%{flavor}" == "mixer"
  ENABLE_GENERICAVC=no \
  ENABLE_ALL=no \
  BUILD_TESTS=no \
  BUILD_MIXER=True \
%endif
  SERIALIZE_USE_EXPAT=no \
  DEBUG=no \
  PYPKGDIR=%{python3_sitelib} \
  ENABLE_OPTIMIZATIONS=yes \
  COMPILE_FLAGS="%{optflags} -fno-strict-aliasing -ggdb ${EXTRA_FLAGS}" \
  CUSTOM_ENV=True \
  PYTHON_INTERPRETER="%{_bindir}/python3"

%install
mkdir -p %{buildroot}%{python3_sitelib}
# WARNING: the install scons statement must be identical to the build one otherwise a complete rebuild is executed.
export EXTRA_FLAGS="-Wno-deprecated-declarations -fpermissive --std=gnu++11"
%ifarch %arm
export EXTRA_FLAGS="${EXTRA_FLAGS} -fPIC"
%endif
#export DBUS1_FLAGS="$DBUS1_FLAGS -lpthread"
scons   DESTDIR=%{buildroot} install \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir} \
  MANDIR=%{_mandir} \
  UDEVDIR=%{_udevrulesdir} \
%if "%{flavor}" == ""
  ENABLE_GENERICAVC=yes \
  ENABLE_ALL=yes \
  ENABLE_SETBUFFERSIZE_API_VER=auto \
  BUILD_TESTS=yes \
  BUILD_MIXER=False \
  ENABLE_DICE=true \
%endif
%if "%{flavor}" == "mixer"
  ENABLE_GENERICAVC=no \
  ENABLE_ALL=no \
  BUILD_TESTS=no \
  BUILD_MIXER=True \
%endif
  SERIALIZE_USE_EXPAT=no \
  DEBUG=no \
  PYPKGDIR=%{python3_sitelib} \
  ENABLE_OPTIMIZATIONS=yes \
  DETECT_USERSPACE_ENV=False \
  COMPILE_FLAGS="%{optflags} -fno-strict-aliasing -ggdb ${EXTRA_FLAGS}" \
  CUSTOM_ENV=True \
  PYTHON_INTERPRETER="%{_bindir}/python3"

%if "%{flavor}" == ""
rm -Rfv %{buildroot}%{_libdir}/libffado
%endif

%if "%{flavor}" == "mixer"
rm -Rfv %{buildroot}/%{_libdir}/%tname.* %{buildroot}/%{_includedir}/libffado \
	%{buildroot}/%{_libdir}/pkgconfig

# Remove the useless udev rules and man pages on the mixer package
rm -Rfv %{buildroot}/%{_mandir} %{buildroot}/%{_udevrulesdir}

rpm -ql ffado | while read file; do
	rm -v "%{buildroot}/$file" || :
done

rm -Rfv %{buildroot}/%{_libdir}/libffado

mkdir -pv %{buildroot}/%{_datadir}/applications/
mkdir -pv %{buildroot}/%{_datadir}/pixmaps
cp -av support/xdg/hi64-apps-ffado.png %{buildroot}%{_datadir}/pixmaps/ffadomixer.png
%suse_update_desktop_file -c ffadomixer FfadoMixer "Mixer for ffado" ffado-mixer ffadomixer "AudioVideo;Mixer;HardwareSettings;Qt"

find ./ -empty -delete
%endif

%fdupes -s %{buildroot}%{_datadir}
%python3_fix_shebang

%ldconfig_scriptlets -n libffado%{sover}

%files
%if "%{flavor}" == ""
%doc README
%doc AUTHORS
%license LICENSE.GPLv2 LICENSE.GPLv3
#%%doc ChangeLog
%{_bindir}/dumpiso_mod
%{_bindir}/gen-loadpulses
%{_bindir}/scan-devreg
%{_bindir}/test-avccmd
%{_bindir}/test-bufferops
%{_bindir}/test-clock_nanosleep
%{_bindir}/test-devicestringparser
%{_bindir}/test-dice-eap
%{_bindir}/test-echomixer
%{_bindir}/test-enhanced-mixer
%{_bindir}/test-focusrite
%{_bindir}/test-fw410
%{_bindir}/test-ieee1394service
%{_bindir}/test-ipcringbuffer
%{_bindir}/test-messagequeue
%{_bindir}/test-scs
%{_bindir}/test-shm
%{_bindir}/test-streamdump
%{_bindir}/test-sysload
%{_bindir}/test-timestampedbuffer
%{_bindir}/test-volume
%{_bindir}/test-watchdog
%{_bindir}/unmute-ozonic
%{_bindir}/test-cycle-time
%{_bindir}/set-default-router-config-dice-eap
%{_datadir}/dbus-1/services/org.ffado.Control.service
%{_bindir}/ffado*
%{_datadir}/%{tname}
%{_mandir}/man1/ffado-bridgeco-downloader.1.gz
%{_mandir}/man1/ffado-dbus-server.1.gz
%{_mandir}/man1/ffado-diag.1.gz
%{_mandir}/man1/ffado-dice-firmware.1.gz
%{_mandir}/man1/ffado-fireworks-downloader.1.gz
%endif
%if "%{flavor}" == "mixer"
%{_bindir}/ffado-mixer
%{_datadir}/%{tname}/
%{_datadir}/icons/*
%{_datadir}/pixmaps/ffadomixer.png
%{_datadir}/applications/*
%{python3_sitelib}/*
%{_datadir}/metainfo/org.ffado.FfadoMixer.metainfo.xml
%endif

%if "%{flavor}" == ""
%files -n ffado-devel
%dir %{_includedir}/%{tname}
%{_includedir}/%{tname}/*.h
%{_libdir}/%{tname}*.so
%{_libdir}/pkgconfig/%{tname}.pc
%endif

%if "%{flavor}" == ""
%files -n libffado%{sover}
%{_libdir}/%{tname}.so.%{sover}*
%dir %{_udevrulesdir}
%dir %{_udevrulesdir}/..
%{_udevrulesdir}/60-ffado.rules
%endif

%changelog
