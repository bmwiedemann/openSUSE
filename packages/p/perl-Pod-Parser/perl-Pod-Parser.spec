#
# spec file for package perl-Pod-Parser
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Pod-Parser
Version:        1.63
Release:        0
%define cpan_name Pod-Parser
Summary:        Base Class for Creating Pod Filters and Translators
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Pod-Parser/
Source0:        http://www.cpan.org/authors/id/M/MA/MAREKR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
*NOTE: This module is considered legacy; modern Perl releases (5.18 and
higher) are going to remove Pod-Parser from core and use Pod-Simple for all
things POD.*

*Pod::Parser* is a base class for creating POD filters and translators. It
handles most of the effort involved with parsing the POD sections from an
input stream, leaving subclasses free to be concerned only with performing
the actual translation of text.

*Pod::Parser* parses PODs, and makes method calls to handle the various
components of the POD. Subclasses of *Pod::Parser* override these methods
to translate the POD into whatever output format they desire.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc ANNOUNCE CHANGES README TODO

%changelog
