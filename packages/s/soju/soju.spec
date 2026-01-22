#
# spec file for package soju
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           soju
Version:        0.10.1
Release:        0
Summary:        IRCv3 bouncer
License:        AGPL-3.0-only
URL:            https://soju.im/
Source0:        https://codeberg.org/emersion/soju/releases/download/v%{version}/soju-%{version}.tar.gz
Source1:        https://codeberg.org/emersion/soju/releases/download/v%{version}/soju-%{version}.tar.gz.sig
Source2:        vendor.tar.zst
Source3:        soju-sysusers.conf
Source4:        soju-tmpfiles.conf
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig
BuildRequires:  scdoc
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
BuildRequires:  zstd
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(sqlite3)

%description
Soju is an IRC bouncer. It connects to upstream IRC servers on
behalf of the user to provide extra functionality and supports
features such as multiple users, numerous IRCv3 extensions,
chat history playback and detached channels.
It is well-suited for both small and large deployments.

%prep
%autosetup -p1 -a2

%build
%make_build GOFLAGS="-mod=vendor -buildmode=pie -tags=libsqlite3,pam"

%sysusers_generate_pre %{SOURCE3} soju soju.conf

%install
%make_install PREFIX=%{_prefix}
install -D -m0644 -t %{buildroot}%{_unitdir} contrib/soju.service
install -D -m0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/soju.conf
install -D -m0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/soju.conf

%check
go test ./...

%pre -f soju.pre
%service_add_pre soju.service

%preun
%service_del_preun soju.service

%post
%tmpfiles_create %{_tmpfilesdir}/soju.conf
%service_add_post soju.service

%postun
%service_del_postun soju.service

%files
%license LICENSE
%doc README.md doc/*.md doc/ext
%{_bindir}/soju*
%{_mandir}/man1/soju*
%dir %{_sysconfdir}/soju
%config(noreplace) %{_sysconfdir}/soju/config

%{_unitdir}/*.service
%{_sysusersdir}/soju.conf
%{_tmpfilesdir}/soju.conf
%ghost %dir %attr(0755,soju,soju) /run/soju

%changelog
