#
# spec file for package perl-Net-OBS-Client
#
# Copyright (c) 2021 SUSE LLC
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


Name:           perl-Net-OBS-Client
Version:        0.0.6
Release:        0
%define cpan_name Net-OBS-Client
Summary:        Simple OBS API calls
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/F/FS/FSM/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Config::INI::Reader)
BuildRequires:  perl(Config::Tiny)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(XML::Structured)
Requires:       perl(Config::INI::Reader)
Requires:       perl(Config::Tiny)
Requires:       perl(HTTP::Cookies)
Requires:       perl(HTTP::Request)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Moose)
Requires:       perl(Moose::Role)
Requires:       perl(Path::Class)
Requires:       perl(URI::URL)
Requires:       perl(XML::Structured)
%{perl_requires}

%description
Net::OBS::Client aims to simplify usage of OBS
(https://openbuildservice.org) API calls in perl.

%prep
%setup -q -n %{cpan_name}

rm -f pm_to_blib

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
%doc Changes ignore.txt KankuFile README

%changelog
