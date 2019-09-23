#
# spec file for package perl-Context-Preserve
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


Name:           perl-Context-Preserve
Version:        0.03
Release:        0
%define cpan_name Context-Preserve
Summary:        Run code after a subroutine call, preserving the context the subroutine [cut]
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Context-Preserve/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(ok)
%{perl_requires}

%description
Sometimes you need to call a function, get the results, act on the results,
then return the result of the function. This is painful because of
contexts; the original function can behave different if it's called in
void, scalar, or list context. You can ignore the various cases and just
pick one, but that's fragile. To do things right, you need to see which
case you're being called in, and then call the function in that context.
This results in 3 code paths, which is a pain to type in (and maintain).

This module automates the process. You provide a coderef that is the
"original function", and another coderef to run after the original runs.
You can modify the return value (aliased to @_) here, and do whatever else
you need to do. 'wantarray' is correct inside both coderefs; in "after",
though, the return value is ignored and the value 'wantarray' returns is
related to the context that the original function was called in.

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
%doc Changes CONTRIBUTING LICENCE README

%changelog
