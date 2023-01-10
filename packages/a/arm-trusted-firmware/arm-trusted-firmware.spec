#
# spec file for package arm-trusted-firmware
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


%global platform @BUILD_FLAVOR@%{nil}

%if "%{platform}" == "a3700" || "%{platform}" == "imx8mq"
# Debug build not supported for UART boot on a3700
# Debug build is too big on imx8mq, see: https://developer.trustedfirmware.org/T626
%global debug_build 0
%else
%global debug_build 1
%endif

%bcond_without A3700_tools

%bcond_with atf_optee

%if %{with atf_optee}
%define use_optee 1
%if "%{platform}" == "" || "%{platform}" == "tegra186" || "%{platform}" == "tegra210" || "%{platform}" == "rk3328" || "%{platform}" == "rk3368" || "%{platform}" == "rk3399" || "%{platform}" == "rpi4"
# OP-TEE not available
%define use_optee 0
%endif
%if "%{platform}" == "a3700" || "%{platform}" == "a80x0_mcbin" || "%{platform}" == "imx8qm" || "%{platform}" == "imx8qx" || "%{platform}" == "imx8mq" || "%{platform}" == "imx8mm" || "%{platform}" == "sun50i_a64" || "%{platform}" == "sun50i_h6" || "%{platform}" == "sun50i_h616" || "%{platform}" == "zynqmp"
# TBD
%define use_optee 0
%endif
%else
%define use_optee 0
%endif

%if "%{platform}" == ""
Name:           arm-trusted-firmware
%else
Name:           arm-trusted-firmware-%{platform}
%endif
Version:        2.7
Release:        0
%define srcversion 2.7
%define mv_ddr_ver armada-atf-master
%define mv_bin_ver 10.0.1.0
%define a3700_utils_ver master
Summary:        Arm Trusted Firmware-A
License:        BSD-3-Clause
Group:          System/Boot
URL:            https://www.trustedfirmware.org/
Source:         https://git.trustedfirmware.org/TF-A/trusted-firmware-a.git/snapshot/trusted-firmware-a-%{srcversion}.tar.gz
Source1:        mv-ddr-marvell-%{mv_ddr_ver}.tar.gz
Source2:        A3700-utils-marvell-%{a3700_utils_ver}.tar.gz
Source3:        binaries-marvell-%{mv_bin_ver}.tar.gz
Patch1:         atf-allow-non-git-dir.patch
Patch2:         rockchip-rk3399-Align-default-baudrate-with-u-boot.patch
Patch3:         Workaround-gcc-7-constant-assignment-error.patch
# Workaround for GCC12 bug - https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105523
Patch100:       fix-mv-ddr-marvell-armada.patch
# Fix build with GCC12 - https://github.com/MarvellEmbeddedProcessors/mv-ddr-marvell/issues/37
Patch101:       fix-a3700_tool.patch
Patch150:       A3700_utils-drop-git.patch
BuildRequires:  fdupes
%if "%{platform}" != ""
#!BuildIgnore: gcc-PIE
%endif
%if "%{platform}" == "a3700"
BuildRequires:  arm-trusted-firmware-tools
BuildRequires:  cross-arm-none-newlib-devel
BuildRequires:  gcc-c++
BuildRequires:  libcryptopp-devel
%endif
%if "%{platform}" == "a3700" || "%{platform}" == "rk3399"
BuildRequires:  cross-arm-none-gcc%{gcc_version}
%endif
%if "%{platform}" == "a80x0_mcbin" && 0
BuildRequires:  edk2-Armada80x0McBin
%endif
%if "%{platform}" == "hikey"
BuildRequires:  edk2-hikey
%endif
%if "%{platform}" == "hikey960"
BuildRequires:  edk2-hikey960
%endif
%if "%{platform}" == ""
BuildRequires:  gcc-c++
%endif
BuildRequires:  git
%if "%{platform}" == ""
BuildRequires:  libcryptopp-devel
%endif
BuildRequires:  libopenssl-devel
%if %{use_optee}
%if "%{platform}" == "qemu_sbsa"
BuildRequires:  optee-qemu-armv8a
%else
%if "%{platform}" == "a3700"
BuildRequires:  optee-armada3700
%else
%if "%{platform}" == "a80x0_mcbin"
BuildRequires:  optee-armada7k8k
%else
BuildRequires:  optee-%{platform}
%endif
%endif
%endif
%endif
%if "%{platform}" == "qemu"
BuildRequires:  qemu-uefi-aarch64
%endif
%if "%{platform}" == "rpi3" || "%{platform}" == "rpi4"
# For /boot/vc
BuildRequires:  raspberrypi-firmware
%endif
%if "%{platform}" == "a3700"
BuildRequires:  u-boot-mvebuespressobin-88f3720
%endif
%if "%{platform}" == "a80x0_mcbin" && 1
BuildRequires:  u-boot-mvebumcbin-88f8040
%endif
%if "%{platform}" == "hikey"
BuildRequires:  u-boot-hikey
%endif
%if "%{platform}" == "poplar"
BuildRequires:  u-boot-poplar
%endif
%if "%{platform}" == "rpi3"
BuildRequires:  u-boot-rpi3
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if "%{platform}" != ""
BuildArch:      noarch
ExclusiveArch:  aarch64
%endif

%if "%{platform}" == "rpi4"
Supplements:    modalias(of:N*T*Cbrcm%2Cbcm2711*C*)
%endif

%description
Trusted Firmware-A (TF-A) provides a reference implementation of secure world
software for Armv7-A and Armv8-A, including a Secure Monitor executing at
Exception Level 3 (EL3).

%if "%{platform}" == "poplar"
%package devel
Summary:        ARM Trusted Firmware -- %{platform} development files
Group:          System/Boot
Requires:       %{name} = %{version}

%description devel
ARM Trusted Firmware provides a reference implementation of
secure world software for ARMv8-A, including a Secure Monitor executing at
Exception Level 3 (EL3). It implements various ARM interface standards,
such as the Power State Coordination Interface (PSCI),
Trusted Board Boot Requirements (TBBR, ARM DEN0006C-1) and
SMC Calling Convention. As far as possible the code is designed for reuse
or porting to other ARMv8-A model and hardware platforms.

This sub-package contains development files.
%endif

%if "%{platform}" == ""
%package tools
Summary:        Tools for ARM Trusted Firmware-A
Group:          System/Boot

%description tools
Trusted Firmware-A (TF-A) provides a reference implementation of
secure world software for ARMv8-A, including a Secure Monitor executing at
Exception Level 3 (EL3). It implements various ARM interface standards,
such as the Power State Coordination Interface (PSCI),
Trusted Board Boot Requirements (TBBR, ARM DEN0006C-1) and
SMC Calling Convention. As far as possible the code is designed for reuse
or porting to other ARMv8-A model and hardware platforms.

This package contains fiptool.
%endif

%prep
%if "%{platform}" == "a3700" || "%{platform}" == "a80x0_mcbin"
%if "%{platform}" == "a3700"
%setup -q -n trusted-firmware-a-%{srcversion} -a 1 -a 2
%else
%setup -q -n trusted-firmware-a-%{srcversion} -a 1 -a 3
%endif
# git repo or branch.txt file are expected
echo "%{mv_ddr_ver}" > mv-ddr-marvell-%{mv_ddr_ver}/branch.txt
pushd mv-ddr-marvell-%{mv_ddr_ver}
%if %{suse_version} > 1550
# Workaround for GCC12 bug - https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105523
%patch100 -p1
%endif
%patch101 -p1
popd
%else
%if "%{platform}" == ""
%setup -q -n trusted-firmware-a-%{srcversion} -a 2
%else
%setup -q -n trusted-firmware-a-%{srcversion}
%endif
%endif
%if "%{platform}" == "" || "%{platform}" == "a3700"
pushd A3700-utils-marvell-%{a3700_utils_ver}
# git repo or branch.txt file are expected
echo "%{a3700_utils_ver}" >  branch.txt
%if "%{platform}" != ""
install -D -m 0755 %{_bindir}/TBB wtptp/linux/tbb_linux
%endif
%patch150 -p1
popd
%endif
%patch1 -p1
%patch2 -p1
%patch3 -p1
%if %{suse_version} <= 1500
# GCC7 does not support -mbranch-protection option
sed -i -e "s/TF_CFLAGS_aarch64	+=	-mbranch-protection=none//" plat/xilinx/zynqmp/platform.mk
%endif

%build
export TF_LDFLAGS=--no-warn-rwx-segments
export BUILD_MESSAGE_TIMESTAMP="\"$(date -d "$(head -n 2 %{_sourcedir}/arm-trusted-firmware.changes | tail -n 1 | cut -d- -f1 )" -u "+%%H:%%M:%%S, %%b %%e %%Y")\""
%if "%{platform}" == "a3700"
export CRYPTOPP_LIBDIR=%{_libdir}
export CRYPTOPP_INCDIR=%{_includedir}/cryptopp
%endif

%if "%{platform}" == ""
make %{?_smp_mflags} V=1 fiptool

%if %{with A3700_tools}
pushd A3700-utils-marvell-%{a3700_utils_ver}
make %{?_smp_mflags} -C wtptp/src/TBB_Linux -f TBB_linux.mak INCDIR=%{_includedir}/cryptopp LIBDIR=%{_libdir}
make %{?_smp_mflags} -C wtptp/src/Wtpdownloader_Linux -f makefile.mk
popd
%endif

%else
%if "%{platform}" == "a3700"
export CROSS_CM3=arm-none-eabi-
%define variants ebin_512M_spinor ebin_v3_1G_spinor ebin_v5_2G_spinor ebin_v7_1G_spinor ebin_v7_2G_spinor ebin_512M_sata ebin_v3_1G_sata ebin_v5_2G_sata ebin_v7_1G_sata ebin_v7_2G_sata
for variant in %{variants}; do
  partnum=0
  case "${variant}" in
  ebin_*)
    clockspreset=CPU_1000_DDR_800
    ;;
  esac
  case "${variant}" in
  ebin_512M_*)
    ddr_topology=0
    ;;
  ebin_v3_1G_*)
    ddr_topology=2
    ;;
  ebin_v5_2G_*)
    ddr_topology=7
    ;;
  ebin_v7_1G_*)
    ddr_topology=5
    ;;
  ebin_v7_2G_*)
    ddr_topology=6
    ;;
  esac
  case "${variant}" in
  *_emmc)    bootdev=EMMCNORM ;;
  *_sata)    bootdev=SATA ;;
  *_spinand) bootdev=SPINAND ;;
  *_spinor)  bootdev=SPINOR ;;
  esac
  make distclean
%endif
%if "%{platform}" == "poplar"
for dram_size in one_gig two_gig; do
%endif
%if 0%{suse_version} > 1550
# Workaround for GCC12 bug - https://gcc.gnu.org/bugzilla/show_bug.cgi?id=105523
export TF_CFLAGS="$TF_CFLAGS --param=min-pagesize=0"
export CFLAGS="$CFLAGS --param=min-pagesize=0"
# Workaround for binutils 2.39 https://developer.trustedfirmware.org/T996
export LDFLAGS="$LDFLAGS --no-warn-rwx-segment"
%endif
make \
%if "%{platform}" != "a3700" && "%{platform}" != "a80x0_mcbin"
     %{?_smp_mflags} \
%endif
     V=1 DISABLE_PEDANTIC=1 DEBUG=%{debug_build} \
%if "%{platform}" == "tegra186" || "%{platform}" == "tegra210"
%if "%{platform}" == "tegra186"
%define target_soc t186
%endif
%if "%{platform}" == "tegra210"
%define target_soc t210
%endif
     PLAT=tegra TARGET_SOC=%{target_soc} \
%else
     PLAT=%{platform} \
%endif
%if %{use_optee}
     SPD=opteed \
     BL32=/boot/tee-header_v2.bin \
     BL32_EXTRA1=/boot/tee-pager_v2.bin \
     BL32_EXTRA2=/boot/tee-pageable_v2.bin \
%endif
%if "%{platform}" == "a3700" || "%{platform}" == "a80x0_mcbin"
     LOG_LEVEL=30 \
     MV_DDR_PATH=$(pwd)/mv-ddr-marvell-%{mv_ddr_ver} \
%if "%{platform}" == "a3700"
     WTP=$(pwd)/A3700-utils-marvell-%{a3700_utils_ver} \
     CLOCKSPRESET=${clockspreset} DDR_TOPOLOGY=${ddr_topology} \
     USE_COHERENT_MEM=0 \
%if %{use_optee}
     LLC_ENABLE=1 LLC_SRAM=1 \
%endif
     BOOTDEV=${bootdev} PARTNUM=${partnum} \
     MARVELL_SECURE_BOOT=0 \
%endif
%if "%{platform}" == "a80x0_mcbin"
     SCP_BL2=$(pwd)/binaries-marvell-%{mv_bin_ver}/mrvl_scp_bl2.img \
%endif
%if "%{platform}" == "a80x0_mcbin" && 0
     BL33=/boot/ARMADA_EFI.fd \
%else
     BL33=/boot/u-boot.bin \
%endif
%if "%{platform}" == "a3700" || "%{platform}" == "a80x0_mcbin"
     mrvl_flash \
%if "%{platform}" == "a3700"
     mrvl_uart  \
%endif
%endif
     all fip
%if "%{platform}" == "a3700"
mv build build.${variant}
done
%endif
%else
%if "%{platform}" == "hikey"
     SCP_BL2=/boot/mcuimage.bin \
     BL33=/boot/u-boot.bin \
     all fip
%else
%if "%{platform}" == "hikey960"
     SCP_BL2=/boot/lpm3.img \
     BL33=/boot/BL33_AP_UEFI.fd \
     all fip
%else
%if "%{platform}" == "poplar"
     BL33=/boot/u-boot.bin \
     POPLAR_DRAM_SIZE=${dram_size} \
     all fip
mv build build.${dram_size}
make %{?_smp_mflags} V=1 DISABLE_PEDANTIC=1 DEBUG=%{debug_build} \
     PLAT=poplar POPLAR_RECOVERY=1 \
     BL33=/boot/u-boot.bin \
     POPLAR_DRAM_SIZE=${dram_size} \
     all fip
mv build build.${dram_size}.recovery
done
%else
%if "%{platform}" == "rpi3"
     BL33=/boot/vc/u-boot.bin \
     RPI3_PRELOADED_DTB_BASE=0x01000000 \
     RPI3_DIRECT_LINUX_BOOT=1 \
     RPI3_RUNTIME_UART=1 \
     all
%else
%if "%{platform}" == "qemu"
     BL33=%{_datadir}/qemu/qemu-uefi-aarch64.bin \
     all fip
%else
%if "%{platform}" == "qemu_sbsa"
     all fip
%else
     all
%endif
%endif
%endif
%endif
%endif
%endif
%endif
%endif

%install
%if "%{platform}" == ""
mkdir -p %{buildroot}%{_bindir}
install -m 755 tools/fiptool/fiptool %{buildroot}%{_bindir}/fiptool

%if %{with A3700_tools}
pushd A3700-utils-marvell-%{a3700_utils_ver}
# No need to have a _linux suffix on Linux
install -D -m 0755 wtptp/src/TBB_Linux/release/TBB_linux %{buildroot}%{_bindir}/TBB
install -D -m 0755 wtptp/src/Wtpdownloader_Linux/WtpDownload_linux %{buildroot}%{_bindir}/WtpDownload
popd
%endif
%else

export NO_BRP_STRIP_DEBUG=true
export NO_DEBUGINFO_STRIP_DEBUG=true

mkdir -p %{buildroot}%{_datadir}/%{name}

%if 0%{?debug_build}
%global dir debug
%else
%global dir release
%endif
%define outdir build/%{platform}/%{dir}
%if "%{platform}" == "tegra186" || "%{platform}" == "tegra210"
%define outdir build/tegra/%{target_soc}/%{dir}
%endif
%if "%{platform}" == "a3700"
for v in %{variants}; do
  outdir=build.${v}/%{platform}/%{dir}
  destdir=%{buildroot}%{_datadir}/%{name}/${v}
  install -D -m 0644 ${outdir}/bl1.bin ${destdir}/bl1.bin
  install -D -m 0644 ${outdir}/bl2.bin ${destdir}/bl2.bin
  install -D -m 0644 ${outdir}/bl31.bin ${destdir}/bl31.bin
  install -D -m 0644 ${outdir}/fip.bin ${destdir}/fip.bin
  install -D -m 0644 ${outdir}/flash-image.bin ${destdir}/flash-image.bin
  install -D -m 0644 ${outdir}/uart-images/TIM_ATF.bin ${destdir}/uart/TIM_ATF.bin
  install -D -m 0644 ${outdir}/uart-images/boot-image_h.bin ${destdir}/uart/boot-image_h.bin
  install -D -m 0644 ${outdir}/uart-images/wtmi_h.bin ${destdir}/uart/wtmi_h.bin
done
%else
%if "%{platform}" == "poplar"
for v in one_gig two_gig one_gig.recovery two_gig.recovery; do
  outdir=build.${v}/%{platform}/%{dir}
  destdir=%{buildroot}%{_datadir}/%{name}/${v}
  install -D -m 0644 ${outdir}/bl1.bin ${destdir}/bl1.bin
  install -D -m 0644 ${outdir}/fip.bin ${destdir}/fip.bin
done
mkdir -p %{buildroot}%{_includedir}/%{name}
install -D -m 0644 plat/hisilicon/poplar/include/poplar_layout.h %{buildroot}%{_includedir}/%{name}/
%else

# u-boot for rockchip requires bl31.elf file
%if "%{platform}" == "rk3328" || "%{platform}" == "rk3368" || "%{platform}" == "rk3399" || "%{platform}" == "zynqmp"
install -D -m 0644 %{outdir}/bl31/bl31.elf %{buildroot}%{_datadir}/%{name}/bl31.elf
%else
install -D -m 0644 %{outdir}/bl31.bin %{buildroot}%{_datadir}/%{name}/bl31.bin
%endif

%if "%{platform}" == "a80x0_mcbin" || "%{platform}" == "hikey" || "%{platform}" == "hikey960" || "%{platform}" == "qemu" || "%{platform}" == "qemu_sbsa" || "%{platform}" == "rpi3"
install -D -m 0644 %{outdir}/bl1.bin %{buildroot}%{_datadir}/%{name}/bl1.bin
install -D -m 0644 %{outdir}/fip.bin %{buildroot}%{_datadir}/%{name}/fip.bin
%endif
%if "%{platform}" == "a80x0_mcbin" || "%{platform}" == "hikey" || "%{platform}" == "hikey960" || "%{platform}" == "rpi3"
install -D -m 0644 %{outdir}/bl2.bin %{buildroot}%{_datadir}/%{name}/bl2.bin
%endif
%if "%{platform}" == "rpi3"
install -D -m 0644 %{outdir}/armstub8.bin %{buildroot}/boot/vc/armstub8.bin
%endif
%if "%{platform}" == "rpi4"
install -D -m 0644 %{outdir}/bl31.bin %{buildroot}/boot/vc/armstub8-rpi4.bin
%endif
%if "%{platform}" == "a80x0_mcbin"
install -D -m 0644 %{outdir}/ble.bin %{buildroot}%{_datadir}/%{name}/ble.bin
install -D -m 0644 %{outdir}/flash-image.bin %{buildroot}%{_datadir}/%{name}/flash-image.bin
%endif

%endif
%endif

%endif

%fdupes %{buildroot}%{_prefix}

%if "%{platform}" == "rpi3" || "%{platform}" == "rpi4"
%post
if mountpoint -q /boot/efi; then
  if ! [[ "$(readlink -f /boot/efi)" -ef "$(readlink -f /boot/vc)" ]]; then
    cp /boot/vc/armstub8* /boot/efi/
  fi
fi
%endif

%files
%defattr(-,root,root)
%license license.rst
%doc docs/about/acknowledgements.rst docs/process/contributing.rst docs/about/maintainers.rst readme.rst dco.txt
%if "%{platform}" != ""
%{_datadir}/%{name}
%endif
%if "%{platform}" == "rpi3" || "%{platform}" == "rpi4"
/boot/vc/armstub8*
%endif

%if "%{platform}" == ""
%files tools
%defattr(-,root,root)
%{_bindir}/fiptool
%if %{with A3700_tools}
%{_bindir}/TBB
%{_bindir}/WtpDownload
%endif
%endif

%if "%{platform}" == "poplar"
%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%endif

%changelog
