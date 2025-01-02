#
# spec file for package perl-autobox
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


%define cpan_name autobox
Name:           perl-autobox
Version:        3.0.2
Release:        0
# v3.0.2 -> normalize -> 3.0.2
%define cpan_version v3.0.2
License:        Artistic-2.0
Summary:        Call methods on native types
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHOCOLATE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IPC::System::Simple) >= 1.30
BuildRequires:  perl(Scope::Guard) >= 0.21
BuildRequires:  perl(Test::Fatal) >= 0.017
BuildRequires:  perl(version) >= 0.77
Requires:       perl(Scope::Guard) >= 0.21
Requires:       perl(version) >= 0.77
%{perl_requires}

%description
The autobox pragma allows methods to be called on integers, floats,
strings, arrays, hashes, and code references in exactly the same manner as
blessed references.

Autoboxing is transparent: values are not blessed into their (user-defined)
implementation class (unless the method elects to bestow such a blessing) -
they simply use its methods as though they are.

The classes (packages) into which the native types are boxed are fully
configurable. By default, a method invoked on a non-object value is assumed
to be defined in a class whose name corresponds to the 'ref()' type of that
value - or SCALAR if the value is a non-reference.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%license LICENSE.md

%changelog
