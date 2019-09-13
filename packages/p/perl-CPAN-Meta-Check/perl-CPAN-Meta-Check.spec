#
# spec file for package perl-CPAN-Meta-Check
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


Name:           perl-CPAN-Meta-Check
Version:        0.014
Release:        0
%define cpan_name CPAN-Meta-Check
Summary:        Verify requirements in a CPAN::Meta object
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/CPAN-Meta-Check/
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta) >= 2.120920
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.132830
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121000
BuildRequires:  perl(Module::Metadata) >= 1.000023
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(CPAN::Meta::Prereqs) >= 2.132830
Requires:       perl(CPAN::Meta::Requirements) >= 2.121000
Requires:       perl(Module::Metadata) >= 1.000023
%{perl_requires}

%description
This module verifies if requirements described in a CPAN::Meta object are
present.

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
