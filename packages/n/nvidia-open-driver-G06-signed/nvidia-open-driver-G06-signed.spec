#
# spec file for package nvidia-open-driver-G06-signed
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


%if 0%{?suse_version} < 1550
%define hardcode_pci_list 1
%else
%define hardcode_pci_list 0
%endif

%if %{undefined kernel_module_directory}
%if 0%{?usrmerged}
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
Name:           nvidia-open-driver-G06-signed
Version:        525.85.05
Release:        0
Summary:        NVIDIA open kernel module driver for GeForce RTX 2000 series and newer
License:        GPL-2.0-only AND MIT
Group:          System/Kernel
URL:            https://github.com/NVIDIA/open-gpu-kernel-modules/
Source0:        open-gpu-kernel-modules-%{version}.tar.gz
Source1:        my-find-supplements
Source2:        pci_ids-%{version}
Source3:        kmp-filelist
Source4:        kmp-post.sh
Source5:        kmp-postun.sh
Source6:        modprobe.nvidia.install
Source7:        preamble
Source8:        json-to-pci-id-list.py
Source9:        pci_ids-unsupported-%{version}
Source10:       pci_ids-unsupported
Source11:       pesign-copy-sources
Source12:       pesign-spec-macros
Source13:       generati-pci-table.sh
Patch0:         0001-Don-t-override-INSTALL_MOD_DIR.patch
Patch2:         persistent-nvidia-id-string.patch
Patch3:         pci-table.patch
BuildRequires:  %{kernel_module_package_buildreqs}
BuildRequires:  gcc-c++
BuildRequires:  kernel-source
BuildRequires:  kernel-syms
BuildRequires:  perl-Bootloader
BuildRequires:  pesign-obs-integration
BuildRequires:  zstd
%ifnarch aarch64
%if 0%{?sle_version} >= 120400 && !0%{?is_opensuse}
BuildRequires:  kernel-syms-azure
%endif
%endif
ExclusiveArch:  x86_64 aarch64

%if 0%{!?kmp_template_name:1}
%define kmp_template_name /usr/lib/rpm/kernel-module-subpackage
%endif
%(sed -e '/^%%post\>/ r %_sourcedir/kmp-post.sh' -e '/^%%postun\>/ r %_sourcedir/kmp-postun.sh' %kmp_template_name >%_builddir/nvidia-kmp-template)
%kernel_module_package -n %{name} -t %_builddir/nvidia-kmp-template -f %_sourcedir/kmp-filelist -p %_sourcedir/preamble

%if ! 0%{hardcode_pci_list}
## create hardware supplements for manual builds
%{load:%{SOURCE12}}
%endif

# newer rpmbuilds attach the kernel version and the major part of release to %%pci_id_file of the __kmp_supplements script
# boo#1190210
%define kbuildver %(rpm -q --queryformat '%%{VERSION}_%%{RELEASE}' kernel-syms | sed -n 's/\\(.*\\)\\.[0-9]\\{1,\\}/\\1/p')

%description
This package provides the open-source NVIDIA kernel module driver
for GeForce RTX 2000 series and newer GPUs.

%prep
%setup -q -n open-gpu-kernel-modules-%{version}
%patch0 -p1
%patch2 -p1
%if 0%{hardcode_pci_list}
%patch3 -p0
pushd kernel-open
%if 0%{?suse_version} >= 1550
sh %{SOURCE13} %{SOURCE2}
%else
sh %{SOURCE13} %{SOURCE9}
%endif
popd
%endif
set -- *
mkdir source
mv "$@" source/
mkdir obj

pushd %_sourcedir
chmod 755 my-find-supplements*
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
        make %{?_smp_mflags} %{?linux_make_arch} modules
        popd
done

%install
export BRP_PESIGN_FILES="*.ko"
export BRP_PESIGN_COMPRESS_MODULE=%{compress_modules}
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
for flavor in %{flavors_to_build}; do
	pushd obj/$flavor
	if [ -d /usr/src/linux-$flavor ]; then
	  export SYSSRC=/usr/src/linux-$flavor
	else
	  export SYSSRC=/usr/src/linux
	fi
	export SYSOUT=/usr/src/linux-obj/%_target_cpu/$flavor
        make %{?linux_make_arch} modules_install
	popd
done

%if 0%{?suse_version} >= 1550
MODPROBE_DIR=%{buildroot}/usr/lib/modprobe.d
%else
MODPROBE_DIR=%{buildroot}%{_sysconfdir}/modprobe.d
%endif

mkdir -p $MODPROBE_DIR
for flavor in %flavors_to_build; do
    cat > $MODPROBE_DIR/50-nvidia-$flavor.conf << EOF
blacklist nouveau
options nvidia-drm modeset=1
### Enable support on *all* Turing/Ampere GPUs: Alpha Quality!
%if 0%{hardcode_pci_list}
%if 0%{?suse_version} >= 1550
#options nvidia NVreg_OpenRmEnableUnsupportedGpus=1
%else
options nvidia NVreg_OpenRmEnableUnsupportedGpus=1
%endif
%else
#options nvidia NVreg_OpenRmEnableUnsupportedGpus=1
%endif
EOF
    echo -n "install nvidia " >> $MODPROBE_DIR/50-nvidia-$flavor.conf
    tail -n +3 %_sourcedir/modprobe.nvidia.install | awk '{ printf "%s ", $0 }' >> $MODPROBE_DIR/50-nvidia-$flavor.conf
# otherwise nvidia-uvm is missing in initrd and won't get loaded when nvidia
# module is loaded in initrd; so better let's load all the nvidia modules
# later ...
%if 0%{?suse_version} >= 1550
  mkdir -p %{buildroot}/usr/lib/dracut/dracut.conf.d
  cat  >   %{buildroot}/usr/lib/dracut/dracut.conf.d/60-nvidia-$flavor.conf << EOF
%else
  mkdir -p %{buildroot}/etc/dracut.conf.d
  cat  > %{buildroot}/etc/dracut.conf.d/60-nvidia-$flavor.conf << EOF
%endif
omit_drivers+=" nvidia nvidia-drm nvidia-modeset nvidia-uvm "
EOF
done

%changelog
