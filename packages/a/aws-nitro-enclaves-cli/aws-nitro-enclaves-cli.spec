#
# spec file for package aws-nitro-enclaves-cli
#
# Copyright (c) 2021 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
%define ne_system_group ne
%define ne_rundir %_rundir/nitro_enclaves


Name:           aws-nitro-enclaves-cli
Version:        1.2.2~git0.4ccc639
Release:        0
Summary:        Tools for managing enclaves
License:        Apache-2.0
Url:            https://github.com/aws/aws-nitro-enclaves-cli
ExclusiveArch:  aarch64 x86_64
Patch0:         %name.patch
Source0:        %name-%version.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source3:        aws-nitro-enclaves-cli-rpmlintrc
Source9:        aws-nitro-enclaves-sdk-bootstrap-746ec5d2713e539b94e651601b5c24ec1247c955.tar.xz
Requires(pre):  system-group-%ne_system_group = %version-%release
Requires(post): coreutils
Requires:       aws-nitro-enclaves-binaryblobs
Requires:       jq
BuildRequires:  cargo > 1.58
BuildRequires:  clang
BuildRequires:  glibc-devel-static
BuildRequires:  openssl-devel
BuildRequires:  rust > 1.58
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools

%description
A collection of tools and commands used for managing the lifecycle of
enclaves. The Nitro CLI needs to be installed on the parent instance,
and it can be used to start, manage, and terminate enclaves.

%package -n aws-nitro-enclaves-binaryblobs-upstream
Summary:        Upstream kernel binary for AWS Nitro Enclaves
Provides:       aws-nitro-enclaves-binaryblobs = %version-%release
%description  -n aws-nitro-enclaves-binaryblobs-upstream
This package contains a kernel binary and a helper binary, which is
used by the nitro-cli build-enclave command to generate a Enclave
Image File.

%package -n system-group-%ne_system_group
Summary:        System group %ne_system_group for AWS Nitro Enclaves
%?sysusers_requires

%description -n system-group-%ne_system_group
System group %ne_system_group for Nitro Enclaves.

%prep
%autosetup -p1 -a1

%build
tar --extract --verbose --strip-components=1 '--file=%SOURCE9'
ln vsock_proxy/README.md README.vsock_proxy.md
ln third_party/linuxkit/LICENSE LICENSE.linuxkit
ln drivers/COPYING COPYING.binary-kernel
tee README.md <<'_EOR_'
Nitro Enclaves are "secondary VMs" running in an EC2 instance.
Their only storage is the memory which is assigned to them.
Their only way to communicate with the primary is the usage of AF_VSOCK.
The "primary VM" releases some of its memory and cpus, which is then assigned to the enclaves.
This is done by nitro-enclaves-allocator.service, which uses
%_sysconfdir/nitro_enclaves/allocator.yaml as configuration file.
This systemd service has to be enabled manually, and started:
  systemctl enable nitro-enclaves-allocator
  systemctl start nitro-enclaves-allocator

This command has to be used to run an existing Enclave Image File:
  nitro-cli run-enclave --eif-path /path/to/file.eif --cpu-count 2 --memory 512

How to build and run an example enclave:
  zypper in -y docker
  systemctl enable docker
  systemctl start docker
  docker pull opensuse/leap
  tee Dockerfile <<'_EOF_'
FROM opensuse/leap
ENV HELLO="Hello from the enclave side!"
COPY hello.sh /bin/hello.sh
CMD ["/bin/hello.sh"]
_EOF_
  tee hello.sh <<'_EOF_'
#!/bin/sh
# Copyright 2020 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
count=123
while test $count -gt 0; do
    printf "[%4d] $HELLO\n" $count
    count=$((count-1))
    sleep 5
done
_EOF_
  chmod -v 555 *.sh
  docker build -t hello-enclave:1.0 ./
  nitro-cli build-enclave --docker-uri hello-enclave:1.0 --output-file hello.eif
  nitro-cli run-enclave --eif-path hello.eif --cpu-count 2 --memory 512 --debug-mode --attach-console
_EOR_
%install
mkdir .cargo
cp %{SOURCE2} .cargo/config
%if 0%{?__debug_package}
rustflags='-Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=2'
release=
dir='debug'
%else
rustflags='-Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=0'
release='--release'
dir='release'
%endif
RUSTFLAGS="${rustflags}" cargo build ${release} --manifest-path=./Cargo.toml
RUSTFLAGS="${rustflags}" cargo build ${release} --manifest-path=./vsock_proxy/Cargo.toml

mkdir -vp '%buildroot%_unitdir'
cp -aviLt "$_" \
	bootstrap/nitro-enclaves-allocator.service \
	vsock_proxy/service/nitro-enclaves-vsock-proxy.service \
	%nil
mkdir -vp '%buildroot%_bindir'
cp -aviLt "$_" \
	target/${dir}/nitro-cli \
	target/${dir}/vsock-proxy \
	bootstrap/nitro-enclaves-allocator \
	bootstrap/nitro-cli-config \
	%nil

d='%buildroot%_datadir/nitro_enclaves'
mkdir -vp "${d}"
cp -aviLt "$_" \
	bootstrap/allocator.yaml \
	vsock_proxy/configs/vsock-proxy.yaml \
	%nil
blobs="${d}/blobs"
mkdir -vp "${blobs}"
%ifarch aarch64
cp -aviLt "${blobs}" blobs/aarch64/*
tee "${blobs}/cmdline" <<'_EOC_'
reboot=k panic=3 pci=off nomodules console=ttyS0 random.trust_cpu=on root=/dev/ram0
_EOC_
%endif
%ifarch x86_64
cp -aviLt "${blobs}" blobs/x86_64/*
tee "${blobs}/cmdline" <<'_EOC_'
reboot=k panic=3 pci=off nomodules console=ttyS0 i8042.noaux i8042.nomux i8042.nopnp i8042.dumbkbd random.trust_cpu=on
_EOC_
%endif
gcc -Wall %optflags -static -o "${blobs}/init" init.c

mkdir -vp '%buildroot%_tmpfilesdir'
tee '%buildroot%_tmpfilesdir/%name.conf' <<_EOF_
d %{ne_rundir} 0775 root %ne_system_group
_EOF_

mkdir -vp '%buildroot%_udevrulesdir'
tee '%buildroot%_udevrulesdir/%name.conf' <<'_EOF_'
KERNEL=="nitro_enclaves", SUBSYSTEM=="misc", OWNER="root", GROUP="%{ne_group}", MODE="0660", TAG+="systemd"
_EOF_

suc='system-group-%ne_system_group.conf'
tee "${suc}" <<'_EOC_'
g %ne_system_group -
_EOC_
mkdir -p '%buildroot%_sysusersdir'
cp -aviLt "$_" "${suc}"
%sysusers_generate_pre "${suc}" system-group-%ne_system_group

%files -n system-group-%ne_system_group
%_sysusersdir/*.conf

%pre -n system-group-%ne_system_group -f system-group-%ne_system_group.pre
%pre
%service_add_pre nitro-enclaves-allocator.service nitro-enclaves-vsock-proxy.service
%post
if test "$1" -eq 1
then
	mkdir -vpm 0755 '%_sysconfdir/nitro_enclaves'
	cp -aviLt '%_sysconfdir/nitro_enclaves' \
	%_datadir/nitro_enclaves/allocator.yaml
fi
ld='/var/log/nitro_enclaves'
mkdir -vp "${ld}"
chmod -v 0770 "${ld}"
chown -v '0:%ne_system_group' "${ld}"
%tmpfiles_create %_tmpfilesdir/%name.conf
%udev_rules_update
%service_add_post nitro-enclaves-allocator.service nitro-enclaves-vsock-proxy.service
%preun
%service_del_preun nitro-enclaves-allocator.service nitro-enclaves-vsock-proxy.service
%postun
%service_del_postun_without_restart nitro-enclaves-allocator.service nitro-enclaves-vsock-proxy.service

%files
%doc README.md
%doc README.vsock_proxy.md
%doc docs/image_signing.md
%license LICENSE
%license THIRD_PARTY_LICENSES
%license THIRD_PARTY_LICENSES*.html
%dir %_datadir/nitro_enclaves
%_bindir/*
%_datadir/nitro_enclaves/allocator.yaml
%_datadir/nitro_enclaves/vsock-proxy.yaml
%_tmpfilesdir/%name.conf
%_udevrulesdir/%name.conf
%_unitdir/nitro-enclaves-allocator.service
%_unitdir/nitro-enclaves-vsock-proxy.service

%files -n aws-nitro-enclaves-binaryblobs-upstream
%license COPYING.binary-kernel
%license LICENSE.linuxkit
%dir %_datadir/nitro_enclaves
%_datadir/nitro_enclaves/blobs

%changelog

