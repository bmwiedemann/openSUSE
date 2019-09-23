#
# spec file for package perl-DateTime-Locale
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


Name:           perl-DateTime-Locale
Version:        1.240000
Release:        0
%define cpan_version 1.24
Provides:       perl(DateTime::Locale) = 1.240000
%define cpan_name DateTime-Locale
Summary:        Localization support for DateTime.pm
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Check) >= 0.011
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Dist::CheckConflicts) >= 0.02
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::ShareDir::Install) >= 0.03
BuildRequires:  perl(IPC::System::Simple)
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Params::ValidationCompiler) >= 0.13
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::File::ShareDir::Dist)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(namespace::autoclean) >= 0.19
Requires:       perl(Dist::CheckConflicts) >= 0.02
Requires:       perl(File::ShareDir)
Requires:       perl(List::Util) >= 1.45
Requires:       perl(Params::ValidationCompiler) >= 0.13
Requires:       perl(Specio::Declare)
Requires:       perl(Specio::Library::String)
Requires:       perl(namespace::autoclean) >= 0.19
%{perl_requires}

%description
DateTime::Locale is primarily a factory for the various locale subclasses.
It also provides some functions for getting information on all the
available locales.

If you want to know what methods are available for locale objects, then
please read the 'DateTime::Locale::FromData' documentation.

%prep
%setup -q -n %{cpan_name}-%{cpan_version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc appveyor.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE LICENSE.cldr

%changelog
