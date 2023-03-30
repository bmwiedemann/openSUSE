#
# spec file for package kernel-firmware-nvidia-gsp-G06
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


%define simpletest 1

%ifarch x86_64
%define arch x86_64
%else
%define arch aarch64
%endif

%if %{undefined _firmwaredir}
%define _firmwaredir /lib/firmware
%endif

Name:           kernel-firmware-nvidia-gsp-G06
URL:            https://www.nvidia.com/en-us/drivers/unix/
Version:        525.105.17
Release:        0
Summary:        Kernel firmware file for open NVIDIA kernel module driver G06
License:        GPL-2.0-only AND SUSE-Firmware AND GPL-2.0-or-later AND MIT
Group:          System/Kernel
Source0:        NVIDIA-Linux-x86_64-%{version}.run
Source1:        NVIDIA-Linux-aarch64-%{version}.run
NoSource:       0
%if 0%{simpletest} == 1
Source2:        %{name}-rpmlintrc
ExclusiveArch:  x86_64 aarch64
%else
BuildArch:      noarch
%endif

%description
This package contains the versioned kernel firmware file "gsp.bin" for
the OpenSource NVIDIA kernel module driver G06.

%prep
sh %{_sourcedir}/NVIDIA-Linux-%{arch}-%{version}.run -x

%build

%install
mkdir -p %{buildroot}%{_firmwaredir}/nvidia/%{version}
install -m 644 NVIDIA-Linux-%{arch}-%{version}/firmware/{gsp_ad10x.bin,gsp_tu10x.bin} \
  %{buildroot}%{_firmwaredir}/nvidia/%{version}
%if 0%{simpletest} == 1
mkdir -p %{buildroot}/usr/lib/%{name}
install -m 755 ./NVIDIA-Linux-%{arch}-%{version}/nvidia-smi %{buildroot}/usr/lib/%{name}
install -m 755 ./NVIDIA-Linux-%{arch}-%{version}/libnvidia-ml.so.%{version} %{buildroot}/usr/lib/%{name}
ln -snf libnvidia-ml.so.%{version} %{buildroot}/usr/lib/%{name}/libnvidia-ml.so.1
%endif

%if 0%{simpletest} == 1
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%dir %{_firmwaredir}/nvidia
%dir %{_firmwaredir}/nvidia/%{version}
%{_firmwaredir}/nvidia/%{version}/gsp_ad10x.bin
%{_firmwaredir}/nvidia/%{version}/gsp_tu10x.bin
%if 0%{simpletest} == 1
%dir /usr/lib/%{name}
/usr/lib/%{name}/nvidia-smi
/usr/lib/%{name}/libnvidia-ml.so.%{version}
/usr/lib/%{name}/libnvidia-ml.so.1
%endif

%changelog
