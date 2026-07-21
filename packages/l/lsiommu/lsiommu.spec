#
# spec file for package lsiommu
#
# Copyright (c) 2026 SUSE LLC
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           lsiommu
Version:        1.0
Release:        0
Summary:        List IOMMU groups with their PCIe devices and USB controllers
License:        MIT
URL:            https://gist.github.com/r15ch13/ba2d738985fce8990a4e9f32d07c6ada
Source1:        iommu.sh
Source2:        lsiommu.1
Requires:       pciutils
Requires:       usbutils
BuildArch:      noarch

%description
A hardware inspection utility that shows the relationships between
IOMMU groups, physical PCIe hardware, and nested USB buses.

It is commonly used when setting up Kernel-based Virtual Machines (KVM) with
VFIO hardware passthrough (i.e., PCIe passthrough of a host device, such as a
graphics card or a network interface) to a guest VM.

%prep

%build

%install
install -D %{SOURCE1} %{buildroot}/%{_bindir}/%{name}
install -D -m 644 %{SOURCE2} %{buildroot}/%{_mandir}/man1/%{name}.1

%check

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
