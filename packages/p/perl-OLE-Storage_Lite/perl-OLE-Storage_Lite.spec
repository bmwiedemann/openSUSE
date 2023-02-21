#
# spec file for package perl-OLE-Storage_Lite
#
# Copyright (c) 2023 SUSE LLC
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
Version:        0.22
Release:        0
#Upstream:  Japan. All rights reserved. You may distribute under the terms of either the GNU General Public License or the Artistic License, as specified in the Perl README file.
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Read and write OLE storage files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JM/JMCNAMARA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
OLE::Storage_Lite allows you to read and write an OLE structured file.

OLE::Storage_Lite::PPS is a class representing PPS.
OLE::Storage_Lite::PPS::Root, OLE::Storage_Lite::PPS::File and
OLE::Storage_Lite::PPS::Dir are subclasses of OLE::Storage_Lite::PPS.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
