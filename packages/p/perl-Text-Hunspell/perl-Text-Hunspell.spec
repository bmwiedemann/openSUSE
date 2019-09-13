#
# spec file for package perl-Text-Hunspell
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Text-Hunspell
Version:        2.11
Release:        0
%define cpan_name Text-Hunspell
Summary:        Perl interface to the Hunspell library
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-Hunspell/
Source0:        http://www.cpan.org/authors/id/C/CO/COSIMO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::PkgConfig)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
# MANUAL END

%description
This module provides a Perl interface to the *Hunspell* library. This
module is to meet the need of looking up many words, one at a time, in a
single session, such as spell-checking a document in memory.

The example code describes the interface on http://hunspell.sf.net

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc Changes examples perlobject.map README

%changelog
