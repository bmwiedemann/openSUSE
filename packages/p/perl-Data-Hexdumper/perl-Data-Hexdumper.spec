#
# spec file for package perl-Data-Hexdumper
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Data-Hexdumper
Name:           perl-Data-Hexdumper
Version:        3.0.100
Release:        0
# 3.0001 -> normalize -> 3.0.100
%define cpan_version 3.0001
#Upstream:  This software is free-as-in-speech software, and may be used, distributed, and modified under the terms of either the GNU General Public Licence version 2 or the Artistic Licence. It's up to you which one you use. The full text of the licences can be found in the files GPL2.txt and ARTISTIC.txt, respectively.
License:        Artistic-1.0 OR GPL-2.0-or-later
Summary:        Make binary data human-readable
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.65
Requires:       perl(Test::More) >= 0.65
Provides:       perl(Data::Hexdumper) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
'Data::Hexdumper' provides a simple way to format arbitrary binary data
into a nice human-readable format, somewhat similar to the Unix 'hexdump'
utility.

It gives the programmer a considerable degree of flexibility in how the
data is formatted, with sensible defaults. It is envisaged that it will
primarily be of use for those wrestling alligators in the swamp of binary
file formats, which is why it was written in the first place.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc CHANGELOG README
%license ARTISTIC.txt GPL2.txt

%changelog
