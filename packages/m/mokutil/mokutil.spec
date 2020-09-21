#
# spec file for package mokutil
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


Name:           mokutil
Version:        0.4.0
Release:        0
Summary:        Tools for manipulating machine owner keys
License:        GPL-3.0-only
Group:          Productivity/Security
URL:            https://github.com/lcp/mokutil
Source:         https://github.com/lcp/%{name}/archive/%{version}.tar.gz
Source1:        modhash
# PATCH-FIX-UPSTREAM mokutil-remove-shebang-from-bash-completion-file.patch glin@suse.com -- Remove shebang from bash-completion/mokutil
Patch1:         mokutil-remove-shebang-from-bash-completion-file.patch
# PATCH-FIX-UPSTREAM mokutil-bsc1173115-add-ca-and-keyring-checks.patch bsc#1173115 glin@suse.com -- Add options for CA and kernel keyring checks
Patch2:         mokutil-bsc1173115-add-ca-and-keyring-checks.patch
# PATCH-FIX-SUSE mokutil-remove-libkeyutils-check.patch glin@suse.com -- Disable the check of libkeyutils version
Patch3:         mokutil-remove-libkeyutils-check.patch
Patch100:       mokutil-support-revoke-builtin-cert.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  efivar-devel >= 0.12
BuildRequires:  keyutils-devel >= 1.5.0
BuildRequires:  libopenssl-devel >= 0.9.8
BuildRequires:  pkg-config
Requires:       openssl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64 aarch64 ppc64le ppc64

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
%patch100 -p1

%build
./autogen.sh
%configure
make

%install
%makeinstall
install -m 755 -D %{SOURCE1} %{buildroot}/%{_bindir}/modhash

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/mokutil
%{_bindir}/modhash
%{_mandir}/man?/*
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/mokutil

%changelog
