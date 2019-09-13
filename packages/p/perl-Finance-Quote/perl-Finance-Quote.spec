#
# spec file for package perl-Finance-Quote
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Finance-Quote
Version:        1.47
Release:        0
#Upstream: GPL-1.0+
%define cpan_name Finance-Quote
Summary:        Get stock and mutual fund quotes from various exchanges
License:        GPL-3.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Finance-Quote/
Source0:        http://www.cpan.org/authors/id/E/EC/ECOCODE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch2:         perl-Finance-Quote-66235-Cdnfundlibrary-row.patch
Patch3:         perl-Finance-Quote-debian-03_whatis.patch
Patch5:         perl-Finance-Quote-debian-06_seb.patch
Patch6:         perl-Finance-Quote-debian-10_whatis.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CGI)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(HTML::Parser)
BuildRequires:  perl(HTML::TableExtract)
BuildRequires:  perl(HTML::TokeParser)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::QueryParam)
Requires:       perl(CGI)
Requires:       perl(DateTime)
Requires:       perl(HTML::Parser)
Requires:       perl(HTML::TableExtract)
Requires:       perl(HTML::TokeParser)
Requires:       perl(HTML::TreeBuilder)
Requires:       perl(HTTP::Cookies)
Requires:       perl(HTTP::Headers)
Requires:       perl(HTTP::Request::Common)
Requires:       perl(HTTP::Status)
Requires:       perl(JSON)
Requires:       perl(LWP::Protocol::https)
Requires:       perl(LWP::Simple)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Time::Piece)
Requires:       perl(URI)
Requires:       perl(URI::Escape)
Requires:       perl(URI::QueryParam)
%{perl_requires}

%description
This module gets stock quotes from various internet sources, including
Yahoo! Finance, Fidelity Investments, and the Australian Stock Exchange.
There are two methods of using this module -- a functional interface that
is deprecated, and an object-orientated method that provides greater
flexibility and stability.

With the exception of straight currency exchange rates, all information is
returned as a two-dimensional hash (or a reference to such a hash, if
called in a scalar context). For example:

    %info = $q->fetch("australia","CML");
    print "The price of CML is ".$info{"CML","price"};

The first part of the hash (eg, "CML") is referred to as the stock. The
second part (in this case, "price") is referred to as the label.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644
%patch2 -p1
%patch3
%patch5
%patch6

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
%doc ChangeLog.1 Changes LICENSE README

%changelog
