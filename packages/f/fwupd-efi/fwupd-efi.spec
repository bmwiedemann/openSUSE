#
# spec file for package fwupd-efi
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
# needssslcertforbuild

Name:           fwupd-efi
Version:        1.1
Release:        0
Summary:        Firmware update EFI binaries
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Management
URL:            https://github.com/fwupd/fwupd-efi
# Do not use upstream tarball, we are using source service!
Source:         %{name}-%{version}.tar.xz

Patch1:		0001-meson-using-local-copy-ldscript-when-local-copy-crt0.patch
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  gnu-efi
BuildRequires:  pesign-obs-integration
BuildRequires:  pkgconfig(efiboot)
BuildRequires:  pkgconfig(efivar) >= 33
Requires:       shim >= 11
ExclusiveArch:  x86_64 aarch64

%description
A UEFI binary for the fwupd project for installing updates using the UpdateCapsule
runtime service.

It was originally imported from the combined fwupd project, and is now
maintained separately to allow fwupd userspace releases and fwupd-efi UEFI
executable releases to follow a different cadence.

%prep
%autosetup -p1

%build
# Since Tumbleweed is still using openSUSE signkey, the SBAT distro id
# should be opensuse.
%if 0%{?sle_version}
distro_id="sle"
distro_name="SUSE Linux Enterprise"
%else
distro_id="opensuse"
distro_name="The openSUSE project"
%endif

# Dell support requires direct SMBIOS access,
# Synaptics requires Dell support, i.e. x86 only
%meson \
  -Defi_sbat_distro_id="${distro_id}" \
  -Defi_sbat_distro_summary="${distro_name}" \
  -Defi_sbat_distro_pkgname="%{name}" \
  -Defi_sbat_distro_version="%{version}" \
  -Defi_sbat_distro_url="https://build.opensuse.org" \
%meson_build

%install
export BRP_PESIGN_FILES='%{_libexecdir}/fwupd/efi/fwupd*.efi'
%meson_install

# link fwupd*.efi.signed to fwupd*.efi (bsc#1129466)
FWUPD_EFI=`basename %{buildroot}/%{_libexecdir}/fwupd/efi/fwupd*.efi`
ln -s %{_libexecdir}/fwupd/efi/$FWUPD_EFI %{buildroot}/%{_libexecdir}/fwupd/efi/$FWUPD_EFI.signed

# do not need pc file yet 
rm $RPM_BUILD_ROOT%{_libdir}/pkgconfig/fwupd-efi.pc

%postun
if [ -e /etc/os-release ]; then
  . /etc/os-release
  efi_distributor="$(echo "${NAME} ${VERSION}" | tr 'A-Z' 'a-z' | cut -d' ' -f1)"
fi
if [ "$1" = 0 ] && [ -d "/boot/efi/EFI/$efi_distributor" ]; then
  # Remove all capsule files
  rm -rf /boot/efi/EFI/"$efi_distributor"/fw
  # Remove the UEFI firmware update program
  rm -f /boot/efi/EFI/"$efi_distributor"/fwupd*.efi
fi

%files

%license COPYING
%doc README.md
%{_libexecdir}/fwupd

%changelog
