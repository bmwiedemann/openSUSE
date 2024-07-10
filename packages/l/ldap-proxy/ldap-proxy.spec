#
# spec file for package ldap-proxy
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) specCURRENT_YEAR SUSE LLC
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


%define configdir %{_sysconfdir}/ldap-proxy

Name:           ldap-proxy
Version:        0.1.0~6
Release:        0
Summary:        An in-memory caching proxy for LDAP
License:        MPL-2.0 AND MPL-2.0+
URL:            https://github.com/kanidm/ldap-proxy
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  libopenssl-3-devel
ExclusiveArch:  %{rust_tier1_arches}

%description
An in-memory caching proxy for LDAP that allows limiting of DN searches.

%prep
%autosetup -a1
install -D -m 644 %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{configdir}
install -D -d -m 0755 %{buildroot}%{_sbindir}
install -D -d -m 0755 %{buildroot}%{_unitdir}

install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_sbindir}/%{name}
install -m 0644 %{_builddir}/%{name}-%{version}/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -m 0644 %{_builddir}/%{name}-%{version}/config.toml %{buildroot}%{configdir}/

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%dir %{configdir}
%config(noreplace) %{configdir}/config.toml
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
