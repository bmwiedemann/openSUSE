#
# spec file for package perl-Test-File-Contents
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


Name:           perl-Test-File-Contents
Version:        0.23
Release:        0
%define cpan_name Test-File-Contents
Summary:        Test routines for examining the contents of files
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-File-Contents/
Source0:        http://www.cpan.org/authors/id/D/DW/DWHEELER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.300000
BuildRequires:  perl(Test::Builder) >= 0.70
BuildRequires:  perl(Test::More) >= 0.70
BuildRequires:  perl(Text::Diff) >= 0.35
Requires:       perl(Test::Builder) >= 0.70
Requires:       perl(Text::Diff) >= 0.35
Recommends:     perl(Test::Pod) >= 1.41
Recommends:     perl(Test::Pod::Coverage) >= 1.06
%{perl_requires}

%description
Test routines for examining the contents of files

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
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
