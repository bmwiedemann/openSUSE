#
# spec file for package perl-Module-Depends
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


Name:           perl-Module-Depends
Version:        0.16
Release:        0
%define cpan_name Module-Depends
Summary:        Identify the Dependencies of a Distribution
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Module-Depends/
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCLAMP/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         left-brace.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor::Chained)
BuildRequires:  perl(Module::Build) >= 0.360000
BuildRequires:  perl(Parse::CPAN::Meta)
Requires:       perl(Class::Accessor::Chained)
Requires:       perl(Parse::CPAN::Meta)
%{perl_requires}

%description
Module::Depends extracts module dependencies from an unpacked distribution
tree.

Module::Depends only evaluates the META.yml shipped with a distribution.
This won't be effective until all distributions ship META.yml files, so we
suggest you take your life in your hands and look at
Module::Depends::Intrusive.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
%patch0 -p1

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
