#
# spec file for package perl-GDGraph
#
# Copyright (c) 2024 SUSE LLC
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
Version:        1.560.0
Release:        0
# 1.56 -> normalize -> 1.560.0
%define cpan_version 1.56
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND GPL-2.0-or-later
Summary:        Produces charts with GD
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         perl-GDGraph-XBM-Magic.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.30
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(GD) >= 1.18
BuildRequires:  perl(GD::Text) >= 0.80
BuildRequires:  perl(Test::Exception) >= 0.40
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(GD) >= 1.18
Requires:       perl(GD::Text) >= 0.80
Provides:       perl(GD::Graph) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Produces charts with GD

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

# MANUAL BEGIN
perl -pi -e 's/\r\n/\n/' samples/sample64.pl
# MANUAL END

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES Dustismo.LICENSE Dustismo_Sans.ttf README samples

%changelog
