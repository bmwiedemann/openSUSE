#
# spec file for package perl-B-Keywords
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


%define cpan_name B-Keywords
Name:           perl-B-Keywords
Version:        1.270.0
Release:        0
# 1.27 -> normalize -> 1.270.0
%define cpan_version 1.27
#Upstream:  2017-2021 Reini Urban, All rights reserved. This program is free software; you can redistribute it and/or modify it under the terms of either: a) the GNU General Public License as published by the Free Software Foundation; version 2, or b) the "Artistic License" which comes with Perl.
License:        Artistic-1.0 OR GPL-2.0-only
Summary:        Lists of reserved barewords and symbol names
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(B::Keywords) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
'B::Keywords' supplies several arrays of exportable keywords: '@Scalars',
'@Arrays', '@Hashes', '@Filehandles', '@Symbols', '@Functions',
'@Barewords', '@BarewordsExtra', '@TieIOMethods', '@UNIVERSALMethods' and
'@ExporterSymbols'.

The '@Symbols' array includes the contents of each of '@Scalars',
'@Arrays', '@Hashes', '@Functions' and '@Filehandles'.

Similarly, '@Barewords' adds a few non-function keywords and operators to
the '@Functions' array.

'@BarewordsExtra' adds a few barewords which are not in keywords.h.

All additions and modifications are welcome.

The perl parser uses a static list of keywords from _regen/keywords.pl_
which constitutes the strict list of keywords @Functions and @Barewords,
though some @Functions are not functions in the strict sense. Several
library functions use more special symbols, handles and methods.

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
%license LICENSE

%changelog
