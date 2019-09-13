#
# spec file for package perl-Scalar-String
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


Name:           perl-Scalar-String
Version:        0.003
Release:        0
%define cpan_name Scalar-String
Summary:        String Aspects of Scalars
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Scalar-String/
Source0:        https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
Requires:       perl(parent)
%{perl_requires}

%description
This module is about the string part of plain Perl scalars. A scalar has a
string value, which is notionally a sequence of Unicode codepoints, but may
be internally encoded in either ISO-8859-1 or UTF-8. In places, and more so
in older versions of Perl, the internal encoding shows through. To fully
understand Perl strings it is necessary to understand these implementation
details.

This module provides functions to classify a string by encoding and to
encode a string in a desired way.

This module is implemented in XS, with a pure Perl backup version for
systems that can't handle XS.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
