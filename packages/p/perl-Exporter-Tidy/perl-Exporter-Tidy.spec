#
# spec file for package perl-Exporter-Tidy
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


Name:           perl-Exporter-Tidy
Version:        0.08
Release:        0
%define cpan_name Exporter-Tidy
Summary:        Another way of exporting symbols
License:        SUSE-Public-Domain
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Exporter-Tidy/
Source:         http://www.cpan.org/authors/id/J/JU/JUERD/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module serves as an easy, clean alternative to Exporter. Unlike
Exporter, it is not subclassed, but it simply exports a custom import()
into your namespace.

With Exporter::Tidy, you don't need to use any package global in your
module. Even the subs you export can be lexically scoped.

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

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
