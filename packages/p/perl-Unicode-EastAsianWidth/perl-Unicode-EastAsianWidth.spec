#
# spec file for package perl-Unicode-EastAsianWidth
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


%define cpan_name Unicode-EastAsianWidth
Name:           perl-Unicode-EastAsianWidth
Version:        12.0.0
Release:        0
# 12.0 -> normalize -> 12.0.0
%define cpan_version 12.0
#Upstream:  This work is under the *CC0 1.0 Universal* license. or neighboring rights to Unicode-EastAsianWidth. This work is published from Taiwan. the http://creativecommons.org/publicdomain/zero/1.0 manpage
License:        CC0-1.0
Summary:        East Asian Width properties
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AU/AUDREYT/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
Provides:       perl(Unicode::EastAsianWidth) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provide user-defined Unicode properties that deal with width
status of East Asian characters, as specified in
http://www.unicode.org/unicode/reports/tr11/.

It exports the following functions to the caller's scope, to be used by
Perl's Unicode matching system: 'InEastAsianFullwidth',
'InEastAsianHalfwidth', 'InEastAsianAmbiguous', 'InEastAsianNarrow'
'InEastAsianWide', 'InEastAsianNeutral'.

In accord to TR11 cited above, two additional context-sensitive properties
are exported: 'InFullwidth' (union of 'Fullwidth' and 'Wide') and
'InHalfwidth' (union of 'Halfwidth', 'Narrow' and 'Neutral').

_Ambiguous_ characters are treated by default as part of 'InHalfwidth', but
you can modify this behaviour by assigning a true value to
'$Unicode::EastAsianWidth::EastAsian' at compile time within a 'BEGIN'
block before loading this module:

    BEGIN { $Unicode::EastAsianWidth::EastAsian = 1; }
    use Unicode::EastAsianWidth;

Setting '$Unicode::EastAsianWidth::EastAsian' at run-time used to work on
Perl versions between 5.8 and 5.14 due to an implementation detail, but it
will no longer work on Perl 5.16 and later versions, and hence is not
recommended.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README README.mkdn

%changelog
