#
# spec file for package perl-Algorithm-CheckDigits
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


Name:           perl-Algorithm-CheckDigits
Version:        1.3.2
Release:        0
%define cpan_name Algorithm-CheckDigits
Summary:        Perl extension to generate and test check digits
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Algorithm-CheckDigits/
Source0:        http://www.cpan.org/authors/id/M/MA/MAMAWE/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.380000
BuildRequires:  perl(Probe::Perl)
BuildRequires:  perl(version)
Requires:       perl(version)
%{perl_requires}

%description
Perl extension to generate and test check digits

%prep
%setup -q -n %{cpan_name}-v%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc cgi-bin Changes README

%changelog
