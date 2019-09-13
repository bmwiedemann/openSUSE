#
# spec file for package perl-File-Path
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


Name:           perl-File-Path
Version:        2.160000
Release:        0
%define cpan_version 2.16
Provides:       perl(File::Path) = 2.160000
#Upstream:  James Keenan and Richard Elberger 1995-2018. All rights reserved.
%define cpan_name File-Path
Summary:        Create or remove directory trees
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-Path/
Source0:        https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module provides a convenient way to create directories of arbitrary
depth and to delete an entire directory subtree from the filesystem.

%prep
%setup -q -n %{cpan_name}-%{cpan_version}

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
