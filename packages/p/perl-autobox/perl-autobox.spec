#
# spec file for package perl-autobox
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-autobox
Version:        3.0.1
Release:        0
%define cpan_name autobox
Summary:        Call Methods On Native Types
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/autobox/
Source0:        https://cpan.metacpan.org/authors/id/C/CH/CHOCOLATE/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IPC::System::Simple) >= 1.25
BuildRequires:  perl(Scope::Guard) >= 0.21
BuildRequires:  perl(Test::Fatal) >= 0.014
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
%setup -q -n %{cpan_name}-v%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
%license LICENSE.md

%changelog
