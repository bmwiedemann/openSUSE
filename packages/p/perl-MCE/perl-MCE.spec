#
# spec file for package perl-MCE
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


%define cpan_name MCE
Name:           perl-MCE
Version:        1.882
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Many-Core Engine for Perl providing parallel processing capabilities
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARIOROY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
Recommends:     perl(Sereal::Decoder) >= 3.015
Recommends:     perl(Sereal::Encoder) >= 3.015
%{perl_requires}

%description
MCE spawns a pool of workers and therefore does not fork a new process per
each element of data. Instead, MCE follows a bank queuing model. Imagine
the line being the data and bank-tellers the parallel workers. MCE enhances
that model by adding the ability to chunk the next n elements from the
input stream to the next available worker.

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
%doc Changes Credits README.md
%license Copying LICENSE

%changelog
