#
# spec file for package perl-common-sense
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


%define cpan_name common-sense
Name:           perl-common-sense
Version:        3.750.0
Release:        0
# 3.75 -> normalize -> 3.750.0
%define cpan_version 3.75
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Save a tree AND a kitten, use common::sense!
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
# MANUAL
#BuildArch:     noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
Provides:       perl(common::sense) = %{version}
# MANUAL END

%description
   “Nothing is more fairly distributed than common sense: no one thinks
   he needs more of it than he already has.”

   – René Descartes

This module implements some sane defaults for Perl programs, as defined by
two typical (or not so typical - use your common sense) specimens of Perl
coders. In fact, after working out details on which warnings and strict
modes to enable and make fatal, we found that we (and our code written so
far, and others) fully agree on every option, even though we never used
warnings before, so it seems this module indeed reflects a "common" sense
among some long-time Perl coders.

The basic philosophy behind the choices made in common::sense can be
summarised as: "enforcing strict policies to catch as many bugs as
possible, while at the same time, not limiting the expressive power
available to the programmer".

Two typical examples of how this philosophy is applied in practise is the
handling of uninitialised and malloc warnings:

* _uninitialised_

'undef' is a well-defined feature of perl, and enabling warnings for using
it rarely catches any bugs, but considerably limits you in what you can do,
so uninitialised warnings are disabled.

* _malloc_

Freeing something twice on the C level is a serious bug, usually causing
memory corruption. It often leads to side effects much later in the program
and there are no advantages to not reporting this, so malloc warnings are
fatal by default.

Unfortunately, there is no fine-grained warning control in perl, so often
whole groups of useful warnings had to be excluded because of a single
useless warning (for example, perl puts an arbitrary limit on the length of
text you can match with some regexes before emitting a warning, making the
whole 'regexp' category useless).

What follows is a more thorough discussion of what this module does, and
why it does it, and what the advantages (and disadvantages) of this
approach are.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
