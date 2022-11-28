#
# spec file for package pam_saslauthd
#
# Copyright (c) 2022 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           pam_saslauthd
#               This will be set by osc services, that will run after this.
Version:        0.1.0~1
Release:        0
Summary:        A pam module to authenticated saslauthd as a provider
#               If you know the license, put it's SPDX string here.
#               Alternately, you can use cargo lock2rpmprovides to help generate this.
License:        MPL-2.0
#               Select a group from this link:
#               https://en.opensuse.org/openSUSE:Package_group_guidelines
Group:          Productivity/Networking/Security
Url:            https://github.com/Firstyear/pam_saslauthd
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging
BuildRequires:  pam-devel
# Because tar doesn't req zstd even though it's a valid and auto-impled compression.
BuildRequires:  zstd
Requires:       cyrus-sasl-saslauthd
ExclusiveArch:  %{rust_tier1_arches}

%description
A pam module that allows authentication to saslauthd as a provider. This only provides authentication
not authorisation so you MUST not use this as a complete auth provider.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
%if 0%{?suse_version} > 1549
install -D -d -m 0755 %{buildroot}%{_pam_vendordir}
install -m 0644 %{_builddir}/%{name}-%{version}/saslauthd.pam %{buildroot}%{_pam_vendordir}/saslauthd

install -D -d -m 0755 %{buildroot}/%{_pam_moduledir}
install -m 0644 %{_builddir}/%{name}-%{version}/target/release/libpam_saslauthd.so %{buildroot}/%{_pam_moduledir}/pam_saslauthd.so
%else
install -D -d -m 0755 %{buildroot}%{_sysconfdir}
install -D -d -m 0755 %{buildroot}%{_sysconfdir}/pam.d/
install -m 0644 %{_builddir}/%{name}-%{version}/saslauthd.pam %{buildroot}%{_sysconfdir}/pam.d/saslauthd

install -D -d -m 0755 %{buildroot}/%_lib/security
install -m 0644 %{_builddir}/%{name}-%{version}/target/release/libpam_saslauthd.so %{buildroot}/%_lib/security/pam_saslauthd.so
%endif

%files
%defattr(-,root,root)
%if 0%{?suse_version} > 1549
%{_pam_vendordir}/saslauthd
%{_pam_moduledir}/pam_saslauthd.so
%else
%dir %{_sysconfdir}/pam.d
%config(noreplace) %{_sysconfdir}/pam.d/saslauthd
/%_lib/security/pam_saslauthd.so
%endif

%changelog
