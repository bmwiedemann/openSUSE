#
# spec file for package ffado
#
# Copyright (c) 2024 SUSE LLC
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


%define sover 2
%define tname libffado
Name:           ffado
Version:        2.4.7
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
BuildRequires:  scons >= 3.0.2
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1) >= 1.0
BuildRequires:  pkgconfig(dbus-c++-1)
BuildRequires:  pkgconfig(dbus-python)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libavc1394)
BuildRequires:  pkgconfig(libconfig++)
BuildRequires:  pkgconfig(libiec61883) >= 1.1.0
BuildRequires:  pkgconfig(libraw1394) >= 2.0.5
BuildRequires:  pkgconfig(libxml++-3.0) >= 3.0.0
Requires:       libffado%{sover} = %{version}
Recommends:     ffado-mixer = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FFADO aims to provide a generic, open-source solution
to support FireWire(IEEE1394, iLink) based (semi-)
professional audio interfaces.
It's the successor of the FreeBoB project. FFADO is a
volunteer-based community effort, trying to provide Linux
with at least the same level of functionality that is
present on the other operating systems.
The range of FireWire Audio Devices that we would like
to support is broad: from pure audio interfaces over
mixed audio-control devices to DSP algorithm devices.
This is a snapshot of svn revision 1855

%package -n libffado-devel
Summary:        Development files for ffado
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libconfig-devel
Requires:       libdbus-c++-devel
Requires:       libffado%{sover} = %{version}

%description -n libffado-devel
This package supplys the files necessary to develop
applications that use the FFADO libraries and api.

%package -n libffado%{sover}
Summary:        FireWire 1394 support for audio devices
Group:          System/Libraries

%description -n libffado%{sover}
This package provides the libffado shared library that
provides a unified programming interface to configure and
use all supported devices. Currently this library is used
by the 'firewire' backends of the jack audio connection kit
sound server. This backend provides audio and midi support,
and is available in jackd. Access to the device internal
configuration (e,g, internal mixer) is exposed using the
ffado-dbus-server daemon. This daemon exposes the
configurable parameters of all detected devices through
DBUS. The ffadomixer application in support/mixer presents
a GUI to control these parameters (only for officially
supported devices).

%prep

%setup -q -n %{tname}-%{version}
%autopatch -p0

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
  ENABLE_GENERICAVC=yes \
  SERIALIZE_USE_EXPAT=no \
  DEBUG=no \
  ENABLE_ALL=yes \
  PYPKGDIR=%{python_sitelib} \
  ENABLE_OPTIMIZATIONS=yes \
  DETECT_USERSPACE_ENV=False \
  ENABLE_SETBUFFERSIZE_API_VER=auto \
  BUILD_TESTS=yes \
  BUILD_MIXER=False \
  ENABLE_DICE=true \
  COMPILE_FLAGS="%{optflags} -fno-strict-aliasing -ggdb ${EXTRA_FLAGS}" \
  CUSTOM_ENV=True \
  PYTHON_INTERPRETER="%{_bindir}/python3"

%install
# WARNING: the install scons statement must be identical to the build one otherwise a complete rebuild is executed.
export EXTRA_FLAGS="-Wno-deprecated-declarations -fpermissive --std=gnu++11"
%if 0%{?gcc_version} > 5
export EXTRA_FLAGS="${EXTRA_FLAGS}  -Werror=date-time"
%endif
%ifarch %arm
export EXTRA_FLAGS="${EXTRA_FLAGS} -fPIC"
%endif
#export DBUS1_FLAGS="$DBUS1_FLAGS -lpthread"
scons   DESTDIR=%{buildroot} install \
  PREFIX=%{_prefix} \
  LIBDIR=%{_libdir} \
  MANDIR=%{_mandir} \
  UDEVDIR=%{_udevrulesdir} \
  ENABLE_GENERICAVC=yes \
  SERIALIZE_USE_EXPAT=no \
  DEBUG=no \
  ENABLE_ALL=yes \
  PYPKGDIR=%{python_sitelib} \
  ENABLE_OPTIMIZATIONS=yes \
  DETECT_USERSPACE_ENV=False \
  ENABLE_SETBUFFERSIZE_API_VER=auto \
  BUILD_TESTS=yes \
  BUILD_MIXER=False \
  ENABLE_DICE=true \
  COMPILE_FLAGS="%{optflags} -fno-strict-aliasing -ggdb ${EXTRA_FLAGS}" \
  CUSTOM_ENV=True \
  PYTHON_INTERPRETER="%{_bindir}/python3"

rm -rf %{buildroot}%{_libdir}/libffado

%fdupes -s %{buildroot}%{_datadir}

%python3_fix_shebang

%post -n libffado%{sover} -p /sbin/ldconfig
%postun -n libffado%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root)
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

%files -n libffado-devel
%defattr(-,root,root)
%dir %{_includedir}/%{tname}
%{_includedir}/%{tname}/*.h
%{_libdir}/%{tname}*.so
%{_libdir}/pkgconfig/%{tname}.pc

%files -n libffado%{sover}
%defattr(-,root,root)
%{_libdir}/%{tname}.so.%{sover}*
%dir %{_udevrulesdir}
%dir %{_udevrulesdir}/..
%{_udevrulesdir}/60-ffado.rules

%changelog
