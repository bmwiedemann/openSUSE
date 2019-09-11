#
# spec file for package perl-File-Slurp-Unicode
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



Name:           perl-File-Slurp-Unicode
%define cpan_name File-Slurp-Unicode
Summary:        Reading/Writing of Complete Files with Character Encoding Support
Version:        0.7.1
Release:        1
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-Slurp-Unicode/
Source:         http://www.cpan.org/authors/id/D/DA/DAVID/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl >= 5.10
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(File::Slurp)
Requires:       perl(File::Slurp)
%{perl_requires}

%description
This module wraps the File::Slurp manpage and adds character encoding
support through the *'encoding'* parameter. It exports the same functions
which take all the same parameters as File::Slurp. Please see the the
File::Slurp manpage documentation for basic usage; only the differences are
described from here on out.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
