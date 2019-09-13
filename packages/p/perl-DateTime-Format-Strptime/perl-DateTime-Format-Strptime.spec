#
# spec file for package perl-DateTime-Format-Strptime
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


Name:           perl-DateTime-Format-Strptime
Version:        1.76
Release:        0
%define cpan_name DateTime-Format-Strptime
Summary:        Parse and format strp and strf time patterns
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime) >= 1.00
BuildRequires:  perl(DateTime::Locale) >= 1.230000
BuildRequires:  perl(DateTime::Locale::Base)
BuildRequires:  perl(DateTime::Locale::FromData)
BuildRequires:  perl(DateTime::TimeZone) >= 2.09
BuildRequires:  perl(Params::ValidationCompiler)
BuildRequires:  perl(Specio) >= 0.33
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Exporter)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(parent)
Requires:       perl(DateTime) >= 1.00
Requires:       perl(DateTime::Locale) >= 1.230000
Requires:       perl(DateTime::Locale::Base)
Requires:       perl(DateTime::Locale::FromData)
Requires:       perl(DateTime::TimeZone) >= 2.09
Requires:       perl(Params::ValidationCompiler)
Requires:       perl(Specio) >= 0.33
Requires:       perl(Specio::Declare)
Requires:       perl(Specio::Exporter)
Requires:       perl(Specio::Library::Builtins)
Requires:       perl(Specio::Library::String)
Requires:       perl(Try::Tiny)
Requires:       perl(parent)
%{perl_requires}

%description
This module implements most of 'strptime(3)', the POSIX function that is
the reverse of 'strftime(3)', for 'DateTime'. While 'strftime' takes a
'DateTime' and a pattern and returns a string, 'strptime' takes a string
and a pattern and returns the 'DateTime' object associated.

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
%doc bench Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
