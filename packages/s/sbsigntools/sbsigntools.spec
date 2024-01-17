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
Version:        0.9.5
Release:        0
URL:            http://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git
Source:         %{name}-%{version}.tar.gz
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
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
CFLAGS="%optflags -Wno-error=maybe-uninitialized"
%configure
%make_build

%check
%make_build check

%install
%make_install

%files
%license COPYING
%{_bindir}/sbattach
%{_bindir}/sbkeysync
%{_bindir}/sbsiglist
%{_bindir}/sbsign
%{_bindir}/sbvarsign
%{_bindir}/sbverify
%{_mandir}/man1/sbattach.1%{?ext_man}
%{_mandir}/man1/sbkeysync.1%{?ext_man}
%{_mandir}/man1/sbsiglist.1%{?ext_man}
%{_mandir}/man1/sbsign.1%{?ext_man}
%{_mandir}/man1/sbvarsign.1%{?ext_man}
%{_mandir}/man1/sbverify.1%{?ext_man}

%changelog
