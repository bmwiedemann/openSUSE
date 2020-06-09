#
# spec file for package ebiso
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           ebiso
Version:        0.2.7
Release:        0
Summary:        UEFI bootable ISO image creator for Relax-and-Recover
License:        GPL-3.0
Group:          Productivity/Archiving/Backup
# Refer to http://license.opensuse.org/
# for the list of known licences and their exact spelling:
# ebiso is only used by rear to make UEFI bootable ISO images
# accordingly ebiso is in the same RPM group as rear:
Url:            https://gitlab.com/gozora/ebiso
Source0:        https://gitlab.com/gozora/ebiso/-/archive/%{version}/ebiso-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Supplements is a reverse "Recommends" which means
# (cf. https://tr.opensuse.org/Libzypp/Dependencies):
# ebiso should be be installed if rear is is provided by an installed package.
# In particular ebiso should be be installed if rear is (to be) installed.
# The dependency resolver will do a best-try approach to install ebiso.
# If ebiso cannot be installed, installing ebiso is silently skipped.
# Also uninstalling ebiso is (silently) accepted.
# The reverse "Recommends" is used because ebiso is only available on x86_64
# so that a "Recommends: ebiso" in rear.spec could be often uninstallable.
# In contrast "Supplements: rear" in ebiso.spec can be usually fulfilled:
Supplements:    rear
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Enable building only on architectures which support UEFI
ExclusiveArch:  x86_64

%description
ebiso is needed by Relax-and-Recover (abbreviated ReaR)
to create bootable ISO images with enabled UEFI boot
on 64-bit x86_64 architecture.

ebiso only works for systems with UEFI boot.
ebiso cannot create legacy bootable ISOs.

See project pages at https://gitlab.com/gozora/ebiso

%prep
%setup -q

%build
# Setting our preferred architecture-specific flags for the compiler and linker:
export CFLAGS="%{optflags}"
# Do not strip installed binaries as this would prevent -debuginfo package
# from being created
sed -i "s|strip|/bin/true|g" Makefile
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%{_bindir}/ebiso
%{_mandir}/man1/ebiso.1%{ext_man}

%changelog
