#
# spec file for package perl-Net-HTTPServer
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           perl-Net-HTTPServer
%define cpan_name Net-HTTPServer
Summary:        A simple perl Http Server
Version:        1.1.1
Release:        10
License:        LGPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-HTTPServer/
#Source:         http://www.cpan.org/authors/id/R/RE/REATMON/Net-HTTPServer-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
Patch0:         handlewidechar.patch
Patch1:         escaped_characters.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(URI) >= 1.27
Requires:       perl(URI) >= 1.27
%{perl_requires}

%description
Net::HTTPServer basically turns a CGI script into a stand alone server.
Useful for temporary services, mobile/local servers, or embedding an HTTP
server into another program.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(644,root,root,755)
%doc CHANGES LICENSE.LGPL README

%changelog
