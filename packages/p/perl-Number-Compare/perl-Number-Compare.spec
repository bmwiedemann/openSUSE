#
# spec file for package perl-Number-Compare
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



Name:           perl-Number-Compare
Version:        0.03
Release:        1
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name Number-Compare
Summary:        Numeric comparisons
Url:            http://search.cpan.org/dist/Number-Compare/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/R/RC/RCLAMP/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{perl_requires}

%description
Number::Compare compiles a simple comparison to an anonymous subroutine,
which you can call with a value to be tested again.

Now this would be very pointless, if Number::Compare didn't understand
magnitudes.

The target value may use magnitudes of kilobytes ('k', 'ki'), megabytes
('m', 'mi'), or gigabytes ('g', 'gi'). Those suffixed with an 'i' use the
appropriate 2**n version in accordance with the IEC standard:
http://physics.nist.gov/cuu/Units/binary.html

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean
rm -rf %{buildroot}

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes

%changelog
