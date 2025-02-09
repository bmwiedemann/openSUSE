#
# spec file for package perl-Class-Singleton
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


%define cpan_name Class-Singleton
Name:           perl-Class-Singleton
Version:        1.600.0
Release:        0
# 1.6 -> normalize -> 1.600.0
%define cpan_version 1.6
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Implementation of a "Singleton" class
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHAY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
Provides:       perl(Class::Singleton) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This is the 'Class::Singleton' module. A Singleton describes an object
class that can have only one instance in any system. An example of a
Singleton might be a print spooler or system registry. This module
implements a Singleton class from which other classes can be derived. By
itself, the 'Class::Singleton' module does very little other than manage
the instantiation of a single object. In deriving a class from
'Class::Singleton', your module will inherit the Singleton instantiation
method and can implement whatever specific functionality is required.

For a description and discussion of the Singleton class, see "Design
Patterns", Gamma et al, Addison-Wesley, 1995, ISBN 0-201-63361-2.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README
%license Artistic Copying LICENCE

%changelog
