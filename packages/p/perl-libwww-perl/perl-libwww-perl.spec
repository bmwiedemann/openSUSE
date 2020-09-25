#
# spec file for package perl-libwww-perl
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-libwww-perl
Version:        6.49
Release:        0
%define cpan_name libwww-perl
Summary:        The World-Wide Web library for Perl
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(File::Listing) >= 6
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::HeadParser)
BuildRequires:  perl(HTTP::Cookies) >= 6
BuildRequires:  perl(HTTP::Daemon) >= 6
BuildRequires:  perl(HTTP::Date) >= 6
BuildRequires:  perl(HTTP::Negotiate) >= 6
BuildRequires:  perl(HTTP::Request) >= 6
BuildRequires:  perl(HTTP::Request::Common) >= 6
BuildRequires:  perl(HTTP::Response) >= 6
BuildRequires:  perl(HTTP::Status) >= 6.07
BuildRequires:  perl(LWP::MediaTypes) >= 6
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Net::HTTP) >= 6.18
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI) >= 1.10
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(WWW::RobotRules) >= 6
Requires:       perl(Encode::Locale)
Requires:       perl(File::Listing) >= 6
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::HeadParser)
Requires:       perl(HTTP::Cookies) >= 6
Requires:       perl(HTTP::Daemon) >= 6
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(HTTP::Negotiate) >= 6
Requires:       perl(HTTP::Request) >= 6
Requires:       perl(HTTP::Request::Common) >= 6
Requires:       perl(HTTP::Response) >= 6
Requires:       perl(HTTP::Status) >= 6.07
Requires:       perl(LWP::MediaTypes) >= 6
Requires:       perl(Net::HTTP) >= 6.18
Requires:       perl(Try::Tiny)
Requires:       perl(URI) >= 1.10
Requires:       perl(URI::Escape)
Requires:       perl(WWW::RobotRules) >= 6
%{perl_requires}
# MANUAL BEGIN
Recommends:     perl(LWP::Protocol::https) >= 6.06
# MANUAL END

%description
The World-Wide Web library for Perl

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
%doc Changes CONTRIBUTING.md examples README.SSL talk-to-ourself
%license LICENSE

%changelog
