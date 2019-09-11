#
# spec file for package mokutil
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mokutil
Version:        0.3.0
Release:        0
Summary:        Tools for manipulating machine owner keys
License:        GPL-3.0-only
Group:          Productivity/Security
Url:            https://github.com/lcp/mokutil
Source:         %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM mokutil-fix-overflow.patch glin@suse.com -- Fix the potential buffer overflow
Patch1:         mokutil-fix-overflow.patch
# PATCH-FIX-UPSTREAM mokutil-fshort-wchar.patch glin@suse.com -- Add "-fshort-wchar" to make sure the UEFI strings are UCS-2 encoding
Patch2:         mokutil-fshort-wchar.patch
# PATCH-FIX-UPSTREAM mokutil-set-efi-variable-file-mode.patch glin@suse.com -- Be explicit about file modes in all cases
Patch3:         mokutil-set-efi-variable-file-mode.patch
# PATCH-FIX-UPSTREAM mokutil-constify-efi-guid.patch glin@suse.com -- Make all efi_guild_t variables const
Patch4:         mokutil-constify-efi-guid.patch
# OPENSUSE ONLY
# PATCH-FIX-OPENSUSE mokutil-support-revoke-builtin-cert.patch glin@suse.com -- Add an option to revoke the built-in certificate
Patch100:       mokutil-support-revoke-builtin-cert.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  efivar-devel >= 0.12
BuildRequires:  libopenssl-devel >= 0.9.8
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64 aarch64

%description
This program provides the means to enroll and erase the machine owner
keys (MOK) stored in the database of shim.



Authors:
--------
    Gary Lin <glin@suse.com>

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch100 -p1

%build
autoreconf
%configure
make

%install
%makeinstall

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/mokutil
%{_mandir}/man?/*

%changelog
