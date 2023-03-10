#
# spec file for package perl-Sereal
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


%define cpan_name Sereal
Name:           perl-Sereal
Version:        5.003
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Binary serialization module for Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Y/YV/YVES/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Sereal::Decoder) >= 5.003
BuildRequires:  perl(Sereal::Encoder) >= 5.003
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
Requires:       perl(Sereal::Decoder) >= 5.003
Requires:       perl(Sereal::Encoder) >= 5.003
%{perl_requires}

%description
_Sereal_ is an efficient, compact-output, binary and feature-rich
serialization protocol. The Perl encoder is implemented as the
Sereal::Encoder module, the Perl decoder correspondingly as
Sereal::Decoder. They are distributed separately to allow for safe
upgrading without downtime. (Hint: Upgrade the decoder everywhere first,
then the encoder.)

This 'Sereal' module is a very thin wrapper around both 'Sereal::Encoder'
and 'Sereal::Decoder'. It depends on both and loads both. So if you have a
user of both encoder and decoder, it is enough to depend on a particular
version of 'Sereal' and you'll get the most recent released versions of
'Sereal::Encoder' and 'Sereal::Decoder' whose version is smaller than or
equal to the version of 'Sereal' you depend on.

The protocol specification and many other bits of documentation can be
found in the github repository. Right now, the specification is at
https://github.com/Sereal/Sereal/blob/master/sereal_spec.pod, there is a
discussion of the design objectives in
https://github.com/Sereal/Sereal/blob/master/README.pod, and the output of
our benchmarks can be seen at
https://github.com/Sereal/Sereal/wiki/Sereal-Comparison-Graphs.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
