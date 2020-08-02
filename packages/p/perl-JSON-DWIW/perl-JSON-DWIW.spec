#
# spec file for package perl-JSON-DWIW
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



Name:           perl-JSON-DWIW
Version:        0.47
Release:        1
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name JSON-DWIW
Summary:        JSON converter that Does What I Want
Url:            http://search.cpan.org/dist/JSON-DWIW/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/D/DO/DOWENS/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Other JSON modules require setting several parameters before calling the
conversion methods to do what I want. This module does things by default
that I think should be done when working with JSON in Perl. This module
also encodes and decodes faster than the JSON manpage.pm and the JSON::Syck
manpage in my benchmarks.

This means that any piece of data in Perl (assuming it's valid unicode)
will get converted to something in JSON instead of throwing an exception.
It also means that output will be strict JSON, while accepted input will be
flexible, without having to set any options.

For a list of changes in recent versions, see the documentation for the
JSON::DWIW::Changes manpage.

This module can be downloaded from the
http://www.cpan.org/authors/id/D/DO/DOWENS/ manpage.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
%defattr(-,root,root,755)
%doc Artistic README WhatsNew

%changelog
