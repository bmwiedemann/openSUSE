#
# spec file for package pcm
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


Name:           pcm
Version:        202405
Release:        0
Summary:        Intel Performance Counter Monitor
License:        BSD-3-Clause
URL:            https://github.com/intel/pcm
Source:         https://github.com/intel/pcm/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
ExclusiveArch:  %{ix86} x86_64

%description
Intel Performance Counter Monitor (PCM) is an application programming
interface (API) and a set of tools based on the API to monitor performance and
energy metrics of Intel Core, Xeon, Atom and Xeon Phi processors.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=CUSTOM -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_DOCDIR=%{_docdir}/pcm
%{!?cmake_build:%define cmake_build %{__cmake}}
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_docdir}/pcm/CUSTOM-COMPILE-OPTIONS.md
rm -rf %{buildroot}%{_docdir}/pcm/DOCKER_README.md
rm -rf %{buildroot}%{_docdir}/pcm/FREEBSD_HOWTO.txt
rm -rf %{buildroot}%{_docdir}/pcm/MAC_HOWTO.txt
rm -rf %{buildroot}%{_docdir}/pcm/WINDOWS_HOWTO.md
rm -rf %{buildroot}%{_docdir}/pcm/STARS.md
rm -rf %{buildroot}%{_docdir}/pcm/generate_summary_readme.md

%files
%license LICENSE
%doc doc/*HOWTO*
%dir %{_docdir}/pcm
%{_docdir}/pcm/ENVVAR_README.md
%{_docdir}/pcm/FAQ.md
%{_docdir}/pcm/LINUX_HOWTO.txt
%{_docdir}/pcm/PCM-EXPORTER.md
%{_docdir}/pcm/PCM-SENSOR-SERVER-README.md
%{_docdir}/pcm/PCM_RAW_README.md
%{_docdir}/pcm/CXL_README.md
%{_docdir}/pcm/PCM_ACCEL_README.md
%{_docdir}/pcm/README.md
%{_docdir}/pcm/license.txt
%{_sbindir}/pcm
%{_sbindir}/pcm-core
%{_sbindir}/pcm-iio
%{_sbindir}/pcm-latency
%{_sbindir}/pcm-lspci
%{_sbindir}/pcm-memory
%{_sbindir}/pcm-msr
%{_sbindir}/pcm-tpmi
%{_sbindir}/pcm-mmio
%{_sbindir}/pcm-numa
%{_sbindir}/pcm-accel
%{_sbindir}/pcm-pcicfg
%{_sbindir}/pcm-pcie
%{_sbindir}/pcm-power
%{_sbindir}/pcm-sensor
%{_sbindir}/pcm-tsx
%{_bindir}/pcm-client
%{_sbindir}/pcm-bw-histogram
%{_sbindir}/pcm-daemon
%{_sbindir}/pcm-sensor-server
%{_sbindir}/pcm-raw
%dir %{_datadir}/pcm
%{_datadir}/pcm/opCode-106.txt
%{_datadir}/pcm/opCode-85.txt
%{_datadir}/pcm/opCode-134.txt
%{_datadir}/pcm/opCode-143.txt
%{_datadir}/pcm/opCode-143-accel.txt
%{_datadir}/pcm/opCode-175.txt
%{_datadir}/pcm/opCode-207.txt
%{_datadir}/pcm/PMURegisterDeclarations

%changelog
