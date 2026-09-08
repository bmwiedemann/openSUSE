#
# spec file for package perl-Net-IDN-Encode
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Net-IDN-Encode
Name:           perl-Net-IDN-Encode
Version:        2.502.0
Release:        0
# 2.502 -> normalize -> 2.502.0
%define cpan_version 2.502
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Internationalizing Domain Names in Applications (UTS #46)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build) >= 0.420
BuildRequires:  perl(Test::NoWarnings)
Provides:       perl(Net::IDN::Encode) = %{version}
Provides:       perl(Net::IDN::Punycode) = %{version}
Provides:       perl(Net::IDN::Punycode::PP) = %{version}
Provides:       perl(Net::IDN::UTS46) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides an easy-to-use interface for encoding and decoding
Internationalized Domain Names (IDNs).

IDNs use characters drawn from a large repertoire (Unicode), but IDNA
allows the non-ASCII characters to be represented using only the ASCII
characters already allowed in so-called host names today
(letter-digit-hyphen, '/[A-Z0-9-]/i').

Use this module if you just want to convert domain names (or email
addresses), using whatever IDNA standard is the best choice at the moment.

You should be familiar with Unicode support in perl, as this module expects
correctly encoded input. See perlunitut, perluniintro and perlunicode for
details.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
