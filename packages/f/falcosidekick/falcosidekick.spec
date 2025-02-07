#
# spec file for package falcosidekick
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


Name:           falcosidekick
Version:        2.31.1
Release:        0
Summary:        A simple daemon for connecting Falco to your ecosystem
License:        Apache-2.0
URL:            https://github.com/falcosecurity/falcosidekick
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
# taken from https://github.com/falcosecurity/falcosidekick?tab=readme-ov-file#with-systemd
Source2:        %{name}.service
BuildRequires:  go >= 1.23

%description
A simple daemon for connecting Falco to your ecosystem. It takes a Falco events
and forward them to different outputs in a fan-out way.

It works as a single endpoint for as many Falco instances as you want.

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X main.GitVersion=%{version} \
   -X main.gitCommit=${COMMIT_HASH} \
   -X main.gitTreeState=clean \
   -X main.buildDate=${BUILD_DATE}" \
   -o bin/%{name} .

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

# systemd unit
install -D -m 0644 %{SOURCE2} %{buildroot}/%{_unitdir}/%{name}.service

# configuration directory
install -d -m 0755 %{buildroot}/%{_sysconfdir}/%{name}

%pre
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
%dir %attr(770,root,root) %config %{_sysconfdir}/%{name}

%changelog
