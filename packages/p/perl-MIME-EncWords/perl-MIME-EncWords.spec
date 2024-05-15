#
# spec file for package perl-MIME-EncWords
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


%define cpan_name MIME-EncWords
Name:           perl-MIME-EncWords
Version:        1.15.0
Release:        0
# 1.015.0 -> normalize -> 1.15.0
%define cpan_version 1.015.0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Deal with RFC 2047 encoded words (improved)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(MIME::Charset) >= 1.10.1
Requires:       perl(MIME::Charset) >= 1.10.1
Provides:       perl(Encode::MIME::EncWords) = 0.03
Provides:       perl(MIME::EncWords) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Fellow Americans, you probably won't know what the hell this module is for.
Europeans, Russians, et al, you probably do. ':-)'.

For example, here's a valid MIME header you might get:

      From: =?US-ASCII?Q?Keith_Moore?= <moore@cs.utk.edu>
      To: =?ISO-8859-1?Q?Keld_J=F8rn_Simonsen?= <keld@dkuug.dk>
      CC: =?ISO-8859-1?Q?Andr=E9_?= Pirard <PIRARD@vm1.ulg.ac.be>
      Subject: =?ISO-8859-1?B?SWYgeW91IGNhbiByZWFkIHRoaXMgeW8=?=
       =?ISO-8859-2?B?dSB1bmRlcnN0YW5kIHRoZSBleGFtcGxlLg==?=
       =?US-ASCII?Q?.._cool!?=

The fields basically decode to (sorry, I can only approximate the Latin
characters with 7 bit sequences /o and 'e):

      From: Keith Moore <moore@cs.utk.edu>
      To: Keld J/orn Simonsen <keld@dkuug.dk>
      CC: Andr'e  Pirard <PIRARD@vm1.ulg.ac.be>
      Subject: If you can read this you understand the example... cool!

*Supplement*: Fellow Americans, Europeans, you probably won't know what the
hell this module is for. East Asians, et al, you probably do. '(^_^)'.

For example, here's a valid MIME header you might get:

      Subject: =?EUC-KR?B?sNTAuLinKGxhemluZXNzKSwgwvzB9ri7seIoaW1w?=
       =?EUC-KR?B?YXRpZW5jZSksILGzuLgoaHVicmlzKQ==?=

The fields basically decode to (sorry, I cannot approximate the non-Latin
multibyte characters with any 7 bit sequences):

      Subject: ???(laziness), ????(impatience), ??(hubris)

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%license ARTISTIC GPL

%changelog
