#
# spec file for package perl-HTTP-Body
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


%define cpan_name HTTP-Body
Name:           perl-HTTP-Body
Version:        1.230.0
Release:        0
# 1.23 -> normalize -> 1.230.0
%define cpan_version 1.23
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        HTTP Body Parser
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GE/GETTY/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(IO::File) >= 1.14
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.86
Requires:       perl(HTTP::Headers)
Requires:       perl(IO::File) >= 1.14
Provides:       perl(HTTP::Body) = %{version}
Provides:       perl(HTTP::Body::MultiPart) = %{version}
Provides:       perl(HTTP::Body::OctetStream) = %{version}
Provides:       perl(HTTP::Body::UrlEncoded) = %{version}
Provides:       perl(HTTP::Body::XForms) = %{version}
Provides:       perl(HTTP::Body::XFormsMultipart) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
HTTP::Body parses chunks of HTTP POST data and supports
application/octet-stream, application/json,
application/x-www-form-urlencoded, and multipart/form-data.

Chunked bodies are supported by not passing a length value to new().

It is currently used by Catalyst, Dancer, Maypole, Web::Simple and Jedi.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes README
%license LICENSE

%changelog
