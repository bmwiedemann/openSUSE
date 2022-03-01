#
# spec file for package perl-GDGraph
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name GDGraph
Name:           perl-GDGraph
Version:        1.54
Release:        0
Summary:        Produces charts with GD
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND GPL-2.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/GDGraph
Source0:        https://cpan.metacpan.org/modules/by-module/GD/GDGraph-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         perl-GDGraph-XBM-Magic.patch
BuildRequires:  perl
BuildRequires:  perl-ExtUtils-MakeMaker >= 6.76
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.30
BuildRequires:  perl(GD) >= 1.23
BuildRequires:  perl(GD::Text) >= 0.80
BuildRequires:  perl(Test::Exception) >= 0.400000
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(GD) >= 1.23
Requires:       perl(GD::Text) >= 0.80
BuildArch:      noarch
%{perl_requires}

%description
Produces charts with GD

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1
perl -pi -e 's/\r\n/\n/' samples/sample64.pl

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make_build test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%license Dustismo.LICENSE
%doc CHANGES Dustismo_Sans.ttf README samples

%changelog
