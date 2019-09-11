#
# spec file for package perl-URI-Fetch
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


Name:           perl-URI-Fetch
Version:        0.13
Release:        0
%define cpan_name URI-Fetch
Summary:        Smart URI fetching/caching
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/URI-Fetch/
Source0:        http://www.cpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::ErrorHandler)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Test::RequiresInternet) >= 0.05
BuildRequires:  perl(URI)
Requires:       perl(Class::ErrorHandler)
Requires:       perl(LWP::UserAgent)
Requires:       perl(URI)
%{perl_requires}

%description
_URI::Fetch_ is a smart client for fetching HTTP pages, notably syndication
feeds (RSS, Atom, and others), in an intelligent, bandwidth- and
time-saving way. That means:

* * GZIP support

If you have _Compress::Zlib_ installed, _URI::Fetch_ will automatically try
to download a compressed version of the content, saving bandwidth (and
time).

* * _Last-Modified_ and _ETag_ support

If you use a local cache (see the _Cache_ parameter to _fetch_),
_URI::Fetch_ will keep track of the _Last-Modified_ and _ETag_ headers from
the server, allowing you to only download pages that have been modified
since the last time you checked.

* * Proper understanding of HTTP error codes

Certain HTTP error codes are special, particularly when fetching
syndication feeds, and well-written clients should pay special attention to
them. _URI::Fetch_ can only do so much for you in this regard, but it gives
you the tools to be a well-written client.

The response from _fetch_ gives you the raw HTTP response code, along with
special handling of 4 codes:

  * * 200 (OK)

Signals that the content of a page/feed was retrieved successfully.

  * * 301 (Moved Permanently)

Signals that a page/feed has moved permanently, and that your database of
feeds should be updated to reflect the new URI.

  * * 304 (Not Modified)

Signals that a page/feed has not changed since it was last fetched.

  * * 410 (Gone)

Signals that a page/feed is gone and will never be coming back, so you
should stop trying to fetch it.

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
