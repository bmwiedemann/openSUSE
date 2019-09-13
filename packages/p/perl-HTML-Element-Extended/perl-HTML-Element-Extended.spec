#
# spec file for package perl-HTML-Element-Extended
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



Name:           perl-HTML-Element-Extended
Version:        1.18
Release:        1
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name HTML-Element-Extended
Summary:        Extension for HTML::Element
Url:            http://search.cpan.org/dist/HTML-Element-Extended/
Group:          Development/Libraries/Perl
#Source:         http://search.cpan.org/CPAN/authors/id/M/MS/MSISK/%{name}-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.bz2
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(HTML::Element) >= 3.01
Requires:       perl(Data::Dumper)
Requires:       perl(HTML::Element) >= 3.01
%{perl_requires}

%description
HTML-Element-Extended is a package of several enhanced HTML::Element
classes, most of which arose during the effort to implement an
HTML::Element based table class.

The modules are:
        HTML::ElementTable
        HTML::ElementSuper
        HTML::ElementGlob
        HTML::ElementRaw

The resulting functionality enables:
        tables
        element globs
        element coordinates
        content replacement
        content wrapping
        element cloning
        raw HTML string adoption

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes README

%changelog
