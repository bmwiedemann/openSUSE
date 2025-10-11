#
# spec file for package perl-Class-Accessor
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define cpan_name Class-Accessor
Name:           perl-Class-Accessor
Version:        0.510.0
Release:        0
# 0.51 -> normalize -> 0.510.0
%define cpan_version 0.51
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Automated accessor generation
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KASEI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Class::Accessor) = %{version}
Provides:       perl(Class::Accessor::Fast) = %{version}
Provides:       perl(Class::Accessor::Faster) = %{version}
%undefine       __perllib_provides
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
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README

%changelog
