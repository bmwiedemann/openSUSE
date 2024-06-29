#
# spec file for package perl-CGI
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


%define cpan_name CGI
Name:           perl-CGI
Version:        4.660.0
Release:        0
# 4.66 -> normalize -> 4.660.0
%define cpan_version 4.66
License:        Artistic-2.0
Summary:        Handle Common Gateway Interface requests and responses
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEEJO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Temp) >= 0.17
BuildRequires:  perl(HTML::Entities) >= 3.69
BuildRequires:  perl(Test::More) >= 0.98
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Warn) >= 0.3
BuildRequires:  perl(URI) >= 1.76
BuildRequires:  perl(parent) >= 0.225
Requires:       perl(File::Temp) >= 0.17
Requires:       perl(HTML::Entities) >= 3.69
Requires:       perl(URI) >= 1.76
Requires:       perl(parent) >= 0.225
Provides:       perl(CGI)
Provides:       perl(CGI::Carp) = %{version}
Provides:       perl(CGI::Cookie)
Provides:       perl(CGI::File::Temp) = %{version}
Provides:       perl(CGI::HTML::Functions)
Provides:       perl(CGI::MultipartBuffer)
Provides:       perl(CGI::Pretty) = %{version}
Provides:       perl(CGI::Push)
Provides:       perl(CGI::Util) = %{version}
Provides:       perl(Fh) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
CGI.pm is a stable, complete and mature solution for processing and
preparing HTTP requests and responses. Major features including processing
form submissions, file uploads, reading and writing cookies, query string
generation and manipulation, and processing and preparing HTTP headers.

CGI.pm performs very well in a vanilla CGI.pm environment and also comes
with built-in support for mod_perl and mod_perl2 as well as FastCGI.

It has the benefit of having developed and refined over 20 years with input
from dozens of contributors and being deployed on thousands of websites.
CGI.pm was included in the perl distribution from perl v5.4 to v5.20,
however is has now been removed from the perl core...

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes examples README.md
%license LICENSE

%changelog
