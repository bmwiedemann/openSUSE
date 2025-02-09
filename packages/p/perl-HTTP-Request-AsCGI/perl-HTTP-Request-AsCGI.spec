#
# spec file for package perl-HTTP-Request-AsCGI
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name HTTP-Request-AsCGI
Name:           perl-HTTP-Request-AsCGI
Version:        1.200.0
Release:        0
# 1.2 -> normalize -> 1.200.0
%define cpan_version 1.2
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Set up a CGI environment from an HTTP::Request
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response) >= 1.530
BuildRequires:  perl(URI::Escape)
Requires:       perl(Class::Accessor)
Requires:       perl(HTTP::Request)
Requires:       perl(HTTP::Response) >= 1.530
Requires:       perl(URI::Escape)
Provides:       perl(HTTP::Request::AsCGI) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Provides a convenient way of setting up an CGI environment from an
HTTP::Request.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes examples README
%license LICENSE

%changelog
