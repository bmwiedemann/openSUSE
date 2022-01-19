#
# spec file for package perl-MRO-Compat
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name MRO-Compat
Name:           perl-MRO-Compat
Version:        0.15
Release:        0
Summary:        Mro::* interface compatibility for Perls < 5.9.5
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The "mro" namespace provides several utilities for dealing with method
resolution order and method caching in general in Perl 5.9.5 and higher.

This module provides those interfaces for earlier versions of Perl (back to
5.6.0 anyways).

It is a harmless no-op to use this module on 5.9.5+. That is to say, code
which properly uses MRO::Compat will work unmodified on both older Perls
and 5.9.5+.

If you're writing a piece of software that would like to use the parts of
5.9.5+'s mro:: interfaces that are supported here, and you want
compatibility with older Perls, this is the module for you.

Some parts of this code will work better and/or faster with Class::C3::XS
installed (which is an optional prereq of Class::C3, which is in turn a
prereq of this package), but it's not a requirement.

This module never exports any functions. All calls must be fully qualified
with the 'mro::' prefix.

The interface documentation here serves only as a quick reference of what
the function basically does, and what differences between MRO::Compat and
5.9.5+ one should look out for. The main docs in 5.9.5's mro are the real
interface docs, and contain a lot of other useful information.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README
%license LICENSE

%changelog
