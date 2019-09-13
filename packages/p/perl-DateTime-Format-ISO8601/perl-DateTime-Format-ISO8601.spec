#
# spec file for package perl-DateTime-Format-ISO8601
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


Name:           perl-DateTime-Format-ISO8601
Version:        0.08
Release:        0
%define cpan_name DateTime-Format-ISO8601
Summary:        Parses ISO8601 formats
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/DateTime-Format-ISO8601/
Source0:        http://www.cpan.org/authors/id/J/JH/JHOBLITT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime) >= 0.18
BuildRequires:  perl(DateTime::Format::Builder) >= 0.77
BuildRequires:  perl(Module::Build) >= 0.380000
Requires:       perl(DateTime) >= 0.18
Requires:       perl(DateTime::Format::Builder) >= 0.77
Recommends:     perl(File::Find::Rule) >= 0.24
Recommends:     perl(Test::Distribution) >= 1.22
Recommends:     perl(Test::Pod) >= 0.95
%{perl_requires}

%description
Parses almost all ISO8601 date and time formats. ISO8601 time-intervals
will be supported in a later release.

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
%doc Changes LICENSE README Todo

%changelog
