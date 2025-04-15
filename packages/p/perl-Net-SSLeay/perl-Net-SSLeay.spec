#
# spec file for package perl-Net-SSLeay
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


%define cpan_name Net-SSLeay
Name:           perl-Net-SSLeay
Version:        1.940.0
Release:        0
# 1.94 -> normalize -> 1.940.0
%define cpan_version 1.94
License:        Artistic-2.0
Summary:        Perl bindings for OpenSSL and LibreSSL
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHRISN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
# PATCH-FIX-UPSTREAM: Fix build with openssl >= 3.4.1
Patch:          test-32_x509_get_cert_info-allow-single-colon.patch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Net::SSLeay) = %{version}
Provides:       perl(Net::SSLeay::Handle) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libopenssl-devel
BuildRequires:  zlib-devel
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Test::Warn)
# MANUAL END

%description
This module provides Perl bindings for libssl (an SSL/TLS API) and
libcrypto (a cryptography API).

%prep
%autosetup -p1 -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING.md Credits examples QuickRef README README.OSX README.VMS README.Win32
%license LICENSE

%changelog
