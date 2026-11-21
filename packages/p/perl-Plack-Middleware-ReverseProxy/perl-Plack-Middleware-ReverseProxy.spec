#
# spec file for package perl-Plack-Middleware-ReverseProxy
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Plack-Middleware-ReverseProxy
Name:           perl-Plack-Middleware-ReverseProxy
Version:        0.170.0
Release:        0
# 0.17 -> normalize -> 0.170.0
%define cpan_version 0.17
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Supports app to run as a reverse proxy backend
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(Plack) >= 0.998.800
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(parent)
Requires:       perl(Plack) >= 0.998.800
Requires:       perl(Plack::Middleware)
Requires:       perl(Plack::Request)
Requires:       perl(parent)
Provides:       perl(Plack::Middleware::ReverseProxy) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Plack::Middleware::ReverseProxy resets some HTTP headers, which changed by
reverse-proxy. You can specify the reverse proxy address and stop fake
requests using 'enable_if' directive in your app.psgi.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
