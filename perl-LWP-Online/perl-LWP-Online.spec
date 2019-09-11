#
# spec file for package perl-LWP-Online
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-LWP-Online
Version:        1.08
Release:        0
%define cpan_name LWP-Online
Summary:        Does your process have access to the web
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/LWP-Online/
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(LWP::Simple) >= 5.805
BuildRequires:  perl(URI) >= 1.35
Requires:       perl(LWP::Simple) >= 5.805
Requires:       perl(URI) >= 1.35
%{perl_requires}

%description
This module attempts to answer, as accurately as it can, one of the
nastiest technical questions there is.

*Am I on the internet?*

The answer is useful in a wide range of decisions. For example...

_Should my test scripts run the online portion of the tests or just skip
them?_

_Do I try to fetch fresh data from the server?_

_If my request to the server breaks, is it because I'm offline, or because
the server is offline?_

And so on, and so forth.

But a host of networking and security issues make this problem very
difficult. There are firewalls, proxies (both well behaved and badly
behaved). We might not have DNS. We might not have a network card at all!

You might have network access, but only to a for-money wireless network
that responds to ever HTTP request with a page asking you to enter your
credit card details for paid access. Which means you don't "REALLY" have
access.

The mere nature of the question makes it practically unsolvable.

But with the answer being so useful, and the only other alternative being
to ask the user "duh... are you online?" (when you might not have a user at
all) it's my gut feeling that it is worthwhile at least making an attempt
to solve the problem, if only in a limited way.

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
