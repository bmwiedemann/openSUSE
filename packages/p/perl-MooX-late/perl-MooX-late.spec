#
# spec file for package perl-MooX-late
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-MooX-late
Version:        0.015
Release:        0
%define cpan_name MooX-late
Summary:        easily translate Moose code to Moo
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooX-late/
Source:         http://www.cpan.org/authors/id/T/TO/TOBYINK/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moo) >= 1.006000
BuildRequires:  perl(Test::Fatal) >= 0.010
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires) >= 0.06
BuildRequires:  perl(Type::Utils) >= 1.000001
Requires:       perl(Moo) >= 1.006000
Requires:       perl(Type::Utils) >= 1.000001
Recommends:     perl(MooX::HandlesVia) >= 0.001004
%{perl_requires}

%description
the Moo manpage is a light-weight object oriented programming framework
which aims to be compatible with the Moose manpage. It does this by
detecting when Moose has been loaded, and automatically "inflating" its
classes and roles to full Moose classes and roles. This way, Moo classes
can consume Moose roles, Moose classes can extend Moo classes, and so
forth.

However, the surface syntax of Moo differs somewhat from Moose. For example
the 'isa' option when defining attributes in Moose must be either a string
or a blessed the Moose::Meta::TypeConstraint manpage object; but in Moo
must be a coderef. These differences in surface syntax make porting code
from Moose to Moo potentially tricky. the MooX::late manpage provides some
assistance by enabling a slightly more Moosey surface syntax.

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

  Handles certain attribute traits. Currently 'Hash', 'Array' and 'Code'
  are supported. This feature requires the MooX::HandlesVia manpage.

  'String', 'Number', 'Counter' and 'Bool' are unlikely to ever be
  supported because of internal implementation details of Moo. If you need
  another attribute trait to be supported, let me know and I will consider
  it.

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
%doc Changes CONTRIBUTING COPYRIGHT CREDITS doap.ttl examples LICENSE README TODO

%changelog
