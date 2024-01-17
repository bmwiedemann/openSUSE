#
# spec file for package perl-TAP-Harness-JUnit
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


Name:           perl-TAP-Harness-JUnit
Version:        0.42
Release:        0
%define cpan_name TAP-Harness-JUnit
Summary:        Generate JUnit compatible output from TAP results
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/TAP-Harness-JUnit/
Source:         http://www.cpan.org/authors/id/J/JL/JLAVALLEE/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(TAP::Harness) >= 3.05
BuildRequires:  perl(TAP::Parser)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(XML::Simple)
Requires:       perl(TAP::Harness) >= 3.05
Requires:       perl(TAP::Parser)
Requires:       perl(XML::Simple)
%{perl_requires}

%description
The only difference between this module and _TAP::Harness_ is that this
module adds the optional arguments 'xmlfile', 'package', and 'namemangle'
that cause the output to be formatted into XML in a format similar to the
one that is produced by the JUnit testing framework.

%prep
%setup -q -n %{cpan_name}-%{version}
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
%doc ChangeLog README.md

%changelog
