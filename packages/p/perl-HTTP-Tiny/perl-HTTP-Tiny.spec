#
# spec file for package perl-HTTP-Tiny
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name HTTP-Tiny
Name:           perl-HTTP-Tiny
Version:        0.090
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Small, simple, correct HTTP/1.1 client
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Test::More) >= 0.96
Recommends:     perl(HTTP::CookieJar) >= 0.001
Recommends:     perl(IO::Socket::IP) >= 0.32
Recommends:     perl(IO::Socket::SSL) >= 1.968
Recommends:     perl(Net::SSLeay) >= 1.49
%{perl_requires}

%description
This is a very simple HTTP/1.1 client, designed for doing simple requests
without the overhead of a large framework like LWP::UserAgent.

It is more correct and more complete than HTTP::Lite. It supports proxies
and redirection. It also correctly resumes after EINTR.

If IO::Socket::IP 0.25 or later is installed, HTTP::Tiny will use it
instead of IO::Socket::INET for transparent support for both IPv4 and IPv6.

Cookie support requires HTTP::CookieJar or an equivalent class.

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes CONTRIBUTING.mkdn README
%license LICENSE

%changelog
