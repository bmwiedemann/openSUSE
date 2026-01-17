#
# spec file for package static-initrd
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


%define build_signed %{?signed_override}%{!?signed_override:0}

%if %{build_signed}
# needssslcertforbuild
%endif

# Versions variables to set
# -------------------------
%define ver 0.1
%define patch_ver 0
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

# Kernel flavors
# -------------------------
%global kernel_flavors "default vanilla"
# -------------------------

# Flavors conditions
# -------------------------
%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" != ""
%define name_suffix -%{?flavor}
%endif
# -------------------------

# Useful variables
# -------------------------
%define project_version %{ver}.%{patch_ver}
%global kernel_version %(rpm -q --queryformat '%{VERSION}' kernel-default)
%define initrd_name static-initrd%{?name_suffix}
%define certs_name %{initrd_name}
# -------------------------

Name:           static-initrd
Version:        %{project_version}_k%{kernel_version}
Release:        0
Summary:        Pre-build static initrd
License:        GPL-3.0-only
Group:          System/Base
URL:            https://kernel.org
%if "%{flavor}" == ""
ExclusiveArch:  do_not_build
%endif
Source1:        openSUSE-UEFI-CA-Certificate.crt
Source2:        packages-base
Source3:        packages-network
BuildRequires:  binutils
BuildRequires:  dracut
BuildRequires:  grub2
BuildRequires:  kernel-default
BuildRequires:  kernel-firmware
BuildRequires:  kernel-vanilla
BuildRequires:  uki-tool >= 1.5.0
Requires:       uki-tool >= 1.5.0
%if %{build_signed}
BuildRequires:  pesign-obs-integration
%endif
BuildRequires:  update-bootloader
%ifnarch s390 s390x
BuildRequires:  rng-tools
%endif

# Dependencies for a base initrd
# -------------------------
BuildRequires:  bash
BuildRequires:  btrfsprogs
BuildRequires:  e2fsprogs
BuildRequires:  kbd
BuildRequires:  less
BuildRequires:  lvm2
BuildRequires:  procps
BuildRequires:  systemd
BuildRequires:  udev
BuildRequires:  util-linux
BuildRequires:  util-linux-systemd
BuildRequires:  xfsprogs
BuildRequires:  zstd
# -------------------------

# Dependencies for a generic initrd
# -------------------------
%if "%{flavor}" == "generic"
%ifarch x86_64
BuildRequires:  biosdevname
BuildRequires:  connman
BuildRequires:  connman-client
%endif
BuildRequires:  NetworkManager
BuildRequires:  cifs-utils
BuildRequires:  curl
BuildRequires:  dbus-1-daemon
BuildRequires:  dbus-broker
BuildRequires:  fcoe-utils
BuildRequires:  gpg2
BuildRequires:  iproute2
BuildRequires:  jq
BuildRequires:  keyutils
BuildRequires:  mdadm
BuildRequires:  nbd
BuildRequires:  nfs-client
BuildRequires:  ntfs-3g
BuildRequires:  nvme-cli
BuildRequires:  open-lldp
BuildRequires:  openssh-clients
BuildRequires:  openssh-common
BuildRequires:  pcsc-lite
BuildRequires:  rpcbind
BuildRequires:  squashfs
BuildRequires:  systemd-coredump
BuildRequires:  systemd-experimental
BuildRequires:  systemd-network
BuildRequires:  systemd-portable
BuildRequires:  wicked
# Dependencies for TPM/PCR
BuildRequires:  tpm2.0-tools
BuildRequires:  tpm2-0-tss-devel
%endif
# -------------------------

# Dependencies for a network initrd
# -------------------------
%if "%{flavor}" == "network"
BuildRequires:  NetworkManager
BuildRequires:  NetworkManager-dns-dnsmasq
BuildRequires:  dbus-broker
BuildRequires:  grep
BuildRequires:  iproute2
BuildRequires:  iputils
BuildRequires:  nfs-client
BuildRequires:  rpcbind
%endif
# -------------------------

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       shim >= 11

# With Default kernel flavor
# -------------------------
%package -n static-initrd-%{?flavor}-default
Provides:       static-initrd-%{?flavor} = %{version}-%{release}
Obsoletes:      static-initrd-%{?flavor} < %{version}-%{release}
Summary:        Pre-build static %{?flavor} initrd with kernel default.
Requires:       kernel-default = %{kernel_version}

%description -n static-initrd-%{?flavor}-default
The signed static %{flavor} Initrd build for kernel-default %{kernel_version}.

%package -n static-initrd-%{?flavor}-default-unsigned
Provides:       static-initrd-%{?flavor}-unsigned = %{version}-%{release}
Obsoletes:      static-initrd-%{?flavor}-unsigned < %{version}-%{release}
Summary:        Unsigned static %{flavor} initrd with kernel default.
Requires:       kernel-default = %{kernel_version}

%description -n static-initrd-%{?flavor}-default-unsigned
The Unsigned static %{flavor} Initrd build for kernel-default
%{kernel_version}.

%if %{build_signed}
%files -n static-initrd-%{?flavor}-default
%defattr(-,root,root)
/boot/%{name}-*-default
%dir %{_datarootdir}/initrd/
%dir %{_datarootdir}/initrd/certs
%{_datarootdir}/initrd/certs/*-%{name}.crt
%endif

%files -n static-initrd-%{?flavor}-default-unsigned
%defattr(-,root,root)
%dir %{_datarootdir}/initrd/
%{_datarootdir}/initrd/%{name}-*-default.unsigned
# -------------------------

# With vanilla kernel flavor
# -------------------------
%package -n static-initrd-%{?flavor}-vanilla
Summary:        Pre-build static %{?flavor} initrd with kernel vanilla.
Requires:       kernel-vanilla = %{kernel_version}

%description -n static-initrd-%{?flavor}-vanilla
The Unsigned static %{flavor} Initrd build for kernel-vanilla
%{kernel_version}.

%package -n static-initrd-%{?flavor}-vanilla-unsigned
Summary:        Unsigned static %{flavor} initrd with kernel vanilla.
Requires:       kernel-vanilla = %{kernel_version}

%description -n static-initrd-%{?flavor}-vanilla-unsigned
The Unsigned static %{flavor} Initrd build for kernel-vanilla
%{kernel_version}.

%if %{build_signed}
%files -n static-initrd-%{?flavor}-vanilla
%defattr(-,root,root)
/boot/%{name}-*-vanilla
%dir %{_datarootdir}/initrd/
%dir %{_datarootdir}/initrd/certs
%{_datarootdir}/initrd/certs/*-%{name}.crt
%endif

%files -n static-initrd-%{?flavor}-vanilla-unsigned
%defattr(-,root,root)
%dir %{_datarootdir}/initrd/
%{_datarootdir}/initrd/%{name}-*-vanilla.unsigned
# -------------------------

%description
The static %{flavor} Initrd build for kernel %{kernel_version} in efi format.

%prep
%if %{build_signed}
# Store the certificate file used to sign the initrd file
if test -e %{_sourcedir}/_projectcert.crt ; then
    cp %{_sourcedir}/_projectcert.crt ./%{certs_name}.crt
else
    echo "No _projectcert file in sources"
    cp %{SOURCE1} ./%{certs_name}.crt
fi
openssl x509 -in ./%{certs_name}.crt -outform DER -out ./%{certs_name}.der
%endif

%build
omit_modules="iscsi lunmask multipath memstrack"
%ifnarch x86_64 aarch64
omit_modules="$omit_modules connman biosdevname systemd-pcrphase"
%endif
%ifarch s390x s390
omit_modules="$omit_modules rngd"
%endif

# Create the config file to the list of packages according the flavors
conf_file="./dracut.conf"
list_packages=""
%if "%{flavor}" == "base"
    list_packages="%{SOURCE2}"
%endif
%if "%{flavor}" == "network"
    list_packages="%{SOURCE3}"
%endif
touch $conf_file

[ -d ~/dracut.tmp ] || mkdir ~/dracut.tmp
flavors=$(echo "%kernel_flavors" | tr "\n" " ")
for k_flavor in $flavors; do
  uname="$(ls /usr/lib/modules/ | grep "${k_flavor}" | tail -n1)"
  if [[ "$list_packages" != "" ]]; then
      echo "dracutmodules+=\" \\" > "$conf_file"
      while IFS= read -r line; do
          check=$(dracut --list-modules --kver=${uname} | grep -x "$line")
          if [[ "$check" == "$line" ]]; then
              echo "$line \\" >> "$conf_file"
          else
              echo "Warning $line is not in the dracut modules list"
          fi
      done <"$list_packages"
  else
      echo "add_dracutmodules+=\" \\" > "$conf_file"
      echo "systemd-pcrphase \\" >> "$conf_file"
      echo "tpm2-tss \\" >> "$conf_file"
  fi
  echo "\"" >> "$conf_file"
  # Build the initramfs for each kernel flavor
  dracut \
    --confdir ~/dracut.tmp \
    --reproducible \
    --kernel-image /lib/modules/${uname}/%{ker_name} \
    --kver ${uname} \
    --kmoddir /lib/modules/${uname} \
    --fwdir /lib/firmware \
    --no-hostonly \
    --no-hostonly-cmdline \
    --no-hostonly-default-device \
    --conf=$conf_file \
    --kernel-cmdline "rw security=apparmor rd.multipath=0" \
    --omit "${omit_modules}" \
    --xz \
    --show-modules \
    --add-drivers="fat vfat" \
    --filesystems="vfat ext4 xfs btrfs overlay" \
    ./initrd-${uname}
done
rm -rf ~/dracut.tmp

%install
mkdir %{buildroot}/boot
mkdir -p %{buildroot}%{_datarootdir}/initrd
flavors=$(echo "%kernel_flavors" | tr "\n" " ")
for k_flavor in $flavors; do
  uname="$(ls /usr/lib/modules/ | grep "${k_flavor}" | tail -n1)"
%if %{build_signed}
  grub2-wrap -O x86_64-efi \
    -n .GRUBini \
    -i "./initrd-${uname}" \
    -o "./initrd-${uname}.dll"
  install -m 0600 \
    ./initrd-${uname}.dll \
    %{buildroot}/boot/%{initrd_name}-${uname}
  export BRP_PESIGN_FILES="/boot/%{initrd_name}-${uname}"
  # install certs
  if test -e ./%{certs_name}.der ; then
      mkdir -p %{buildroot}%{_datarootdir}/initrd/certs
      fpr=$(openssl x509 -sha1 -fingerprint -inform DER -noout \
            -in ./%{certs_name}.der \
            | cut -c 18- \
            | cut -d ":" -f 1,2,3,4 \
            | sed 's/://g')
      install -m 644 \
        ./%{certs_name}.der \
        %{buildroot}%{_datarootdir}/initrd/certs/${fpr}-%{initrd_name}.crt
  fi
%endif
  install -m 0600 \
    ./initrd-${uname} \
    %{buildroot}%{_datarootdir}/initrd/%{initrd_name}-${uname}.unsigned
done

%post
if [[ -d /etc/grub.d ]];then
    initrd_file=$(basename /boot/%{name}-*)
    uname=${initrd_file#%{name}-}
    # Create the grub entry
    uki-tool grub2 \
      --add \
      --initrd /boot/${initrd_file} \
      --kerver /boot/vmlinuz-${uname}
fi

%postun
if [[ -d /etc/grub.d ]];then
    initrd_file=$(basename /boot/%{name}-*)
    uki-tool grub2 \
      --remove \
      --initrd /boot/${initrd_file}
fi

%changelog
