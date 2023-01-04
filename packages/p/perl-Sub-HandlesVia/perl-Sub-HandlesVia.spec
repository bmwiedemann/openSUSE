#
# spec file for package perl-Sub-HandlesVia
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


%define cpan_name Sub-HandlesVia
Name:           perl-Sub-HandlesVia
Version:        0.046
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Alternative handles_via implementation
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Exporter::Shiny)
BuildRequires:  perl(List::Util) >= 1.54
BuildRequires:  perl(Role::Hooks) >= 0.008
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Tiny) >= 1.004
Requires:       perl(Class::Method::Modifiers)
Requires:       perl(Exporter::Shiny)
Requires:       perl(List::Util) >= 1.54
Requires:       perl(Role::Hooks) >= 0.008
Requires:       perl(Role::Tiny)
Requires:       perl(Type::Tiny) >= 1.004
Recommends:     perl(Sub::Util)
%{perl_requires}

%description
If you've used Moose's native attribute traits, or MooX::HandlesVia before,
you should have a fairly good idea what this does.

Why re-invent the wheel? Well, this is an implementation that should work
okay with Moo, Moose, Mouse, and any other OO toolkit you throw at it. One
ring to rule them all, so to speak.

For details of how to use it, see the manual.

* Sub::HandlesVia::Manual::WithMoo

How to use Sub::HandlesVia with Moo and Moo::Role.

* Sub::HandlesVia::Manual::WithMoose

How to use Sub::HandlesVia with Moose and Moose::Role.

* Sub::HandlesVia::Manual::WithMouse

How to use Sub::HandlesVia with Mouse and Mouse::Role.

* Sub::HandlesVia::Manual::WithMite

How to use Sub::HandlesVia with Mite.

* Sub::HandlesVia::Manual::WithClassTiny

How to use Sub::HandlesVia with Class::Tiny.

* Sub::HandlesVia::Manual::WithObjectPad

How to use Sub::HandlesVia with Object::Pad classes.

* Sub::HandlesVia::Manual::WithGeneric

How to use Sub::HandlesVia with other OO toolkits, and hand-written Perl
classes.

Note: as Sub::HandlesVia needs to detect which toolkit you are using, and
often needs to detect whether your package is a class or a role, it needs
to be loaded _after_ Moo/Moose/Mouse/etc. Your 'use Moo' or 'use
Moose::Role' or whatever needs to be _before_ your 'use Sub::HandlesVia'.

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
%doc Changes COPYRIGHT CREDITS doap.ttl README
%license LICENSE

%changelog
