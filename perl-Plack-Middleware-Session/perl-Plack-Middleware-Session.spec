#
# spec file for package perl-Plack-Middleware-Session
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


Name:           perl-Plack-Middleware-Session
Version:        0.33
Release:        0
%define cpan_name Plack-Middleware-Session
Summary:        Middleware for session management
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Cookie::Baker) >= 0.10
BuildRequires:  perl(Digest::HMAC_SHA1) >= 1.03
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Plack) >= 0.9910
BuildRequires:  perl(Test::Fatal) >= 0.006
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
Requires:       perl(Cookie::Baker) >= 0.10
Requires:       perl(Digest::HMAC_SHA1) >= 1.03
Requires:       perl(Digest::SHA)
Requires:       perl(Plack) >= 0.9910
%{perl_requires}

%description
This is a Plack Middleware component for session management. By default it
will use cookies to keep session state and store data in memory. This
distribution also comes with other state and store solutions. See perldoc
for these backends how to use them.

It should be noted that we store the current session as a hash reference in
the 'psgix.session' key inside the '$env' where you can access it as
needed.

*NOTE:* As of version 0.04 the session is stored in 'psgix.session' instead
of 'plack.session'.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
# put . back into @INC for tests
export PERL5LIB=$PWD
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples README
%license LICENSE

%changelog
