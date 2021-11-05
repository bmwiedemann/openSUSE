#
# spec file for package sassist
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2017 Dell, Inc.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           sassist
Version:        0.8.6
Release:        0
Summary:        Dell SupportAssist log collector
License:        MIT
Group:          System/Monitoring
URL:            http://www.dell.com/en-us/work/learn/supportassist
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  systemd
Requires:       supportutils
Requires:       freeipmi
Requires:       zip
BuildArch:      noarch

%description
Dell SupportAssist log collector for Linux.

%prep
%setup -q -n %{name}-%{version}

%build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

install -p -m755 src/sassist.sh %{buildroot}%{_bindir}
install -p -m644 src/systemd/sassist.service %{buildroot}%{_unitdir}
install -p -m644 src/systemd/sassist-collect.service %{buildroot}%{_unitdir}
install -p -m644 src/systemd/run-media-iDRAC_NATOSC.mount %{buildroot}%{_unitdir}

%files
%license COPYING
%{_bindir}/sassist.sh
%{_unitdir}/sassist.service
%{_unitdir}/sassist-collect.service
%{_unitdir}/run-media-iDRAC_NATOSC.mount

%post
%systemd_post sassist.service

%preun
%systemd_preun sassist.service

%postun
%systemd_postun_with_restart sassist.service