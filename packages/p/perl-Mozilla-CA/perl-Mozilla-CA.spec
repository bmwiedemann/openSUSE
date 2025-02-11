#
# spec file for package perl-Mozilla-CA
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


%define cpan_name Mozilla-CA
Name:           perl-Mozilla-CA
Version:        20250202.0.0
Release:        0
# 20250202 -> normalize -> 20250202.0.0
%define cpan_version 20250202
#Upstream: SUSE-Public-Domain
License:        GPL-2.0-or-later OR MPL-1.1 OR LGPL-2.1-or-later
Summary:        Mozilla's CA cert bundle in PEM format
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LW/LWP/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
# PATCH-FIX-OPENSUSE https://bugzilla.suse.com/show_bug.cgi?id=1228762
Patch0:         Mozilla-CA-20240730-Redirect-to-ca-certificates-bundle.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.94
Provides:       perl(Mozilla::CA) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  ca-certificates-mozilla
Requires:       ca-certificates-mozilla
# MANUAL END

%description
Mozilla::CA provides a copy of Mozilla's bundle of Certificate Authority
certificates in a form that can be consumed by modules and libraries based
on OpenSSL.

The module provide a single function:

* SSL_ca_file()

Returns the absolute path to the Mozilla's CA cert bundle PEM file.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
