#
# spec file for package ca-certificates
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


%define cabundle  %{_localstatedir}/lib/ca-certificates/ca-bundle.pem

%if 0%{?_build_in_place}
%define git_version %(git log '-n1' '--date=format:%Y%m%d' '--no-show-signature' "--pretty=format:+git%cd.%h")
BuildRequires:  git-core
%else
# this is required for obs' source validator. It's
# 20-files-present-and-referenced ignores all conditionals. So the
# definition of git_version actually happens always.
%define git_version %{nil}
%endif

# the ca bundle file was meant as compat option for e.g.
# proprietary packages. It's not meant to be used at all.
# unfortunately glib-networking has such a complicated abstraction
# on top of gnutls that we have to live with the bundle for now
%bcond_without cabundle

Name:           ca-certificates
Version:        2+git20260203.5937e9f%{git_version}
Release:        0
Summary:        Utilities for system wide CA certificate installation
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://github.com/openSUSE/ca-certificates
Source0:        ca-certificates-%{version}.tar
BuildRequires:  p11-kit-devel
#
Requires:       %{_bindir}/readlink
Requires:       p11-kit
Requires:       p11-kit-tools >= 0.23.1
# needed for post
Requires(post): %{_bindir}/readlink
Requires(post): p11-kit-tools
Recommends:     ca-certificates-mozilla
# no need for a separate Java package anymore. The bundle is
# created by C code.
Obsoletes:      java-ca-certificates = 1
Provides:       java-ca-certificates = %{version}-%{release}
BuildArch:      noarch

%description
Update-ca-certificates is intended to keep the certificate stores of
SSL libraries like OpenSSL or GnuTLS in sync with the system's CA
certificate store that is managed by p11-kit.

%prep
%setup -q

%build

%install
%if %{without cabundle}
rm -f certbundle.run
%endif
%make_install
install -d -m 755 %{buildroot}%{_prefix}/lib/ca-certificates/update.d
install -d -m 555 %{buildroot}%{_localstatedir}/lib/ca-certificates/pem
install -d -m 555 %{buildroot}%{_localstatedir}/lib/ca-certificates/openssl
install -d -m 755 %{buildroot}/%{_prefix}/lib/systemd/system

%pre
%service_add_pre ca-certificates.path ca-certificates.service ca-certificates-setup.service

%post
%service_add_post ca-certificates.path ca-certificates.service ca-certificates-setup.service

%posttrans
# force rebuilding all certificate stores.
update-ca-certificates -f || true

%preun
%service_del_preun ca-certificates.path ca-certificates.service ca-certificates-setup.service

%postun
if [ "$1" -eq 0 ]; then
	rm -rf %{_localstatedir}/lib/ca-certificates/pem %{_localstatedir}/lib/ca-certificates/openssl
fi
%service_del_postun ca-certificates.path ca-certificates.service ca-certificates-setup.service

%files
%license COPYING
%doc README
%dir %{_prefix}/lib/ca-certificates
%dir %{_prefix}/lib/ca-certificates/update.d
%{_prefix}/lib/systemd/system/*
%{_sbindir}/update-ca-certificates
%{_mandir}/man8/update-ca-certificates.8%{?ext_man}
%{_prefix}/lib/ca-certificates/update.d/*java.run
%{_prefix}/lib/ca-certificates/update.d/*etc_ssl.run
%{_prefix}/lib/ca-certificates/update.d/*openssl.run
#
%if %{with cabundle}
%{_prefix}/lib/ca-certificates/update.d/*certbundle.run
%endif

%changelog
