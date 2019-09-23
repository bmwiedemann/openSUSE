#
# spec file for package perl-Sub-Exporter-GlobExporter
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


Name:           perl-Sub-Exporter-GlobExporter
Version:        0.005
Release:        0
%define cpan_name Sub-Exporter-GlobExporter
Summary:        Export Shared Globs with Sub::Exporter Collectors
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Sub-Exporter-GlobExporter/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Sub::Exporter)
%{perl_requires}

%description
Sub::Exporter::GlobExporter provides only one routine, 'glob_exporter',
which may be called either by its full name or may be imported on request.

  my $exporter = glob_exporter( $default_name, $globref_locator );

The routine returns a collection validator|Sub::Exporter/Collector
Configuration that will export a glob into the importing package. It will
export it under the name '$default_name', unless an alternate name is given
(as shown above). The glob that is installed is specified by the
'$globref_locator', which can be either the globref itself, or a reference
to a string which will be called on the exporter

For an example, see the /SYNOPSIS, in which a method is defined to produce
the globref to share. This allows the glob-exporting package to be
subclassed, so the subclass may choose to either re-use the same glob when
exporting or to export a new one.

If there are entries in the arguments to the globref-exporting collector
_other_ than those beginning with a dash, a hashref of them will be passed
to the globref locator. In other words, if we were to write this:

  use Shared::Symbol '$Symbol' => { arg => 1, -as => 2 };

It would result in a call like the following:

  my $globref = Shared::Symbol->_shared_globref({ arg => 1 });

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
