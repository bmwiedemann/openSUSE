#
# spec file for package lxd-ovmf-setup
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

%define ovmf_suse_dir %{_datadir}/qemu

%define lxd_dir %{_datadir}/lxd
%define lxd_ovmf_dir %{lxd_dir}/ovmf

Name:           lxd-ovmf-setup
Version:        20241211
Release:        0
Source0:        README.txt
Summary:        Default OVMF links for LXD
URL:            https://build.opensuse.org
License:        MIT
Group:          Development/Libraries/Other
BuildArch:      noarch
BuildRequires:  qemu-ovmf-x86_64
BuildRequires:  qemu-uefi-aarch64

%description
Provides the default links for OVMF

%package x86_64
Summary:  Symlink package for OVMF x86_64
Group:    Development/Libraries/Other
Requires: qemu-ovmf-x86_64

%description x86_64
Provides the default links for OVMF
for software which doesn't use the QEMU firmware files
such as LXD and Incus

%package aarch64
Summary:  Symlink package for OVMF aarch64
Group:    Development/Libraries/Other
Requires: qemu-uefi-aarch64

%description aarch64
Provides the default links for OVMF
for software which doesn't use the QEMU firmware files
such as LXD and Incus

%prep
true

%build
true

%install
mkdir -p %{buildroot}%{lxd_ovmf_dir}

# X86_64
ln -s %{ovmf_suse_dir}/ovmf-x86_64-4m-code.bin %{buildroot}%{lxd_ovmf_dir}/OVMF_CODE_4M.fd
ln -s %{ovmf_suse_dir}/ovmf-x86_64-4m-vars.bin %{buildroot}%{lxd_ovmf_dir}/OVMF_VARS_4M.fd
ln -s %{ovmf_suse_dir}/ovmf-x86_64-ms-4m-code.bin %{buildroot}%{lxd_ovmf_dir}/OVMF_CODE_4M.ms.fd
ln -s %{ovmf_suse_dir}/ovmf-x86_64-ms-4m-vars.bin %{buildroot}%{lxd_ovmf_dir}/OVMF_VARS_4M.ms.fd

# aarch64
ln -s %{ovmf_suse_dir}/aavmf-aarch64-code.bin %{buildroot}%{lxd_ovmf_dir}/AAVMF_CODE.fd
ln -s %{ovmf_suse_dir}/aavmf-aarch64-vars.bin %{buildroot}%{lxd_ovmf_dir}/AAVMF_VARS.fd
ln -s %{ovmf_suse_dir}/aavmf-aarch64-ms-code.bin %{buildroot}%{lxd_ovmf_dir}/AAVMF_CODE.ms.fd
ln -s %{ovmf_suse_dir}/aavmf-aarch64-ms-vars.bin %{buildroot}%{lxd_ovmf_dir}/AAVMF_VARS.ms.fd


%files x86_64
%dir %{lxd_dir}
%dir %{lxd_ovmf_dir}
%{lxd_ovmf_dir}/OVMF_CODE_4M.fd
%{lxd_ovmf_dir}/OVMF_VARS_4M.fd
%{lxd_ovmf_dir}/OVMF_CODE_4M.ms.fd
%{lxd_ovmf_dir}/OVMF_VARS_4M.ms.fd

%files aarch64
%dir %{lxd_dir}
%dir %{lxd_ovmf_dir}
%{lxd_ovmf_dir}/AAVMF_CODE.fd
%{lxd_ovmf_dir}/AAVMF_VARS.fd
%{lxd_ovmf_dir}/AAVMF_CODE.ms.fd
%{lxd_ovmf_dir}/AAVMF_VARS.ms.fd

%changelog
