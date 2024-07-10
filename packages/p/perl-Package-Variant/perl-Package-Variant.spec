#
# spec file for package perl-Package-Variant
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


Name:           perl-Package-Variant
Version:        1.003002
Release:        0
%define cpan_name Package-Variant
Summary:        Parameterizable packages
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Package-Variant/
Source0:        http://www.cpan.org/authors/id/M/MS/MSTROUT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Import::Into) >= 1.000000
BuildRequires:  perl(Module::Runtime) >= 0.013
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(strictures) >= 2.000000
Requires:       perl(Import::Into) >= 1.000000
Requires:       perl(Module::Runtime) >= 0.013
Requires:       perl(strictures) >= 2.000000
%{perl_requires}

%description
This module allows you to build a variable package that contains a package
template and can use it to build variant packages at runtime.

Your variable package will export a subroutine which will build a variant
package, combining its arguments with the template, and return the name of
the new variant package.

The implementation does not care about what kind of packages it builds, be
they simple function exporters, classes, singletons or something entirely
different.

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
%doc Changes README

%changelog
