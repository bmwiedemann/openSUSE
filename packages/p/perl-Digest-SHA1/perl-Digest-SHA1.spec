#
# spec file for package perl-Digest-SHA1
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


%define cpan_name Digest-SHA1
Name:           perl-Digest-SHA1
Version:        2.130.0
Release:        0
# 2.13 -> normalize -> 2.130.0
%define cpan_version 2.13
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl interface to the SHA-1 algorithm
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GAAS/%{cpan_name}-%{cpan_version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Digest::SHA1) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The 'Digest::SHA1' module allows you to use the NIST SHA-1 message digest
algorithm from within Perl programs. The algorithm takes as input a message
of arbitrary length and produces as output a 160-bit "fingerprint" or
"message digest" of the input.

In 2005, security flaws were identified in SHA-1, namely that a possible
mathematical weakness might exist, indicating that a stronger hash function
would be desirable. The Digest::SHA module implements the stronger
algorithms in the SHA family.

The 'Digest::SHA1' module provide a procedural interface for simple use, as
well as an object oriented interface that can handle messages of arbitrary
length and which can read files directly.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes fip180-1.gif fip180-1.html README

%changelog
