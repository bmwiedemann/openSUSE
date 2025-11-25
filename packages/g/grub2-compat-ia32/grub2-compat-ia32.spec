#
# spec file for package grub2-compat-ia32
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           grub2-compat-ia32
Version:        1
Release:        0
Summary:        Enable IA32 emulation support in the kernel
License:        MIT
URL:            https://en.opensuse.org/GRUB#Enabling_32bit_x86_support_in_Kernel
Source1:        README.md

Requires:       glibc-32bit
Requires:       update-bootloader
Requires(post): update-bootloader
Requires(postun): update-bootloader

BuildRequires:  update-bootloader

BuildArch:      noarch
ExclusiveArch:  x86_64

%description
Newer versions of openSUSE Leap and SLE disable 32-bit x86 (IA32) emulation by default.
Software like Steam, Wine, or VirtualBox requires 32-bit library support.
This package enables IA32 support by appending `ia32_emulation=1` to the kernel parameters via GRUB.

%prep
cp -a %{SOURCE1} .

%build

%install
# Nothing to do

%files
%doc README.md

%post
%{_sbindir}/update-bootloader --add-option "ia32_emulation=1"
%{_sbindir}/update-bootloader --config
echo "IA32 emulation has been enabled. Please reboot to apply changes."

%postun
# Only delete the option on uninstall, not upgrade
if [ "$1" -eq 0 ]; then
    %{_sbindir}/update-bootloader --del-option "ia32_emulation=1"
    %{_sbindir}/update-bootloader --config
    echo "IA32 emulation has been removed. Please reboot to apply changes."
fi

%changelog
