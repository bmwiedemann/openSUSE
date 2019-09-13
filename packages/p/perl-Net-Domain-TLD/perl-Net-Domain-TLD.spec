#
# spec file for package perl-Net-Domain-TLD
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Net-Domain-TLD
Version:        1.75
Release:        0
%define cpan_name Net-Domain-TLD
Summary:        Work with TLD names
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-Domain-TLD/
Source0:        http://www.cpan.org/authors/id/A/AL/ALEXP/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes LICENSE README

%changelog
