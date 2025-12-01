#
# spec file for package perl-OLE-Storage_Lite
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name OLE-Storage_Lite
Name:           perl-OLE-Storage_Lite
Version:        0.240.0
Release:        0
# 0.24 -> normalize -> 0.240.0
%define cpan_version 0.24
#Upstream:  Japan. All rights reserved. You may distribute under the terms of either the GNU General Public License or the Artistic License, as specified in the Perl README file.
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Read and write OLE storage files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMCNAMARA/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(OLE::Storage_Lite) = %{version}
Provides:       perl(OLE::Storage_Lite::PPS) = %{version}
Provides:       perl(OLE::Storage_Lite::PPS::Dir) = %{version}
Provides:       perl(OLE::Storage_Lite::PPS::File) = %{version}
Provides:       perl(OLE::Storage_Lite::PPS::Root) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
OLE::Storage_Lite allows you to read and write an OLE structured file.

OLE::Storage_Lite::PPS is a class representing PPS.
OLE::Storage_Lite::PPS::Root, OLE::Storage_Lite::PPS::File and
OLE::Storage_Lite::PPS::Dir are subclasses of OLE::Storage_Lite::PPS.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README

%changelog
