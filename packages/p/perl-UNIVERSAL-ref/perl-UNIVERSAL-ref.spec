#
# spec file for package perl-UNIVERSAL-ref
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-UNIVERSAL-ref
Version:        0.14
Release:        0
%define cpan_name UNIVERSAL-ref
Summary:        Turns ref() into a multimethod
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JJ/JJORE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         UNIVERSAL-ref-0.14-Fix-building-with-Perl-5.25.1.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Utils)
Requires:       perl(B::Utils)
%{perl_requires}

%description
This module changes the behavior of the builtin function ref(). If ref() is
called on an object that has requested an overloaded ref, the object's
'->ref' method will be called and its return value used instead.

%prep
%autosetup -p1 -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
