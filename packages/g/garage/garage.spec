#
# spec file for package garage
#
# Copyright (c) 2024 SUSE LLC
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


Name:           garage
Version:        1.0.1
Release:        0
Summary:        S3-compatible object store for small self-hosted geo-distributed deployments
License:        AGPL-3.0-only
URL:            https://git.deuxfleurs.fr/Deuxfleurs/garage
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        %{name}.service
Source21:       system-user-%{name}.conf
BuildRequires:  cargo >= 1.77
BuildRequires:  cargo-packaging
BuildRequires:  libseccomp-devel
BuildRequires:  sysuser-tools
BuildRequires:  zstd

ExcludeArch:    %{ix86}

%description
Garage is an S3-compatible distributed object storage service designed for
self-hosting at a small-to-medium scale.

Garage is designed for storage clusters composed of nodes running at different
physical locations, in order to easily provide a storage service that
replicates data at these different locations and stays available even when some
servers are unreachable. Garage also focuses on being lightweight, easy to
operate, and highly resilient to machine failures.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

# system-user
%sysusers_generate_pre %{SOURCE21} user

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

# server systemd unit file
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

# configuration in /etc/garage/
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}/

# directory in /var/lib/
install -d -m 0755 %{buildroot}%{_sharedstatedir}/%{name}
install -d -m 0755 %{buildroot}%{_sharedstatedir}/%{name}/data/
install -d -m 0755 %{buildroot}%{_sharedstatedir}/%{name}/meta/

# system user
install -Dm644 %{SOURCE21} %{buildroot}%{_sysusersdir}/system-user-%{name}.conf

%pre -f user.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/system-user-%{name}.conf

%dir %attr(755,root, %{name}) %{_sysconfdir}/%{name}/
%ghost %config(noreplace) %{_sysconfdir}/%{name}/%{name}.toml
%dir %attr(750,%{name}, %{name}) %{_sharedstatedir}/%{name}/
%dir %attr(750,%{name}, %{name}) %{_sharedstatedir}/%{name}/data/
%dir %attr(750,%{name}, %{name}) %{_sharedstatedir}/%{name}/meta/

%changelog
