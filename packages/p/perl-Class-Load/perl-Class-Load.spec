#
# spec file for package perl-Class-Load
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define cpan_name Class-Load
Name:           perl-Class-Load
Version:        0.250.0
Release:        0
# 0.25 -> normalize -> 0.250.0
%define cpan_version 0.25
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Working (require "Class::Name") and more
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::OptList) >= 0.110
BuildRequires:  perl(Module::Implementation) >= 0.40
BuildRequires:  perl(Module::Runtime) >= 0.12
BuildRequires:  perl(Package::Stash) >= 0.140
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(version)
Requires:       perl(Data::OptList) >= 0.110
Requires:       perl(Module::Implementation) >= 0.40
Requires:       perl(Module::Runtime) >= 0.12
Requires:       perl(Package::Stash) >= 0.140
Requires:       perl(Try::Tiny)
Provides:       perl(Class::Load) = %{version}
Provides:       perl(Class::Load::PP) = %{version}
%undefine       __perllib_provides
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
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
