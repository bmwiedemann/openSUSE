#
# spec file for package perl-Sub-Spec
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


Name:           perl-Sub-Spec
Version:        1.0.7
Release:        0
%define cpan_name Sub-Spec
Summary:        Subroutine metadata specification
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Sub-Spec/
Source:         http://www.cpan.org/authors/id/S/SH/SHARYANTO/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Log::Any)
BuildRequires:  perl(Module::Build) >= 0.3601
BuildRequires:  perl(Probe::Perl)
BuildRequires:  perl(Test::More) >= 0.96
#BuildRequires: perl(Sub::Spec::Util)
Requires:       perl(File::Which)
Requires:       perl(Log::Any)
Requires:       perl(Probe::Perl)
Requires:       perl(Test::More) >= 0.96
%{perl_requires}

%description
Subroutine metadata specification

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
%doc Changes LICENSE README

%changelog
