#
# spec file for package perl-Module-Find
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


Name:           perl-Module-Find
Version:        0.13
Release:        0
%define cpan_name Module-Find
Summary:        Find and use installed modules in a (sub)category
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Module-Find/
Source0:        http://www.cpan.org/authors/id/C/CR/CRENZ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
Recommends:     perl(Test::Pod) >= 1.14
Recommends:     perl(Test::Pod::Coverage) >= 1.04
%{perl_requires}

%description
Module::Find lets you find and use modules in categories. This can be very
useful for auto-detecting driver or plugin modules. You can differentiate
between looking in the category itself or in all subcategories.

If you want Module::Find to search in a certain directory on your harddisk
(such as the plugins directory of your software installation), make sure
you modify '@INC' before you call the Module::Find functions.

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
%doc Changes examples MANIFEST.skip README

%changelog
