#
# spec file for package nvidia-jetson-36_3
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


%if %{undefined kernel_module_directory}
%if 0%{?usrmerged}
%define kernel_module_directory /usr/lib/modules
%else
%define kernel_module_directory /lib/modules
%endif
%endif

%define compress_modules zstd
Name:           nvidia-jetson-36_3
Version:        36.3.1_20240516220919
Release:        0
Summary:        Open-Source NVIDIA Jetson Orin graphics drivers
License:        GPL-2.0-only AND MIT
Group:          System/Kernel
URL:            https://developer.nvidia.com/embedded/jetson-linux-r363
Source0:        nvidia-oot-l4t-l4t-r36.3.1_eng_2024-05-29.tar.bz2
Source1:        kmp-post-extra.sh
Source2:        kmp-postun-extra.sh
Source3:        kmp-filelist
Source4:        kmp-post.sh
Source5:        kmp-postun.sh
Source7:        preamble
Source8:        kmp-filelist-extra
Source9:        preamble-extra
Source14:       _constraints
Source22:       nvgpu-l4t-l4t-r36.3.1_eng_2024-05-29.tar.bz2
Source23:       hwpm-l4t-l4t-r36.3.1_eng_2024-05-29.tar.bz2
Source24:       nvdisplay-l4t-l4t-r36.3.1_eng_2024-05-29.tar.bz2
Source25:       nvethernetrm-l4t-l4t-r36.3.1_eng_2024-05-29.tar.bz2
Source26:       hardware_nvidia_t23x_nv-public-l4t-l4t-r36.3.1_eng_2024-05-29.tar.bz2
Source27:       hardware_nvidia_tegra_nv-public-l4t-l4t-r36.3.1_eng_2024-05-29.tar.bz2
Source28:       Makefile-NVIDIA-BUG-4460318
#Source30:       https://developer.nvidia.com/downloads/igx/v1.0.0/jetson_linux_r36.3.1_aarch64.tbz2
Source30:       nvidia-l4t-firmware_36.3.1-20240516220919_arm64.tbz2
# Create on SolidDriver Program build service with ...
# osc buildlog SLE_15_SP6 aarch64 | grep "missing supported flag" | sed -E 's|.*/([^/]+\.ko).*|\1 external|' | sort | uniq > Module.supported
# Unfortunately this is currently not working when building on build.suse.de
# But dracut file below could be used for information as well ...
Source29:       Module.supported
Patch0:         micro6-kernel.patch
Patch1:         reimplement-v4l2_match_dv_timings.patch
Patch2:         persistent-nvidia-id-string.patch
Patch3:         nv_repackager-no-sudo-use-bzip2.patch
Patch4:         df9e50c.diff
Patch5:         ASoC-tegra-Fix-redefinition-error-for-Linux-v6.11.patch
Patch6:         drivers-pva-Fix-build-for-Linux-v6.11.patch
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  kernel-source
BuildRequires:  kernel-syms
BuildRequires:  perl-Bootloader
BuildRequires:  pesign-obs-integration
BuildRequires:  zstd
ExclusiveArch:  aarch64

%if 0%{!?kmp_template_name:1}
%define kmp_template_name /usr/lib/rpm/kernel-module-subpackage
%endif
%(sed -e '/^%%post\>/ r %_sourcedir/kmp-post.sh' -e '/^%%postun\>/ r %_sourcedir/kmp-postun.sh' %kmp_template_name >%_builddir/nvidia-kmp-template)
%(sed -e '/^%%post\>/ r %_sourcedir/kmp-post-extra.sh' -e '/^%%postun\>/ r %_sourcedir/kmp-postun-extra.sh' %kmp_template_name >%_builddir/nvidia-kmp-extra-template)
%kernel_module_package -n %{name} -t %_builddir/nvidia-kmp-template -f %_sourcedir/kmp-filelist -p %_sourcedir/preamble
%kernel_module_package -n %{name}-extra -t %_builddir/nvidia-kmp-extra-template -f %_sourcedir/kmp-filelist-extra -p %_sourcedir/preamble-extra
%define kver %(for dir in /usr/src/linux-obj/*/*/; do make %{?jobs:-j%jobs} -s -C "$dir" kernelversion 2>/dev/null; break; done |perl -ne '/(\\d+)\\.(\\d+)\\.(\\d+)?/&&printf "%%d%%02d%%03d\\n",$1,$2,$3')

%description
This package provides the Open-Source NVIDIA Jetson Orin graphics drivers.
This requires the additional Open-Source NVIDIA Jetson Orin drivers
(nvidia-jetson-36_3-extra KMP) but conflicts with the traditional graphics
drivers for dedicated GPUs (nvidia-driver-G06-kmp,
nvidia-open-driver-G06-signed-kmp) due to kernel module name conflicts.

### needs to be set in preamble-extra
#Summary:        Open-Source NVIDIA Jetson Orin drivers

%description -n nvidia-jetson-36_3-extra-kmp-default
This package provides additional Open-Source NVIDIA Jetson Orin drivers,
which are also required by the NVIDIA Jetson Orin graphics drivers
(nvidia-jetson-36_3 KMP).

### needs to be set in preamble-extra
#Summary:        Open-Source NVIDIA Jetson Orin drivers

%description -n nvidia-jetson-36_3-extra-kmp-64kb
This package provides additional Open-Source NVIDIA Jetson Orin drivers,
which are also required by the NVIDIA Jetson Orin graphics drivers
(nvidia-jetson-36_3 KMP).

%package -n kernel-firmware-nvidia-jetson-36_3
Summary:        Firmware files for NVIDIA Jetson Orin (graphics) drivers
Group:          System/Kernel
Provides:       kernel-firmware-nvidia-jetson = %{version}
Obsoletes:      kernel-firmware-nvidia-jetson < %{version}

%description -n kernel-firmware-nvidia-jetson-36_3
This package includes the needed firmware files for NVIDIA Jetson
Orin (graphics) drivers.

%prep
echo suse_version: %suse_version
echo sle_version: %sle_version
echo "kver: %kver"
%setup -q -n src -c src -a 22 -a 23 -a 24 -a 26 -a 27
pushd nvidia-oot/drivers/net/ethernet/nvidia/nvethernet
tar xf %{SOURCE25}
popd
cp $RPM_SOURCE_DIR/Makefile-NVIDIA-BUG-4460318 Makefile
# needed for SL Micro 6.0 (SUSE:ALP:Source:Standard:1.0) Kernel, but not for
# sle15-sp6 Kernel !!!
%if 0%{?suse_version} == 1600
%patch0 -p0
pushd nvidia-oot
%patch5 -p1
%patch6 -p1
popd
%endif
%patch1 -p1
%patch2 -p1
pushd nvidia-oot
%patch4 -p1
popd

set -- *
mkdir source
mv "$@" source/

cp $RPM_SOURCE_DIR/Module.supported source/
for dir in nvdisplay nvgpu hwpm nvidia-oot hardware hwpm/drivers/tegra/hwpm nvgpu/drivers/gpu/nvgpu; do
 cp source/Module.supported source/${dir}/
done

mkdir obj

pushd ..
#tar xf %{SOURCE30}
#cd Linux_for_Tegra
#%%patch3 -p1
#./nv_tools/scripts/nv_repackager.sh -o ./nv_tegra/l4t_tar_packages --convert-all
#popd

%build
# -Wall is upstream default
export CFLAGS="-Wall -mno-outline-atomics"
# kernel was compiled using a different compiler
export CC=gcc
echo "flavors to build: %{flavors_to_build}"
for flavor in %{flavors_to_build}; do
        rm -rf obj/$flavor
        cp -r source obj/$flavor
	pushd obj/$flavor
        KREL=$(make -siC %{kernel_source $flavor} kernelrelease)
        export KERNEL_HEADERS=/lib/modules/$KREL/source
        export  KERNEL_OUTPUT=/lib/modules/$KREL/build
        make %{?_smp_mflags} %{?linux_make_arch} modules
        popd
done

%install
export BRP_PESIGN_FILES="*.ko"
export BRP_PESIGN_COMPRESS_MODULE=%{compress_modules}
export INSTALL_MOD_PATH=%{buildroot}
for flavor in %{flavors_to_build}; do
	pushd obj/$flavor
	KREL=$(make -siC %{kernel_source $flavor} kernelrelease)
	export KERNEL_HEADERS=/lib/modules/$KREL/source
	export  KERNEL_OUTPUT=/lib/modules/$KREL/build
        make %{?linux_make_arch} modules_install
	popd
done

MODPROBE_DIR=%{buildroot}/lib/modprobe.d

mkdir -p $MODPROBE_DIR
for flavor in %flavors_to_build; do
    cat > $MODPROBE_DIR/50-nvidia-$flavor.conf << EOF
options nvidia-drm modeset=0
blacklist nvethernet
options nvidia NVreg_DeviceFileUID=0 NVreg_DeviceFileGID=REALGID NVreg_DeviceFileMode=0660 rm_firmware_active="all" NVreg_RegistryDwords="RMHdcpKeyglobZero=1"
install nvidia /sbin/modprobe tegra_drm; /sbin/modprobe --ignore-install nvidia; /sbin/modprobe nvidia-modeset
EOF
    mkdir -p %{buildroot}/usr/lib/dracut/dracut.conf.d
    dracutfile=%{buildroot}/usr/lib/dracut/dracut.conf.d/60-nvidia-jetson-36_3-$flavor.conf
    dracutfile_extra=%{buildroot}/usr/lib/dracut/dracut.conf.d/60-nvidia-jetson-36_3-extra-$flavor.conf
    cat > ${dracutfile} << EOF
add_drivers+=" nvidia-drm nvidia-modeset nvidia "
EOF
    cat > ${dracutfile_extra}
# SL Micro 6.0 (SUSE:ALP:Source:Standard:1.0)
%if 0%{?suse_version} == 1600
    drivers=$(find %{buildroot}/usr/lib/modules/*-${flavor}/updates -name "*.ko*"|grep -v -E "nvidia-drm.ko|nvidia-modeset.ko|nvidia.ko")
%else
    drivers=$(find %{buildroot}/lib/modules/*-${flavor}/updates -name "*.ko*"|grep -v -E "nvidia-drm.ko|nvidia-modeset.ko|nvidia.ko")
%endif
    for driver in ${drivers}; do
        dname=$(basename $driver|sed 's/.ko.*//g')
        if [ "$dname" == "tegra-drm" ]; then
            echo "add_drivers+=${dname}" >> ${dracutfile_extra}
        else
            echo "omit_drivers+=${dname}" >> ${dracutfile_extra}
        fi
    done
    mkdir -p %{buildroot}/usr/lib/modules-load.d/
    cat > %{buildroot}/usr/lib/modules-load.d/nvidia-load-${flavor}.conf << EOF
nvidia
EOF
done

#pushd ../Linux_for_Tegra/nv_tegra/l4t_tar_packages
#  tar xjf nvidia-l4t-firmware_*_arm64.tbz2 -C $RPM_BUILD_ROOT/
#popd
tar xjf $RPM_SOURCE_DIR/nvidia-l4t-firmware_*_arm64.tbz2 -C $RPM_BUILD_ROOT/

pushd $RPM_BUILD_ROOT/
# etc/systemd/
mkdir -p usr/lib/systemd
mv  etc/systemd/*  usr/lib/systemd
sed -i 's+/etc+/usr/lib+g' usr/lib/systemd/system/nvwifibt.service
rmdir etc/systemd
rmdir etc
# lib/systemd/system/bluetooth.service/
mv lib/systemd/system/bluetooth.service.d usr/lib/systemd/system
rmdir lib/systemd/system
rmdir lib/systemd
# usr/share/doc
mkdir -p usr/share/doc/packages/kernel-firmware-nvidia-jetson-36_3
mv usr/share/doc/{bluez,nvidia-l4t-firmware,nvidia-tegra} usr/share/doc/packages/kernel-firmware-nvidia-jetson-36_3
ln -snf service usr/sbin/rcnvwifibt
popd

%fdupes -s %{buildroot}/lib/firmware

%files -n kernel-firmware-nvidia-jetson-36_3
%doc /usr/share/doc/packages/kernel-firmware-nvidia-jetson-36_3/
/lib/firmware/
/usr/lib/systemd/
/usr/sbin/brcm_patchram_plus
/usr/sbin/rcnvwifibt

%changelog
