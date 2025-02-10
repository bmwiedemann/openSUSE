#
# spec file for package mokutil
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


Name:           mokutil
Version:        0.7.2
Release:        0
Summary:        Tools for manipulating machine owner keys
License:        GPL-3.0-only
Group:          Productivity/Security
URL:            https://github.com/lcp/mokutil
Source:         https://github.com/lcp/%{name}/archive/%{version}.tar.gz
# PATCH-FIX-SUSE mokutil-remove-libkeyutils-check.patch glin@suse.com -- Disable the check of libkeyutils version
Patch1:         mokutil-remove-libkeyutils-check.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  efivar-devel >= 0.12
BuildRequires:  keyutils-devel >= 1.5.0
BuildRequires:  libopenssl-devel >= 0.9.8
BuildRequires:  pkgconfig
Requires:       openssl
ExclusiveArch:  x86_64 aarch64 ppc64le ppc64

%description
This program provides the means to enroll and erase the machine owner
keys (MOK) stored in the database of shim.

%prep
%setup -q
%if 0%{?suse_version} <= 1500
%patch -P 1 -p1
%endif

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_bindir}/mokutil
%{_mandir}/man?/*
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/mokutil

%changelog
