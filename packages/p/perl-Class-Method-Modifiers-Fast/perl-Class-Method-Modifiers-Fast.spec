#
# spec file for package perl-Class-Method-Modifiers-Fast
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


Name:           perl-Class-Method-Modifiers-Fast
Version:        0.041
Release:        0
%define cpan_name Class-Method-Modifiers-Fast
Summary:        Provides Moose-Like Method Modifiers
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-Method-Modifiers-Fast/
Source0:        https://cpan.metacpan.org/authors/id/K/KI/KITANO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Util) >= 0.55
Requires:       perl(Data::Util) >= 0.55
BuildRequires:  perl(Sub::Uplevel)
%{perl_requires}

%description
Method modifiers are a powerful feature from the CLOS (Common Lisp Object
System) world.

'Class::Method::Modifiers::Fast' provides three modifiers: 'before',
'around', and 'after'. 'before' and 'after' are run just before and after
the method they modify, but can not really affect that original method.
'around' is run in place of the original method, with a hook to easily call
that original method. See the 'MODIFIERS' section for more details on how
the particular modifiers work.

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install;/use lib q[.];\nuse inc::Module::Install;/' Makefile.PL
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
