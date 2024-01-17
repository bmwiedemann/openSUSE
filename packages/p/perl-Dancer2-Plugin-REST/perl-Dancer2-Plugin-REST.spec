#
# spec file for package perl-Dancer2-Plugin-REST
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           perl-Dancer2-Plugin-REST
Version:        1.02
Release:        0
%define cpan_name Dancer2-Plugin-REST
Summary:        Plugin for writing RESTful apps with Dancer2
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/Y/YA/YANICK/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Dancer2) >= 0.203000
BuildRequires:  perl(Dancer2::Core::HTTP) >= 0.203000
BuildRequires:  perl(Dancer2::Core::Request)
BuildRequires:  perl(Dancer2::Plugin)
BuildRequires:  perl(Dancer2::Serializer::Mutable)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::Requires)
Requires:       perl(Dancer2) >= 0.203000
Requires:       perl(Dancer2::Core::HTTP) >= 0.203000
Requires:       perl(Dancer2::Plugin)
Requires:       perl(Dancer2::Serializer::Mutable)
Requires:       perl(Moo)
%{perl_requires}

%description
This plugin helps you write a RESTful webservice with Dancer2.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes doap.xml README README.mkdn
%license LICENSE

%changelog
