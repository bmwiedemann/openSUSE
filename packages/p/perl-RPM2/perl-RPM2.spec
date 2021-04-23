#
# spec file for package perl-RPM2
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


Name:           perl-RPM2
Version:        1.4
Release:        0
Summary:        Perl bindings for the RPM Package Manager API
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/RPM2/
Source0:        http://search.cpan.org/CPAN/authors/id/L/LK/LKUNDRAK/RPM2-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  rpm-devel >= 4.6
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build) >= 0.4200
Requires:       perl(File::Basename)
Requires:       perl(File::Spec)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
The RPM2 module provides an object-oriented interface to querying both the
installed RPM database as well as files on the filesystem.

%prep
%setup -q -n RPM2-%{version}

%build
perl ./Build.PL
./Build

%install
./Build pure_install --destdir %{buildroot} --installdirs vendor
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%perl_process_packlist
%perl_gen_filelist

%check
./Build test verbose=1

%files -f %{name}.files
%defattr(-,root,root,-)
%doc Changes README

%changelog
