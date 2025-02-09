#
# spec file for package perl-Digest-MD4
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


%define cpan_name Digest-MD4
Name:           perl-Digest-MD4
Version:        1.900.0
Release:        0
# 1.9 -> normalize -> 1.900.0
%define cpan_version 1.9
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl interface to the MD4 Algorithm
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIKEM/DigestMD4/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Digest::MD4) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The 'Digest::MD4' module allows you to use the RSA Data Security Inc. MD4
Message Digest algorithm from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 128-bit
"fingerprint" or "message digest" of the input.

The 'Digest::MD4' module provide a procedural interface for simple use, as
well as an object oriented interface that can handle messages of arbitrary
length and which can read files directly.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README rfc1320.txt

%changelog
