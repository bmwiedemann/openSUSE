#
# spec file for package kernel-default-base
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
# needssslcertforbuild


# To be defined by user
%define build_flavor default
# variant includes dash: %%define variant -azure
%define variant %{nil}
%define subpackage base
%define extrasummary base modules
%define extradescription This package contains only the base modules, required in all installs.

%define misc_modules button edd i6300esb efivarfs qemu_fw_cfg hid-generic

%define virtio_modules virtio virtio_.* virtio-.*

%define xen_modules xenblk xennet xen-.*

%define vmware_modules vmxnet3 vmw_.*

%define hyperv_modules hid-hyperv hv_balloon hv_utils \
hv_vmbus hyperv-keyboard hv_netvsc hv_storvsc scsi_transport_fc hyperv_fb

%define net_drivers  8390 ne2k-pci tulip e100 e1000 e1000e 8139cp 8139too

%define scsi_modules scsi_transport_iscsi sd_mod sg sr_mod st scsi_mod

%define block_drivers loop dm-mod ahci ata_piix mptsas mptspi BusLogic sym53c8xx aam53c974 rbd brd

%define usb_modules usb-common usbcore ehci-hcd ehci-pci ohci-hcd ohci-pci uhci-hcd \
xhci-hcd xhci-pci typec_ucsi ucsi_acpi typec ums-alauda ums-cypress ums-datafab \
ums-eneub6250 ums-freecom ums-isd200 ums-jumpshot ums-karma ums-onetouch \
ums-realtek ums-sddr09 ums-sddr55 ums-usbat usb-storage usbhid

%define filesystems autofs4 btrfs ext4 vfat isofs jbd2 mbcache nfsv2 nfsv3 nfsv4 overlay xfs \
        nls_cp437 nls_iso8859-1 ceph cifs

%define networking \
af_packet arptable_filter arp_tables arpt_mangle bpfilter bridge br_netfilter    \
ebt_.* ebtable_.* ebtables ip6table_.* ip6_tables ip6t_.* ip_.* ipt_.* iptable_.* \
nf_.* nfnetlink.* nft_.* tun veth xfrm.*_tunnel xfrm_.* x_tables xt_.* tcp_diag \
vxlan

%define crypto_modules \
%(rpm -ql %{kernel_package_name} | grep -E 'kernel/crypto/|kernel/arch/.*/crypto/' | xargs basename -a | cut -d. -f1)

%define modules %usb_modules %net_drivers %scsi_modules %block_drivers \
                %hyperv_modules %virtio_modules %vmware_modules %xen_modules \
                %networking %filesystems %misc_modules %crypto_modules

# Reasonable defaults that might be overriden if needed
%define kernel_package_name kernel-%build_flavor
%define package_name %kernel_package_name-%subpackage
%define url %(rpm -q --qf '%%{URL}' %kernel_package_name)
%define group %(rpm -q --qf '%%{GROUP}' %kernel_package_name)
%define summary %(rpm -q --qf '%%{SUMMARY}' %kernel_package_name) - %extrasummary

Name:           %package_name
BuildRequires:  %kernel_package_name
BuildRequires:  %kernel_package_name-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  grep
BuildRequires:  kernel-subpackage-macros
Summary:        %summary
License:        GPL-2.0-only
Group:          %group
URL:            %url
# on SLE limit to architectures that actually have a kernel :-)
%if 0%{?sle_version}
ExclusiveArch:  aarch64 armv7hl ppc64le s390x x86_64
%endif

# Internal stuff begins
%define rpm_kver %(rpm -q --qf '%%{VERSION}' %kernel_package_name)
%define rpm_krel %(rpm -q --qf '%%{RELEASE}' %kernel_package_name)
Version:        %rpm_kver
Release:        %rpm_krel.<RELEASE>

%define scriptdir /usr/lib/rpm/kernel
%include %scriptdir/kernel-subpackage-spec

%changelog
