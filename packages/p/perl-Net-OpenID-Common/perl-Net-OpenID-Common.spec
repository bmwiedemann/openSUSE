#
# spec file for package perl-Net-OpenID-Common
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


Name:           perl-Net-OpenID-Common
Version:        1.20
Release:        0
%define cpan_name Net-OpenID-Common
Summary:        Libraries shared between Net::OpenID::Consumer and Net::OpenID::Server
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-OpenID-Common/
Source0:        http://www.cpan.org/authors/id/W/WR/WROG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Crypt::DH::GMP) >= 0.00011
BuildRequires:  perl(HTML::Parser) >= 3.40
BuildRequires:  perl(HTTP::Headers::Util)
BuildRequires:  perl(HTTP::Message) >= 5.814
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(XML::Simple)
Requires:       perl(Crypt::DH::GMP) >= 0.00011
Requires:       perl(HTML::Parser) >= 3.40
Requires:       perl(HTTP::Headers::Util)
Requires:       perl(HTTP::Message) >= 5.814
Requires:       perl(HTTP::Request)
Requires:       perl(HTTP::Status)
Requires:       perl(XML::Simple)
%{perl_requires}

%description
The Consumer and Server implementations share a few libraries which live
with this module. This module is here largely to hold the version number
and this documentation, though it also incorporates some utility functions
inherited from previous versions of Net::OpenID::Consumer.

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
%doc Changes LICENSE README

%changelog
