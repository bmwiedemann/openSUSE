#
# spec file for package perl-checkbot (Version 1.80)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-checkbot
%define cpan_name checkbot
Summary:        WWW Link Verifier
Version:        1.80
Release:        2
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/checkbot/
#Source:         http://www.cpan.org/modules/by-module/checkbot/checkbot-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.bz2
Patch0:         %{cpan_name}-1.80-webserver.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl(LWP) >= 5.803
BuildRequires:  perl(URI) >= 1.10
BuildRequires:  perl(HTML::Parser) >= 3.33
BuildRequires:  perl(MIME::Base64) >= 2.00
BuildRequires:  perl(Net::FTP) >= 2.58
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Mail::Send)
BuildRequires:  perl(Time::Duration)
BuildRequires:  perl-macros
Requires:       perl(LWP) >= 5.803
Requires:       perl(URI) >= 1.10
Requires:       perl(HTML::Parser) >= 3.33
Requires:       perl(MIME::Base64) >= 2.00
Requires:       perl(Net::FTP) >= 2.58
Requires:       perl(Digest::MD5)
Requires:       perl(Mail::Send)
Requires:       perl(Time::Duration)

%description
Checkbot is a perl5 script which can verify links within a region of
the World Wide Web. It checks all pages within an identified region,
and all links within that region. After checking all links within the
region, it will also check all links which point outside of the
region, and then stop.

Checkbot regularly writes reports on its findings, including all
servers found in the region, and all links with problems on those
servers.

Checkbot was written originally to check a number of servers at
once. This has implied some design decisions, so you might want to
keep that in mind when making suggestions. Speaking of which, be sure
to check the to do file on the website for things which have been
suggested for Checkbot.

Authors:
--------
    Hans de Graaff <hans@degraaff.org>, 1994-2005.
    Based on Dimitri Tischenko, Delft University of Technology, 1994

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
# do not perl_process_packlist (noarch)
# remove .packlist file
%{__rm} -rf $RPM_BUILD_ROOT%perl_vendorarch
# remove perllocal.pod file
%{__rm} -rf $RPM_BUILD_ROOT%perl_archlib
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root,-)
%doc ChangeLog checkbot.css README TODO

%changelog
