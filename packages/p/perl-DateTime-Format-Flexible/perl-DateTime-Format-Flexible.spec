#
# spec file for package perl-DateTime-Format-Flexible
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name DateTime-Format-Flexible
Name:           perl-DateTime-Format-Flexible
Version:        0.370.0
Release:        0
# 0.37 -> normalize -> 0.370.0
%define cpan_version 0.37
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        DateTime::Format::Flexible - Flexibly parse strings and turn them into D[cut]
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TH/THINC/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::Builder) >= 0.74
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::NoWarnings)
Requires:       perl(DateTime)
Requires:       perl(DateTime::Format::Builder) >= 0.74
Requires:       perl(DateTime::TimeZone)
Provides:       perl(DateTime::Format::Flexible) = %{version}
Provides:       perl(DateTime::Format::Flexible::lang)
Provides:       perl(DateTime::Format::Flexible::lang::de)
Provides:       perl(DateTime::Format::Flexible::lang::en)
Provides:       perl(DateTime::Format::Flexible::lang::es)
%undefine       __perllib_provides
%{perl_requires}

%description
If you have ever had to use a program that made you type in the date a
certain way and thought "Why can't the computer just figure out what date I
wanted?", this module is for you.

_DateTime::Format::Flexible_ attempts to take any string you give it and
parse it into a DateTime object.

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
%doc Changes example README TODO
%license LICENSE

%changelog
