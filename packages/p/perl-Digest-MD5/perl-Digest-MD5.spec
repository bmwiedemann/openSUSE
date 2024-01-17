#
# spec file for package perl-Digest-MD5
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


%define cpan_name Digest-MD5
Name:           perl-Digest-MD5
Version:        2.590.0
Release:        0
%define cpan_version 2.59
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl interface to the MD-5 algorithm
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Digest::MD5) = %{version}
%define         __perllib_provides /bin/true
%{perl_requires}

%description
The 'Digest::MD5' module allows you to use the RSA Data Security Inc. MD5
Message Digest algorithm from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 128-bit
"fingerprint" or "message digest" of the input.

Note that the MD5 algorithm is not as strong as it used to be. It has since
2005 been easy to generate different messages that produce the same MD5
digest. It still seems hard to generate messages that produce a given
digest, but it is probably wise to move to stronger algorithms for
applications that depend on the digest to uniquely identify a message.

The 'Digest::MD5' module provide a procedural interface for simple use, as
well as an object oriented interface that can handle messages of arbitrary
length and which can read files directly.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes README rfc1321.txt

%changelog
