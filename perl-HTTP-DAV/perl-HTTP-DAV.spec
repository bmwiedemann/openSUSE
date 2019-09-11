#
# spec file for package perl-HTTP-DAV
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-HTTP-DAV
Version:        0.49
Release:        0
#Upstream:  Patrick Collins G03 Gloucester Place, Kensington Sydney, Australia Email: pcollins@cpan.org Phone: +61 2 9663 4916 All rights reserved. Current co-maintainer of the module is Cosimo Streppone for Opera Software ASA, the opera@cpan.org manpage. You may distribute this module under the terms of either the GNU General Public License or the Artistic License, as specified in the Perl README file.
%define cpan_name HTTP-DAV
Summary:        WebDAV client library for Perl5
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CO/COSIMO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%{perl_requires}

%description
HTTP::DAV is a Perl API for interacting with and modifying content on
webservers using the WebDAV protocol. Now you can LOCK, DELETE and PUT
files and much more on a DAV-enabled webserver.

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
%doc Changes doc README TODO

%changelog
