#
# spec file for package perl-Mixin-Linewise
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


Name:           perl-Mixin-Linewise
Version:        0.108
Release:        0
%define cpan_name Mixin-Linewise
Summary:        write your linewise code for handles; this does the rest
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Mixin-Linewise/
Source:         http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(PerlIO::utf8_strict)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(PerlIO::utf8_strict)
Requires:       perl(Sub::Exporter)
%{perl_requires}

%description
It's boring to deal with opening files for IO, converting strings to
handle-like objects, and all that. With the Mixin::Linewise::Readers
manpage and the Mixin::Linewise::Writers manpage, you can just write a
method to handle handles, and methods for handling strings and filenames
are added for you.

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
%doc Changes LICENSE README

%changelog
