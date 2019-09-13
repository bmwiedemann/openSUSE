#
# spec file for package perl-HTTP-Request-AsCGI
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           perl-HTTP-Request-AsCGI
Version:        1.2
Release:        1
Summary:        Set up a CGI environment from an HTTP::Request
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name HTTP-Request-AsCGI
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTTP-Request-AsCGI/
#Source:        http://www.cpan.org/modules/by-module/HTTP/HTTP-Request-AsCGI-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response) >= 1.53
BuildRequires:  perl(IO::File)
BuildRequires:  perl(URI::Escape)
Requires:       perl(Carp)
Requires:       perl(Class::Accessor)
Requires:       perl(HTTP::Request)
Requires:       perl(HTTP::Response) >= 1.53
Requires:       perl(IO::File)
Requires:       perl(URI::Escape)
%{perl_requires}

%description
Provides a convenient way of setting up an CGI environment from an
HTTP::Request.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes dist.ini examples LICENSE README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
