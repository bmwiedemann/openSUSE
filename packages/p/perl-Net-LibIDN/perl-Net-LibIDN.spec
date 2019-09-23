#
# spec file for package perl-Net-LibIDN (Version 0.12)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-Net-LibIDN
%define cpan_name Net-LibIDN
Summary:        Net::LibIDN Perl module
Version:        0.12
Release:        1
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-LibIDN/
Source:         http://www.cpan.org/modules/by-module/Net/Net-LibIDN-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  libidn-devel
%{perl_requires}

%description
This module provides Perl bindings for GNU Libidn by Simon Josefsson
(http://www.gnu.org/software/libidn/) in way that was heavily inspired by
PHP bindings for the same library done by Turbo Fredriksson (http://php-
idn.bayour.com/).

Authors:
--------
    Thomas Jacob, http://internet24.de

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root,-)
%doc Artistic Changes README

%changelog
