#
# spec file for package perl-SQL-Abstract-Classic
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-SQL-Abstract-Classic
Version:        1.91
Release:        0
%define cpan_name SQL-Abstract-Classic
Summary:        Generate SQL from Perl data structures
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(MRO::Compat) >= 0.12
BuildRequires:  perl(SQL::Abstract) >= 1.79
BuildRequires:  perl(Test::Deep) >= 0.101
BuildRequires:  perl(Test::Exception) >= 0.310000
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Text::Balanced) >= 2.00
Requires:       perl(MRO::Compat) >= 0.12
Requires:       perl(SQL::Abstract) >= 1.79
Requires:       perl(Text::Balanced) >= 2.00
%{perl_requires}

%description
This module was inspired by the excellent DBIx::Abstract. However, in using
that module I found that what I really wanted to do was generate SQL, but
still retain complete control over my statement handles and use the DBI
interface. So, I set out to create an abstract SQL generation module.

While based on the concepts used by DBIx::Abstract, there are several
important differences, especially when it comes to WHERE clauses. I have
modified the concepts used to make the SQL easier to generate from Perl
data structures and, IMO, more intuitive. The underlying idea is for this
module to do what you mean, based on the data structures you provide it.
The big advantage is that you don't have to modify your code every time
your data changes, as this module figures it out.

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
%doc Changes

%changelog
