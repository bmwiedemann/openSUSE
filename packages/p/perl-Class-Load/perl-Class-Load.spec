#
# spec file for package perl-Class-Load
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


Name:           perl-Class-Load
Version:        0.25
Release:        0
%define cpan_name Class-Load
Summary:        Working (Require "Class::Name") and More
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-Load/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::OptList) >= 0.110
BuildRequires:  perl(Module::Implementation) >= 0.04
BuildRequires:  perl(Module::Runtime) >= 0.012
BuildRequires:  perl(Package::Stash) >= 0.14
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(version)
Requires:       perl(Data::OptList) >= 0.110
Requires:       perl(Module::Implementation) >= 0.04
Requires:       perl(Module::Runtime) >= 0.012
Requires:       perl(Package::Stash) >= 0.14
Requires:       perl(Try::Tiny)
%{perl_requires}

%description
'require EXPR' only accepts 'Class/Name.pm' style module names, not
'Class::Name'. How frustrating! For that, we provide 'load_class
'Class::Name''.

It's often useful to test whether a module can be loaded, instead of
throwing an error when it's not available. For that, we provide
'try_load_class 'Class::Name''.

Finally, sometimes we need to know whether a particular class has been
loaded. Asking '%INC' is an option, but that will miss inner packages and
any class for which the filename does not correspond to the package name.
For that, we provide 'is_class_loaded 'Class::Name''.

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
