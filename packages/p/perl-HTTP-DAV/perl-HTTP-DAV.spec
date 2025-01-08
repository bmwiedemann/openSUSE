#
# spec file for package perl-HTTP-DAV
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


%define cpan_name HTTP-DAV
Name:           perl-HTTP-DAV
Version:        0.500.0
Release:        0
# 0.50 -> normalize -> 0.500.0
%define cpan_version 0.50
#Upstream:  Patrick Collins G03 Gloucester Place, Kensington Sydney, Australia Email: pcollins@cpan.org Phone: +61 2 9663 4916 All rights reserved. Current co-maintainer of the module is Cosimo Streppone for Opera Software ASA, the opera@cpan.org manpage. You may distribute this module under the terms of either the GNU General Public License or the Artistic License, as specified in the Perl README file.
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        WebDAV client library for Perl5
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CO/COSIMO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(LWP) >= 5.48
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(XML::DOM)
Requires:       perl(LWP) >= 5.48
Requires:       perl(URI)
Requires:       perl(URI::Escape)
Requires:       perl(XML::DOM)
Provides:       perl(HTTP::DAV) = %{version}
Provides:       perl(HTTP::DAV::Comms)
Provides:       perl(HTTP::DAV::Headers)
Provides:       perl(HTTP::DAV::Lock) = 0.09
Provides:       perl(HTTP::DAV::Resource) = %{version}
Provides:       perl(HTTP::DAV::ResourceList) = 0.11
Provides:       perl(HTTP::DAV::Response) = 0.14
Provides:       perl(HTTP::DAV::UserAgent)
Provides:       perl(HTTP::DAV::Utils) = 0.11
%undefine       __perllib_provides
%{perl_requires}

%description
HTTP::DAV is a Perl API for interacting with and modifying content on
webservers using the WebDAV protocol. Now you can LOCK, DELETE and PUT
files and much more on a DAV-enabled webserver.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes doc README TODO

%changelog
