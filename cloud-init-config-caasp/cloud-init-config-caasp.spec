#
# spec file for package cloud-init-config-caasp
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


Name:           cloud-init-config-caasp
Version:        1.0
Release:        0
Summary:        SUSE CaaSP Configuration file for could-init
License:        GPL-3.0-only
Group:          System/Management
Source0:        cloud.cfg
Source1:        COPYING
BuildRequires:  cloud-init
Requires:       cloud-init >= 17.1
Provides:       cloud-init-config = 0.7
BuildArch:      noarch

%description
This package contains the SUSE Containers as a Service Platform
specific configuration file for cloud-init.

%prep
# empty on purpose

%build
cp %{SOURCE1} .

%install
mkdir -p %{buildroot}%{_sysconfdir}/cloud/cloud.cfg.d
install -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/cloud/

%files
%license COPYING
%config(noreplace) %{_sysconfdir}/cloud/cloud.cfg

%changelog
