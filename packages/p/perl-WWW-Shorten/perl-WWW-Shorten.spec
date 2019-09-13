#
# spec file for package perl-WWW-Shorten
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


Name:           perl-WWW-Shorten
Version:        3.093
Release:        0
%define cpan_name WWW-Shorten
Summary:        Interface to URL shortening sites
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/WWW-Shorten/
Source0:        http://www.cpan.org/authors/id/C/CA/CAPOEIRAB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Getopt::Long) >= 2.4
BuildRequires:  perl(LWP::UserAgent) >= 5.835
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny) >= 0.24
Requires:       perl(Getopt::Long) >= 2.4
Requires:       perl(LWP::UserAgent) >= 5.835
Requires:       perl(Try::Tiny) >= 0.24
%{perl_requires}

%description
A Perl interface to various services that shorten URLs. These sites
maintain databases of long URLs, each of which has a unique identifier.

# DEPRECATION NOTICE

The following shorten services have been deprecated as the endpoints no
longer exist or function:

  * WWW::Shorten::LinkToolbot

  * WWW::Shorten::Linkz

  * WWW::Shorten::MakeAShorterLink

  * WWW::Shorten::Metamark

  * WWW::Shorten::TinyClick

  * WWW::Shorten::Tinylink

  * WWW::Shorten::Qurl

  * WWW::Shorten::Qwer

When version '3.100' is released, these deprecated services will not be
part of the distribution.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
# MANUAL no testing (needs network)
#%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README.md

%changelog
