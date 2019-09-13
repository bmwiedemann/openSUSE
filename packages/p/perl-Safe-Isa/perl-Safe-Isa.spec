#
# spec file for package perl-Safe-Isa
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Safe-Isa
Version:        1.000010
Release:        0
%define cpan_name Safe-Isa
Summary:        Call isa, can, does and DOES safely on things that may not be objects
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Safe-Isa/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
How many times have you found yourself writing:

  if ($obj->isa('Something')) {

and then shortly afterwards cursing and changing it to:

  if (Scalar::Util::blessed($obj) and $obj->isa('Something')) {

Right. That's why this module exists.

Since perl allows us to provide a subroutine reference or a method name to
the -> operator when used as a method call, and a subroutine doesn't
require the invocant to actually be an object, we can create safe versions
of isa, can and friends by using a subroutine reference that only tries to
call the method if it's used on an object. So:

  my $isa_Foo = $maybe_an_object->$_call_if_object(isa => 'Foo');

is equivalent to

  my $isa_Foo = do {
    if (Scalar::Util::blessed($maybe_an_object)) {
      $maybe_an_object->isa('Foo');
    } else {
      undef;
    }
  };

Note that we don't handle trying class names, because many things are valid
class names that you might not want to treat as one (like say "Matt") - the
'is_module_name' function from Module::Runtime is a good way to check for
something you might be able to call methods on if you want to do that.

We are careful to make sure that scalar/list context is preserved for the
method that is eventually called.

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
