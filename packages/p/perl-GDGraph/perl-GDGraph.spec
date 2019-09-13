#
# spec file for package perl-GDGraph
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


Name:           perl-GDGraph
Version:        1.54
Release:        0
%define cpan_name GDGraph
Summary:        Produces charts with GD
License:        (Artistic-1.0 or GPL-1.0+) and GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/GDGraph/
Source0:        http://www.cpan.org/authors/id/R/RU/RUZ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-ExtUtils-MakeMaker >= 6.76
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.30
BuildRequires:  perl(GD) >= 1.18
BuildRequires:  perl(GD::Text) >= 0.80
BuildRequires:  perl(Test::Exception) >= 0.400000
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(GD) >= 1.18
Requires:       perl(GD::Text) >= 0.80
%{perl_requires}

%description
Produces charts with GD

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
%doc CHANGES Dustismo.LICENSE Dustismo_Sans.ttf README samples

%changelog
