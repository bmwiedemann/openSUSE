#
# spec file for package perl-Struct-Dumb
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Struct-Dumb
Version:        0.09
Release:        0
%define cpan_name Struct-Dumb
Summary:        Make Simple Lightweight Record-Like Structures
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Struct-Dumb/
Source0:        http://www.cpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.400400
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
%{perl_requires}

%description
'Struct::Dumb' creates record-like structure types, similar to the 'struct'
keyword in C, C++ or C#, or 'Record' in Pascal. An invocation of this
module will create a construction function which returns new object
references with the given field values. These references all respond to
lvalue methods that access or modify the values stored.

It's specifically and intentionally not meant to be an object class. You
cannot subclass it. You cannot provide additional methods. You cannot apply
roles or mixins or metaclasses or traits or antlers or whatever else is in
fashion this week.

On the other hand, it is tiny, creates cheap lightweight array-backed
structures, uses nothing outside of core. It's intended simply to be a
slightly nicer way to store data structures, where otherwise you might be
tempted to abuse a hash, complete with the risk of typoing key names. The
constructor will 'croak' if passed the wrong number of arguments, as will
attempts to refer to fields that don't exist. Accessor-mutators will
'croak' if invoked with arguments. (This helps detect likely bugs such as
accidentally passing in the new value as an argument, or attempting to
invoke a stored 'CODE' reference by passing argument values directly to the
accessor.)

 $ perl -E 'use Struct::Dumb; struct Point => [qw( x y )]; Point(30)'
 usage: main::Point($x, $y) at -e line 1

 $ perl -E 'use Struct::Dumb; struct Point => [qw( x y )]; Point(10,20)->z'
 main::Point does not have a 'z' field at -e line 1

 $ perl -E 'use Struct::Dumb; struct Point => [qw( x y )]; Point(1,2)->x(3)'
 main::Point->x invoked with arguments at -e line 1.

Objects in this class are (currently) backed by an ARRAY reference store,
though this is an internal implementation detail and should not be relied
on by using code. Attempting to dereference the object as an ARRAY will
throw an exception.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
