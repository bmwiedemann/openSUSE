#
# spec file for package perl-Encode
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Encode
Name:           perl-Encode
Version:        3.200.0
Release:        0
%define cpan_version 3.20
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Character encodings in Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        perl-Encode-rpmlintrc
Source2:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(parent) >= 0.221
Requires:       perl(parent) >= 0.221
Provides:       perl(Encode) = 3.200.0
Provides:       perl(Encode::Alias) = 2.25
Provides:       perl(Encode::CJKConstants) = 2.200.0
Provides:       perl(Encode::CN::HZ) = 2.10
Provides:       perl(Encode::Config) = 2.500.0
Provides:       perl(Encode::Encoder) = 2.300.0
Provides:       perl(Encode::Encoding) = 2.800.0
Provides:       perl(Encode::GSM0338) = 2.10
Provides:       perl(Encode::Guess) = 2.800.0
Provides:       perl(Encode::JP::H2Z) = 2.200.0
Provides:       perl(Encode::JP::JIS7) = 2.800.0
Provides:       perl(Encode::KR::2022_KR) = 2.400.0
Provides:       perl(Encode::MIME::Header) = 2.29
Provides:       perl(Encode::MIME::Header::ISO_2022_JP) = 1.900.0
Provides:       perl(Encode::MIME::Name) = 1.300.0
Provides:       perl(Encode::UTF_EBCDIC)
Provides:       perl(Encode::Unicode::UTF7) = 2.10
Provides:       perl(Encode::XS)
Provides:       perl(Encode::utf8)
Provides:       perl(encoding) = 3.00
%define         __perllib_provides /bin/true
%{perl_requires}

%description
The 'Encode' module provides the interface between Perl strings and the
rest of the system. Perl strings are sequences of _characters_.

The repertoire of characters that Perl can represent is a superset of those
defined by the Unicode Consortium. On most platforms the ordinal values of
a character as returned by 'ord(_S_)' is the _Unicode codepoint_ for that
character. The exceptions are platforms where the legacy encoding is some
variant of EBCDIC rather than a superset of ASCII; see perlebcdic.

During recent history, data is moved around a computer in 8-bit chunks,
often called "bytes" but also known as "octets" in standards documents.
Perl is widely used to manipulate data of many types: not only strings of
characters representing human or computer languages, but also "binary"
data, being the machine's representation of numbers, pixels in an image, or
just about anything.

When Perl is processing "binary data", the programmer wants Perl to process
"sequences of bytes". This is not a problem for Perl: because a byte has
256 possible values, it easily fits in Perl's much larger "logical
character".

This document mostly explains the _how_. perlunitut and perlunifaq explain
the _why_.

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
# MANUAL BEGIN
%__rm -f ${RPM_BUILD_ROOT}/usr/bin/enc2xs
%__rm -f ${RPM_BUILD_ROOT}/usr/bin/encguess
%__rm -f ${RPM_BUILD_ROOT}/usr/bin/piconv
%__rm -f ${RPM_BUILD_ROOT}/usr/share/man/man1/enc2xs.1*
%__rm -f ${RPM_BUILD_ROOT}/usr/share/man/man1/encguess.1*
%__rm -f ${RPM_BUILD_ROOT}/usr/share/man/man1/piconv.1*
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%doc AUTHORS Changes README

%changelog
