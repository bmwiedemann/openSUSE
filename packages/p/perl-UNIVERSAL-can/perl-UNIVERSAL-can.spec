#
# spec file for package perl-UNIVERSAL-can
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-UNIVERSAL-can
Version:        1.20140328
Release:        0
%define cpan_name UNIVERSAL-can
Summary:        work around buggy code calling UNIVERSAL::can() as a function
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/UNIVERSAL-can/
Source:         http://www.cpan.org/authors/id/C/CH/CHROMATIC/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The UNIVERSAL class provides a few default methods so that all objects can
use them. Object orientation allows programmers to override these methods
in subclasses to provide more specific and appropriate behavior.

Some authors call methods in the UNIVERSAL class on potential invocants as
functions, bypassing any possible overriding. This is wrong and you should
not do it. Unfortunately, not everyone heeds this warning and their bad
code can break your good code.

This module replaces 'UNIVERSAL::can()' with a method that checks to see if
the first argument is a valid invocant has its own 'can()' method. If so,
it gives a warning and calls the overridden method, working around buggy
code. Otherwise, everything works as you might expect.

Some people argue that you must call 'UNIVERSAL::can()' as a function
because you don't know if your proposed invocant is a valid invocant.
That's silly. Use 'blessed()' from the Scalar::Util manpage if you want to
check that the potential invocant is an object or call the method anyway in
an 'eval' block and check for failure (though check the exception
_returned_, as a poorly-written 'can()' method could break Liskov and throw
an exception other than "You can't call a method on this type of
invocant").

Just don't break working code.

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
