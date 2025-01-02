#
# spec file for package uki
#
# Copyright (c) 2024 SUSE LLC
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
# needsbinariesforbuild
# needssslcertforbuild


%global debug_package %{nil}

# Flavors conditions
# -------------------------
%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" != ""
%define name_suffix -%{flavor}
%endif
# -------------------------
# Kernel name
# -------------------------
%ifarch %ix86 x86_64
%define ker_name vmlinuz
%endif
%ifarch ppc ppc64 ppc64le
%define ker_name vmlinux
%endif
%ifarch s390 s390x
%define ker_name image
%endif
%ifarch %arm
%define ker_name zImage
%endif
%ifarch aarch64 riscv64
%define ker_name Image
%endif
# -------------------------
# usefull variables
# -------------------------
%global uname %(ls /lib/modules | head -n 1)
%global kernel_version %(rpm -q --queryformat '%%{VERSION}' kernel-%{flavor})
%global initrd_pkg static-initrd-generic-unsigned
%global initrd_version %(rpm -q --queryformat '%{VERSION}' %{initrd_pkg} | sed 's|_k.*||')
%global initrd_release %(rpm -q --queryformat '%{RELEASE}' %{initrd_pkg})
%define etf /boot/efi
%define distro opensuse
%define efi_dir EFI/%{distro}
%define efi_path %{etf}/%{efi_dir}
%define efi_name uki-%{flavor}-%{initrd_version}-%{initrd_release}
%define url https://uapi-group.org/specifications/specs/unified_kernel_image
%define uki_install_dir %{kernel_module_directory}/%{uname}
%define uki_extra_dir %{kernel_module_directory}/uki.extra.d/
%global cert_install %(if [ -f %{_sourcedir}/_projectcert.crt ]; then echo 1; else echo 0; fi)
%define cert_name uki-%{flavor}
%define cert_install_dir %{_datarootdir}/unified/certs
# -------------------------
# Module Kernel macro
# -------------------------
# TW is usrmerged
%if %{undefined usrmerged} && 0%{?suse_version} >= 1550
%define usrmerged 1
%endif

%if 0%{?usrmerged}
%define kernel_module_directory /usr/lib/modules
%else
%define kernel_module_directory /lib/modules
%endif
# -------------------------

Name:           uki%{?name_suffix}
Version:        %{initrd_version}_%{initrd_release}_k%{kernel_version}
Release:        0
Summary:        Signed Unified Kernel Image
License:        Apache-2.0
URL:            %{url}
Group:          System/Kernel
Provides:       uki:%{cert_install_dir}
Provides:       uki:%{uki_extra_dir}
%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%else
ExclusiveArch:  x86_64
%endif
BuildRequires:  pesign-obs-integration
# -------------------------
# Needed to have the ukify tool
# -------------------------
BuildRequires:  systemd, systemd-experimental
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pefile}
# -------------------------
BuildRequires:  %{initrd_pkg}
BuildRequires:  gptfdisk
BuildRequires:  kernel-%{flavor}
BuildRequires:  openssl
BuildRequires:  pesign
BuildRequires:  systemd-boot
BuildRequires:  tpm2.0-tools
BuildRequires:  udev
BuildRequires:  uki-tool >= 1.4.1+0
BuildRequires:  update-bootloader
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Requires:       uki-tool >= 0.3.0+15
# Needed in post to change the type of the partition
Requires:       gptfdisk
Requires:       shim >= 11
# Needed by systemd-pcrphase at boot
Requires:       pkgconfig(tss2-tcti-device)
# Install the UKI with the correct kernel version
Requires:       kernel-%{flavor} = %{kernel_version}

%description
Generic signed Unified Kernel Image based on kernel %{flavor}

%prep
# Get the certificates used to sign
if test -e %{_sourcedir}/_projectcert.crt ; then
    cp %{_sourcedir}/_projectcert.crt ./%{cert_name}.crt
    openssl x509 -in ./%{cert_name}.crt -outform DER -out ./%{cert_name}.der
fi
# Get the static initrd from RPM.
rpm2cpio /.build.binaries/static-initrd-generic-unsigned*.rpm | cpio -idmv

%build
staticinitrd="./usr/share/initrd/$(basename ./usr/share/initrd/static-initrd-generic-*.unsigned)"
if [ ! -f "$staticinitrd" ]; then
    echo "No static initrd extracted"
    exit 1
fi
uki-tool create \
    -k %{uname} \
    -i "$staticinitrd" \
    -c "rw quiet systemd.show_status=1 console=ttyS0,115200 console=tty0"\
    -n %{efi_name}.efi \
    -o .

%install
export BRP_PESIGN_FILES="%{uki_install_dir}/%{efi_name}.efi"
install -d -m 0700 %{buildroot}%{uki_install_dir}/
install -m 0755 ./%{efi_name}.efi \
    %{buildroot}%{uki_install_dir}/%{efi_name}.efi
install -d -m 0700 %{buildroot}%{uki_install_dir}/%{efi_name}.efi.extra.d
install -d -m 0700 %{buildroot}%{uki_extra_dir}

%if %{cert_install}
install -d -m 0700 %{buildroot}%{cert_install_dir}
fpr=$(openssl x509 -sha1 -fingerprint -inform DER -noout -in ./%{cert_name}.der \
    | cut -c 18- | cut -d ":" -f 1,2,3,4 | sed 's/://g')
install -m 644 ./%{cert_name}.der \
    %{buildroot}%{cert_install_dir}/%{efi_name}-${fpr}.crt
%endif

%posttrans
# Change type of the file system partition from 8300 to 8304
dev_name=$(df -h / | tail -1 | cut -d ' ' -f1)
dev_part=${dev_name::-1}
dev_no=${dev_name: -1}
if [[ $dev_no && $dev_part ]] &&\
   [[ -b "${dev_part}${dev_no}" ]]; then
    echo "Change partition type of ${dev_part}${dev_no} in 8304"
    sgdisk -t $dev_no:8304 $dev_part || true
fi
# Add menuentry to bootloaders
entry_added=0
if [ $(command -v sdbootutil) ] && [ "$(sdbootutil bootloader)" == "systemd-boot" ]; then
  if (command -v sdbootutil > /dev/null 2>&1); then
    if uki-tool sdboot \
      --add \
      --all-ukis \
      --efi %{efi_dir}; then
        echo "Entry for UKI has been added to sdboot"
        entry_added=1
    else
        echo "Entry for UKI has not been added to sdboot"
        exit 0
    fi
  fi
else
  if (command -v grub2-mkconfig > /dev/null 2>&1); then
    if uki-tool grub2 \
      --add \
      --all-ukis \
      --efi %{efi_dir}; then
        echo "Entry for UKI has been added to Grub"
        entry_added=1
    else
        echo "Entry for UKI hasn't been added to Grub"
        exit 0
    fi
  fi
fi
cert_file=$(basename %{cert_install_dir}/%{efi_name}-*.crt)
cert_file_p="%{cert_install_dir}/${cert_file}"
if test "$entry_added" = "1" -a -f ${cert_file_p} ]; then
    echo -e "\033[0;32mTo enroll the uki certificate key please run:\033[0m"
    echo -e "\033[0;32mmokutil \
--import ${cert_file_p}\033[0m"
fi

%preun
if [ $(command -v sdbootutil) ] && [ "$(sdbootutil bootloader)" == "systemd-boot" ]; then
  if uki-tool sdboot \
    --remove \
    --all-ukis \
    --efi %{efi_dir}; then
    echo "Entry for UKI has been removed from sdboot"
  else
    echo "Entry for UKI has not been removed from sdboot"
    exit 0
  fi
else
  if (command -v grub2-mkconfig > /dev/null 2>&1); then
    if uki-tool grub2 \
      --remove \
      --all-ukis \
      --efi %{efi_dir}; then
        echo "Entries for UKI has been removed from grub2"
    else
        echo "Entries for UKI has not been removed from grub2"
        exit 0
    fi
  fi
fi

%files
%defattr(-,root,root)
%{kernel_module_directory}/*/%{efi_name}.efi*
%dir %{uki_extra_dir}
%if %{cert_install}
%dir %{_datarootdir}/unified
%dir %{_datarootdir}/unified/certs
%{cert_install_dir}/%{efi_name}-*.crt
%endif

%changelog
