# vim: set sw=4 ts=4 et nu:
#
# spec file for package perl-File-ReadBackwards
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
Name:           perl-File-ReadBackwards
Version:        1.05
Release:        0
Summary:        Read a file backwards by lines
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Source:         http://search.cpan.org/CPAN/authors/id/U/UR/URI/File-ReadBackwards-%{version}.tar.gz
Url:            http://search.cpan.org/dist/File-ReadBackwards
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This module reads a file backwards line by line. It is simple to use, memory
efficient and fast. It supports both an object and a tied handle interface.

It is intended for processing log and other similar text files which typically
have their newest entries appended to them. By default files are assumed to be
plain text and have a line ending appropriate to the OS. But you can set the
input record separator string on a per file basis.

%prep
%setup -q -n "File-ReadBackwards-%{version}"
%__sed -i '/^auto_install/d' Makefile.PL

%build
%__perl Makefile.PL PREFIX="%{_prefix}"
%__make %{?jobs:-j%{jobs}}

%install
%perl_make_install
%perl_process_packlist

%check
%__make test

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/File
%{perl_vendorlib}/File/ReadBackwards.pm
%dir %{perl_vendorarch}/auto/File
%{perl_vendorarch}/auto/File/ReadBackwards
%doc %{perl_man3dir}/File::ReadBackwards.%{perl_man3ext}%{ext_man}

%changelog
