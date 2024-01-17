#
# spec file for package perl-HTTP-Body
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-HTTP-Body
Version:        1.22
Release:        0
%define cpan_name HTTP-Body
Summary:        HTTP Body Parser
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTTP-Body/
Source:         http://www.cpan.org/authors/id/G/GE/GETTY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::File) >= 1.14
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.86
Requires:       perl(HTTP::Headers)
Requires:       perl(IO::File) >= 1.14
%{perl_requires}

%description
HTTP::Body parses chunks of HTTP POST data and supports
application/octet-stream, application/json,
application/x-www-form-urlencoded, and multipart/form-data.

Chunked bodies are supported by not passing a length value to new().

It is currently used by the Catalyst manpage to parse POST bodies.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes LICENSE README scripts

%changelog
