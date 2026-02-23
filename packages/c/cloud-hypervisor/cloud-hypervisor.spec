#
# spec file for package cloud-hypervisor
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           cloud-hypervisor
Version:        51.1
Release:        0
Summary:        A Virtual Machine Monitor
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://cloudhypervisor.org
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  bison
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  flex
BuildRequires:  git-core
BuildRequires:  qemu-tools
BuildRequires:  rust >= 1.89
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(ossp-uuid)
#riscv is still not ready
ExclusiveArch:  aarch64 riscv64 x86_64

%description
Cloud Hypervisor is an open source Virtual Machine Monitor (VMM) that runs on
top of the KVM hypervisor and the Microsoft Hypervisor (MSHV).

The project focuses on running modern, Cloud Workloads, on specific, common,
hardware architectures. In this case Cloud Workloads refers to those that are
run by customers inside a Cloud Service Provider. This means modern operating
systems with most I/O handled by paravirtualised devices (e.g. virtio), no
requirement for legacy devices, and 64-bit CPUs.

Cloud Hypervisor is implemented in Rust and is based on the Rust VMM crates.

%package remote
Summary:        Remote tool for accessing a cloud hypervisor instance

%description remote
%{summary}.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
install -Dm0755 ./target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dm0755 ./target/release/ch-remote %{buildroot}%{_bindir}/ch-remote

%ifnarch riscv64
%check
# skipped tests need kvm enabled
%{cargo_test} -- --test unit_tests:: \
                 --skip cpu::unit_tests:: \
                 --skip unit_tests::test_vmm_vm_cold_add_device \
                 --skip unit_tests::test_vmm_vm_cold_add_disk \
                 --skip unit_tests::test_vmm_vm_cold_add_fs \
                 --skip unit_tests::test_vmm_vm_cold_add_net \
                 --skip unit_tests::test_vmm_vm_cold_add_pmem \
                 --skip unit_tests::test_vmm_vm_cold_add_user_device \
                 --skip unit_tests::test_vmm_vm_cold_add_vdpa \
                 --skip unit_tests::test_vmm_vm_cold_add_vsock \
                 --skip unit_tests::test_vmm_vm_create \
                 --skip vm::unit_tests::test_vm \
                 --skip kvm::aarch64:: \
                 --skip vm::unit_tests::test_create_fdt_with_devices
%endif

%files
%license LICENSES/Apache-2.0.txt LICENSES/BSD-3-Clause.txt LICENSES/CC-BY-4.0.txt
%doc README.md
%caps(cap_net_admin+ep) %{_bindir}/%{name}

%files remote
%license LICENSES/Apache-2.0.txt LICENSES/BSD-3-Clause.txt LICENSES/CC-BY-4.0.txt
%doc README.md
%{_bindir}/ch-remote

%changelog
