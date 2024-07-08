#
# spec file for package installation-images
#
# Copyright (c) 2020 SUSE LLC
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
# needsrootforbuild
# needsbinariesforbuild

# This is for building a test iso for debugging. Note when building
# locally with osc you need --nopreinstallimage --userootforbuild
%bcond_with iso

# The files from i-i are, in parts, extracted and published in the FTP Tree
# Since they are all auto-generated files, so they keep on changing. Having the mtime
# constant though causes issues for rsync - which uses this information by default to decide
# wether there is something to sync or not
%global clamp_mtime_to_source_date_epoch 0

# do not build 32-bit s390
ExcludeArch:    s390

%if "@BUILD_FLAVOR@" == ""
ExclusiveArch:  do_not_build
%endif

%global flavor @BUILD_FLAVOR@%nil

%define with_vbox 0
%define with_plymouth 1
%define with_shim 1
%define with_storage_ng 1
%define with_fips 1
%define with_exfat 0
%define with_kernel_extra 0
%bcond_without sbl
%bcond_without vnc
%bcond_with xen
%bcond_with xenkmp

# ===  Repo arch may differ from OBS build arch  ===

%define the_arch %{_target_cpu}
%ifarch ppc64 ppc64le
%define the_arch ppc
%endif
%ifarch s390x
%define the_arch zsystems
%endif
%ifarch riscv64
%define the_arch riscv
%endif

# ===  sort out which flavor to build  ===

%if "%flavor" == "openSUSE"
%if 0%{?is_opensuse}
%define theme openSUSE
%if 0%{?sle_version}
%define with_kernel_extra 1
# define the_version %(echo %sle_version | sed -Ee 's/^([0-9][0-9])(0|([0-9]))([0-9]).*/\\1.\\3\\4/')
%define the_version \\$releasever
%if "%{the_version}" == ""
%error "bad version string"
%endif
%ifarch %arm
%define net_repo https://download.opensuse.org/ports/%{the_arch}/distribution/leap/%{the_version}/repo/oss
%else
%define net_repo https://download.opensuse.org/distribution/leap/%{the_version}/repo/oss
%endif
%else
%define with_exfat 1
%ifarch %arm aarch64 ppc64 ppc64le riscv64 s390x
%define net_repo https://download.opensuse.org/ports/%{the_arch}/tumbleweed/repo/oss/
%else
%define net_repo https://download.opensuse.org/tumbleweed/repo/oss
%endif
%endif
%endif
%endif

%if "%flavor" == "Slowroll"
%define theme Slowroll
%define product_name_suffix -Slowroll
%define net_repo https://download.opensuse.org/slowroll/repo/oss
%endif

%if "%flavor" == "SMO"
%if 0%{?is_smo}
# build for both Leap and SLE
%if 0%{?sle_version}
%ifnarch %ix86
%define theme SMO
%endif
%endif
%endif
%endif

%if "%flavor" == "LeapMicro"
# build only on Leap
%if 0%{?is_opensuse} && 0%{?sle_version}
%define theme LeapMicro
%endif
%endif

%if "%flavor" == "MicroOS"
# don't build on Leap for now
%if 0%{?is_opensuse} && !0%{?sle_version}
%ifnarch %ix86
%define theme MicroOS
%endif
%endif
%endif

%if "%flavor" == "SLED"
# build SLED only on x86_64
%if "%{_target_cpu}" == "x86_64" && 0%{?sle_version} && !0%{?is_opensuse}
%define theme SLED
%endif
%endif

%if "%flavor" == "SLES"
%if 0%{?sle_version} && !0%{?is_opensuse}
%ifnarch %ix86
%define theme SLES
%endif
%endif
%endif

%if "%flavor" == "SLES_SAP"
%if 0%{?sle_version} && 0%{?is_susesap} && ( "%{_target_cpu}" == "x86_64" || "%{_target_cpu}" == "ppc64le" )
%define theme SLES_SAP
%endif
%endif

%if "%flavor" == "CAASP"
%if 0%{?is_susecaasp}
%ifnarch %ix86
%define theme CAASP
%endif
%endif
%endif

# ===  set product string (based on required packages)  ===

%global product_name %(bash %_sourcedir/product_name)%{?product_name_suffix}

# ===  define each theme  ===

%if "%{?theme}" == ""
ExclusiveArch:  do_not_build
%endif

%if "%theme" == "openSUSE"
%define with_storage_ng 1
%define with_fips 0
%define branding_skelcd   openSUSE
%define branding_systemd  openSUSE
%define branding_plymouth openSUSE
%define branding_grub2    openSUSE
%define branding_gfxboot  openSUSE
BuildRequires:  adobe-sourcesanspro-fonts
BuildRequires:  openSUSE-release
BuildRequires:  susepaste
%if 0%{?is_opensuse} && !0%{?sle_version}
BuildRequires:  distribution-logos-openSUSE-Tumbleweed
%else
BuildRequires:  distribution-logos-openSUSE-Leap
%endif
%endif

%if "%theme" == "Slowroll"
%define with_storage_ng 1
%define with_fips 0
%define branding_skelcd   openSUSE-Slowroll
%define branding_systemd  openSUSE
%define branding_plymouth openSUSE
%define branding_grub2    openSUSE
%define branding_gfxboot  openSUSE
BuildRequires:  adobe-sourcesanspro-fonts
BuildRequires:  openSUSE-release
BuildRequires:  susepaste
BuildRequires:  distribution-logos-openSUSE-Slowroll
%endif

%if "%theme" == "SMO" || "%theme" == "LeapMicro"
%define with_storage_ng 1
%define branding_skelcd   SMO
%define branding_systemd  SMO
%if "%theme" == "LeapMicro"
%define with_fips 0
BuildRequires:  Leap-Micro-release
BuildRequires:  distribution-logos-openSUSE-LeapMicro
%define branding_plymouth openSUSE
%define branding_grub2    openSUSE
%define branding_gfxboot  openSUSE
%else
BuildRequires:  SLE-Micro-release
%define branding_plymouth SLE
%define branding_grub2    SLE
%define branding_gfxboot  SLE
%endif
%define config_bootmenu_no_upgrade 1
# system-group-kvm needed for 15-SP2 based MicroOS
BuildRequires:  system-group-kvm
%endif

%if "%theme" == "MicroOS"
%define with_storage_ng 1
%define with_fips 0
%define branding_skelcd   MicroOS
%define branding_systemd  MicroOS
%define branding_plymouth openSUSE
%define branding_grub2    openSUSE
%define branding_gfxboot  openSUSE
%define config_bootmenu_no_upgrade 1
BuildRequires:  MicroOS-release
BuildRequires:  adobe-sourcesanspro-fonts
BuildRequires:  distribution-logos-openSUSE-MicroOS
%endif

%if "%theme" == "SLED"
%define branding_skelcd   leanos
%define branding_systemd  SLE
%define branding_plymouth SLE
%define branding_grub2    SLE
%define branding_gfxboot  SLE
BuildRequires:  unified-installer-release
%endif

%if "%theme" == "SLES"
%define branding_skelcd   leanos
%define branding_systemd  SLE
%define branding_plymouth SLE
%define branding_grub2    SLE
%define branding_gfxboot  SLE
BuildRequires:  skelcd-fallbackrepo-SLES
BuildRequires:  system-role-common-criteria
%ifarch x86_64
BuildRequires:  skelcd-fallbackrepo-SLED
BuildRequires:  skelcd-fallbackrepo-SLES_SAP
BuildRequires:  skelcd-fallbackrepo-SLE_HPC
BuildRequires:  skelcd-fallbackrepo-SLE_RT
%endif
%ifarch ppc64le
BuildRequires:  skelcd-fallbackrepo-SLES_SAP
%endif
%ifarch aarch64
BuildRequires:  skelcd-fallbackrepo-SLE_HPC
%endif
BuildRequires:  unified-installer-release
%endif

%if "%theme" == "SLES_SAP"
%define branding_skelcd   leanos
%define branding_systemd  SLE
%define branding_plymouth SLE
%define branding_grub2    SLE
%define branding_gfxboot  SLE
BuildRequires:  unified-installer-release
%endif

%if "%theme" == "CAASP"
%define branding_skelcd   CAASP
%define branding_systemd  CAASP
%define branding_plymouth SLE
%define branding_grub2    SLE
%define branding_gfxboot  SLE
%define config_bootmenu_no_upgrade 1
BuildRequires:  caasp-release
BuildRequires:  skelcd-fallbackrepo-CAASP
%endif

# ===  product name with architecture appended  ===

%global product_name_arch %product_name-%{_target_cpu}

# ===  branding specific packages  ===

BuildRequires:  skelcd-control-%branding_skelcd
BuildRequires:  systemd-presets-branding-%branding_systemd
%if %with_plymouth
BuildRequires:  plymouth-branding-%branding_plymouth
%endif
%ifarch %ix86 x86_64
BuildRequires:  gfxboot-branding-%branding_gfxboot
%endif
%ifarch %ix86 x86_64 aarch64 %{arm} riscv64
BuildRequires:  grub2-branding-%branding_grub2
%endif

# ===  branding end  ===

# no i586 in Leap
%if %suse_version == 1500
ExcludeArch:    %ix86
%endif

BuildRequires:  xf86-input-libinput
BuildRequires:  google-roboto-fonts
BuildRequires:  noto-sans-fonts
%ifarch ia64 %ix86 x86_64
BuildRequires:  libsmbios_c2
%endif
BuildRequires:  Mesa-dri
BuildRequires:  Mesa-libEGL1
BuildRequires:  Mesa-libGL1
BuildRequires:  aaa_base
BuildRequires:  aaa_base-extras
BuildRequires:  adaptec-firmware
BuildRequires:  alsa
BuildRequires:  alsa-utils
BuildRequires:  arphic-uming-fonts
BuildRequires:  audit-libs
BuildRequires:  bc
BuildRequires:  bcache-tools
BuildRequires:  bcm43xx-firmware
BuildRequires:  bind-utils
BuildRequires:  blueprint-cursor-theme
BuildRequires:  btrfsprogs
BuildRequires:  build-key
BuildRequires:  busybox
BuildRequires:  bzip2
BuildRequires:  ca-certificates-mozilla
BuildRequires:  cairo
BuildRequires:  checkmedia
BuildRequires:  cifs-utils
BuildRequires:  cpio-mt
BuildRequires:  cracklib
BuildRequires:  cracklib-dict-full
BuildRequires:  cron
BuildRequires:  cryptsetup
BuildRequires:  cups-libs
BuildRequires:  curl
BuildRequires:  dash
BuildRequires:  dbus-1-daemon
BuildRequires:  dbus-1-x11
BuildRequires:  dd_rescue
BuildRequires:  debuginfod-client
BuildRequires:  dejavu-fonts
BuildRequires:  dhcp-server
BuildRequires:  dmraid
BuildRequires:  dosfstools
BuildRequires:  dump
BuildRequires:  e2fsprogs
BuildRequires:  ed
BuildRequires:  elfutils
BuildRequires:  ethtool
BuildRequires:  google-noto-naskharabic-fonts
%if %with_exfat
BuildRequires:  exfatprogs
%endif
BuildRequires:  fonts-config
BuildRequires:  gamin-server
BuildRequires:  gdb
BuildRequires:  gettext-runtime
BuildRequires:  glibc-i18ndata
BuildRequires:  glibc-locale
BuildRequires:  gpart
BuildRequires:  gpg2
BuildRequires:  gpm
BuildRequires:  gptfdisk
BuildRequires:  graphviz
BuildRequires:  graphviz-gnome
BuildRequires:  hdparm
BuildRequires:  hex
BuildRequires:  hfsutils
BuildRequires:  hostname
BuildRequires:  icewm-lite
BuildRequires:  icmpinfo
BuildRequires:  indic-fonts
BuildRequires:  initviocons
BuildRequires:  ipa-gothic-fonts
BuildRequires:  iproute2
BuildRequires:  iptables
BuildRequires:  iputils
BuildRequires:  iscsiuio
BuildRequires:  jfsutils
BuildRequires:  joe
BuildRequires:  kbd
BuildRequires:  kernel-default
%if %with_kernel_extra
BuildRequires:  kernel-default-extra
BuildRequires:  kernel-default-optional
%endif
BuildRequires:  kernel-firmware-all
BuildRequires:  kexec-tools
BuildRequires:  khmeros-fonts
BuildRequires:  kmod-compat
BuildRequires:  krb5-devel
BuildRequires:  less
%if %with_fips
BuildRequires:  dracut-fips
BuildRequires:  openssh-fips
%endif
BuildRequires:  libpcsclite1
BuildRequires:  libsolv-tools
BuildRequires:  libyui-ncurses
BuildRequires:  libyui-ncurses-pkg
BuildRequires:  libyui-ncurses-rest-api
BuildRequires:  libyui-qt
BuildRequires:  libyui-qt-graph
BuildRequires:  libyui-qt-pkg
BuildRequires:  libyui-qt-rest-api
BuildRequires:  linuxrc
BuildRequires:  lklug-fonts
BuildRequires:  lsscsi
BuildRequires:  lvm2
BuildRequires:  mdadm
BuildRequires:  mingetty
BuildRequires:  mkfontdir
BuildRequires:  mkfontscale
BuildRequires:  mtools
BuildRequires:  multipath-tools
BuildRequires:  nasm
BuildRequires:  ncurses-utils
BuildRequires:  netcat-openbsd
BuildRequires:  netpbm
BuildRequires:  nfs-client
BuildRequires:  nfs-kernel-server
BuildRequires:  nfs-utils
BuildRequires:  novnc
BuildRequires:  ntfs-3g
BuildRequires:  ntfsprogs
BuildRequires:  nvme-cli
BuildRequires:  open-iscsi
BuildRequires:  openldap2-client
BuildRequires:  openslp-server
BuildRequires:  openssh
BuildRequires:  pango
BuildRequires:  pango-tools
BuildRequires:  parted
BuildRequires:  pciutils
BuildRequires:  pcre-devel
BuildRequires:  pcsc-lite
BuildRequires:  perl-Config-Crontab
BuildRequires:  perl-HTML-Parser
BuildRequires:  perl-Switch
BuildRequires:  perl-XML-Bare
BuildRequires:  perl-XML-NamespaceSupport
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-XML-Simple
BuildRequires:  perl-solv
BuildRequires:  pinentry
BuildRequires:  python3-websockify
BuildRequires:  google-poppins-fonts
BuildRequires:  samba
BuildRequires:  snapper
BuildRequires:  suse-module-tools
BuildRequires:  systemd
BuildRequires:  systemd-presets-branding
BuildRequires:  sysvinit-tools
BuildRequires:  tftpboot-installation-common
BuildRequires:  thai-fonts
BuildRequires:  tpm2.0-abrmd
BuildRequires:  tpm2.0-tools
BuildRequires:  tunctl
BuildRequires:  udev
BuildRequires:  vlan
BuildRequires:  vsftpd
%if %with_plymouth
BuildRequires:  plymouth
BuildRequires:  plymouth-branding
BuildRequires:  plymouth-plugin-script
BuildRequires:  plymouth-scripts
BuildRequires:  plymouth-theme-tribar
%endif
BuildRequires:  klogd
BuildRequires:  ltrace
BuildRequires:  nscd
BuildRequires:  polkit
BuildRequires:  popt-devel
BuildRequires:  pothana2000
BuildRequires:  procinfo
BuildRequires:  procps
BuildRequires:  psmisc
BuildRequires:  rgb
BuildRequires:  rpcbind
BuildRequires:  rsync
BuildRequires:  rsyslog
BuildRequires:  screen
BuildRequires:  sdparm
BuildRequires:  setserial
BuildRequires:  setxkbmap
BuildRequires:  sg3_utils
BuildRequires:  sharutils
BuildRequires:  smartmontools
BuildRequires:  smp_utils
BuildRequires:  socat
BuildRequires:  sqlite3
BuildRequires:  squashfs
BuildRequires:  star
BuildRequires:  strace
BuildRequires:  tcpd-devel
BuildRequires:  terminfo
BuildRequires:  udftools
BuildRequires:  un-fonts
BuildRequires:  usbutils
BuildRequires:  util-linux
BuildRequires:  util-linux-systemd
BuildRequires:  valgrind
BuildRequires:  vim-small
# libproxy1 requires libpxbackend-1_0; to counter cycles, this exists also as mini (bsc#215290)
#!BuildConflicts: libpxbackend-1_0-mini
BuildRequires:  wicked
BuildRequires:  wicked-nbft
BuildRequires:  wireless-tools
%ifnarch s390 s390x
BuildRequires:  wpa_supplicant
%endif
BuildRequires:  chrony
BuildRequires:  xauth
BuildRequires:  xdm
BuildRequires:  xdpyinfo
BuildRequires:  xfsdump
BuildRequires:  xfsprogs
BuildRequires:  xhost
BuildRequires:  xkbcomp
BuildRequires:  xkeyboard-config
BuildRequires:  xmodmap
BuildRequires:  xorg-x11-fonts
BuildRequires:  xorg-x11-fonts-legacy
BuildRequires:  xorg-x11-server
BuildRequires:  xrandr
BuildRequires:  xrefresh
BuildRequires:  xset
BuildRequires:  xterm
BuildRequires:  xz
BuildRequires:  yast2-devtools
%if "%flavor" == "SMO" || "%flavor" == "LeapMicro" || "%flavor" == "MicroOS"
BuildRequires:  yast2-schema-micro
%else
BuildRequires:  yast2-schema-default
%endif
BuildRequires:  yast2-trans-allpacks
BuildRequires:  yast2-widget-demo
%if 0%{?with_storage_ng}
BuildRequires:  libstorage-ng-lang
BuildRequires:  yast2-storage-ng
#!BuildIgnore:  yast2-storage
#!BuildIgnore:  libstorage7
%endif
%if %{with sbl}
BuildRequires:  sbl
%endif
%if %{with vnc}
BuildRequires:  xorg-x11-Xvnc
%endif
# kmps
%ifarch %ix86 x86_64
BuildRequires:  atmel-firmware
BuildRequires:  dos2unix
BuildRequires:  ftp
BuildRequires:  hyper-v
BuildRequires:  ipw-firmware
BuildRequires:  tftp
BuildRequires:  xen-tools-domU
%if %{with xen}
BuildRequires:  kernel-xen
%if %{with xenkmp}
BuildRequires:  xen-kmp-default
%endif
%else
##BuildIgnore: kernel-xen
%endif
%endif
%ifnarch s390 s390x
%ifarch ppc64 ppc64le
BuildRequires:  iprutils
%endif
BuildRequires:  kbd
%ifarch %ix86 x86_64
BuildRequires:  xf86-video-amdgpu
BuildRequires:  xf86-video-intel
BuildRequires:  xf86-video-qxl
BuildRequires:  xf86-video-vesa
%endif
BuildRequires:  xf86-input-wacom
BuildRequires:  xf86-video-fbdev
%endif
BuildRequires:  grub2
%ifarch ppc ppc64 ppc64le
%ifnarch ppc64le
BuildRequires:  pdisk
%endif
BuildRequires:  grub2-powerpc-ieee1275
BuildRequires:  powerpc-utils
%endif
%ifarch %ix86 x86_64
BuildRequires:  acpica
BuildRequires:  biosdevname
BuildRequires:  dhcp-client
BuildRequires:  dmidecode
BuildRequires:  elilo
BuildRequires:  memtest86+
BuildRequires:  syslinux
%if %with_vbox
BuildRequires:  virtualbox-guest-kmp-default
BuildRequires:  virtualbox-guest-x11
%endif
%endif
%ifarch %ix86
BuildRequires:  dos2unix
BuildRequires:  ftp
BuildRequires:  tftp
%endif
%ifarch x86_64
BuildRequires:  grub2-x86_64-efi
%if %with_shim
BuildRequires:  shim
BuildRequires:  mokutil
%endif
#!BuildIgnore:  glibc-32bit
%endif
%ifarch %ix86 x86_64
BuildRequires:  grub2-i386-efi
BuildRequires:  efibootmgr
%endif
%ifarch ia64
BuildRequires:  acpica
BuildRequires:  dmidecode
BuildRequires:  efibootmgr
BuildRequires:  elilo
BuildRequires:  fpswa
%endif
%ifarch s390x
BuildRequires:  s390-tools-hmcdrvfs
%endif
%ifarch %ix86 x86_64
BuildRequires:  gfxboot-branding
%endif
%ifarch %ix86 x86_64 aarch64 %{arm} riscv64
BuildRequires:  grub2-branding
%endif
%ifnarch s390 s390x
#BuildRequires:  enic-kmp-default fnic-kmp-default ofed-kmp-default
%endif
BuildRequires:  dmz-icon-theme-cursors
%ifarch aarch64
BuildRequires:  grub2-arm64-efi
BuildRequires:  raspberrypi-firmware
BuildRequires:  raspberrypi-firmware-config
BuildRequires:  raspberrypi-firmware-dt
BuildRequires:  arm-trusted-firmware-rpi4
BuildRequires:  u-boot-rpiarm64
BuildRequires:  lenovo-x13s-firmware-dt
%if %with_shim
BuildRequires:  shim
%endif
%endif
%ifarch %arm
BuildRequires:  grub2-arm-efi
%endif
%ifarch riscv64
BuildRequires:  grub2-riscv64-efi
%endif
# inst-sys module for libstoragemgmt
BuildRequires:  libstoragemgmt-smis-plugin
# our images are not reproducible and it's taking time
#!BuildIgnore:  build-compare

%if %{with iso}
BuildRequires:  createrepo_c
BuildRequires:  mkisofs
BuildRequires:  mksusecd
BuildRequires:  skelcd-openSUSE
%endif

%if "@BUILD_FLAVOR@" == ""
# This package is never built - but it helps the bots seeing that this package
# is intentionally as messed up as it is
Name:           installation-images
%else
Name:           installation-images-%{theme}
%endif
AutoReqProv:    off
Summary:        Installation Image Files for %theme
License:        GPL-2.0-or-later
Group:          Metapackages
Version:        17.131
Release:        0
Provides:       installation-images = %version-%release
Conflicts:      otherproviders(installation-images)
Source:         installation-images-%{version}.tar.xz
Source1:        installation-images-rpmlintrc
Source2:        product_name
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%define _binary_payload w.ufdio

%description -n installation-images-%{theme}
Files needed for %theme installation media.


%package -n     install-initrd-%{theme}
Provides:       install-initrd = %version-%release
Conflicts:      otherproviders(install-initrd)
Obsoletes:      install-initrd-%theme < %version-%release
Obsoletes:      install-initrd-branding-%theme < %version-%release
AutoReqProv:    off
Summary:        Create initrd for %theme installation
Group:          System/Kernel
PreReq:         /bin/ln

%description -n install-initrd-%{theme}
You can create an initrd for %theme installation. Useful, for example, to set
up a UML or XEN environment.


%package -n     tftpboot-installation-%{product_name_arch}
AutoReqProv:    off
Summary:        tftp installation tree
Group:          System/Management
BuildArch:      noarch

%description -n tftpboot-installation-%{product_name_arch}
This package contains the kernel, initrd and installation images
to install SUSE CaaS Platform with PXE boot/tftpboot on x86-64.


%package -n     skelcd-installer-%{theme}
Provides:       skelcd-installer = %version-%release
Conflicts:      otherproviders(skelcd-installer)
Conflicts:      rescue-server
AutoReqProv:    off
Summary:        installer and related files needed on dvd1
Group:          Metapackages

%description -n skelcd-installer-%{theme}
This package contains kernel, initrd and installation images
needed on the first product dvds to start an installation.


%package -n     skelcd-installer-net-%{theme}
Provides:       skelcd-installer = %version-%release
Conflicts:      otherproviders(skelcd-installer)
Conflicts:      rescue-server
AutoReqProv:    off
Summary:        installer and related files needed on network medium
Group:          Metapackages

%description -n skelcd-installer-net-%{theme}
This package contains kernel, initrd and installation images
needed on the network install medium to start an installation.


%package -n     installation-images-debuginfodeps-%{theme}
Provides:       installation-images-debuginfodeps = %version-%release
Conflicts:      otherproviders(installation-images-debuginfodeps)
Obsoletes:      installation-images-debuginfodeps-%theme < %version-%release
Summary:        Debuginfo dependencies for %theme installation-images
Group:          Metapackages

%description -n installation-images-debuginfodeps-%{theme}
Package that holds debuginfo dependencies for image files in installation-image.


%define __debuginfo_requires   xargs grep build-id
%define __debuginfo_path       ^/usr/share/debuginfodeps

%prep
if [ "$UID" != 0 ] ; then
    echo "ERROR: need to run this as root. e.g. with osc build --userootforbuild"
    exit 1
fi
%setup -n installation-images-%{version}
rm -f /usr/lib/build/checks/04-check-filelist

%build
echo building product "'%product_name_arch'"
unset MALLOC_CHECK_
BUILD_DISTRIBUTION_NAME="%distribution"
export BUILD_DISTRIBUTION_NAME
test ! -z "$BUILD_DISTRIBUTION_NAME"
# build id (for linuxrc to start the correct instsys)
export instsys_build_id=`bin/build_id`
# beta only: warn testers about wrong instsys
export instsys_complain=1
# careful: will make all non-matching initrds fail hard
# export instsys_complain_root=2
# beta only: ignore non-critical errors
# export debug=ignore
# remove 'upgrade' option from boot menu
%if 0%{?config_bootmenu_no_upgrade}
export BOOTMENU_NO_UPGRADE=1
%endif
# force selfupdate setting, if defined
%if 0%{?config_yast_selfupdate:1}
export YAST_SELFUPDATE=%{config_yast_selfupdate}
%endif
# check that we are generally ok
make test
# build it
make THEMES=%theme
%ifarch %ix86 x86_64
%if %{with xen}
# build xen initrd & kernel
image=initrd-xen kernel=kernel-xen MOD_CFG=xen make initrd+modules THEMES=%theme
MOD_CFG=xen make kernel
%endif
%endif
%ifarch ppc ppc64
image=initrd-default kernel=kernel-default MOD_CFG=ppc64 make initrd+modules+gefrickel THEMES=%theme
%endif
%ifarch ppc64le
image=initrd-default kernel=kernel-default MOD_CFG=ppc64le make initrd+modules+gefrickel THEMES=%theme
%endif

%if %{with iso}
make THEMES=%theme iso
%endif

%install
BUILD_DISTRIBUTION_NAME="%distribution"
export BUILD_DISTRIBUTION_NAME
test ! -z "$BUILD_DISTRIBUTION_NAME"
make install DESTDIR=%{buildroot} THEMES=%theme
# make debuginfo DESTDIR=%{buildroot}
make install-initrd DESTDIR=%{buildroot}/usr/lib/install-initrd THEMES=%theme
ln -s %theme %{buildroot}/usr/lib/install-initrd/branding
install -d -m 755 %{buildroot}/usr/sbin
install -m 755 etc/mkinstallinitrd %{buildroot}/usr/sbin
%ifarch x86_64
%if %{without xen}
ln -s loader/initrd %{buildroot}/branding/%theme/CD1/boot/x86_64/initrd-xen
ln -s loader/linux %{buildroot}/CD1/boot/x86_64/vmlinuz-xen
%endif
%endif
# get rid of /usr/lib/rpm/brp-strip-debug
# strip kills the zImage.chrp-rs6k
export NO_BRP_STRIP_DEBUG=true
export NO_DEBUGINFO_STRIP_DEBUG=true
# for compatibility
mv %{buildroot}/branding %{buildroot}/SuSE
# file list for install-initrd
echo '%defattr(-,root,root)' >install-initrd.files
( cd %{buildroot}/usr/lib/install-initrd ; find -maxdepth 1 | sed -e '/\.$/d ; /\.\/branding/d ; s#\.#/usr/lib/install-initrd#' ) >>install-initrd.files
echo '%ghost' /usr/lib/install-initrd/branding >>install-initrd.files
echo '%dir' /usr/lib/install-initrd >>install-initrd.files
echo /usr/sbin/mkinstallinitrd >>install-initrd.files
# cd1
mkdir -p %{buildroot}/usr/lib/skelcd/CD1
cp -a %{buildroot}/usr/share/tftpboot-installation/*/* %{buildroot}/usr/lib/skelcd/CD1
rm -f %{buildroot}/usr/lib/skelcd/CD1/boot/*/rpmlist
rm -f %{buildroot}/usr/lib/skelcd/CD1/boot/*/mkbootdisk
rm -rf %{buildroot}/usr/lib/skelcd/CD1/{README,net}
# net
cp -a %{buildroot}/usr/lib/skelcd/CD1 %{buildroot}/usr/lib/skelcd/NET
rm -f %{buildroot}/usr/lib/skelcd/NET/boot/*/*.rpm
rm -f %{buildroot}/usr/lib/skelcd/NET/boot/*/{bind,common,config,control.xml,gdb,libstoragemgmt,rescue,root}
if [ -n "%{net_repo}" ] ; then
  CPU=%{_target_cpu}
  [ "$CPU" = i586 ] && CPU=i386
  RD=%{buildroot}/usr/lib/skelcd/NET/boot/$CPU/initrd
  if [ ! -f $RD ] ; then
    RD=%{buildroot}/usr/lib/skelcd/NET/boot/$CPU/loader/initrd
  fi
  if [ -f $RD ] ; then
    mkdir -p tmp_xxx/etc/linuxrc.d
    echo defaultrepo=%{net_repo} > tmp_xxx/etc/linuxrc.d/10_repo
    ( cd tmp_xxx ; find etc | cpio -o -H newc ) | xz --check=crc32 -c >> $RD
    rm -rf tmp_xxx
  fi
fi

%if %{with iso}
install -D -m 644 images/cd1.iso %{_topdir}/ISO/cd1.iso
%endif

%post -n install-initrd-%{theme}
/bin/ln -snf %theme /usr/lib/install-initrd/branding 2>/dev/null || true

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/CD1
/SuSE
%exclude /usr/share/debuginfodeps
/usr/share/mini-iso-rmlist
%ifarch x86_64
/usr/share/rescue-server
%endif

%files -n install-initrd-%{theme} -f install-initrd.files

%files -n tftpboot-installation-%{product_name_arch}
%defattr(-,root,root)
%dir %attr(0755,tftp,tftp) /usr/share/tftpboot-installation
/usr/share/tftpboot-installation

%files -n skelcd-installer-%{theme}
%defattr(-,root,root)
%dir /usr/lib/skelcd
/usr/lib/skelcd/CD1

%files -n skelcd-installer-net-%{theme}
%defattr(-,root,root)
%dir /usr/lib/skelcd
/usr/lib/skelcd/NET

%files -n installation-images-debuginfodeps-%{theme}
%defattr(-,root,root)
/usr/share/debuginfodeps

%changelog
