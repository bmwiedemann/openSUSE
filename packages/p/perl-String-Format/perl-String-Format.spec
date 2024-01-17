#
# spec file for package perl-String-Format
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


Name:           perl-String-Format
Version:        1.18
Release:        0
%define cpan_name String-Format
Summary:        Sprintf-Like String Formatting Capabilities With
License:        GPL-2.0-only
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/String-Format/
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SREZIC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
String::Format lets you define arbitrary printf-like format sequences to be
expanded. This module would be most useful in configuration files and
reporting tools, where the results of a query need to be formatted in a
particular way. It was inspired by mutt's index_format and related
directives (see
<URL:http://www.mutt.org/doc/manual/manual-6.html#index_format>).

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
%license COPYING

%changelog
