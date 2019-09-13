#
# spec file for package perl-Class-C3-Componentised
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


Name:           perl-Class-C3-Componentised
Version:        1.001002
Release:        0
%define cpan_name Class-C3-Componentised
Summary:        Load mix-ins or components to your C3-based class
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-C3-Componentised/
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::C3) >= 0.20
BuildRequires:  perl(Class::Inspector) >= 1.32
BuildRequires:  perl(MRO::Compat) >= 0.09
BuildRequires:  perl(Test::Exception) >= 0.310000
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Class::C3) >= 0.20
Requires:       perl(Class::Inspector) >= 1.32
Requires:       perl(MRO::Compat) >= 0.09
%{perl_requires}

%description
This will inject base classes to your module using the Class::C3 method
resolution order.

Please note: these are not plugins that can take precedence over methods
declared in MyModule. If you want something like that, consider
MooseX::Object::Pluggable.

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
