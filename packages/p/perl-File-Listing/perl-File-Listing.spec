#
# spec file for package perl-File-Listing
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


Name:           perl-File-Listing
Version:        6.04
Release:        0
%define cpan_name File-Listing
Summary:        parse directory listing
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-Listing/
Source:         http://www.cpan.org/authors/id/G/GA/GAAS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Date) >= 6
#BuildRequires: perl(File::Listing)
#BuildRequires: perl(LWP::Simple)
Requires:       perl(HTTP::Date) >= 6
%{perl_requires}

%description
This module exports a single function called parse_dir(), which can be used
to parse directory listings.

The first parameter to parse_dir() is the directory listing to parse. It
can be a scalar, a reference to an array of directory lines or a glob
representing a filehandle to read the directory listing from.

The second parameter is the time zone to use when parsing time stamps in
the listing. If this value is undefined, then the local time zone is
assumed.

The third parameter is the type of listing to assume. Currently supported
formats are 'unix', 'apache' and 'dosftp'. The default value is 'unix'.
Ideally, the listing type should be determined automatically.

The fourth parameter specifies how unparseable lines should be treated.
Values can be 'ignore', 'warn' or a code reference. Warn means that the
perl warn() function will be called. If a code reference is passed, then
this routine will be called and the return value from it will be
incorporated in the listing. The default is 'ignore'.

Only the first parameter is mandatory.

The return value from parse_dir() is a list of directory entries. In a
scalar context the return value is a reference to the list. The directory
entries are represented by an array consisting of [ $filename, $filetype,
$filesize, $filetime, $filemode ]. The $filetype value is one of the
letters 'f', 'd', 'l' or '?'. The $filetime value is the seconds since Jan
1, 1970. The $filemode is a bitmask like the mode returned by stat().

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
