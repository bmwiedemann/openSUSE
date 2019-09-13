#
# spec file for package cloud-init-vmware-guestinfo
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


Name:           cloud-init-vmware-guestinfo
Version:        1.1.0
Release:        0
Source:         %{name}-%{version}.tar.gz
Summary:        A cloud-init datasource that uses VMware GuestInfo
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/vmware/cloud-init-vmware-guestinfo
Requires:       cloud-init
BuildRequires:  python-rpm-macros
BuildRequires:  cloud-init
BuildArch:      noarch

%description
A cloud-init datasource that uses VMware GuestInfo. The main
purpose is to allow the use of extra-config in Terraform.

%prep
%setup

%build

%install
install -d 0755 %{buildroot}%{_sysconfdir}/cloud/cloud.cfg.d
install -d 0755 %{buildroot}%{python3_sitelib}/cloudinit/sources/
install -m 0644 99-DataSourceVMwareGuestInfo.cfg %{buildroot}%{_sysconfdir}/cloud/cloud.cfg.d/99-DataSourceVMwareGuestInfo.cfg
install -m 0644 DataSourceVMwareGuestInfo.py %{buildroot}%{python3_sitelib}/cloudinit/sources/DataSourceVMwareGuestInfo.py

%clean

%files
%defattr(0644, root, root, 0755)
%config %{_sysconfdir}/cloud/cloud.cfg.d/99-DataSourceVMwareGuestInfo.cfg
%{python3_sitelib}/cloudinit/sources/DataSourceVMwareGuestInfo.py

%changelog
