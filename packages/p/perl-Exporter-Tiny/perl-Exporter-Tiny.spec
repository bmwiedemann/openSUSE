#
# spec file for package perl-Exporter-Tiny
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Exporter-Tiny
Version:        1.002001
Release:        0
%define cpan_name Exporter-Tiny
Summary:        An Exporter with the Features of Sub::Exporter but Only Core Dependencies
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Exporter-Tiny/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Exporter::Tiny supports many of Sub::Exporter's external-facing features
including renaming imported functions with the '-as', '-prefix' and
'-suffix' options; explicit destinations with the 'into' option; and
alternative installers with the 'installer' option. But it's written in
only about 40% as many lines of code and with zero non-core dependencies.

Its internal-facing interface is closer to Exporter.pm, with configuration
done through the '@EXPORT', '@EXPORT_OK' and '%EXPORT_TAGS' package
variables.

If you are trying to *write* a module that inherits from Exporter::Tiny,
then look at:

  * Exporter::Tiny::Manual::QuickStart

  * Exporter::Tiny::Manual::Exporting

If you are trying to *use* a module that inherits from Exporter::Tiny, then
look at:

  * Exporter::Tiny::Manual::Importing

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
%doc Changes COPYRIGHT CREDITS doap.ttl examples README TODO
%license LICENSE

%changelog
