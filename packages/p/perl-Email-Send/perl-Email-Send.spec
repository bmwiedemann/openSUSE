#
# spec file for package perl-Email-Send
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Email-Send
Version:        2.201
Release:        0
%define cpan_name Email-Send
Summary:        Simply Sending Email
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Email-Send/
Source:         http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Email::Abstract)
BuildRequires:  perl(Email::Address) >= 1.80
BuildRequires:  perl(Email::Simple) >= 1.92
BuildRequires:  perl(MIME::Entity)
BuildRequires:  perl(Mail::Internet)
BuildRequires:  perl(Module::Pluggable) >= 2.97
BuildRequires:  perl(Return::Value)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Email::Abstract)
Requires:       perl(Email::Address) >= 1.80
Requires:       perl(Email::Simple) >= 1.92
Requires:       perl(Module::Pluggable) >= 2.97
Requires:       perl(Return::Value)
%{perl_requires}

%description
This module provides a very simple, very clean, very specific interface to
multiple Email mailers. The goal of this software is to be small and
simple, easy to use, and easy to extend.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc Changes LICENSE README util

%changelog
