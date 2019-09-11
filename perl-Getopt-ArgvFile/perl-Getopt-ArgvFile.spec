#
# spec file for package perl-Getopt-ArgvFile
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Getopt-ArgvFile
Version:        1.11
Release:        0
Summary:        Perl Module to interpolate Script Options from Files into @ARGV
License:        Artistic-1.0 or Artistic-2.0
Group:          Development/Libraries/Perl
Source:         http://search.cpan.org/CPAN/authors/id/J/JS/JSTENZEL/Getopt-ArgvFile-%{version}.tar.gz
Url:            http://search.cpan.org/dist/Getopt-ArgvFile/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  dos2unix
BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00

%description
This module simply interpolates option file hints in @ARGV by the contents of
the pointed files. This enables option reading from files instead of or
additional to the usual reading from the command line.

Alternatively, you can process any array instead of @ARGV which is used by
default and mentioned mostly in this manual.

The interpolated @ARGV could be subsequently processed by the usual option
handling, e.g. by a Getopt::xxx module. Getopt::ArgvFile does not perform any
option handling itself, it only prepares the array @ARGV.

%prep
%setup -q -n "Getopt-ArgvFile-%{version}"
%__sed -i '/^auto_install/d' Makefile.PL
dos2unix Changes

%build
%__perl Makefile.PL PREFIX="%{_prefix}"
%__make %{?jobs:-j%{jobs}}

%install
%perl_make_install
%perl_process_packlist

%check
%__make test

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/Getopt
%{perl_vendorlib}/Getopt/ArgvFile.pm
%dir %{perl_vendorarch}/auto/Getopt
%{perl_vendorarch}/auto/Getopt/ArgvFile
%doc %{perl_man3dir}/Getopt::ArgvFile.%{perl_man3ext}*

%changelog
