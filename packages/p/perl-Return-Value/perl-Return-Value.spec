#
# spec file for package perl-Return-Value
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


Name:           perl-Return-Value
Version:        1.666005
Release:        0
%define cpan_name Return-Value
Summary:        (deprecated) polymorphic return values
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Return-Value/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.96
%{perl_requires}

%description
Polymorphic return values are a horrible idea, but this library was written
based on the notion that they were useful. Often, we just want to know if
something worked or not. Other times, we'd like to know what the error text
was. Still others, we may want to know what the error code was, and what
the error properties were. We don't want to handle objects or data
structures for every single return value, but we do want to check error
conditions in our code because that's what good programmers do.

When functions are successful they may return true, or perhaps some useful
data. In the quest to provide consistent return values, this gets confusing
between complex, informational errors and successful return values.

This module provides these features with a simplistic API that should get
you what you're looking for in each context a return value is used in.

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
