#
# spec file for package perl-Time-Out
#
# Copyright (c) 2023 SUSE LLC
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
Version:        0.240.0
Release:        0
%define cpan_version 0.24
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Easily timeout long running operations
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SV/SVW/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::cpanminus) >= 1.7046
BuildRequires:  perl(ExtUtils::MakeMaker::CPANfile) >= 0.09
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(Try::Tiny)
Provides:       perl(Time::Out) = %{version}
Provides:       perl(Time::Out::Exception) = %{version}
Provides:       perl(Time::Out::ParamConstraints) = %{version}
%define         __perllib_provides /bin/true
Recommends:     perl(Time::HiRes) >= 1.972.600
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
