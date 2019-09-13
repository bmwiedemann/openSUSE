#
# spec file for package perl-Class-Accessor
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


Name:           perl-Class-Accessor
Version:        0.51
Release:        0
%define cpan_name Class-Accessor
Summary:        Automated accessor generation
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-Accessor/
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KASEI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module automagically generates accessors/mutators for your class.

Most of the time, writing accessors is an exercise in cutting and pasting.
You usually wind up with a series of methods like this:

    sub name {
        my $self = shift;
        if(@_) {
            $self->{name} = $_[0];
        }
        return $self->{name};
    }

    sub salary {
        my $self = shift;
        if(@_) {
            $self->{salary} = $_[0];
        }
        return $self->{salary};
    }

  # etc...

One for each piece of data in your object. While some will be unique, doing
value checks and special storage tricks, most will simply be exercises in
repetition. Not only is it Bad Style to have a bunch of repetitious code,
but it's also simply not lazy, which is the real tragedy.

If you make your module a subclass of Class::Accessor and declare your
accessor fields with mk_accessors() then you'll find yourself with a set of
automatically generated accessors which can even be customized!

The basic set up is very simple:

    package Foo;
    use base qw(Class::Accessor);
    Foo->mk_accessors( qw(far bar car) );

Done. Foo now has simple far(), bar() and car() accessors defined.

Alternatively, if you want to follow Damian's _best practice_ guidelines
you can use:

    package Foo;
    use base qw(Class::Accessor);
    Foo->follow_best_practice;
    Foo->mk_accessors( qw(far bar car) );

*Note:* you must call 'follow_best_practice' before calling 'mk_accessors'.

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
%doc Changes examples README

%changelog
