#
# spec file for package perl-CGI-FastTemplate
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-CGI-FastTemplate
%define cpan_name CGI-FastTemplate
Summary:        Perl extension for managing templates, and performing variable interpolation
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Version:        1.09
Release:        0
Url:            https://metacpan.org/release/%{cpan_name}
Source:         https://cpan.metacpan.org/authors/id/J/JM/JMOORE/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
CGI::FastTemplate manages templates and parses templates replacing
variable names with values. It was designed for mid to large scale
web applications (CGI, mod_perl) where there are great benefits to
separating the logic of an application from the specific
implementation details.

%prep
%setup -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
%perl_make_install
# do not perl_process_packlist (noarch)
# remove .packlist file
%{__rm} -rf $RPM_BUILD_ROOT%perl_vendorarch
# remove perllocal.pod file
%{__rm} -rf $RPM_BUILD_ROOT%perl_archlib
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files 
%defattr(-, root, root)
%doc README

%changelog
