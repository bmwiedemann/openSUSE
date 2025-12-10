#
# spec file for package shim-leap
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


# Move 'efi'-executables to '/usr/share/efi' (FATE#326960, bsc#1166523)
%define sysefibasedir  %{_datadir}/efi
%define sysefidir      %{sysefibasedir}/%{_target_cpu}
%if 0%{?suse_version} < 1600
# provide compatibility sym-link for residual kiwi, etc.
%define shim_lib64_share_compat 1
%endif

Name:           shim-leap
Version:        15.8
Release:        0
Summary:        UEFI shim loader
License:        BSD-2-Clause
Group:          System/Boot
Source0:        shim-15.8-lp155.8.2.x86_64.rpm
Source1:        shim-15.8-lp155.8.8.aarch64.rpm
Source2:        README
Source3:        shim-install
BuildRequires:  fde-tpm-helper-rpm-macros
BuildRequires:  update-bootloader-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64 aarch64

%description
does not exist

%package -n shim
Summary:        UEFI shim loader
Group:          System/Boot
Requires:       perl-Bootloader
%if 0%{?fde_tpm_update_requires:1}
%fde_tpm_update_requires
%endif

%description -n shim
shim is a trivial EFI application that, when run, attempts to open and
execute another application.

%prep
%ifarch         x86_64
rpm2cpio %{SOURCE0} | cpio --extract --unconditional --preserve-modification-time --make-directories
%else
rpm2cpio %{SOURCE1} | cpio --extract --unconditional --preserve-modification-time --make-directories
%endif

%build

%install
# purely repackaged
cp -a etc usr %{buildroot}
cp %{S:2} .

# Override shim-install
install -m 755 %{S:3} %{buildroot}/%{_sbindir}/shim-install

%if %{undefined shim_lib64_share_compat}
# Remove the sym-links in /usr/lib64/efi
rm -rf %{buildroot}/usr/lib64/efi
%endif

%post -n shim
%if 0%{?fde_tpm_update_post:1}
%fde_tpm_update_post shim
%endif

%if 0%{?update_bootloader_check_type_reinit_post:1}
%update_bootloader_check_type_reinit_post grub2-efi
%else
/sbin/update-bootloader --reinit || true
%endif

%posttrans -n shim
%{?update_bootloader_posttrans}
%{?fde_tpm_update_posttrans}

%files -n shim
%doc README
%dir %{?sysefibasedir}
%dir %{sysefidir}
%{sysefidir}/shim.efi
%{sysefidir}/shim-*.efi
%{sysefidir}/shim-*.der
%{sysefidir}/MokManager.efi
%{sysefidir}/fallback.efi
%if %{defined shim_lib64_share_compat}
# provide compatibility sym-link for previous kiwi, etc.
%dir /usr/lib64/efi
/usr/lib64/efi/*.efi
%endif
/etc/uefi
%{_sbindir}/shim-install
/usr/share/doc/packages/shim

%changelog
