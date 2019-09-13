#
# spec file for package perl-B-Keywords
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


Name:           perl-B-Keywords
Version:        1.20
Release:        0
#Upstream:  2017-2019 Reini Urban, All rights reserved. This program is free software; you can redistribute it and/or modify it under the terms of either: a) the GNU General Public License as published by the Free Software Foundation; version 2, or b) the "Artistic License" which comes with Perl.
%define cpan_name B-Keywords
Summary:        Lists of reserved barewords and symbol names
License:        GPL-2.0-only OR Artistic-1.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RURBAN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
'B::Keywords' supplies several arrays of exportable keywords: '@Scalars',
'@Arrays', '@Hashes', '@Filehandles', '@Symbols', '@Functions',
'@Barewords', '@TieIOMethods', '@UNIVERSALMethods' and '@ExporterSymbols'.

The '@Symbols' array includes the contents of each of '@Scalars',
'@Arrays', '@Hashes', '@Functions' and '@Filehandles'.

Similarly, '@Barewords' adds a few non-function keywords and operators to
the '@Functions' array.

All additions and modifications are welcome.

The perl parser uses a static list of keywords from _regen/keywords.pl_
which constitutes the strict list of keywords @Functions and @Barewords,
though some @Functions are not functions in the strict sense. Several
library functions use more special symbols, handles and methods.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
