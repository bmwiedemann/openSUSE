#
# spec file for package cloud-init-config-MicroOS
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


Name:           cloud-init-config-MicroOS
Version:        1.1
Release:        0
Summary:        openSUSE MicroOS configuration file for could-init
License:        GPL-3.0-only
Group:          System/Management
Source0:        cloud.cfg
Source1:        COPYING
BuildRequires:  cloud-init
Requires:       cloud-init >= 17.1
Provides:       cloud-init-config = 0.7
Obsoletes:      cloud-init-config-caasp <= 1.0
BuildArch:      noarch

%description
This package contains the openSUSE MicroOS specific
configuration file for cloud-init.

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
