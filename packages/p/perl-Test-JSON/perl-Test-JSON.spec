#
# spec file for package perl-Test-JSON
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


Name:           perl-Test-JSON
Version:        0.11
Release:        0
%define cpan_name Test-JSON
Summary:        Test JSON data
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-JSON/
Source:         http://www.cpan.org/authors/id/O/OV/OVID/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(JSON::Any) >= 1.2
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Differences) >= 0.47
BuildRequires:  perl(Test::Tester) >= 0.107
Requires:       perl(JSON::Any) >= 1.2
Requires:       perl(Test::Differences) >= 0.47
Requires:       perl(Test::Tester) >= 0.107
%{perl_requires}

%description
JavaScript Object Notation (JSON) is a lightweight data interchange format.
the Test::JSON manpage makes it easy to verify that you have built valid
JSON and that it matches your expected output.

See the http://www.json.org/ manpage for more information.

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
