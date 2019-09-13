#
# spec file for package perl-Net-CIDR-Lite (Version 0.21)
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


Name:           perl-Net-CIDR-Lite
%define cpan_name Net-CIDR-Lite
Summary:        Perl extension for merging IPv4 or IPv6 CIDR addresses
Version:        0.21
Release:        4
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-CIDR-Lite
Source:         http://search.cpan.org/CPAN/authors/id/D/DO/DOUGW/Net-CIDR-Lite-0.21.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
%if 0%{?suse_version} && 0%{?suse_version} <= 1210
BuildRequires:  perl-macros
%endif
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)

%description
Faster alternative to Net::CIDR when merging a large number of CIDR
address ranges. Works for IPv4 and IPv6 addresses.


Authors:
--------
    Douglas Wilson <dougw@cpan.org>

%prep
%setup -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS -Wall"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
# do not perl_process_packlist (noarch)
# remove .packlist file
%{__rm} -rf $RPM_BUILD_ROOT%perl_vendorarch
# remove perllocal.pod file
%{__rm} -rf $RPM_BUILD_ROOT%perl_archlib
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root)
%doc Changes README

%changelog
