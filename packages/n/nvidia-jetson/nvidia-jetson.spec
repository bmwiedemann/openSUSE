#
# spec file for package nvidia-jetson
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

%if %{undefined kernel_module_directory}
%if 0%{?usrmerged}
%define kernel_module_directory /usr/lib/modules
%else
%define kernel_module_directory /lib/modules
%endif
%endif

%define compress_modules zstd
Name:           nvidia-jetson
Version:        36.4.0_20240912212859
Release:        0
Summary:        Open-Source NVIDIA Jetson Orin graphics drivers
License:        GPL-2.0-only AND MIT
Group:          System/Kernel
URL:            https://developer.nvidia.com/embedded/jetson-linux-r3640
Source0:        nvidia-oot-l4t-l4t-r36.4_eng_2024-09-12.tar.bz2
Source1:        kmp-post-extra.sh
Source2:        kmp-postun-extra.sh
Source3:        kmp-filelist
Source4:        kmp-post.sh
Source5:        kmp-postun.sh
Source6:        kmp-preun.sh
Source7:        preamble
Source8:        kmp-filelist-extra
Source9:        preamble-extra
Source10:       load-nvidia-drm.service
Source14:       _constraints
Source22:       nvgpu-l4t-l4t-r36.4_eng_2024-09-12.tar.bz2
Source23:       hwpm-l4t-l4t-r36.4_eng_2024-09-12.tar.bz2
Source24:       nvdisplay-l4t-l4t-r36.4_eng_2024-09-12.tar.bz2
Source25:       nvethernetrm-l4t-l4t-r36.4_eng_2024-09-12.tar.bz2
Source26:       hardware_nvidia_t23x_nv-public-l4t-l4t-r36.4_eng_2024-09-12.tar.bz2
Source27:       hardware_nvidia_tegra_nv-public-l4t-l4t-r36.4_eng_2024-09-12.tar.bz2
Source28:       Makefile-NVIDIA-BUG-4460318
# Create on SolidDriver Program build service with ...
# osc buildlog SLE_15_SP6 aarch64 | grep "missing supported flag" | sed -E 's|.*/([^/]+\.ko).*|\1 external|' | sort | uniq > Module.supported
# Unfortunately this is currently not working when building on build.suse.de
# But dracut file below could be used for information as well ...
Source29:       Module.supported
Patch1:         reimplement-v4l2_match_dv_timings.patch
Patch2:         persistent-nvidia-id-string.patch
Patch4:         dracut-crash-fix.patch
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  kernel-source
BuildRequires:  kernel-syms
BuildRequires:  kmod
BuildRequires:  perl-Bootloader
BuildRequires:  pesign-obs-integration
BuildRequires:  pkgconfig(systemd)
BuildRequires:  zstd
ExclusiveArch:  aarch64

%if 0%{!?kmp_template_name:1}
%define kmp_template_name /usr/lib/rpm/kernel-module-subpackage
%endif
%(sed -e '/^%%post\>/ r %_sourcedir/kmp-post.sh' -e '/^%%postun\>/ r %_sourcedir/kmp-postun.sh' -e '/^%%preun\>/ r %_sourcedir/kmp-preun.sh' %kmp_template_name >%_builddir/nvidia-kmp-template)
%(sed -e '/^%%post\>/ r %_sourcedir/kmp-post-extra.sh' -e '/^%%postun\>/ r %_sourcedir/kmp-postun-extra.sh' %kmp_template_name >%_builddir/nvidia-kmp-extra-template)
%kernel_module_package -n %{name}-36_4 -t %_builddir/nvidia-kmp-template -f %_sourcedir/kmp-filelist -p %_sourcedir/preamble
%kernel_module_package -n %{name}-36_4-extra -t %_builddir/nvidia-kmp-extra-template -f %_sourcedir/kmp-filelist-extra -p %_sourcedir/preamble-extra
%define kver %(for dir in /usr/src/linux-obj/*/*/; do make %{?jobs:-j%jobs} -s -C "$dir" kernelversion 2>/dev/null; break; done |perl -ne '/(\\d+)\\.(\\d+)\\.(\\d+)?/&&printf "%%d%%02d%%03d\\n",$1,$2,$3')

%description
This package provides the Open-Source NVIDIA Jetson Orin graphics drivers.
This requires the additional Open-Source NVIDIA Jetson Orin drivers
(nvidia-jetson-36_4-extra KMP) but conflicts with the traditional graphics
drivers for dedicated GPUs (nvidia-driver-G06-kmp,
nvidia-open-driver-G06-signed-kmp) due to kernel module name conflicts.

### needs to be set in preamble-extra
#Summary:        Open-Source NVIDIA Jetson Orin drivers
%description -n nvidia-jetson-36_4-extra-kmp-default
This package provides additional Open-Source NVIDIA Jetson Orin drivers,
which are also required by the NVIDIA Jetson Orin graphics drivers
(nvidia-jetson-36_4 KMP).

### needs to be set in preamble-extra
#Summary:        Open-Source NVIDIA Jetson Orin drivers
%description -n nvidia-jetson-36_4-extra-kmp-64kb
This package provides additional Open-Source NVIDIA Jetson Orin drivers,
which are also required by the NVIDIA Jetson Orin graphics drivers
(nvidia-jetson-36_4 KMP).

%prep
echo suse_version: %suse_version
echo sle_version: %sle_version
echo "kver: %kver"
%setup -q -n src -c src -a 22 -a 23 -a 24 -a 26 -a 27
pushd nvidia-oot/drivers/net/ethernet/nvidia/nvethernet
tar xf %{SOURCE25} 
popd
cp $RPM_SOURCE_DIR/Makefile-NVIDIA-BUG-4460318 Makefile
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
# IGX needs 0 for modeset; patched during installation
options nvidia-drm modeset=1 fbdev=1
options nvidia NVreg_DeviceFileUID=0 NVreg_DeviceFileGID=REALGID NVreg_DeviceFileMode=0660 rm_firmware_active="all" NVreg_RegistryDwords="RMHdcpKeyglobZero=1"
EOF
    ### Using systemd service file for loading "nvidia-drm" doesn't
    ### work on SLE Micro 6.0 for some reason, but apparently this
    ### line helps
    ### Update: On some sle15-sp6 AGP system this extra line is also needed
    cat >> $MODPROBE_DIR/50-nvidia-$flavor.conf << EOF
install nvidia /sbin/rmmod tegra_drm; /sbin/modprobe --ignore-install nvidia; /sbin/modprobe tegra_drm
EOF
    cat > $MODPROBE_DIR/50-nvidia-extra-$flavor.conf << EOF
blacklist dwmac_tegra
blacklist snd-soc-tegra-audio-graph-card
EOF
    mkdir -p %{buildroot}/usr/lib/dracut/dracut.conf.d
    dracutfile=%{buildroot}/usr/lib/dracut/dracut.conf.d/60-nvidia-jetson-36_4-$flavor.conf
    dracutfile_extra=%{buildroot}/usr/lib/dracut/dracut.conf.d/60-nvidia-jetson-36_4-extra-$flavor.conf
    cat > ${dracutfile} << EOF
omit_drivers+=" nvidia-drm nvidia-modeset nvidia "
EOF
    cat > ${dracutfile_extra} 
# SL Micro 6.0 (SUSE:ALP:Source:Standard:1.0) 
%if 0%{?suse_version} == 1600
    drivers=$(find %{buildroot}/usr/lib/modules/*-${flavor}/updates -name "*.ko*"|grep -v -E "nvidia-drm.ko|nvidia-modeset.ko|nvidia.ko")
%else
    drivers=$(find %{buildroot}/lib/modules/*-${flavor}/updates -name "*.ko*"|grep -v -E "nvidia-drm.ko|nvidia-modeset.ko|nvidia.ko")
%endif
    for driver in ${drivers}; do 
        #dname=$(basename $driver|sed 's/.ko.*//g')
        dname=$(/sbin/modinfo -F name $driver)
        echo "omit_drivers+=\" ${dname} \"" >> ${dracutfile_extra}
    done
    mkdir -p %{buildroot}/usr/lib/systemd/system
    install -m 644 %{SOURCE10} %{buildroot}/usr/lib/systemd/system/load-nvidia-drm-$flavor.service
    mkdir -p %{buildroot}%{_systemd_util_dir}/system-preset
    cat >    %{buildroot}%{_systemd_util_dir}/system-preset/70-nvidia-jetson-36_4-kmp-${flavor}.preset << EOF
enable load-nvidia-drm-${flavor}.service
EOF
done

%changelog
