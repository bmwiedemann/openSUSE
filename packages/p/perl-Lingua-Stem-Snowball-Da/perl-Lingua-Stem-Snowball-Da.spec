#
# spec file for package perl-Lingua-Stem-Snowball-Da
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           perl-Lingua-Stem-Snowball-Da
%define cpan_name Lingua-Stem-Snowball-Da
Summary:        Porters stemming algorithm for Denmark
License:        GPL-2.0
Group:          Development/Libraries/Perl
Version:        1.01
Release:        0
Url:            http://search.cpan.org/dist/Lingua-Stem-Snowball-Da/
Source:         http://www.cpan.org/modules/by-module/Lingua/Lingua-Stem-Snowball-Da-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
The stem function takes a scalar as a parameter and stems the word
according to Martin Porters Danish stemming algorithm, which can be found
at the Snowball website: http://snowball.tartarus.org/.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
# do not perl_process_packlist (noarch)
# remove .packlist file
%{__rm} -rf $RPM_BUILD_ROOT%perl_vendorarch
# remove perllocal.pod file
%{__rm} -rf $RPM_BUILD_ROOT%perl_archlib
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,-)
%doc Changes diffs.txt README stop.txt

%changelog
