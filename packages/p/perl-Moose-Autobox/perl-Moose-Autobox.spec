#
# spec file for package perl-Moose-Autobox
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Moose-Autobox
Version:        0.16
Release:        0
%define cpan_name Moose-Autobox
Summary:        Autoboxed wrappers for Native Perl datatypes
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Moose-Autobox/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::MoreUtils) >= 0.07
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose) >= 0.42
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Syntax::Keyword::Junction::All)
BuildRequires:  perl(Syntax::Keyword::Junction::Any)
BuildRequires:  perl(Syntax::Keyword::Junction::None)
BuildRequires:  perl(Syntax::Keyword::Junction::One)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(autobox) >= 2.23
BuildRequires:  perl(metaclass)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
Requires:       perl(List::MoreUtils) >= 0.07
Requires:       perl(Moose) >= 0.42
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util)
Requires:       perl(Syntax::Keyword::Junction::All)
Requires:       perl(Syntax::Keyword::Junction::Any)
Requires:       perl(Syntax::Keyword::Junction::None)
Requires:       perl(Syntax::Keyword::Junction::One)
Requires:       perl(autobox) >= 2.23
Requires:       perl(metaclass)
Requires:       perl(namespace::autoclean)
Requires:       perl(parent)
%{perl_requires}

%description
Moose::Autobox provides an implementation of SCALAR, ARRAY, HASH & CODE for
use with autobox. It does this using a hierarchy of roles in a manner
similar to what Perl 6 _might_ do. This module, like Class::MOP and Moose,
was inspired by my work on the Perl 6 Object Space, and the 'core types'
implemented there.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING examples LICENSE README

%changelog
