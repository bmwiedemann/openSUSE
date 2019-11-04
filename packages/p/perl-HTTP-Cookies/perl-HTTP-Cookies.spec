#
# spec file for package perl-HTTP-Cookies
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


Name:           perl-HTTP-Cookies
Version:        6.05
Release:        0
%define cpan_name HTTP-Cookies
Summary:        HTTP cookie jars
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/O/OA/OALDERS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Date) >= 6
BuildRequires:  perl(HTTP::Headers::Util) >= 6
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(URI)
Requires:       perl(HTTP::Date) >= 6
Requires:       perl(HTTP::Headers::Util) >= 6
Requires:       perl(HTTP::Request)
%{perl_requires}

%description
This class is for objects that represent a "cookie jar" -- that is, a
database of all the HTTP cookies that a given LWP::UserAgent object knows
about.

Cookies are a general mechanism which server side connections can use to
both store and retrieve information on the client side of the connection.
For more information about cookies refer to at
http://curl.haxx.se/rfc/cookie_spec.html and at
http://www.cookiecentral.com. This module also implements the new style
cookies described in at https://tools.ietf.org/html/rfc2965. The two
variants of cookies are supposed to be able to coexist happily.

Instances of the class _HTTP::Cookies_ are able to store a collection of
Set-Cookie2: and Set-Cookie: headers and are able to use this information
to initialize Cookie-headers in _HTTP::Request_ objects. The state of a
_HTTP::Cookies_ object can be saved in and restored from files.

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
