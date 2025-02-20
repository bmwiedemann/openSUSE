#
# spec file for package palo
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024-2025, Martin Hauke <mardnh@gmx.de>
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


Name:           palo
Version:        2.27
Release:        0
Summary:        Linux boot loader for HP PA-RISC
License:        GPL-2.0-only
Group:          System/Boot
URL:            https://git.kernel.org/pub/scm/linux/kernel/git/deller/palo.git/
Source:         https://git.kernel.org/pub/scm/linux/kernel/git/deller/palo.git/snapshot/%{name}-%{version}.tar.gz
Patch0:         reproducible.patch
BuildRequires:  help2man
# lynx is required for generation of README
BuildRequires:  lynx
Recommends:     e2fsprogs
ExclusiveArch:  %{ix86} x86_64 hppa hppa64

%description
PALO is the boot loader for HP PA-RISC machines. This package contains
both the actual boot loader called iplboot as well as a boot media
management tool after which bears the name PALO. While iplboot
can be used on PA-RISC machines only, the PALO media management tool
runs on any architecture and is used to create boot media for
HP PA-RISC machines.

%prep
%autosetup -p1

%build
%make_build

%install
%make_install DESTDIR=%{buildroot} SBINDIR=%{_sbindir} DOCDIR=%{_docdir} IFLAGS=""

%files
%license COPYING
%doc README README.html
%dir %{_docdir}/palo
%{_docdir}/palo/palo.conf
%exclude %{_docdir}/palo/changelog.gz
%{_sbindir}/palo
%dir %{_datadir}/palo
%{_datadir}/palo/iplboot
%{_mandir}/man8/palo.8%{?ext_man}

%changelog
