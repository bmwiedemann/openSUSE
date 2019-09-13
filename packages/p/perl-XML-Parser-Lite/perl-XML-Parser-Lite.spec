#
# spec file for package perl-XML-Parser-Lite
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


Name:           perl-XML-Parser-Lite
Version:        0.722
Release:        0
%define cpan_name XML-Parser-Lite
Summary:        Lightweight pure-perl XML Parser (based on regexps)
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-Parser-Lite/
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires) >= 0.06
%{perl_requires}

%description
This module implements an XML parser with a interface similar to
XML::Parser. Though not all callbacks are supported, you should be able to
use it in the same way you use XML::Parser. Due to using experimental
regexp features it'll work only on Perl 5.6 and above and may behave
differently on different platforms.

Note that you cannot use regular expressions or split in callbacks. This is
due to a limitation of perl's regular expression implementation (which is
not re-entrant).

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
