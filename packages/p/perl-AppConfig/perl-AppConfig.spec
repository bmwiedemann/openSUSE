#
# spec file for package perl-AppConfig
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


%define cpan_name AppConfig
Name:           perl-AppConfig
Version:        1.710.0
Release:        0
# 1.71 -> normalize -> 1.710.0
%define cpan_version 1.71
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        AppConfig is a bundle of Perl5 modules for reading configuration files a[cut]
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Pod) >= 1.0.0
Provides:       perl(AppConfig) = %{version}
Provides:       perl(AppConfig::Args) = %{version}
Provides:       perl(AppConfig::CGI) = %{version}
Provides:       perl(AppConfig::File) = %{version}
Provides:       perl(AppConfig::Getopt) = %{version}
Provides:       perl(AppConfig::State) = %{version}
Provides:       perl(AppConfig::Sys) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
AppConfig is a Perl5 module for managing application configuration
information. It maintains the state of any number of variables and provides
methods for parsing configuration files, command line arguments and CGI
script parameters.

Variables values may be set via configuration files. Variables may be flags
(On/Off), take a single value, or take multiple values stored as a list or
hash. The number of arguments a variable expects is determined by its
configuration when defined.

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
%doc Changes README TODO
%license LICENSE

%changelog
