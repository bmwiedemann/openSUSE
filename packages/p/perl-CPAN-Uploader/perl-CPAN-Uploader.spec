#
# spec file for package perl-CPAN-Uploader
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


%define cpan_name CPAN-Uploader
Name:           perl-CPAN-Uploader
Version:        0.103.18
Release:        0
# 0.103018 -> normalize -> 0.103.18
%define cpan_version 0.103018
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Upload things to the CPAN
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.84
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(LWP::Protocol::https) >= 1
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Getopt::Long::Descriptive) >= 0.84
Requires:       perl(HTTP::Request::Common)
Requires:       perl(HTTP::Status)
Requires:       perl(LWP::Protocol::https) >= 1
Requires:       perl(LWP::UserAgent)
Requires:       perl(Term::ReadKey)
Provides:       perl(CPAN::Uploader) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
upload things to the CPAN

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
%doc Changes README
%license LICENSE

%changelog
