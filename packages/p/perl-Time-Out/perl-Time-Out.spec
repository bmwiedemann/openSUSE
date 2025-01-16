#
# spec file for package perl-Time-Out
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


%define cpan_name Time-Out
Name:           perl-Time-Out
Version:        1.0.0
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Easily timeout long running operations
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SV/SVW/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.32
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(ExtUtils::MakeMaker::CPANfile) >= 0.09
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Harness) >= 3.50
BuildRequires:  perl(Test::More) >= 1.001005
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(version) >= 0.9915
Requires:       perl(Carp) >= 1.32
Requires:       perl(Try::Tiny)
Requires:       perl(version) >= 0.9915
Recommends:     perl(Time::HiRes) >= 1.9726
%{perl_requires}

%description
The 'Time::Out' module provides an easy interface to alarm(2) based
timeouts. Nested timeouts are supported. The module exports the 'timeout()'
function by default. The function returns whatever the code placed inside
the subroutine reference returns:

  use Time::Out qw( timeout );

  my $result = timeout 5 => sub {
    return 7;
  };
  # $result == 7

If 'Time::Out' sees that Time::HiRes has been loaded, it will use that
'alarm()' function (if available) instead of the default one, allowing
float timeout values to be used effectively:

  use Time::HiRes qw();
  use Time::Out   qw( timeout );

  timeout 3.1416 => sub {
    # ...
  };

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
%doc Changes README
%license LICENSE

%changelog
