#
# spec file for package perl-libwww-perl
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


%define cpan_name libwww-perl
Name:           perl-libwww-perl
Version:        6.810.0
Release:        0
# 6.81 -> normalize -> 6.810.0
%define cpan_version 6.81
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        The World-Wide Web library for Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(File::Listing) >= 6
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::HeadParser) >= 3.710
BuildRequires:  perl(HTTP::CookieJar::LWP)
BuildRequires:  perl(HTTP::Cookies) >= 6
BuildRequires:  perl(HTTP::Daemon) >= 6.120
BuildRequires:  perl(HTTP::Date) >= 6
BuildRequires:  perl(HTTP::Message) >= 7.10
BuildRequires:  perl(HTTP::Negotiate) >= 6
BuildRequires:  perl(HTTP::Request) >= 7.10
BuildRequires:  perl(HTTP::Request::Common) >= 6.180
BuildRequires:  perl(HTTP::Response) >= 7.10
BuildRequires:  perl(HTTP::Status) >= 6.180
BuildRequires:  perl(LWP::MediaTypes) >= 6
BuildRequires:  perl(Module::Load)
BuildRequires:  perl(Net::HTTP) >= 6.180
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::RequiresInternet)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(URI) >= 1.100
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(WWW::RobotRules) >= 6
BuildRequires:  perl(parent) >= 0.217
Requires:       perl(Encode::Locale)
Requires:       perl(File::Listing) >= 6
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::HeadParser) >= 3.710
Requires:       perl(HTTP::Cookies) >= 6
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(HTTP::Message) >= 7.10
Requires:       perl(HTTP::Negotiate) >= 6
Requires:       perl(HTTP::Request) >= 7.10
Requires:       perl(HTTP::Request::Common) >= 6.180
Requires:       perl(HTTP::Response) >= 7.10
Requires:       perl(HTTP::Status) >= 6.180
Requires:       perl(LWP::MediaTypes) >= 6
Requires:       perl(Module::Load)
Requires:       perl(Net::HTTP) >= 6.180
Requires:       perl(Try::Tiny)
Requires:       perl(URI) >= 1.100
Requires:       perl(URI::Escape)
Requires:       perl(WWW::RobotRules) >= 6
Requires:       perl(parent) >= 0.217
Provides:       perl(LWP) = %{version}
Provides:       perl(LWP::Authen::Basic) = %{version}
Provides:       perl(LWP::Authen::Digest) = %{version}
Provides:       perl(LWP::Authen::Ntlm) = %{version}
Provides:       perl(LWP::ConnCache) = %{version}
Provides:       perl(LWP::Debug) = %{version}
Provides:       perl(LWP::Debug::TraceHTTP) = %{version}
Provides:       perl(LWP::DebugFile) = %{version}
Provides:       perl(LWP::MemberMixin) = %{version}
Provides:       perl(LWP::Protocol) = %{version}
Provides:       perl(LWP::Protocol::cpan) = %{version}
Provides:       perl(LWP::Protocol::data) = %{version}
Provides:       perl(LWP::Protocol::file) = %{version}
Provides:       perl(LWP::Protocol::ftp) = %{version}
Provides:       perl(LWP::Protocol::gopher) = %{version}
Provides:       perl(LWP::Protocol::http) = %{version}
Provides:       perl(LWP::Protocol::loopback) = %{version}
Provides:       perl(LWP::Protocol::mailto) = %{version}
Provides:       perl(LWP::Protocol::nntp) = %{version}
Provides:       perl(LWP::Protocol::nogo) = %{version}
Provides:       perl(LWP::RobotUA) = %{version}
Provides:       perl(LWP::Simple) = %{version}
Provides:       perl(LWP::UserAgent) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
Recommends:     perl(LWP::Protocol::https) >= 6.06
# MANUAL END

%description
The World-Wide Web library for Perl

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
%doc Changes CONTRIBUTING.md examples README.SSL SECURITY.md talk-to-ourself
%license LICENSE

%changelog
