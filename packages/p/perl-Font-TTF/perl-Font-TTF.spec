#
# spec file for package perl-Font-TTF
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


Name:           perl-Font-TTF
Version:        1.06
Release:        0
#Upstream: Artistic-2.0
%define cpan_name Font-TTF
Summary:        Perl module for TrueType Font hacking
License:        Artistic-2.0 and OFL-1.1
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Font-TTF/
Source0:        http://www.cpan.org/authors/id/B/BH/BHALLISSY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::String)
Requires:       perl(IO::String)
%{perl_requires}

%description
This module allows you to do almost anything to a TrueType/OpenType Font
including modify and inspect nearly all tables.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes CONTRIBUTORS LICENSE README.TXT TODO

%changelog
