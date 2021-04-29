#
# spec file for package perl-Devel-Hide
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Devel-Hide
Name:           perl-Devel-Hide
Version:        0.0014
Release:        0
Summary:        Forces the unavailability of specified Perl modules (for testing)
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.82
%{perl_requires}

%description
Given a list of Perl modules/filenames, this module makes 'require' and
'use' statements fail (no matter the specified files/modules are installed
or not).

They _die_ with a message like:

    Can't locate Module/ToHide.pm in @INC (hidden)

The original intent of this module is to allow Perl developers to test for
alternative behavior when some modules are not available. In a Perl
installation, where many modules are already installed, there is a chance
to screw things up because you take for granted things that may not be
there in other machines.

For example, to test if your distribution does the right thing when a
module is missing, you can do

    perl -MDevel::Hide=Test::Pod Makefile.PL

forcing 'Test::Pod' to not be found (whether it is installed or not).

Another use case is to force a module which can choose between two
requisites to use the one which is not the default. For example,
'XML::Simple' needs a parser module and may use 'XML::Parser' or 'XML::SAX'
(preferring the latter). If you have both of them installed, it will always
try 'XML::SAX'. But you can say:

    perl -MDevel::Hide=XML::SAX script_which_uses_xml_simple.pl

NOTE. This module does not use Carp. As said before, denial _dies_.

This module is pretty trivial. It uses a code reference in @INC to get rid
of specific modules during require - denying they can be successfully
loaded and stopping the search before they have a chance to be found.

There are three alternative ways to include modules in the hidden list:

* import()

this is probably the most commonly used method, called automagically when
you do this:

    use Devel::Hide qw(Foo Bar::Baz);

or

    perl -MDevel::Hide=...

* setting @Devel::Hide::HIDDEN

* environment variable DEVEL_HIDE_PM

both of these two only support 'global' hiding, whereas 'import()' supports
lexical hiding as well.

Optionally, you can provide some arguments *before* the list of modules:

* -from:children

propagate the list of hidden modules to your process' child processes. This
works by populating 'PERL5OPT', and is incompatible with Taint mode, as
explained in perlrun. Of course, this is unnecessary if your child
processes are just forks of the current one.

* -lexically

This is only available on perl 5.10.0 and later. It is a fatal error to try
to use it on an older perl.

Everything following this will only have effect until the end of the
current scope. Yes, that includes '-quiet'.

* -quiet

suppresses diagnostic output. You will still get told about errors. This is
passed to child processes if -from:children is in effect.

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

%changelog
