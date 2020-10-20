#
# spec file for package perl-File-Share
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


Name:           perl-File-Share
Version:        0.25
Release:        0
%define cpan_name File-Share
Summary:        Extend File::ShareDir to Local Libraries
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-Share/
Source:         http://www.cpan.org/authors/id/I/IN/INGY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::ShareDir) >= 1.03
Requires:       perl(File::ShareDir) >= 1.03
%{perl_requires}

%description
This module is a dropin replacement for the File::ShareDir manpage. It
supports the 'dist_dir' and 'dist_file' functions, except these functions
have been enhanced to understand when the developer's local './share/'
directory should be used.

NOTE: module_dist and module_file are not yet supported, because (afaik)
there is no well known way to populate per-module share files. This may
change in the future. Please contact me if you know how to do this.

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
%doc Changes CONTRIBUTING LICENSE README

%changelog
