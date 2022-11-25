#
# spec file for package perl-Exporter-Tiny
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


%define cpan_name Exporter-Tiny
Name:           perl-Exporter-Tiny
Version:        1.006000
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        An exporter with the features of Sub::Exporter but only core dependencies
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
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
%doc Changes COPYRIGHT CREDITS doap.ttl examples NEWS README TODO
%license LICENSE

%changelog
