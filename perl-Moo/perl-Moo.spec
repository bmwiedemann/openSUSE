#
# spec file for package perl-Moo
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Moo
Version:        2.003004
Release:        0
%define cpan_name Moo
Summary:        Minimalist Object Orientation (with Moose compatibility)
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Moo/
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Method::Modifiers) >= 1.1
BuildRequires:  perl(Devel::GlobalDestruction) >= 0.11
BuildRequires:  perl(Module::Runtime) >= 0.014
BuildRequires:  perl(Role::Tiny) >= 2.000004
BuildRequires:  perl(Sub::Defer) >= 2.003001
BuildRequires:  perl(Sub::Quote) >= 2.003001
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::More) >= 0.94
Requires:       perl(Class::Method::Modifiers) >= 1.1
Requires:       perl(Devel::GlobalDestruction) >= 0.11
Requires:       perl(Module::Runtime) >= 0.014
Requires:       perl(Role::Tiny) >= 2.000004
Requires:       perl(Sub::Defer) >= 2.003001
Requires:       perl(Sub::Quote) >= 2.003001
Recommends:     perl(Class::XSAccessor) >= 1.18
Recommends:     perl(strictures) >= 2
Recommends:     perl(Sub::Name) >= 0.08
%{perl_requires}

%description
'Moo' is an extremely light-weight Object Orientation system. It allows one
to concisely define objects and roles with a convenient syntax that avoids
the details of Perl's object system. 'Moo' contains a subset of Moose and
is optimised for rapid startup.

'Moo' avoids depending on any XS modules to allow for simple deployments.
The name 'Moo' is based on the idea that it provides almost -- but not
quite -- two thirds of Moose.

Unlike Mouse this module does not aim at full compatibility with Moose's
surface syntax, preferring instead to provide full interoperability via the
metaclass inflation capabilities described in MOO AND MOOSE.

For a full list of the minor differences between Moose and Moo's surface
syntax, see INCOMPATIBILITIES WITH MOOSE.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
