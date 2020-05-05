#
# spec file for package perl-IO-Socket-SSL
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


Name:           perl-IO-Socket-SSL
Version:        2.068
Release:        0
%define cpan_name IO-Socket-SSL
Summary:        Nearly transparent SSL encapsulation for IO::Socket::INET
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SU/SULLR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires:  perl(Mozilla::CA)
BuildRequires:  perl(Net::SSLeay) >= 1.46
#Requires:       perl(Mozilla::CA)
Requires:       perl(Net::SSLeay) >= 1.46
%{perl_requires}

%description
IO::Socket::SSL makes using SSL/TLS much easier by wrapping the necessary
functionality into the familiar IO::Socket interface and providing secure
defaults whenever possible. This way, existing applications can be made
SSL-aware without much effort, at least if you do blocking I/O and don't
use select or poll.

But, under the hood, SSL is a complex beast. So there are lots of methods
to make it do what you need if the default behavior is not adequate.
Because it is easy to inadvertently introduce critical security bugs or
just hard to debug problems, I would recommend studying the following
documentation carefully.

The documentation consists of the following parts:

* * "Essential Information About SSL/TLS"

* * "Basic SSL Client"

* * "Basic SSL Server"

* * "Common Usage Errors"

* * "Common Problems with SSL"

* * "Using Non-Blocking Sockets"

* * "Advanced Usage"

* * "Integration Into Own Modules"

* * "Description Of Methods"

Additional documentation can be found in

* * IO::Socket::SSL::Intercept - Doing Man-In-The-Middle with SSL

* * IO::Socket::SSL::Utils - Useful functions for certificates etc

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
rm README.Win32
# MANUAL END

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
%doc BUGS Changes docs example README

%changelog
