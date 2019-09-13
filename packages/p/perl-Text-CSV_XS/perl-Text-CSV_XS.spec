#
# spec file for package perl-Text-CSV_XS
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


Name:           perl-Text-CSV_XS
Version:        1.39
Release:        0
%define cpan_name Text-CSV_XS
Summary:        Comma-Separated Values Manipulation Routines
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HM/HMBRAND/%{cpan_name}-%{version}.tgz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
Recommends:     perl(Encode) >= 2.98
%{perl_requires}

%description
Text::CSV_XS provides facilities for the composition and decomposition of
comma-separated values. An instance of the Text::CSV_XS class will combine
fields into a 'CSV' string and parse a 'CSV' string into fields.

The module accepts either strings or files as input and support the use of
user-specified characters for delimiters, separators, and escapes.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's,/pro/bin/perl,/usr/bin/perl,' examples/*
# MANUAL END

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc ChangeLog CONTRIBUTING.md examples README

%changelog
