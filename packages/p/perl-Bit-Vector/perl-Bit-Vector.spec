#
# spec file for package perl-Bit-Vector
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


Name:           perl-Bit-Vector
Version:        7.4
Release:        0
#Upstream: CHECK(GPL-1.0+ or Artistic-1.0)
%define cpan_name Bit-Vector
Summary:        Bit::Vector Perl module
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Bit-Vector/
Source0:        http://www.cpan.org/authors/id/S/ST/STBEY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         Bit-Vector-7.1.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp::Clan) >= 5.3
BuildRequires:  perl(Storable) >= 2.21
Requires:       perl(Carp::Clan) >= 5.3
Requires:       perl(Storable) >= 2.21
%{perl_requires}

%description
Bit::Vector Perl module

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Artistic.txt CHANGES.txt CREDITS.txt examples GNU_GPL.txt GNU_LGPL.txt INSTALL.txt README.txt

%changelog
