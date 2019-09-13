#
# spec file for package perl-Net-OpenID-Consumer
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


Name:           perl-Net-OpenID-Consumer
Version:        1.18
Release:        0
%define cpan_name Net-OpenID-Consumer
Summary:        Library for consumers of OpenID identities
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-OpenID-Consumer/
Source:         http://www.cpan.org/authors/id/W/WR/WROG/%{cpan_name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM utf-charset.patch rt.cpan.org#106930
Patch:          utf-charset.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Net::OpenID::Common) >= 1.19
BuildRequires:  perl(URI)
Requires:       perl(Digest::SHA)
Requires:       perl(HTTP::Request)
Requires:       perl(JSON)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Net::OpenID::Common) >= 1.19
Requires:       perl(URI)
%{perl_requires}

%description
This is the Perl API for (the consumer half of) OpenID, a distributed
identity system based on proving you own a URL, which is then your
identity. More information is available at:

  http://openid.net/

%prep
%setup -q -n %{cpan_name}-%{version}
%patch -p 1

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
%doc Changes examples LICENSE README

%changelog
