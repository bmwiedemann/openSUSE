#
# spec file for package perl-Clone-PP
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Clone-PP
Version:        1.08
Release:        0
%define cpan_name Clone-PP
Summary:        Recursively copy Perl datatypes
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module provides a general-purpose clone function to make deep copies
of Perl data structures. It calls itself recursively to copy nested hash,
array, scalar and reference types, including tied variables and objects.

The clone() function takes a scalar argument to copy. To duplicate arrays
or hashes, pass them in by reference:

  my $copy = clone(\@array);    my @copy = @{ clone(\@array) };
  my $copy = clone(\%hash);     my %copy = %{ clone(\%hash) };

The clone() function also accepts an optional second parameter that can be
used to limit the depth of the copy. If you pass a limit of 0, clone will
return the same value you supplied; for a limit of 1, a shallow copy is
constructed; for a limit of 2, two layers of copying are done, and so on.

  my $shallow_copy = clone( $item, 1 );

To allow objects to intervene in the way they are copied, the clone()
function checks for a couple of optional methods. If an object provides a
method named 'clone_self', it is called and the result returned without
further processing. Alternately, if an object provides a method named
'clone_init', it is called on the copied object before it is returned.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
