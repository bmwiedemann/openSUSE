#
# spec file for package apache2-mod_auth_gssapi
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2004, 2005 NOVELL (All rights reserved)
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


# kinit: Configuration file does not specify default realm when parsing name maguser
%define test 0
Name:           apache2-mod_auth_gssapi
Version:        1.6.5
Release:        0
Summary:        GSSAPI Module for Apache
License:        MIT
URL:            https://github.com/gssapi/mod_auth_gssapi/
Source0:        https://github.com/gssapi/mod_auth_gssapi/releases/download/v%{version}/mod_auth_gssapi-%{version}.tar.gz
# python3 and other testsuite fixes
Patch0:         apache2-mod_auth_gssapi-test.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  krb5-devel
BuildRequires:  openssl-devel
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}
Requires:       apache2
# SECTION test requirements
%if %{test} == 1
BuildRequires:  krb5-client
BuildRequires:  krb5-plugin-preauth-pkinit
BuildRequires:  krb5-server
BuildRequires:  nss_wrapper
BuildRequires:  python3-gssapi
BuildRequires:  python3-requests-gssapi
BuildRequires:  python3-requests-kerberos
BuildRequires:  socket_wrapper
%endif
# /SECTION

%description
This module has been built as a replacement for the aging
mod_auth_kerb. Its aim is to use only GSSAPI calls and be
as much as possible agnostic of the actual mechanism used.

%prep
%autosetup -p1 -n mod_auth_gssapi-%{version}

%build
export APACHE="%{_sbindir}/httpd"
%configure
%make_build APXS=%{apache_apxs}

%install
%make_install
rm %{buildroot}%{apache_libexecdir}/*.la

%check
%if %{test} == 1
sed -i 's/env python3/python3/' tests/*.py
export PATH="$PATH:%{_sbindir}"
make check
%endif

%files
%license COPYING
%doc README
%{apache_libexecdir}/*.so

%changelog
