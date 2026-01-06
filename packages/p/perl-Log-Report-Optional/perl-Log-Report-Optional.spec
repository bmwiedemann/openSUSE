#
# spec file for package perl-Log-Report-Optional
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name Log-Report-Optional
Name:           perl-Log-Report-Optional
Version:        1.80.0
Release:        0
# 1.08 -> normalize -> 1.80.0
%define cpan_version 1.08
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Log::Report in its lightest form
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(String::Print) >= 0.910
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(Test::Pod) >= 1
Requires:       perl(String::Print) >= 0.910
Requires:       perl(Test::More) >= 0.86
Provides:       perl(Log::Report::Minimal) = %{version}
Provides:       perl(Log::Report::Minimal::Domain) = %{version}
Provides:       perl(Log::Report::Optional) = %{version}
Provides:       perl(Log::Report::Util) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module will allow libraries (helper modules) to have a dependency to a
small module instead of the full Log-Report distribution. The full power of
'Log::Report' is only released when the main program uses that module. In
that case, the module using the 'Optional' will also use the full
Log::Report, otherwise the dressed-down Log::Report::Minimal version.

For the full documentation:

* * see Log::Report when it is used by main

* * see Log::Report::Minimal otherwise

The latter provides the same functions from the former, but is the
simpelest possible way.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc ChangeLog README.md

%changelog
