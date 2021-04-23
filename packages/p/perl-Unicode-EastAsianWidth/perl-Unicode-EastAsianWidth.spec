#
# spec file for package perl-Unicode-EastAsianWidth
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Unicode-EastAsianWidth
Version:        12.0
Release:        0
#Upstream:  This work is under the *CC0 1.0 Universal* license. or neighboring rights to Unicode-EastAsianWidth. This work is published from Taiwan. the http://creativecommons.org/publicdomain/zero/1.0 manpage
%define cpan_name Unicode-EastAsianWidth
Summary:        East Asian Width properties
License:        CC0-1.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AU/AUDREYT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
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
%setup -q -n %{cpan_name}-%{version}

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README README.mkdn

%changelog
