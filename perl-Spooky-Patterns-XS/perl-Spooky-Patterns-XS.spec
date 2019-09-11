#
# spec file for package perl-Spooky-Patterns-XS
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Spooky-Patterns-XS
Version:        1.52
Release:        0
%define cpan_name Spooky-Patterns-XS
Summary:        Spooky::Patterns::XS Perl module
License:        GPL-2.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Spooky-Patterns-XS/
Source0:        Spooky-Patterns-XS-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Algorithm::Diff)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Test::Deep)
ExclusiveArch:  x86_64 ppc64le
%{perl_requires}

%description
Spooky::Patterns::XS Perl module

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes patterns_impl.cc SpookyV2.cpp
%license COPYING

%changelog
