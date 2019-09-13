#
# spec file for package perl-Convert-BinHex
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


Name:           perl-Convert-BinHex
Version:        1.125
Release:        0
%define cpan_name Convert-BinHex
Summary:        Extract Data From Macintosh Binhex Files
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Convert-BinHex/
Source0:        http://www.cpan.org/authors/id/S/ST/STEPHEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Test::Most)
BuildRequires:  perl(autodie)
%{perl_requires}

%description
*BinHex* is a format used by Macintosh for transporting Mac files safely
through electronic mail, as short-lined, 7-bit, semi-compressed data
streams. Ths module provides a means of converting those data streams back
into into binary data.

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
%doc Changes COPYING LICENSE README README-TOO test testin testout

%changelog
