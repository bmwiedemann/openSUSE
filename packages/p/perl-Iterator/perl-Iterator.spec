#
# spec file for package perl-Iterator
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           perl-Iterator
%define cpan_name Iterator
Summary:        A general-purpose iterator class
Version:        0.03
Release:        1
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Iterator/
#Source:         http://www.cpan.org/authors/id/R/RO/ROODE/Iterator-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Exception::Class) >= 1.21
Requires:       perl(Exception::Class) >= 1.21
%{perl_requires}

%description
This module is meant to be the definitive implementation of iterators, as
popularized by Mark Jason Dominus's lectures and recent book (_Higher Order
Perl_, Morgan Kauffman, 2005).

An "iterator" is an object, represented as a code block that generates the
"next value" of a sequence, and generally implemented as a closure. When
you need a value to operate on, you pull it from the iterator. If it
depends on other iterators, it pulls values from them when it needs to.
Iterators can be chained together (see the Iterator::Util manpage for
functions that help you do just that), queueing up work to be done but _not
actually doing it_ until a value is needed at the front end of the chain.
At that time, one data value is pulled through the chain.

Contrast this with ordinary array processing, where you load or compute all
of the input values at once, then loop over them in memory. It's analogous
to the difference between looping over a file one line at a time, and
reading the entire file into an array of lines before operating on it.

Iterator.pm provides a class that simplifies creation and use of these
iterator objects. Other 'Iterator::' modules (see the /"SEE ALSO" manpage)
provide many general-purpose and special-purpose iterator functions.

Some iterators are infinite (that is, they generate infinite sequences),
and some are finite. When the end of a finite sequence is reached, the
iterator code block should throw an exception of the type
'Iterator::X::Am_Now_Exhausted'; this is usually done via the the /is_done
manpage function.. This will signal the Iterator class to mark the object
as exhausted. The the /is_exhausted manpage method will then return true,
and the the /isnt_exhausted manpage method will return false. Any further
calls to the the /value manpage method will throw an exception of the type
'Iterator::X::Exhausted'. See the /DIAGNOSTICS manpage.

Note that in many, many cases, you will not need to explicitly create an
iterator; there are plenty of iterator generation and manipulation
functions in the other associated modules. You can just plug them together
like building blocks.

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

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(644,root,root,755)
%doc Changes README

%changelog
