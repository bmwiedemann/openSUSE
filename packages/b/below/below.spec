#
# spec file for package below
#
# Copyright (c) 2025 SUSE LLC
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


Name:           below
Version:        0.8.1~0
Release:        0
Summary:        A time traveling resource monitor for modern Linux systems
License:        Apache-2.0
URL:            https://github.com/facebookincubator/below
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  libelf-devel
BuildRequires:  systemd-rpm-macros
Recommends:     logrotate
ExclusiveArch:  %{rust_tier1_arches}

%description
below is an interactive tool to view and record historical system data. It has support for:

- information regarding hardware resource utilization
- viewing the cgroup hierarchy
- cgroup and process information
- pressure stall information (PSI)
- record mode to record system data
- replay mode to replay historical system data
- live mode to view live system data
- dump subcommand to report script-friendly information (e.g. JSON and CSV)

below does not have support for cgroup1.

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%check

%install
install -D -m0644 %{_builddir}/%{name}-%{version}%{_sysconfdir}/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -D -p -m0644 %{_builddir}/%{name}-%{version}%{_sysconfdir}/logrotate.conf %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -D -d -m0755 %{buildroot}%{_bindir}
install -m0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -d -m1755 %{buildroot}%{_localstatedir}/log/%{name}

%files
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%dir %{_sysconfdir}/logrotate.d
%dir %{_localstatedir}/log/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%changelog
