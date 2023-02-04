#
# spec file for package sbsigntools
#
# Copyright (c) 2023 SUSE LLC
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


Name:           sbsigntools
Summary:        Canonical EFI binary signing tools
License:        GPL-3.0-only
Version:        0.9.4
Release:        0
URL:            http://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git
Source:         %{name}-%{version}.tar.gz
Patch0:         OpenSSL3.patch
BuildRequires:  binutils-devel
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
%if 0%{?suse_version}
BuildRequires:  gnu-efi
BuildRequires:  pkg-config
%else
BuildRequires:  gnu-efi-devel
BuildRequires:  pkgconfig
%endif
BuildRequires:  automake
BuildRequires:  git
BuildRequires:  help2man

%description
This package installs tools which can cryptographically sign EFI
binaries and drivers.

%prep
%setup -q
%patch0 -p1

%build
NOCONFIGURE=1 ./autogen.sh
CFLAGS="%optflags -Wno-error=deprecated-declarations"
%configure
make %{?jobs:-j%jobs}

%check
make check

%install
%make_install

%files
%license COPYING
%{_bindir}/*
%{_mandir}/man1/*

%changelog
