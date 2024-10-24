#
# spec file for package perl-Try-Tiny
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Try-Tiny
Name:           perl-Try-Tiny
Version:        0.320.0
Release:        0
# 0.32 -> normalize -> 0.320.0
%define cpan_version 0.32
License:        MIT
Summary:        Minimal try/catch with proper preservation of $@
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Try::Tiny) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides bare bones 'try'/'catch'/'finally' statements that are
designed to minimize common mistakes with eval blocks, and NOTHING else.

This is unlike TryCatch which provides a nice syntax and avoids adding
another call stack layer, and supports calling 'return' from the 'try'
block to return from the parent subroutine. These extra features come at a
cost of a few dependencies, namely Devel::Declare and Scope::Upper which
are occasionally problematic, and the additional catch filtering uses Moose
type constraints which may not be desirable either.

The main focus of this module is to provide simple and reliable error
handling for those having a hard time installing TryCatch, but who still
want to write correct 'eval' blocks without 5 lines of boilerplate each
time.

It's designed to work as correctly as possible in light of the various
pathological edge cases (see BACKGROUND) and to be compatible with any
style of error values (simple strings, references, objects, overloaded
objects, etc).

If the 'try' block dies, it returns the value of the last statement
executed in the 'catch' block, if there is one. Otherwise, it returns
'undef' in scalar context or the empty list in list context. The following
examples all assign '"bar"' to '$x':

  my $x = try { die "foo" } catch { "bar" };
  my $x = try { die "foo" } || "bar";
  my $x = (try { die "foo" }) // "bar";

  my $x = eval { die "foo" } || "bar";

You can add 'finally' blocks, yielding the following:

  my $x;
  try { die 'foo' } finally { $x = 'bar' };
  try { die 'foo' } catch { warn "Got a die: $_" } finally { $x = 'bar' };

'finally' blocks are always executed making them suitable for cleanup code
which cannot be handled using local. You can add as many 'finally' blocks
to a given 'try' block as you like.

Note that adding a 'finally' block without a preceding 'catch' block
suppresses any errors. This behaviour is consistent with using a standalone
'eval', but it is not consistent with 'try'/'finally' patterns found in
other programming languages, such as Java, Python, Javascript or C#. If you
learned the 'try'/'finally' pattern from one of these languages, watch out
for this.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes CONTRIBUTING README
%license LICENCE

%changelog
