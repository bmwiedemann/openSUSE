#
# spec file for package perl-Class-Multimethods
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


Name:           perl-Class-Multimethods
Version:        1.701
Release:        0
#Upstream:  This module is free software. It may be used, redistributed and/or modified under the terms of the Perl Artistic License (see http://www.perl.com/perl/misc/Artistic.html)
%define cpan_name Class-Multimethods
Summary:        Support multimethods and function overloading in Perl
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-Multimethods/
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The Class:Multimethod module exports a subroutine (&multimethod) that can
be used to declare other subroutines that are dispatched using a algorithm
different from the normal Perl subroutine or method dispatch mechanism.

%prep
%setup -q -n %{cpan_name}-1.700
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes README tutorial.html

%changelog
