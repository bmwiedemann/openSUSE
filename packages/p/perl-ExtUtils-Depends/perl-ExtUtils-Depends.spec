#
# spec file for package perl-ExtUtils-Depends
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


%define cpan_name ExtUtils-Depends
Name:           perl-ExtUtils-Depends
Version:        0.8002
Release:        0
#Upstream: SUSE-Public-Domain
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Easily build XS extensions that depend on XS extensions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.44
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(ExtUtils::MakeMaker) >= 7.44
%{perl_requires}

%description
This module tries to make it easy to build Perl extensions that use
functions and typemaps provided by other perl extensions. This means that a
perl extension is treated like a shared library that provides also a C and
an XS interface besides the perl one.

This works as long as the base (or "producing") extension is loaded with
the 'RTLD_GLOBAL' flag (usually done with a

	sub dl_load_flags {0x01}

in the main _.pm_ file) if you need to use functions defined in the module.
That "producing" extension will also need to tell ExtUtils::MakeMaker the
specific functions to export, with arguments to 'WriteMakefile' like:

  FUNCLIST => [qw(function_name)],
  DL_FUNCS => { 'Extension::Name' => [] },

The basic scheme of operation is to collect information about a module in
the instance, and then store that data in the Perl library where it may be
retrieved later. The object can also reformat this information into the
data structures required by ExtUtils::MakeMaker's WriteMakefile function.

For information on how to make your module fit into this scheme, see
"hashref = ExtUtils::Depends::load (name)".

When creating a new Depends object, you give it a name, which is the name
of the module you are building. You can also specify the names of modules
on which this module depends. These dependencies will be loaded
automatically, and their typemaps, header files, etc merged with your new
object's stuff. When you store the data for your object, the list of
dependencies are stored with it, so that another module depending on your
needn't know on exactly which modules yours depends.

For example:

  Gtk2 depends on Glib

  Gnome2::Canvas depends on Gtk2

  ExtUtils::Depends->new ('Gnome2::Canvas', 'Gtk2');
     this command automatically brings in all the stuff needed
     for Glib, since Gtk2 depends on it.

When the configuration information is saved, it also includes a class
method called 'Inline', inheritable by your module. This allows you in your
module to simply say at the top:

  package Mymod;
  use parent 'Mymod::Install::Files'; # to inherit 'Inline' method

And users of 'Mymod' who want to write inline code (using Inline) will
simply be able to write:

  use Inline with => 'Mymod';

And all the necessary header files, defines, and libraries will be added
for them.

The 'Mymod::Install::Files' will also implement a 'deps' method, which will
return a list of any modules that 'Mymod' depends on - you will not
normally need to use this:

  require Mymod::Install::Files;
  @deps = Mymod::Install::Files->deps;

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

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
