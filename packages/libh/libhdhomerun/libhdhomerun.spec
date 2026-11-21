#
# spec file for package libhdhomerun
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


%define         SO_NR 2
Name:           libhdhomerun
Version:        20260326
Release:        0
Summary:        HDHomeRun library
License:        LGPL-2.1-only
URL:            https://www.silicondust.com
Source0:        https://download.silicondust.com/hdhomerun/libhdhomerun_%{version}.tgz
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig

%description
HDHomeRun configuration library allows you to discover HDHomeRun ATSC/QAM/DVB
TV tuners on the network. It can configure the tuners, scan for channels, and
retrieve information, including signal strength. A shared library is included
for linking by client applications and a simple console application is included
for scripting.

%package -n libhdhomerun%{SO_NR}
Summary:        HDHomeRun library

%description -n libhdhomerun%{SO_NR}
HDHomeRun configuration library allows you to discover HDHomeRun ATSC/QAM/DVB
TV tuners on the network. It can configure the tuners, scan for channels, and
retrieve information, including signal strength. A shared library is included
for linking by client applications and a simple console application is included
for scripting.

%package devel
Summary:        HDHomeRun library
Requires:       libhdhomerun%{SO_NR} = %{version}
Provides:       libhdhomerun:%{_includedir}/libhdhomerun/hdhomerun.h

%description devel
Development libraries needed to build applications with libhdhomerun.

%package -n hdhomerun_config
Summary:        HDHomeRun Config tool

%description -n hdhomerun_config
hdhomerun_config is a command line tool to discover, configure, and scan
HDHomeRun TV tuners. The tool can also be used to update the tuner's firmware.

Firmware updates can be downloaded from http://www.silicondust.com/support/hdhomerun/downloads/linux

%prep
%setup -q -n libhdhomerun

%build
# Plain Makefile, no configure script: only export the distro flags.
# Upstream names the lib unversioned; pass LIBEXT to keep the .so.2 soname.
%{set_build_flags}
%make_build LIBEXT=.so.%{SO_NR} all

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_includedir}/libhdhomerun

# libraries
cp libhdhomerun.so.%{SO_NR} %{buildroot}/%{_libdir}
ln -s libhdhomerun.so.%{SO_NR} %{buildroot}/%{_libdir}/libhdhomerun.so

# binaries
cp hdhomerun_config %{buildroot}/%{_bindir}

# headers
cp hdhomerun.h %{buildroot}/%{_includedir}/libhdhomerun
cp hdhomerun_os.h %{buildroot}/%{_includedir}/libhdhomerun
cp hdhomerun_os_posix.h %{buildroot}/%{_includedir}/libhdhomerun
cp hdhomerun_types.h %{buildroot}/%{_includedir}/libhdhomerun
cp hdhomerun_pkt.h %{buildroot}/%{_includedir}/libhdhomerun
cp hdhomerun_sock.h %{buildroot}/%{_includedir}/libhdhomerun
cp hdhomerun_debug.h %{buildroot}/%{_includedir}/libhdhomerun
cp hdhomerun_discover.h %{buildroot}/%{_includedir}/libhdhomerun
cp hdhomerun_control.h %{buildroot}/%{_includedir}/libhdhomerun
cp hdhomerun_video.h %{buildroot}/%{_includedir}/libhdhomerun
cp hdhomerun_channels.h %{buildroot}/%{_includedir}/libhdhomerun
cp hdhomerun_channelscan.h %{buildroot}/%{_includedir}/libhdhomerun
cp hdhomerun_device.h %{buildroot}/%{_includedir}/libhdhomerun
cp hdhomerun_device_selector.h %{buildroot}/%{_includedir}/libhdhomerun

%post -n libhdhomerun%{SO_NR} -p /sbin/ldconfig
%postun -n libhdhomerun%{SO_NR} -p /sbin/ldconfig

%files -n libhdhomerun%{SO_NR}
%attr(0755,root,root) %{_libdir}/libhdhomerun.so.%{SO_NR}*
%license LICENSE
%doc README.md

%files devel
%{_includedir}/libhdhomerun
%{_libdir}/libhdhomerun.so

%files -n hdhomerun_config
%{_bindir}/hdhomerun_config

%changelog
