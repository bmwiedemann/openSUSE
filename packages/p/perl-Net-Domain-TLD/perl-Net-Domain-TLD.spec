#
# spec file for package perl-Net-Domain-TLD
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


%define cpan_name Net-Domain-TLD
Name:           perl-Net-Domain-TLD
Version:        1.750.0
Release:        0
# 1.75 -> normalize -> 1.750.0
%define cpan_version 1.75
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Work with TLD names
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/A/AL/ALEXP/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Net::Domain::TLD) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
  The purpose of this module is to provide user with current list of
  available top level domain names including new ICANN additions and ccTLDs
  Currently TLD definitions have been acquired from the following sources:

  http://www.icann.org/tlds/
  http://www.dnso.org/constituency/gtld/gtld.html
  http://www.iana.org/cctld/cctld-whois.htm
  https://www.iana.org/domains/root/db

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README
%license LICENSE

%changelog
