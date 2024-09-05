#
# spec file for package nqptp
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


Name:           nqptp
Version:        1.2.4
Release:        0
Summary:        Not Quite PTP
License:        GPL-2.0-only
URL:            https://github.com/mikebrady/nqptp
Source0:        https://github.com/mikebrady/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        nqptp-user.conf
# Backported from 1.2.5-dev:
Patch0:         backport-050a8c2de9f3e1f4859abf9b36d2f18afd4c34d7.patch
# Backported from 1.2.5-dev:
Patch1:         backport-b5321a88d21b854aaa461dc0f6c226d650309b91.patch
Patch2:         disable-user-group-generation.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
%{?systemd_ordering}
%sysusers_requires

%description
nqptp is a daemon that monitors timing data from any PTP clocks – up to 64 – it
sees on ports 319 and 320. It maintains records for each clock, identified by
Clock ID and IP.

It is a companion application to Shairport Sync and provides timing information
for AirPlay 2 operation.

%prep
%autosetup -p1

%build
autoreconf -i -f
%configure --with-systemd-startup
%make_build
%sysusers_generate_pre %{SOURCE1} nqptp nqptp-user.conf

%install
%make_install
mkdir -p %{buildroot}%{_unitdir}
mv %{buildroot}%{_libdir}/systemd/system/%{name}.service \
   %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/nqptp.conf

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md RELEASE_NOTES.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/nqptp.conf

%changelog
