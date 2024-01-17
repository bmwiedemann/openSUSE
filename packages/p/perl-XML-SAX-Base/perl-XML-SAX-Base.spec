#
# spec file for package perl-XML-SAX-Base
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-XML-SAX-Base
Version:        1.09
Release:        0
%define cpan_name XML-SAX-Base
Summary:        Base class SAX Drivers and Filters
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-SAX-Base/
Source0:        https://cpan.metacpan.org/authors/id/G/GR/GRANTM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
%{perl_requires}

%description
This module has a very simple task - to be a base class for PerlSAX drivers
and filters. It's default behaviour is to pass the input directly to the
output unchanged. It can be useful to use this module as a base class so
you don't have to, for example, implement the characters() callback.

The main advantages that it provides are easy dispatching of events the
right way (ie it takes care for you of checking that the handler has
implemented that method, or has defined an AUTOLOAD), and the guarantee
that filters will pass along events that they aren't implementing to
handlers downstream that might nevertheless be interested in them.

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
%doc Changes README

%changelog
