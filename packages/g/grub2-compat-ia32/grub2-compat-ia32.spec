#
# spec file for package grub2-compat-ia32
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

Name:           grub2-compat-ia32
Version:        1
Release:        0
Summary:        Enable IA32 emulation support in the kernel
License:        MIT
URL:            https://en.opensuse.org/GRUB#Enabling_32bit_x86_support_in_Kernel
Source1:        README.md
Source2:        05_ia32_emulation
BuildRequires:  grub2
Requires:       grub2
Requires:       glibc-32bit
BuildArch:      noarch
ExclusiveArch:  x86_64

%description
Newer versions of openSUSE Leap and SLE disable 32-bit x86 (IA32) emulation by default.
Software like Steam, Wine, or VirtualBox requires 32-bit library support.
This package enables IA32 support by appending `ia32_emulation=1` to the kernel parameters via GRUB.

%prep

%build
cp -a %{SOURCE1} .

%install
install -D -m 0755 %{SOURCE2} %{buildroot}%{_sysconfdir}/grub.d/05_ia32_emulation

%files
%doc README.md
%config(noreplace) %{_sysconfdir}/grub.d/05_ia32_emulation

%post
# Update GRUB config after installing the script
if [ -x %{_sbindir}/grub2-mkconfig ]; then
    %{_sbindir}/grub2-mkconfig -o /boot/grub2/grub.cfg || :
fi
echo "Please reboot the machine to apply IA32 emulation settings."

%changelog
