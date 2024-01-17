#
# spec file for package uefi-mbr
#
# Copyright (c) 2022 SUSE LLC
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


Name:           uefi_mbr
Version:        0+git20221129.53aad69
Release:        0
Summary:        MBR loader that just prints a message.
License:        BSD-3-Clause
URL:            https://github.com/wfeldt/uefi_mbr
Source:         uefi_mbr-%{version}.tar
BuildRequires:  nasm

%description
MBR loader that just prints a message for use in UEFI only
appliances

%prep
%setup -q

%build
make

%install
install -D -m 644 uefi_mbr.bin %{buildroot}/usr/lib/uefi_mbr/uefi_mbr.bin

%files
%license LICENSE
%dir /usr/lib/uefi_mbr
/usr/lib/uefi_mbr/uefi_mbr.bin

%changelog

