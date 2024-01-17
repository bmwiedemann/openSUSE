#
# spec file for package perl-Sub-Exporter-ForMethods
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


%define cpan_name Sub-Exporter-ForMethods
Name:           perl-Sub-Exporter-ForMethods
Version:        0.100055
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Helper routines for using Sub::Exporter to build methods
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Sub::Exporter) >= 0.978
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(Sub::Exporter) >= 0.978
Requires:       perl(Sub::Util)
%{perl_requires}

%description
The synopsis section, above, looks almost indistinguishable from any other
use of Sub::Exporter, apart from the use of 'method_installer'. It is
nearly indistinguishable in behavior, too. The only change is that
subroutines exported from Method::Builder into named slots in
Vehicle::Autobot will be wrapped in a subroutine called
'Vehicle::Autobot::transform'. This will insert a named frame into stack
traces to aid in debugging.

More importantly (for the author, anyway), they will not be removed by
namespace::autoclean. This makes the following code work:

  package MyLibrary;

  use Math::Trig qw(tan);         # uses Exporter.pm
  use String::Truncate qw(trunc); # uses Sub::Exporter's defaults

  use Sub::Exporter::ForMethods qw(method_installer);
  use Mixin::Linewise { installer => method_installer }, qw(read_file);

  use namespace::autoclean;

  ...

  1;

After MyLibrary is compiled, 'namespace::autoclean' will remove 'tan' and
'trunc' as foreign contaminants, but will leave 'read_file' in place. It
will also remove 'method_installer', an added win.

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
