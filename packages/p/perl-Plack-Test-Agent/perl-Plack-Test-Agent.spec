#
# spec file for package perl-Plack-Test-Agent
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


Name:           perl-Plack-Test-Agent
Version:        1.5
Release:        0
%define cpan_name Plack-Test-Agent
Summary:        OO interface for testing low-level Plack/PSGI apps
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Server::Simple::PSGI)
BuildRequires:  perl(Modern::Perl)
BuildRequires:  perl(Plack::Loader)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Util::Accessor)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP)
BuildRequires:  perl(Test::WWW::Mechanize)
BuildRequires:  perl(parent)
Requires:       perl(HTTP::Cookies)
Requires:       perl(HTTP::Message::PSGI)
Requires:       perl(HTTP::Request::Common)
Requires:       perl(HTTP::Response)
Requires:       perl(Plack::Loader)
Requires:       perl(Plack::Util::Accessor)
Requires:       perl(Test::TCP)
Requires:       perl(Test::WWW::Mechanize)
Requires:       perl(parent)
%{perl_requires}

%description
OO interface for testing low-level Plack/PSGI apps

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
%doc Changes CONTRIBUTORS README.md
%license LICENSE

%changelog
