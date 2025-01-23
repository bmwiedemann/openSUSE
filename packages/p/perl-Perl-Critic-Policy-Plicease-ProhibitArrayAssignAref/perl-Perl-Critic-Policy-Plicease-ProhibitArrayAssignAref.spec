#
# spec file for package perl-Perl-Critic-Policy-Plicease-ProhibitArrayAssignAref
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


%define cpan_name Perl-Critic-Policy-Plicease-ProhibitArrayAssignAref
Name:           perl-Perl-Critic-Policy-Plicease-ProhibitArrayAssignAref
Version:        100.0.0
Release:        0
# 100.00 -> normalize -> 100.0.0
%define cpan_version 100.00
License:        GPL-1.0-or-later
Summary:        Don't assign an anonymous arrayref to an array
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Perl::Critic)
BuildRequires:  perl(Perl::Critic::Policy)
BuildRequires:  perl(Perl::Critic::Utils)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Perl::Critic::Policy)
Requires:       perl(Perl::Critic::Utils)
Provides:       perl(Perl::Critic::Policy::Plicease::ProhibitArrayAssignAref) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This policy is a fork of
Perl::Critic::Policy::ValuesAndExpressions::ProhibitArrayAssignAref. It
differs from the original by not having a dependency on List::MoreUtils. It
is unfortunately still licensed as GPL3.

It asks you not to assign an anonymous arrayref to an array

    @array = [ 1, 2, 3 ];       # bad

The idea is that it's rather unclear whether an arrayref is intended, or
might have meant to be a list like

    @array = ( 1, 2, 3 );

This policy is under the "bugs" theme (see Perl::Critic/POLICY THEMES) for
the chance '[]' is a mistake, and since even if it's correct it will likely
make anyone reading it wonder.

A single arrayref can still be assigned to an array, but with parens to
make it clear,

    @array = ( [1,2,3] );       # ok

Dereferences or array and hash slices (see perldata/Slices) are recognised
as an array target and treated similarly,

    @$ref = [1,2,3];            # bad assign to deref
    @{$ref} = [1,2,3];          # bad assign to deref
    @x[1,2,3] = ['a','b','c'];  # bad assign to array slice
    @x{'a','b'} = [1,2];        # bad assign to hash slice

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%license COPYING LICENSE

%changelog
