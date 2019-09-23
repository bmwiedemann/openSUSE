#
# spec file for package perl-PPI
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


Name:           perl-PPI
Version:        1.270
Release:        0
%define cpan_name PPI
Summary:        Parse, Analyze and Manipulate Perl (without perl)
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MITHALDU/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Inspector) >= 1.22
BuildRequires:  perl(Clone) >= 0.30
BuildRequires:  perl(IO::String) >= 1.07
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Params::Util) >= 1.00
BuildRequires:  perl(Storable) >= 2.17
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Object) >= 0.07
BuildRequires:  perl(Test::SubCalls) >= 1.07
Requires:       perl(Clone) >= 0.30
Requires:       perl(IO::String) >= 1.07
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Params::Util) >= 1.00
Requires:       perl(Storable) >= 2.17
Requires:       perl(Task::Weaken)
%{perl_requires}

%description
Parse, Analyze and Manipulate Perl (without perl)

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
%doc Changes dev_notes.txt README
%license LICENSE

%changelog
