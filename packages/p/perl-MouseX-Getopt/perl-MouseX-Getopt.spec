#
# spec file for package perl-MouseX-Getopt
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


%define cpan_name MouseX-Getopt
Name:           perl-MouseX-Getopt
Version:        0.38
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Mouse role for processing command line options
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GF/GFUJI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# PATCH-FIX-UPSTREAM https://github.com/gfx/mousex-getopt/pull/15
Patch0:         pr-15.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Getopt::Long) >= 2.37
BuildRequires:  perl(Getopt::Long::Descriptive) >= 0.091
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(Mouse) >= 0.64
BuildRequires:  perl(Mouse::Meta::Attribute)
BuildRequires:  perl(Mouse::Meta::Class)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Mouse::Util::TypeConstraints)
BuildRequires:  perl(MouseX::ConfigFromFile)
BuildRequires:  perl(MouseX::SimpleConfig)
BuildRequires:  perl(Test::Exception) >= 0.21
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Mouse)
BuildRequires:  perl(Test::Warn) >= 0.21
Requires:       perl(Getopt::Long) >= 2.37
Requires:       perl(Getopt::Long::Descriptive) >= 0.091
Requires:       perl(Mouse) >= 0.64
Requires:       perl(Mouse::Meta::Attribute)
Requires:       perl(Mouse::Role)
Requires:       perl(Mouse::Util::TypeConstraints)
%{perl_requires}

%description
This is a role which provides an alternate constructor for creating objects
using parameters passed in from the command line.

This module attempts to DWIM as much as possible with the command line
params by introspecting your class's attributes. It will use the name of
your attribute as the command line option, and if there is a type
constraint defined, it will configure Getopt::Long to handle the option
accordingly.

You can use the trait MouseX::Getopt::Meta::Attribute::Trait or the
attribute metaclass MouseX::Getopt::Meta::Attribute to get non-default
commandline option names and aliases.

You can use the trait MouseX::Getopt::Meta::Attribute::Trait::NoGetopt or
the attribute metaclass MouseX::Getopt::Meta::Attribute::NoGetopt to have
'MouseX::Getopt' ignore your attribute in the commandline options.

By default, attributes which start with an underscore are not given
commandline argument support, unless the attribute's metaclass is set to
MouseX::Getopt::Meta::Attribute. If you don't want your accessors to have
the leading underscore in their name, you can do this:

  # for read/write attributes
  has '_foo' => (accessor => 'foo', ...);

  # or for read-only attributes
  has '_bar' => (reader => 'bar', ...);

This will mean that Getopt will not handle a --foo param, but your code can
still call the 'foo' method.

If your class also uses a configfile-loading role based on
MouseX::ConfigFromFile, such as MouseX::SimpleConfig, MouseX::Getopt's
'new_with_options' will load the configfile specified by the '--configfile'
option (or the default you've given for the configfile attribute) for you.

Options specified in multiple places follow the following precedence order:
commandline overrides configfile, which overrides explicit new_with_options
parameters.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README.md
%license LICENSE

%changelog
