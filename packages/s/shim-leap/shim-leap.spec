#
# spec file for package shim-leap
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
Version:        15.4
Release:        0
Summary:        UEFI shim loader
License:        BSD-2-Clause
Group:          System/Boot
Source:         shim-15.4-lp152.4.8.1.x86_64.rpm
Source1:        README
Source2:        shim-install
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64

%description
does not exist

%package -n shim
Summary:        UEFI shim loader
Group:          System/Boot
Requires:       perl-Bootloader

%description -n shim
shim is a trivial EFI application that, when run, attempts to open and
execute another application.

%prep
rpm2cpio %{SOURCE0} | cpio --extract --unconditional --preserve-modification-time --make-directories

%build

%install
# purely repackaged
cp -a * %{buildroot}
cp %{S:1} .

# install updated shim-install
chmod +x %{S:2}
cp %{S:2} %{buildroot}/%{_sbindir}/shim-install

%post -n shim
/sbin/update-bootloader --reinit || true

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
