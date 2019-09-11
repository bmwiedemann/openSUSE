#
# spec file for package perl-Class-Accessor-Grouped
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


Name:           perl-Class-Accessor-Grouped
Version:        0.10012
Release:        0
%define cpan_name Class-Accessor-Grouped
Summary:        Lets you build groups of accessors
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-Accessor-Grouped/
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         perl526.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  perl(Module::Runtime) >= 0.012
BuildRequires:  perl(Test::Exception) >= 0.310000
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Module::Runtime) >= 0.012
Recommends:     perl(Class::XSAccessor) >= 1.19
Recommends:     perl(Sub::Name) >= 0.05
%{perl_requires}

%description
This class lets you build groups of accessors that will call different
getters and setters. The documentation of this module still requires a lot
of work (*volunteers welcome >.>*), but in the meantime you can refer to
http://lo-f.at/glahn/2009/08/WritingPowerfulAccessorsForPerlClasses.html
for more information.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1

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
