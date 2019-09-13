#
# spec file for package perl-Term-ReadPassword
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

# norootforbuild


Name:           perl-Term-ReadPassword
Version:        0.11
Release:        52
AutoReqProv:    on
Group:          Development/Libraries/Perl
License:        Artistic-1.0
Url:            http://cpan.org/modules/by-module/Term/
Summary:        Term::ReadPassword - Asking the user for a password
Source:         Term-ReadPassword-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
This module lets you ask the user for a password in the traditional
way, from the keyboard, without echoing.

This is not intended for use over the web; user authentication over the
web is another matter entirely. Also, this module should generally be
used in conjunction with Perl's crypt() function, sold separately.



Authors:
--------
    Tom Phoenix <rootbeer@redcat.com>

%prep
%setup -n Term-ReadPassword-%{version} -q

%build
perl Makefile.PL
make %{?_smp_mflags}

%check
mv t/2_interactive.t t/2_interactive.tt #disable interactive testing
make test

%install
%perl_make_install
%perl_process_packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc 
%doc %{_mandir}/man?/*
%dir %{perl_vendorlib}/Term
%{perl_vendorlib}/Term/*
%dir %{perl_vendorarch}/auto/Term
%{perl_vendorarch}/auto/Term/ReadPassword

%changelog
