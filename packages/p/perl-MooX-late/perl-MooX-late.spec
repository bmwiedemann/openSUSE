#
# spec file for package perl-MooX-late
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-MooX-late
Version:        0.100
Release:        0
%define cpan_name MooX-late
Summary:        Easily translate Moose code to Moo
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moo) >= 2
BuildRequires:  perl(Sub::HandlesVia) >= 0.013
BuildRequires:  perl(Test::Fatal) >= 0.010
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires) >= 0.06
BuildRequires:  perl(Type::Utils) >= 1.000001
Requires:       perl(Moo) >= 2
Requires:       perl(Sub::HandlesVia) >= 0.013
Requires:       perl(Type::Utils) >= 1.000001
%{perl_requires}

%description
Moo is a light-weight object oriented programming framework which aims to
be compatible with Moose. It does this by detecting when Moose has been
loaded, and automatically "inflating" its classes and roles to full Moose
classes and roles. This way, Moo classes can consume Moose roles, Moose
classes can extend Moo classes, and so forth.

However, the surface syntax of Moo differs somewhat from Moose. For example
the 'isa' option when defining attributes in Moose must be either a string
or a blessed Moose::Meta::TypeConstraint object; but in Moo must be a
coderef. These differences in surface syntax make porting code from Moose
to Moo potentially tricky. MooX::late provides some assistance by enabling
a slightly more Moosey surface syntax.

MooX::late does the following:

* 1.

Supports 'isa => $stringytype'.

* 2.

Supports 'does => $rolename' .

* 3.

Supports 'lazy_build => 1'.

* 4.

Exports 'blessed' and 'confess' functions to your namespace.

* 5.

Handles native attribute traits.

Five features. It is not the aim of 'MooX::late' to make every aspect of
Moo behave exactly identically to Moose. It's just going after the
low-hanging fruit. So it does five things right now, and I promise that
future versions will never do more than seven.

Previous releases of MooX::late added support for 'coerce => 1' and
'default => $nonref'. These features have now been added to Moo itself, so
MooX::late no longer has to deal with them.

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
%doc Changes COPYRIGHT CREDITS doap.ttl examples README TODO
%license LICENSE

%changelog
