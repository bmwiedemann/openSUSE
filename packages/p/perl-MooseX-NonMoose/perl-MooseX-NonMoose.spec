#
# spec file for package perl-MooseX-NonMoose
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


Name:           perl-MooseX-NonMoose
Version:        0.26
Release:        0
%define cpan_name MooseX-NonMoose
Summary:        easy subclassing of non-Moose classes
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-NonMoose/
Source:         http://www.cpan.org/authors/id/D/DO/DOY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role) >= 2.0000
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny)
Requires:       perl(List::MoreUtils)
Requires:       perl(Module::Runtime)
Requires:       perl(Moose::Exporter)
Requires:       perl(Moose::Role) >= 2.0000
Requires:       perl(Moose::Util)
Requires:       perl(Try::Tiny)
%{perl_requires}

%description
'MooseX::NonMoose' allows for easily subclassing non-Moose classes with
Moose, taking care of the annoying details connected with doing this, such
as setting up proper inheritance from the Moose::Object manpage and
installing (and inlining, at 'make_immutable' time) a constructor that
makes sure things like 'BUILD' methods are called. It tries to be as
non-intrusive as possible - when this module is used, inheriting from
non-Moose classes and inheriting from Moose classes should work
identically, aside from the few caveats mentioned below. One of the goals
of this module is that including it in a the Moose::Exporter manpage-based
package used across an entire application should be possible, without
interfering with classes that only inherit from Moose modules, or even
classes that don't inherit from anything at all.

There are several ways to use this module. The most straightforward is to
just 'use MooseX::NonMoose;' in your class; this should set up everything
necessary for extending non-Moose modules. the
MooseX::NonMoose::Meta::Role::Class manpage and the
MooseX::NonMoose::Meta::Role::Constructor manpage can also be applied to
your metaclasses manually, either by passing a '-traits' option to your
'use Moose;' line, or by applying them using the Moose::Util::MetaRole
manpage in a the Moose::Exporter manpage-based package. the
MooseX::NonMoose::Meta::Role::Class manpage is the part that provides the
main functionality of this module; if you don't care about inlining, this
is all you need to worry about. Applying the
MooseX::NonMoose::Meta::Role::Constructor manpage as well will provide an
inlined constructor when you immutabilize your class.

'MooseX::NonMoose' allows you to manipulate the argument list that gets
passed to the superclass constructor by defining a 'FOREIGNBUILDARGS'
method. This is called with the same argument list as the 'BUILDARGS'
method, but should return a list of arguments to pass to the superclass
constructor. This allows 'MooseX::NonMoose' to support superclasses whose
constructors would get confused by the extra arguments that Moose requires
(for attributes, etc.)

Not all non-Moose classes use 'new' as the name of their constructor. This
module allows you to extend these classes by explicitly stating which
method is the constructor, during the call to 'extends'. The syntax looks
like this:

  extends 'Foo' => { -constructor_name => 'create' };

similar to how you can already pass '-version' in the 'extends' call in a
similar way.

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
