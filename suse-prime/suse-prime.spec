#
# spec file for package suse-prime
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           suse-prime
Version:        0.5
Release:        0
Summary:        GPU (nvidia/intel) selection for NVIDIA optimus laptops
License:        SUSE-Public-Domain
Group:          System/X11/Utilities
Url:            https://github.com/openSUSE/SUSEPrime
Source0:        https://github.com/openSUSE/SUSEPrime/archive/%{version}.tar.gz#/SUSEPrime-%{version}.tar.gz
Patch0:         U_Corrected-DPI-value-in-xorg-nvidia.conf.patch
Recommends:     nvidia_driver
Supplements:    modalias(nvidia_driver:pci:v00008086d*sv*sd*bc03sc*i*)
Conflicts:      suse-prime-alt
BuildArch:      noarch

%description
A collection of shell scripts that makes it possible to use the
NVIDIA GPU on a Optimus Laptop. The switching is similar to
the feature provided by the nvidia-prime package in Ubuntu.

%prep
%setup -n SUSEPrime-%{version}
%patch0 -p1

%build
:

%install
mkdir -p %{buildroot}%{_sysconfdir}/prime
install -m 0644 xorg-intel.conf  %{buildroot}%{_sysconfdir}/prime/
install -m 0644 xorg-intel-intel.conf  %{buildroot}%{_sysconfdir}/prime/
install -m 0644 xorg-nvidia.conf %{buildroot}%{_sysconfdir}/prime/
install -m 0644 09-nvidia-blacklist.conf %{buildroot}%{_sysconfdir}/prime/
install -m 0644 prime-select.service %{buildroot}%{_sysconfdir}/prime/
echo       "undefined"         > %{buildroot}%{_sysconfdir}/prime/current_type
install -D -m 0755 prime-select.sh %{buildroot}%{_sbindir}/prime-select

%preun
if [ "$1" -eq 0 ]; then
   # cleanup before uninstalling the package completely
   %{_sbindir}/prime-select unset
fi

%files
%defattr(-,root,root)
%doc README.md
%{_sysconfdir}/prime
%config %{_sysconfdir}/prime/xorg-intel.conf
%config %{_sysconfdir}/prime/xorg-intel-intel.conf
%config %{_sysconfdir}/prime/xorg-nvidia.conf
%config %{_sysconfdir}/prime/09-nvidia-blacklist.conf
%config %{_sysconfdir}/prime/prime-select.service
%config(noreplace) %{_sysconfdir}/prime/current_type
%{_sbindir}/prime-select

%changelog
