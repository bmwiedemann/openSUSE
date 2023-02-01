#
# spec file for package perl-Moo
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Moo
Name:           perl-Moo
Version:        2.005005
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Minimalist Object Orientation (with Moose compatibility)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Method::Modifiers) >= 1.10
BuildRequires:  perl(Role::Tiny) >= 2.002003
BuildRequires:  perl(Sub::Defer) >= 2.006006
BuildRequires:  perl(Sub::Quote) >= 2.006006
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Class::Method::Modifiers) >= 1.10
Requires:       perl(Role::Tiny) >= 2.002003
Requires:       perl(Sub::Defer) >= 2.006006
Requires:       perl(Sub::Quote) >= 2.006006
Recommends:     perl(Class::XSAccessor) >= 1.18
Recommends:     perl(Sub::Util)
%{perl_requires}

%description
'Moo' is an extremely light-weight Object Orientation system. It allows one
to concisely define objects and roles with a convenient syntax that avoids
the details of Perl's object system. 'Moo' contains a subset of Moose and
is optimised for rapid startup.

'Moo' avoids depending on any XS modules to allow for simple deployments.
The name 'Moo' is based on the idea that it provides almost -- but not
quite -- two thirds of Moose. As such, the Moose::Manual can serve as an
effective guide to 'Moo' aside from the MOP and Types sections.

Unlike Mouse this module does not aim at full compatibility with Moose's
surface syntax, preferring instead to provide full interoperability via the
metaclass inflation capabilities described in MOO AND MOOSE.

For a full list of the minor differences between Moose and Moo's surface
syntax, see INCOMPATIBILITIES WITH MOOSE.

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
