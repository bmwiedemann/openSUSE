#
# spec file for package efitools
#
# Copyright (c) 2020 SUSE LLC
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


Name:           efitools
Version:        1.9.2
Release:        0
Summary:	UEFI secure boot toolkit
License:        GPL-2.0-only and LGPL-2.1-only
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git
Source:         https://git.kernel.org/pub/scm/linux/kernel/git/jejb/efitools.git/snapshot/%{name}-%{version}.tar.gz
Patch1:         efitools-disable-efisigned.patch
BuildRequires:  gnu-efi
BuildRequires:  help2man
BuildRequires:  openssl-devel
BuildRequires:  perl-File-Slurp
ExclusiveArch:  %{ix86} x86_64 aarch64 %{arm}

%description
The collection of tools for UEFI secure boot (userspace tools only)

%prep
%setup -q
%patch1 -p1

%build
#make_build
make

%install
export BRP_PESIGN_FILES='%{_datadir}/%{name}/efi/*.efi'
%make_install

# Remove COPYING and README installed by "make install"
# Those two files are packaged later.
rm -f %{buildroot}/%{_datadir}/%{name}/COPYING
rm -f %{buildroot}/%{_datadir}/%{name}/README

# Remove EFI binaries
rm -rf %{buildroot}/%{_datadir}/%{name}/

# Also remove efitool-mkusb which needs self-signed EFI binaries
rm -f %{buildroot}/%{_bindir}/efitool-mkusb

%files
%license COPYING
%doc README
%{_bindir}/cert-to-efi-hash-list
%{_bindir}/cert-to-efi-sig-list
%{_bindir}/efi-readvar
%{_bindir}/efi-updatevar
%{_bindir}/flash-var
%{_bindir}/hash-to-efi-sig-list
%{_bindir}/sig-list-to-certs
%{_bindir}/sign-efi-sig-list
%{_mandir}/man1/*

%changelog
