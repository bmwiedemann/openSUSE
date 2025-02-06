#
# spec file for package kernel-firmware-nvidia-gspx-G06
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


%define gfx_version 550.144.03
%define cuda_version 560.35.03

%global flavor @BUILD_FLAVOR@%{?nil}
%if "%{flavor}" == "cuda"
%{bcond_without cuda}
%endif

%define simpletest 0

%define arch x86_64

%if %{undefined _firmwaredir}
%define _firmwaredir /lib/firmware
%endif

Name:           kernel-firmware-nvidia-gspx-G06%{?with_cuda:-cuda}
URL:            https://www.nvidia.com/en-us/drivers/unix/
%if %{with cuda}
Version:        %{cuda_version}
%else
Version:        %{gfx_version}
%endif
Release:        0
Summary:        Kernel firmware file for open NVIDIA kernel module driver G06
License:        SUSE-Firmware
Group:          System/Kernel
%if %{without cuda}
Source0:        http://download.nvidia.com/XFree86/Linux-x86_64/%{version}/NVIDIA-Linux-x86_64-%{version}.run
NoSource:       0
%endif
# This is defined at build, not for 'osc service run download_files` or
# factory_auto. This both sources are seen outside of the build but only
# the matching one will be included in the srpm for the respective flavor.
%if %{undefined linux_arch} || %{with cuda}
Source1:        https://developer.download.nvidia.com/compute/cuda/repos/sles15/x86_64/kernel-firmware-nvidia-gspx-G06-%{cuda_version}-0.x86_64.rpm
NoSource:       1
%endif
Source2:        LICENCE.nvidia
Source4:        kernel-firmware-nvidia-gspx-G06-rpmlintrc

# Only required to distinguish between build and factor-auto
BuildRequires:  kernel-macros
BuildRequires:  zstd
%if 0%{simpletest} == 0
Provides:       multiversion(kernel)
%endif
%if %{with cuda}
Provides:       kernel-firmware-nvidia-gspx-G06 = %version
Conflicts:      kernel-firmware-nvidia-gspx-G06
%endif
Obsoletes:      kernel-firmware-nvidia-gsp-G06 = 535.86.05
ExclusiveArch:  x86_64 aarch64
%if 0%{?sle_version} >= 150700
BuildArch:      noarch
%endif

%description
This package contains the versioned kernel firmware file "gsp.bin" for
the OpenSource NVIDIA kernel module driver G06.

%prep
%if %{without cuda}
sh %{_sourcedir}/NVIDIA-Linux-%{arch}-%{version}.run -x
%else
rpm2cpio %{SOURCE1} | cpio -di
%endif
cp %{SOURCE2} .

%build

%install
%if %{without cuda}
mkdir -p %{buildroot}%{_firmwaredir}/nvidia/%{version}
install -m 644 NVIDIA-Linux-%{arch}-%{version}/firmware/{gsp_ga10x.bin,gsp_tu10x.bin} \
  %{buildroot}%{_firmwaredir}/nvidia/%{version}
%if 0%{simpletest} == 1
mkdir -p %{buildroot}/usr/lib/%{name}
install -m 755 ./NVIDIA-Linux-%{arch}-%{version}/nvidia-smi %{buildroot}/usr/lib/%{name}
install -m 755 ./NVIDIA-Linux-%{arch}-%{version}/libnvidia-ml.so.%{version} %{buildroot}/usr/lib/%{name}
ln -snf libnvidia-ml.so.%{version} %{buildroot}/usr/lib/%{name}/libnvidia-ml.so.1
%endif
%else
mkdir -p %{buildroot}%{_firmwaredir}/nvidia/%{version}
install -m 644 ./lib/firmware/nvidia/%{version}/{gsp_ga10x.bin,gsp_tu10x.bin} \
	%{buildroot}%{_firmwaredir}/nvidia/%{version}
%endif

%if 0%{simpletest} == 1
%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig
%endif

%files
%license LICENCE.nvidia
%dir %{_firmwaredir}/nvidia
%dir %{_firmwaredir}/nvidia/%{version}
%{_firmwaredir}/nvidia/%{version}/gsp_ga10x.bin
%{_firmwaredir}/nvidia/%{version}/gsp_tu10x.bin
%if 0%{simpletest} == 1 && %{without cuda}
%dir /usr/lib/%{name}
/usr/lib/%{name}/nvidia-smi
/usr/lib/%{name}/libnvidia-ml.so.%{version}
/usr/lib/%{name}/libnvidia-ml.so.1
%endif

%changelog
