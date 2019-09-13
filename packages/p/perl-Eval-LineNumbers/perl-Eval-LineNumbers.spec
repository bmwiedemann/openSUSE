#
# spec file for package perl-Eval-LineNumbers
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


Name:           perl-Eval-LineNumbers
Version:        0.34
Release:        0
#Upstream:  This package may be used and redistributed under the terms of either the Artistic 2.0 or LGPL 2.1 license.
%define cpan_name Eval-LineNumbers
Summary:        Add line numbers to heredoc blocks that contain perl source code
License:        Artistic-2.0 or LGPL-2.1
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Eval-LineNumbers/
Source0:        http://www.cpan.org/authors/id/M/MU/MUIR/modules/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Add a '#line "this-file" 392' comment to heredoc/hereis text that is going
to be eval'ed so that error messages will point back to the right place.

Please note: when you embed '\n' in your code, it gets expanded in
double-quote hereis documents so it will mess up your line numbering. Use
'\\n' instead when you can.

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
