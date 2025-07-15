#
# spec file for package patterns-media
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


%bcond_with betatest
Name:           patterns-media
Version:        20170319
Release:        0
Summary:        Patterns for Installation (media patterns)
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains patterns that determine the contents of media
such as DVD's

%package rest_cd_core
%pattern_desktopfunctions
Summary:        Remaining Software
Group:          Metapackages
Provides:       pattern() = rest_cd_core
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1941
Requires:       kernel-default
Requires:       kernel-firmware-all
Requires:       pattern() = base
Requires:       pattern() = enhanced_base
Requires:       pattern() = fonts
Requires:       pattern() = sw_management
Requires:       pattern() = x11
# minimal set of yast modules
Requires:       yast2-bootloader
Requires:       yast2-country
Requires:       yast2-hardware-detection
Requires:       yast2-network
Requires:       yast2-proxy
# branding for the installation
Requires:       yast2-qt-branding-openSUSE
Requires:       yast2-storage-ng
Requires:       yast2-trans-stats
Requires:       yast2-x11
# adaptec-firmware (#298726)
Recommends:     adaptec-firmware
# #396109
Recommends:     alsa-firmware
Recommends:     aspell-en
Recommends:     atmel-firmware
Recommends:     awesfx
# #327506
Recommends:     b43-fwcutter
# supplements by modaliases
Recommends:     bluez-firmware
# filesystem(btrfs)
Recommends:     btrfsprogs
Recommends:     bundle-lang-common-en
Recommends:     chrony
Recommends:     cifs-utils
# prefer the full version for installation
Recommends:     cracklib-dict-full
# crypto partitions
Recommends:     cryptsetup
Recommends:     db-utils
# needed to detect if a system is the same
Recommends:     dmidecode
# filesystem(vfat)
Recommends:     dosfstools
Recommends:     dvb
# filesystem(ext2)
Recommends:     e2fsprogs
Recommends:     espeak
Recommends:     fprintd-pam
Recommends:     gtk2-branding-openSUSE
Recommends:     insserv
# bnc#548325
Recommends:     ipw-firmware
# laptop stuff
Recommends:     irda
Recommends:     iw
# filesystem(jfs)
Recommends:     jfsutils
Recommends:     libatm1
# TPM+FDE
Recommends:     libtss2-tcti-device0
Recommends:     lomoco
Recommends:     lsb-release
#lvm2 support (#301382)
Recommends:     lvm2
# #494547 - just testing
Recommends:     manufacturer-PPDs
# #304219
Recommends:     memtest86+
Recommends:     mpt-firmware
# give vim haters an editor
Recommends:     nano
# filesystem(ntfs-3g)
Recommends:     ntfs-3g
Recommends:     open-iscsi
# bug#591085
Recommends:     open-vm-tools
Recommends:     p7zip
Recommends:     pam_ldap
# needed by yast2-storage-ng for crypt partitions
Recommends:     pam_mount
Recommends:     pcmciautils
Recommends:     ppp
Recommends:     pptp
# yast can configure quota - if present on medium (#348336)
Recommends:     quota
# adding to LiveCD (bnc#419201)
Recommends:     rsync
# LiveCD accessible? (bnc#391327)
Recommends:     sbl
# Required for systemd-boot/grub2-bls
Recommends:     sdbootutil
Recommends:     grub2-arm64-efi-bls
Recommends:     grub2-x86_64-efi-bls
Recommends:     smartmontools
# DELL laptop support
Recommends:     smbios-utils-python
# required by yast2-dsl (#377472)
Recommends:     smpppd
Recommends:     sssd
Recommends:     susehelp_en
Recommends:     suspend
# Required by YaST for FDE+TPM
Recommends:     systemd-boot
Recommends:     systemd-logger
# Required for FDE+TPM
Recommends:     tpm2.0-tools
Recommends:     tpm2-0-tss
Recommends:     unzip
# filesystem(minix)
Recommends:     util-linux
# bug#589416
Recommends:     virtualbox-guest-tools
# enhances virtualbox speed (#365562)
Recommends:     virtualbox-guest-x11
Recommends:     wireless-regdb
Recommends:     wpa_supplicant
# all xf86 drivers
Recommends:     xf86-video-ark
Recommends:     xf86-video-ast
Recommends:     xf86-video-ati
Recommends:     xf86-video-chips
Recommends:     xf86-video-cirrus
Recommends:     xf86-video-dummy
Recommends:     xf86-video-fbdev
Recommends:     xf86-video-glint
Recommends:     xf86-video-i128
Recommends:     xf86-video-intel
Recommends:     xf86-video-mach64
Recommends:     xf86-video-mga
Recommends:     xf86-video-neomagic
Recommends:     xf86-video-nouveau
Recommends:     xf86-video-nv
Recommends:     xf86-video-qxl
Recommends:     xf86-video-r128
Recommends:     xf86-video-savage
Recommends:     xf86-video-siliconmotion
Recommends:     xf86-video-sis
Recommends:     xf86-video-sisusb
Recommends:     xf86-video-tdfx
Recommends:     xf86-video-tga
Recommends:     xf86-video-v4l
Recommends:     xf86-video-vesa
Recommends:     xf86-video-vmware
Recommends:     xf86-video-voodoo
# file system stuff
Recommends:     xfsdump
# filesystem(xfs)
Recommends:     xfsprogs
# decompression to recover something
Recommends:     xz
Recommends:     yast2-trans-cs
Recommends:     yast2-trans-da
Recommends:     yast2-trans-de
Recommends:     yast2-trans-en_GB
Recommends:     yast2-trans-es
Recommends:     yast2-trans-fr
Recommends:     yast2-trans-hu
Recommends:     yast2-trans-it
Recommends:     yast2-trans-ja
Recommends:     yast2-trans-pl
Recommends:     yast2-trans-pt
Recommends:     yast2-trans-pt_BR
Recommends:     yast2-trans-ru
Recommends:     yast2-trans-stats
Recommends:     yast2-trans-sv
Recommends:     yast2-trans-zh_CN
Recommends:     yast2-trans-zh_TW
# Firmware for ZD1211 based WLAN sticks
Recommends:     zd1211-firmware
Recommends:     zip
%ifarch aarch64 x86_64
Recommends:     efibootmgr
%endif
%ifarch x86_64
Recommends:     sssd-32bit
# sssd-32bit pulls in some pam-32bit, which results in the need to also have
# systemd-32bit available (or pam-config -a --systemd will fail later on)
Recommends:     systemd-32bit
%endif

%description rest_cd_core
Packages that are on CD but not in other patterns.

%files rest_cd_core
%dir %{_docdir}/patterns
%{_docdir}/patterns/rest_cd_core.txt

%package rest_dvd
%pattern_desktopfunctions
Summary:        Remaining Software
Group:          Metapackages
Provides:       patterns-openSUSE-rest_dvd = %{version}
Provides:       pattern() = rest_dvd
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1980
Obsoletes:      patterns-openSUSE-rest_dvd < %{version}
%ifnarch s390x
Requires:       pattern() = gnome
Requires:       pattern() = gnome_basis
Requires:       pattern() = gnome_games
Requires:       pattern() = gnome_imaging
Requires:       pattern() = gnome_internet
Requires:       pattern() = gnome_multimedia
Requires:       pattern() = gnome_office
Requires:       pattern() = gnome_utilities
Requires:       pattern() = gnome_yast
Requires:       pattern() = imaging
Requires:       pattern() = kde
Requires:       pattern() = kde_edutainment
Requires:       pattern() = kde_games
Requires:       pattern() = kde_ide
Requires:       pattern() = kde_internet
Requires:       pattern() = kde_multimedia
Requires:       pattern() = kde_office
Requires:       pattern() = kde_plasma
Requires:       pattern() = kde_utilities
Requires:       pattern() = kde_utilities_opt
Requires:       pattern() = kde_yast
%endif
Requires:       arabic-fonts
Requires:       arphic-uming-fonts
Requires:       cracklib-dict-full
Requires:       indic-fonts
Requires:       ipa-gothic-fonts
Requires:       khmeros-fonts
Requires:       lklug-fonts
# boo#1185343
Requires:       udftools
Requires:       pattern() = apparmor
Requires:       pattern() = base
Requires:       pattern() = console
Requires:       pattern() = dhcp_dns_server
Requires:       pattern() = directory_server
Requires:       pattern() = enhanced_base
Requires:       pattern() = file_server
Requires:       pattern() = fonts
Requires:       pattern() = fonts_opt
Requires:       pattern() = games
Requires:       pattern() = lamp_server
Requires:       pattern() = laptop
Requires:       pattern() = mail_server
Requires:       pattern() = multimedia
Requires:       pattern() = office
Requires:       pattern() = print_server
Requires:       pattern() = rest_cd_core
Requires:       pattern() = sw_management
Requires:       pattern() = sw_management_gnome
Requires:       pattern() = x11
%ifarch x86_64
Requires:       pattern() = x86_64_v3
%endif
Recommends:     pattern() = xfce
Recommends:     pattern() = xfce_basis
Recommends:     pattern() = xfce_laptop
Recommends:     pattern() = xfce_office
Requires:       pattern() = yast2_basis
Requires:       pattern() = yast2_install_wf
Requires:       thai-fonts
Requires:       un-fonts
Requires:       yast2-trans-af
Requires:       yast2-trans-ar
Requires:       yast2-trans-bg
Requires:       yast2-trans-bn
Requires:       yast2-trans-bs
Requires:       yast2-trans-ca
Requires:       yast2-trans-cs
Requires:       yast2-trans-cy
Requires:       yast2-trans-da
Requires:       yast2-trans-de
Requires:       yast2-trans-el
Requires:       yast2-trans-en_GB
Requires:       yast2-trans-es
Requires:       yast2-trans-et
Requires:       yast2-trans-fa
Requires:       yast2-trans-fi
Requires:       yast2-trans-fr
Requires:       yast2-trans-gl
Requires:       yast2-trans-gu
Requires:       yast2-trans-hi
Requires:       yast2-trans-hr
Requires:       yast2-trans-hu
Requires:       yast2-trans-id
Requires:       yast2-trans-it
Requires:       yast2-trans-ja
Requires:       yast2-trans-jv
Requires:       yast2-trans-ka
Requires:       yast2-trans-km
Requires:       yast2-trans-ko
Requires:       yast2-trans-lo
Requires:       yast2-trans-lt
Requires:       yast2-trans-mk
Requires:       yast2-trans-mr
Requires:       yast2-trans-nb
Requires:       yast2-trans-nl
Requires:       yast2-trans-pa
Requires:       yast2-trans-pl
Requires:       yast2-trans-pt
Requires:       yast2-trans-pt_BR
Requires:       yast2-trans-ro
Requires:       yast2-trans-ru
Requires:       yast2-trans-si
Requires:       yast2-trans-sk
Requires:       yast2-trans-sl
Requires:       yast2-trans-sr
Requires:       yast2-trans-sv
Requires:       yast2-trans-ta
Requires:       yast2-trans-th
Requires:       yast2-trans-tr
Requires:       yast2-trans-uk
Requires:       yast2-trans-vi
Requires:       yast2-trans-wa
Requires:       yast2-trans-xh
Requires:       yast2-trans-zh_CN
Requires:       yast2-trans-zh_TW
Requires:       yast2-trans-zu
Recommends:     pattern() = books
Recommends:     pattern() = kvm_server
Recommends:     pattern() = minimal_base
Recommends:     pattern() = minimal_base-conflicts
Recommends:     pattern() = x11_yast
# bluncks 2nd baby
Recommends:     apport-gtk
Recommends:     apport-qt
# bnc#431280 (Japanese fonts)
Recommends:     arphic-uming-fonts
# autofs is tested by QA in staging
Recommends:     autofs
Recommends:     capi4hylafax
# FAX
Recommends:     capisuite
Recommends:     cellwriter
Recommends:     clicfs
Recommends:     createrepo
Recommends:     eekboard
Recommends:     git
Recommends:     isns
# kdump+tools
Recommends:     kdump
# all kernel flavors we want to have
Recommends:     kernel-default
Recommends:     kexec-tools
# kiwi as requested by ms
Recommends:     kiwi
Recommends:     kiwi-config-openSUSE
Recommends:     kiwi-desc-isoboot
Recommends:     kiwi-desc-netboot
Recommends:     kiwi-desc-oemboot
Recommends:     kiwi-desc-vmxboot
# needed for kiwi creation
Recommends:     kiwi-media-requires
Recommends:     kiwi-pxeboot
Recommends:     kiwi-templates
Recommends:     libc.so.6
# register your hardware
# no sync pattern
Recommends:     libopensync-plugin-google-calendar
Recommends:     libopensync-plugin-moto
Recommends:     libopensync-plugin-python-module
Recommends:     libpthread.so.0
Recommends:     libstdc++.so.6
Recommends:     libpthread.so.0(GLIBC_2.0)
Recommends:     libpthread.so.0(GLIBC_2.1)
Recommends:     libpthread.so.0(GLIBC_2.2)
Recommends:     libpthread.so.0(GLIBC_2.3.2)
Recommends:     libstdc++.so.6(CXXABI_1.3)
Recommends:     libstdc++.so.6(GLIBCXX_3.4)
Recommends:     libstdc++.so.6(GLIBCXX_3.4.9)
# very special case - 442295
# supporting lib for non-oss
Recommends:     libstdc++33
Recommends:     libsyncml-tools
# bnc#605888
Recommends:     libvdpau1
Recommends:     msynctool
Recommends:     nbd
Recommends:     nbd-doc
# yast needs nvme-cli to install / onto NVME
Recommends:     nvme-cli
# kernel modules
Recommends:     omnibook-kmp-default
Recommends:     omnibook-kmp-desktop
# #391434
Recommends:     open-vm-tools
Recommends:     openslp-server
# pam-extra needs to be present for upgraders, as pam_limits.so moved from pam to pam-extra
Recommends:     pam-extra
# qemu rocks
Recommends:     qemu
# #390825
Recommends:     qemu-kvm
Recommends:     qinternet
# bnc#626952
Recommends:     quota-nfs
Recommends:     rdesktop
# bnc#697047
Recommends:     siga
Recommends:     squashfs
Recommends:     sshfs
# could not find a better pattern
Recommends:     tigervnc
Recommends:     tsclient
# minimal korean support (bnc#390099)
Recommends:     un-fonts
# boo#972499
Recommends:     unbound
Recommends:     unison
Recommends:     vboxgtk
## 306071
Recommends:     virtualbox
Recommends:     virtualbox-guest-kmp-default
Recommends:     virtualbox-guest-kmp-desktop
Recommends:     virtualbox-qt
Recommends:     vmware-guest-kmp-default
Recommends:     vmware-guest-kmp-desktop
Recommends:     wacom-kmp
Recommends:     xorg-x11-driver-input
# #296387
Recommends:     xournal
Recommends:     xstroke
# feature 301945
Recommends:     yast2-add-on-creator
Recommends:     yast2-instserver
Recommends:     yast2-iscsi-server
# Internet Storage Name Service
Recommends:     yast2-isns
Recommends:     yast2-kdump
Recommends:     yast2-live-installer
Recommends:     yast2-nis-server
Recommends:     yast2-product-creator
# #301029
Recommends:     yast2-python3-bindings
Recommends:     yast2-slp-server
Suggests:       krdc
Suggests:       krfb
%ifarch ppc
Recommends:     gtkpbbuttons
# #381940
Recommends:     kernel-ppc64
Recommends:     pbbuttonsd
Recommends:     petitboot
Recommends:     powerprefs
# #387170
Recommends:     ps3-utils
%endif
%ifarch x86_64 ppc
Recommends:     nss_ldap-32bit
Recommends:     pam_krb5-32bit
Recommends:     pam_ldap-32bit
%endif
%ifarch ppc64
Recommends:     nss_ldap-64bit
Recommends:     pam_krb5-64bit
Recommends:     pam_ldap-64bit
%endif
# NVIDIA's openGPU driver
%ifarch x86_64 aarch64
Recommends:     kernel-firmware-nvidia-gsp-G06
Recommends:     nvidia-open-driver-G06-signed-kmp-default
%endif

%description rest_dvd
Packages that are on CD but not in other patterns.

%files rest_dvd
%dir %{_docdir}/patterns
%{_docdir}/patterns/rest_dvd.txt

################################################################################

%prep

%build

%install
mkdir -p "%{buildroot}%{_docdir}/patterns"
for i in rest_cd_core rest_dvd; do
	echo "This file marks the pattern $i to be installed." \
		>"%{buildroot}%{_docdir}/patterns/$i.txt"
done

%changelog
