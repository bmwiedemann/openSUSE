#
# spec file for package shim-leap
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           shim-leap
Version:        14
Release:        0
Summary:        UEFI shim loader
License:        BSD-2-Clause
Group:          System/Boot
Source:         shim-14-lp150.8.5.1.x86_64.rpm
Source1:        shim-install
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64

%description
does not exist

%package -n shim
Summary:        UEFI shim loader
Group:          System/Boot
Requires:       perl-Bootloader

%description -n shim
shim is a trivial EFI application that, when run, attempts to open and
execute another application.

%prep
rpm2cpio %{SOURCE0} | cpio --extract --unconditional --preserve-modification-time --make-directories

%build

%install
# purely repackaged
cp -a * %{buildroot}
install -m 755 %{SOURCE1} %{buildroot}/%{_sbindir}

%post -n shim
/sbin/update-bootloader --reinit || true

%files -n shim
/etc/uefi
/usr/sbin/shim-install
/usr/lib64/efi
/usr/share/doc/packages/shim

%changelog
