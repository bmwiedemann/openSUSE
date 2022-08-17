#
# spec file for package perl-Text-CSV
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Text-CSV
Name:           perl-Text-CSV
Version:        2.02
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Comma-separated values manipulator (using XS or PurePerl)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.71
Requires:       perl(Test::More) >= 0.71
Recommends:     perl(Text::CSV_XS) >= 1.48
%{perl_requires}

%description
Text::CSV is a thin wrapper for Text::CSV_XS-compatible modules now. All
the backend modules provide facilities for the composition and
decomposition of comma-separated values. Text::CSV uses Text::CSV_XS by
default, and when Text::CSV_XS is not available, falls back on
Text::CSV_PP, which is bundled in the same distribution as this module.

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
%doc Changes README.md

%changelog
