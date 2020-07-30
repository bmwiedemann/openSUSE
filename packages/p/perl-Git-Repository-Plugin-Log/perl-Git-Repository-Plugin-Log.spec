#
# spec file for package perl-Git-Repository-Plugin-Log
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


Name:           perl-Git-Repository-Plugin-Log
Version:        1.314
Release:        0
%define cpan_name Git-Repository-Plugin-Log
Summary:        Add a log() method to Git::Repository
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Git-Repository-Plugin-Log/
Source0:        http://www.cpan.org/authors/id/B/BO/BOOK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Git::Repository) >= 1.309
BuildRequires:  perl(Git::Repository::Command)
BuildRequires:  perl(Git::Repository::Plugin)
BuildRequires:  perl(Pod::Coverage::TrustPod) >= 0.100003
BuildRequires:  perl(Test::CPAN::Meta) >= 0.25
BuildRequires:  perl(Test::Git)
BuildRequires:  perl(Test::Pod) >= 1.51
BuildRequires:  perl(Test::Pod::Coverage) >= 1.10
BuildRequires:  perl(Test::Requires::Git) >= 1.005
Requires:       perl(Git::Repository) >= 1.309
Requires:       perl(Git::Repository::Command)
Requires:       perl(Git::Repository::Plugin)
%{perl_requires}

%description
This module adds a new method to Git::Repository.

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
%doc Changes LICENSE README

%changelog
