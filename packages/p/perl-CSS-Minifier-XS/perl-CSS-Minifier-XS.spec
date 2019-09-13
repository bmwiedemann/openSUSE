#
# spec file for package perl-CSS-Minifier-XS
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-CSS-Minifier-XS
Version:        0.09
Release:        0
%define cpan_name CSS-Minifier-XS
Summary:        XS based CSS minifier
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/CSS-Minifier-XS/
Source:         http://www.cpan.org/authors/id/G/GT/GTERMARS/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build) >= 0.40
%{perl_requires}

%description
'CSS::Minifier::XS' is a CSS "minifier"; its designed to remove
un-necessary whitespace and comments from CSS files, while also *not*
breaking the CSS.

'CSS::Minifier::XS' is similar in function to 'CSS::Minifier', but is
substantially faster as its written in XS and not just pure Perl.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
