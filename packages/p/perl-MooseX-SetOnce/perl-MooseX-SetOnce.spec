#
# spec file for package perl-MooseX-SetOnce
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


Name:           perl-MooseX-SetOnce
Version:        0.200002
Release:        0
%define cpan_name MooseX-SetOnce
Summary:        write-once, read-many attributes for Moose
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-SetOnce/
Source:         http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role) >= 0.90
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Moose::Role) >= 0.90
%{perl_requires}

%description
The 'SetOnce' attribute lets your class have attributes that are not lazy
and not set, but that cannot be altered once set.

The logic is very simple: if you try to alter the value of an attribute
with the SetOnce trait, either by accessor or writer, and the attribute has
a value, it will throw an exception.

If the attribute has a clearer, you may clear the attribute and set it
again.

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
