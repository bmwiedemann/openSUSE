#
# spec file for package perl-Text-Reform
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

# norootforbuild


Name:           perl-Text-Reform
%define cpan_name Text-Reform
Summary:        Manual text wrapping and reformatting
Version:        1.20
Release:        8
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-Reform/
#Source:         http://www.cpan.org/modules/by-module/Text/Text-Reform-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl(Module::Build)
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter)
Requires:       perl(Exporter)

%description
The module supplies a re-entrant, highly configurable replacement
for the built-in Perl format() mechanism.

Author:
-------
        Damian Conway <damian@conway.org>

%prep
%setup -q -n %{cpan_name}-%{version}
#rpmlint: wrong-script-end-of-line-encoding
find -type f -exec %{__perl} -p -i -e "s|\r\n|\n|" {} \;

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root,-)
%doc Changes demo README

%changelog
