#
# spec file for package perl-Sereal-Decoder
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


%define cpan_name Sereal-Decoder
Name:           perl-Sereal-Decoder
Version:        5.003
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Binary serialization module for Perl (decoder part)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Y/YV/YVES/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.0
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.21
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
%{perl_requires}

%description
This library implements a deserializer for an efficient, compact-output,
and feature-rich binary protocol called _Sereal_. Its sister module
Sereal::Encoder implements an encoder for this format. The two are released
separately to allow for independent and safer upgrading.

The Sereal protocol versions that are compatible with this decoder
implementation are currently protocol versions 1, 2, 3 and 4. As it stands,
it will refuse to attempt to decode future versions of the protocol, but if
necessary there is likely going to be an option to decode the parts of the
input that are compatible with version 4 of the protocol. The protocol was
designed to allow for this.

The protocol specification and many other bits of documentation can be
found in the github repository. Right now, the specification is at
https://github.com/Sereal/Sereal/blob/master/sereal_spec.pod, there is a
discussion of the design objectives in
https://github.com/Sereal/Sereal/blob/master/README.pod, and the output of
our benchmarks can be seen at
https://github.com/Sereal/Sereal/wiki/Sereal-Comparison-Graphs.

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
# Don't build with smp_flags!
make

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes

%changelog
