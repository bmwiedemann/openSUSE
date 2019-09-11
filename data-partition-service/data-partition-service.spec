#
# spec file for package data-partition-service
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           data-partition-service
Version:        0.1
Release:        0
Summary:        A service that creates a data partition
License:        GPL-3.0-or-later
Group:          System/Management
Source0:        create_data_part
Source1:        data_part.cfg
Source2:        data_part.service
Source3:        LICENSE
BuildRequires:  systemd-rpm-macros
BuildRequires:  coreutils
Requires:       gptfdisk
BuildArch:      noarch
%{?systemd_requires}

%description
A service to create an additional gpt data partition if there
is free unpartitioned space on the disk.

%prep

%build
cp %{SOURCE3} LICENSE

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
install -m 755 %{SOURCE0} %{buildroot}/%{_datadir}/%{name}/create_data_part

mkdir -p %{buildroot}/%{_sysconfdir}
install -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/data_part.cfg

mkdir -p %{buildroot}/%{_unitdir}
install -m 644 %{SOURCE2} %{buildroot}/%{_unitdir}/data_part.service

%post
%service_add_post data_part.service

%preun
%service_del_preun data_part.service

%postun
%service_del_postun data_part.service

%pre
%service_add_pre data_part.service

%files
%config %{_sysconfdir}/data_part.cfg
%{_unitdir}/data_part.service
%{_datadir}/%{name}

%if 0%{?suse_version} < 1500
%doc LICENSE
%else
%license LICENSE
%endif

%changelog
