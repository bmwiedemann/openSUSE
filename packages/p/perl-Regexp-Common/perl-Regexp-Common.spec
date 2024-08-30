#
# spec file for package perl-Regexp-Common
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


%define cpan_name Regexp-Common
Name:           perl-Regexp-Common
Version:        2024080801.0.0
Release:        0
# 2024080801 -> normalize -> 2024080801.0.0
%define cpan_version 2024080801
#Upstream: SUSE-Public-Domain
License:        Artistic-1.0 OR Artistic-2.0 OR BSD-3-Clause OR MIT
Summary:        Provide commonly requested regular expressions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABIGAIL/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Regexp::Common) = %{version}
Provides:       perl(Regexp::Common::CC) = %{version}
Provides:       perl(Regexp::Common::Entry)
Provides:       perl(Regexp::Common::SEN) = %{version}
Provides:       perl(Regexp::Common::URI) = %{version}
Provides:       perl(Regexp::Common::URI::RFC1035) = %{version}
Provides:       perl(Regexp::Common::URI::RFC1738) = %{version}
Provides:       perl(Regexp::Common::URI::RFC1808) = %{version}
Provides:       perl(Regexp::Common::URI::RFC2384) = %{version}
Provides:       perl(Regexp::Common::URI::RFC2396) = %{version}
Provides:       perl(Regexp::Common::URI::RFC2806) = %{version}
Provides:       perl(Regexp::Common::URI::fax) = %{version}
Provides:       perl(Regexp::Common::URI::file) = %{version}
Provides:       perl(Regexp::Common::URI::ftp) = %{version}
Provides:       perl(Regexp::Common::URI::gopher) = %{version}
Provides:       perl(Regexp::Common::URI::http) = %{version}
Provides:       perl(Regexp::Common::URI::news) = %{version}
Provides:       perl(Regexp::Common::URI::pop) = %{version}
Provides:       perl(Regexp::Common::URI::prospero) = %{version}
Provides:       perl(Regexp::Common::URI::tel) = %{version}
Provides:       perl(Regexp::Common::URI::telnet) = %{version}
Provides:       perl(Regexp::Common::URI::tv) = %{version}
Provides:       perl(Regexp::Common::URI::wais) = %{version}
Provides:       perl(Regexp::Common::_support) = %{version}
Provides:       perl(Regexp::Common::balanced) = %{version}
Provides:       perl(Regexp::Common::comment) = %{version}
Provides:       perl(Regexp::Common::delimited) = %{version}
Provides:       perl(Regexp::Common::lingua) = %{version}
Provides:       perl(Regexp::Common::list) = %{version}
Provides:       perl(Regexp::Common::net) = %{version}
Provides:       perl(Regexp::Common::number) = %{version}
Provides:       perl(Regexp::Common::profanity) = %{version}
Provides:       perl(Regexp::Common::whitespace) = %{version}
Provides:       perl(Regexp::Common::zip) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
By default, this module exports a single hash ('%RE') that stores or
generates commonly needed regular expressions (see "List of available
patterns").

There is an alternative, subroutine-based syntax described in
"Subroutine-based interface".

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
%doc Changes COPYRIGHT COPYRIGHT.AL COPYRIGHT.AL2 COPYRIGHT.BSD COPYRIGHT.MIT README TODO
%license LICENSE

%changelog
