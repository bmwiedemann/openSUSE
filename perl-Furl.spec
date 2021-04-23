#
# spec file for package perl-Furl
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


Name:           perl-Furl
Version:        3.13
Release:        0
%define cpan_name Furl
Summary:        Lightning-fast URL fetcher
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Furl/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# PATCH-FIX-OPENCSUSE 0001-Remove-use-of-Mozilla-CA.patch -- rely on system-wide certificates
Patch0:         0001-Remove-use-of-Mozilla-CA.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor::Lite)
BuildRequires:  perl(HTTP::Parser::XS) >= 0.11
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::TCP) >= 2.11
Requires:       perl(Class::Accessor::Lite)
Requires:       perl(HTTP::Parser::XS) >= 0.11
Recommends:     perl(Compress::Raw::Zlib)
Recommends:     perl(HTTP::CookieJar)
Recommends:     perl(IO::Socket::SSL)
Recommends:     perl(Net::IDN::Encode)
%{perl_requires}

%description
Furl is yet another HTTP client library. LWP is the de facto standard HTTP
client for Perl 5, but it is too slow for some critical jobs, and too
complex for weekend hacking. Furl resolves these issues. Enjoy it!

%prep
%setup -q -n %{cpan_name}-%{version}
%autopatch -p1

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes example README.md TODO
%license LICENSE

%changelog
