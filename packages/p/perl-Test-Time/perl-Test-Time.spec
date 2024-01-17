#
# spec file for package perl-Test-Time
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


%define cpan_name Test-Time
Name:           perl-Test-Time
Version:        0.092
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Overrides the time() and sleep() core functions for testing
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANATOFUZ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
%{perl_requires}

%description
Test::Time can be used to test modules that deal with time. Once you 'use'
this module, all references to 'time', 'localtime' and 'sleep' will be
internalized. You can set custom time by passing time => number after the
'use' statement:

    use Test::Time time => 1;

    my $now = time;    # $now is equal to 1
    sleep 300;         # returns immediately, displaying a note
    my $then = time;   # $then equals to 301

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes minil.toml README README.md
%license LICENSE

%changelog
