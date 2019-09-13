#
# spec file for package perl-Time-Duration-Parse
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


Name:           perl-Time-Duration-Parse
Version:        0.15
Release:        0
%define cpan_name Time-Duration-Parse
Summary:        Parse string that represents time duration
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter::Lite)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Time::Duration)
Requires:       perl(Exporter::Lite)
%{perl_requires}

%description
Time::Duration::Parse is a module to parse human readable duration strings
like _2 minutes and 3 seconds_ to seconds.

It does the opposite of Time::Duration/duration_exact function in
Time::Duration and is roundtrip safe. So, the following is always true.

  use Time::Duration::Parse;
  use Time::Duration;

  my $seconds = int rand 100000;
  is( parse_duration(duration_exact($seconds)), $seconds );

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
