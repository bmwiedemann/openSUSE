#
# spec file for package perl-Set-Tiny
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


Name:           perl-Set-Tiny
Version:        0.04
Release:        0
%define cpan_name Set-Tiny
Summary:        Simple sets of strings
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Set-Tiny/
Source0:        http://www.cpan.org/authors/id/T/TR/TRENDELS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Set::Tiny) = %{verison}

%{perl_requires}

%description
Set::Tiny is a thin wrapper around regular Perl hashes to perform often
needed set operations, such as testing two sets of strings for equality, or
checking whether one is contained within the other.

For a more complete implementation of mathematical set theory, see
Set::Scalar. For sets of arbitrary objects, see Set::Object.

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
%doc Changes examples README

%changelog
