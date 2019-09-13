#
# spec file for package perl-Class-XSAccessor
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Class-XSAccessor
Version:        1.19
Release:        0
%define cpan_name Class-XSAccessor
Summary:        Generate fast XS accessors without runtime compilation
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-XSAccessor/
Source:         http://www.cpan.org/authors/id/S/SM/SMUELLER/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(Class::XSAccessor)
#BuildRequires: perl(Class::XSAccessor::Array)
#BuildRequires: perl(Class::XSAccessor::Heavy)
#BuildRequires: perl(Modern::Perl)
%{perl_requires}

%description
Class::XSAccessor implements fast read, write and read/write accessors in
XS. Additionally, it can provide predicates such as 'has_foo()' for testing
whether the attribute 'foo' exists in the object (which is different from
"is defined within the object"). It only works with objects that are
implemented as ordinary hashes. the Class::XSAccessor::Array manpage
implements the same interface for objects that use arrays for their
internal representation.

Since version 0.10, the module can also generate simple constructors
(implemented in XS). Simply supply the 'constructor => 'constructor_name''
option or the 'constructors => ['new', 'create', 'spawn']' option. These
constructors do the equivalent of the following Perl code:

  sub new {
    my $class = shift;
    return bless { @_ }, ref($class)||$class;
  }

That means they can be called on objects and classes but will not clone
objects entirely. Parameters to 'new()' are added to the object.

The XS accessor methods are between 3 and 4 times faster than typical
pure-Perl accessors in some simple benchmarking. The lower factor applies
to the potentially slightly obscure 'sub set_foo_pp {$_[0]->{foo} =
$_[1]}', so if you usually write clear code, a factor of 3.5 speed-up is a
good estimate. If in doubt, do your own benchmarking!

The method names may be fully qualified. The example in the synopsis could
have been written as 'MyClass::get_foo' instead of 'get_foo'. This way,
methods can be installed in classes other than the current class. See also:
the 'class' option below.

By default, the setters return the new value that was set, and the
accessors (mutators) do the same. This behaviour can be changed with the
'chained' option - see below. The predicates return a boolean.

Since version 1.01, 'Class::XSAccessor' can generate extremely simple
methods which just return true or false (and always do so). If that seems
like a really superfluous thing to you, then consider a large class
hierarchy with interfaces such as the PPI manpage. These methods are
provided by the 'true' and 'false' options - see the synopsis.

'defined_predicates' check whether a given object attribute is defined.
'predicates' is an alias for 'defined_predicates' for compatibility with
older versions of 'Class::XSAccessor'. 'exists_predicates' checks whether
the given attribute exists in the object using 'exists'.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
