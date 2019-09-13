#
# spec file for package ftsteutates
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%if 0%{?suse_version} > 1320
# TW 4.8 or later kernel already contains the module
%define build_kmp 0
%else
%define build_kmp 1
%endif

Name:           ftsteutates
Version:        20160601
Release:        0
Summary:        Kernel module ftsteutates
License:        GPL-2.0+
Group:          System/Kernel
Url:            ftp://ftp.ts.fujitsu.com/pub/Mainboard-OEM-Sales/Services/
Source0:        ftp://ftp.ts.fujitsu.com/pub/Mainboard-OEM-Sales/Services/Software&Tools/Linux_SystemMonitoring&Watchdog&GPIO/ftsteutates-module_%{version}.zip
%if %build_kmp
BuildRequires:  %{kernel_module_package_buildreqs}
%endif
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %build_kmp
%kernel_module_package
%endif
ExclusiveArch:  %{ix86} x86_64

%description
System monitoring and thermal management for Teutates chips/Fujitsu
mainboards (D34xx).

%package sensors
Summary:        Sensors config ftsteutates
Group:          System/Monitoring
Requires:       sensors
BuildArch:      noarch

%description sensors
System monitoring and thermal management for Fujitsu mainboards (D34xx).
This package contains the mainboard model specific config files for nice
lm-sensors output.

%prep
%setup -q -n ftsteutates
%if %build_kmp
mkdir source
mkdir obj
cp -a Makefile ftsteutates.c source/
%endif

%build
%if %build_kmp
for flavor in %{flavors_to_build}; do
    rm -rf obj/$flavor
    cp -r source obj/$flavor
    make -C %{_prefix}/src/linux-obj/%{_target_cpu}/$flavor modules \
         M=$PWD/obj/$flavor
done
%endif

%install
%if %build_kmp
# install kernel modules
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
for flavor in %{flavors_to_build}; do
    make -C %{_prefix}/src/linux-obj/%{_target_cpu}/$flavor modules_install \
         M=$PWD/obj/$flavor
done
%endif

%files sensors
%defattr(-,root,root)
%doc assets test

%changelog
