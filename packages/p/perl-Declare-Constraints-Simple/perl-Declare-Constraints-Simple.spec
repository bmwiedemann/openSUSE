#
# spec file for package perl-Declare-Constraints-Simple
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


Name:           perl-Declare-Constraints-Simple
Version:        0.03
Release:        0
%define cpan_name Declare-Constraints-Simple
Summary:        Declarative Validation of Data Structures
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Declare-Constraints-Simple/
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHAYLON/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp::Clan)
BuildRequires:  perl(Class::Inspector)
BuildRequires:  perl(aliased)
Requires:       perl(Carp::Clan)
Requires:       perl(Class::Inspector)
Requires:       perl(aliased)
%{perl_requires}

%description
The main purpose of this module is to provide an easy way to build a
profile to validate a data structure. It does this by giving you a set of
declarative keywords in the importing namespace.

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install/use lib q[.];\nuse inc::Module::Install/' Makefile.PL
# MANUAL END

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
