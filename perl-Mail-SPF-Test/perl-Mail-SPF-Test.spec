#
# spec file for package perl-Mail-SPF-Test
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Mail-SPF-Test
Version:        1.001
Release:        0
%define cpan_name Mail-SPF-Test
Summary:        SPF test-suite class
License:        BSD-3-Clause
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Mail-SPF-Test/
Source:         http://www.cpan.org/authors/id/J/JM/JMEHNLE/mail-spf-test/%{cpan_name}-v%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
%if 0%{?suse_version} && 0%{?suse_version} <= 1210
BuildRequires:  perl-macros
%endif
BuildRequires:  perl(Module::Build) >= 0.2805
BuildRequires:  perl(Net::DNS) >= 0.58
BuildRequires:  perl(NetAddr::IP) >= 4
BuildRequires:  perl(YAML) >= 0.50
BuildRequires:  perl(version)
Requires:       perl(Net::DNS) >= 0.58
Requires:       perl(NetAddr::IP) >= 4
Requires:       perl(YAML) >= 0.50
Requires:       perl(version)
%{perl_requires}

%description
  *Mail::SPF::Test* is a class for reading and manipulating SPF test-suite
  data.

%prep
%setup -q -n %{cpan_name}-v%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc CHANGES examples LICENSE README TODO

%changelog
