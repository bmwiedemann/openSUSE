#
# spec file for package perl-Sub-Exporter-ForMethods
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Sub-Exporter-ForMethods
Version:        0.100052
Release:        0
%define cpan_name Sub-Exporter-ForMethods
Summary:        Helper Routines for Using Sub::Exporter to Build Methods
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Sub-Exporter-ForMethods/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Sub::Exporter) >= 0.978
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(Sub::Exporter) >= 0.978
Requires:       perl(Sub::Name)
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
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
