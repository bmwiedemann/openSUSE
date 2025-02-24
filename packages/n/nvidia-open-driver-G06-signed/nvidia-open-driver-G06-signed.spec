#
# spec file for package nvidia-open-driver-G06-signed
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


%define gfx_version 570.86.16
%define cuda_version 570.86.15

%global flavor @BUILD_FLAVOR@%{?nil}
%if "%{flavor}" == "cuda"
 %if 0%{?suse_version} > 1600
ExclusiveArch:  do_not_build
 %endif
%{bcond_without cuda}
%define mykind cuda
%define otherkind gfx
%else
%define mykind gfx
%define otherkind cuda
%endif
%if %{undefined kernel_module_directory}
%if 0%{?suse_version} >= 1550
%define kernel_module_directory /usr/lib/modules
%else
%define kernel_module_directory /lib/modules
%endif
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
%define compress_modules zstd
%else
%define compress_modules xz
%endif
Name:           nvidia-open-driver-G06-signed%{?with_cuda:-cuda}
%if %{with cuda}
Version:        %{cuda_version}
%else
Version:        %{gfx_version}
%endif

Release:        0
Summary:        NVIDIA open kernel module driver for GeForce 16 series (GTX 16xx) and newer
License:        GPL-2.0-only AND MIT
Group:          System/Kernel
URL:            https://github.com/NVIDIA/open-gpu-kernel-modules/
#Source0:        https://github.com/NVIDIA/open-gpu-kernel-modules/archive/refs/tags/%{version}.tar.gz#/open-gpu-kernel-modules-%{version}.tar.gz
Source0:        open-gpu-kernel-modules-%{version}.tar.gz
# This is defined at build, not for 'osc service run download_files` or
# factory_auto. This both sources are seen outside of the build but only
# the matching one will be included in the srpm for the respective flavor.
%if %{undefined linux_arch}
Source16:       https://github.com/NVIDIA/open-gpu-kernel-modules/archive/refs/tags/%{cuda_version}.tar.gz#/open-gpu-kernel-modules-%{cuda_version}.tar.gz
Source18:       pci_ids-%{cuda_version}
%endif
Source1:        my-find-supplements
Source2:        pci_ids-%{version}
Source3:        kmp-filelist
Source7:        preamble
Source8:        json-to-pci-id-list.py
# Generate:
# CUDA_VER=12.5.1; DRIVER_VER=%version; ARCH=...
# mkdir tmp
# wget https://developer.download.nvidia.com/compute/cuda/<cuda_ver>/local_installers/cuda_${CUDA_VER}_${DRIVER_VER}_linux.run -P ./tmp
# sh tmp/cuda_${CUDA_VER}_${DRIVER_VER}_linux.run --extract=$(pwd)/tmp
# cd tmp; sh ./NVIDIA-Linux-$ARCH-$DRIVER_VER.run -x; cd -
# ./json-to-pci-id-list.py --skiplegacy --kernelopen tmp/NVIDIA-Linux-${ARCH}-${DRIVER_VER}/supported-gpus/supported-gpus.json pci_ids-supported-$DRIVER_VER
Source10:       pci_ids-supported
Source11:       pesign-copy-sources
Source12:       pesign-spec-macros
Source14:       group-source-files.pl
Source15:       kmp-trigger.sh
Patch0:         persistent-nvidia-id-string.patch
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  kernel-source
BuildRequires:  kernel-syms
BuildRequires:  perl-Bootloader
BuildRequires:  pesign-obs-integration
BuildRequires:  zstd
%ifnarch aarch64
# available on SLE, but not on ALP ...
%if !0%{?is_opensuse} && 0%{?suse_version} < 1600
BuildRequires:  kernel-syms-azure
%endif
%endif
%if 0%{?is_opensuse} && 0%{?suse_version} >= 1699
# build KPMs for kernel-longterm in Factory
BuildRequires:  kernel-syms-longterm
%endif
ExclusiveArch:  x86_64 aarch64

%if 0%{!?kmp_template_name:1}
%define kmp_template_name /usr/lib/rpm/kernel-module-subpackage
%endif
%if 0%{!?_builddir:1}
%define _builddir /home/abuild/rpmbuild/BUILD
%endif

%(cat %kmp_template_name > %_builddir/nvidia-kmp-template)
%(echo "%triggerin -p /bin/bash -n %%{-n*}-kmp-%1 -- nvidia-common-G06 = %{version}"      >> %_builddir/nvidia-kmp-template)
%(cat %_sourcedir/kmp-trigger.sh                                                          >> %_builddir/nvidia-kmp-template)
%kernel_module_package -n %{name} -t %_builddir/nvidia-kmp-template -f %_sourcedir/kmp-filelist -p %_sourcedir/preamble
%{expand:%(
      for f in %{flavors_to_build}; do \
	  echo "%package -n %{name}-${f}-devel"; \
	  echo "Summary:      Devel Package to %name"; \
	  echo "%description -n %{name}-${f}-devel"; \
	  echo "Provide build requiresments to build against %{name}"; \
	  echo "%files -n %{name}-${f}-devel -f files-${f}"; \
      done)}

%package -n nv-prefer-signed-open-driver
%define version_major %(i=%{version}; echo ${i%%%%.*})
Summary:        Prefer the signed open driver when installing CUDA
Requires:       nvidia-open-driver-G06-signed-cuda-kmp
# This avoids the package being uninstallable when the CUDA repo is unavaliable preventing problems in staging
# Hard code version 555.42.06 as this requires is only needed for this version
# but since this meta package should apply to all versions.
Requires:       ( nvidia-compute-G06 = 555.42.06 if ( cuda-drivers = 555.42.06 or cuda-drivers-%version_major = 555.42.06) )

%description -n nv-prefer-signed-open-driver
By installing this package, the signed NVIDIA open driver built by SUSE will be preferred during installation
of CUDA components.
Simply run: `zypper install --no-recommends cuda-runtime-<version> nv-prefer-signed-open-driver`

%package -n kernel-firmware-nvidia-gspx-G06%{?with_cuda:-cuda}
Summary:        Kernel firmware file for open NVIDIA kernel module driver G06
Provides:       multiversion(kernel)
# Kill version 555 with a 'Conflicts: kernel-firmware-nvidia-gspx-G06'
Obsoletes:      kernel-firmware-nvidia-gspx-G06 < 560.35.03
Obsoletes:      kernel-firmware-nvidia-gsp-G06 = 535.86.05
Obsoletes:      kernel-firmware-nvidia-gspx-G06-cuda < 560.35.03
Requires:       (kernel-firmware-nvidia-gspx-G06 = %{version} if (nvidia-compute-utils-G06 = %{version} or nvidia-compute-G06 = %{version} or sle-module-NVIDIA-compute-release))
%if 0%{?sle_version} >= 150700
BuildArch:      noarch
%endif

%description -n kernel-firmware-nvidia-gspx-G06%{?with_cuda:-cuda}
This package fetches the versioned kernel firmware file "gsp.bin" for
the OpenSource NVIDIA kernel module driver G06 once it's available.

# SLE16 doesn't set %sle_version; SLE Micro 6.x is already SLE16 !!!
%if (0%{?sle_version:1} || (0%{?suse_version} == 1600 && !0%{?is_opensuse})) && %{with cuda}
%files -n kernel-firmware-nvidia-gspx-G06%{?with_cuda:-cuda}
%endif

%if %{with cuda}
%files -n nv-prefer-signed-open-driver
%endif
## create hardware supplements for manual builds
%{load:%{SOURCE12}}

# newer rpmbuilds attach the kernel version and the major part of release to %%pci_id_file of the __kmp_supplements script
# boo#1190210
%define kbuildver %(rpm -q --queryformat '%%{VERSION}_%%{RELEASE}' kernel-syms | sed -n 's/\\(.*\\)\\.[0-9]\\{1,\\}/\\1/p')

%description
This package provides the open-source NVIDIA kernel module driver
for GeForce 16 series (GTX 16xx) and newer GPUs, i.e. Turing GPU family
and newer (Turing, Ampere, Ada Lavelace, Hopper, Blackwell, ...).

%prep
%autosetup -p1 -n open-gpu-kernel-modules-%{version}

set -- *
mkdir source
mv "$@" source/
mkdir obj

pushd %_sourcedir
chmod 755 my-find-supplements*
%if %{with cuda}
# make sure it's empty for -cuda variant
rm  pci_ids-%{version}
touch  pci_ids-%{version}
%endif
# symlink the %pci_id_file to the one, that rpmbuild generates, to enable my-find-supplement to succeed properly
# boo#1190210
ln -sv pci_ids-%{version} pci_ids-%{version}_k%{kbuildver}
popd

%build
%ifarch aarch64
# -Wall is upstream default
export CFLAGS="-Wall -mno-outline-atomics"
%endif
# kernel was compiled using a different compiler
export CC=gcc
# no longer needed and never worked anyway (it was only a stub) [boo#1211892]
export NV_EXCLUDE_KERNEL_MODULES=nvidia-peermem
for flavor in %{flavors_to_build}; do
        rm -rf obj/$flavor
        cp -r source obj/$flavor
	pushd obj/$flavor
	if [ -d /usr/src/linux-$flavor ]; then
	  export SYSSRC=/usr/src/linux-$flavor
	else
	  export SYSSRC=/usr/src/linux
	fi
	export SYSOUT=/usr/src/linux-obj/%_target_cpu/$flavor
        make %{?_smp_mflags} modules
        popd
done

%install
export BRP_PESIGN_FILES="*.ko"
export BRP_PESIGN_COMPRESS_MODULE=%{compress_modules}
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=%{kernel_module_package_moddir}/%{name}-%{version}
for flavor in %{flavors_to_build}; do
	pushd obj/$flavor
	if [ -d /usr/src/linux-$flavor ]; then
	  export SYSSRC=/usr/src/linux-$flavor
	else
	  export SYSSRC=/usr/src/linux
	fi
	export SYSOUT=/usr/src/linux-obj/%_target_cpu/$flavor
        make modules_install
	popd
done

for flavor in %{flavors_to_build}; do
    mkdir -p %{buildroot}%{_prefix}/src/kernel-modules/nvidia-%{version}-${flavor}
    cp -r source/kernel-open/* %{buildroot}%{_prefix}/src/kernel-modules/nvidia-%{version}-${flavor}
    echo %dir %{_prefix}/src/kernel-modules > files-${flavor}
    perl %{S:14} -L %{buildroot}%{_prefix}/src/kernel-modules/nvidia-%{version}-${flavor} | sed -e "s@%{buildroot}@@" | sort -u >> files-${flavor}
    %fdupes -s %{buildroot}%{_prefix}/src/kernel-modules/nvidia-%{version}-${flavor}
done

%changelog
