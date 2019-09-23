#
# spec file for package perl-MLDBM-Sync
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-MLDBM-Sync
%define cpan_name MLDBM-Sync
BuildRequires:  dos2unix
BuildRequires:  perl-MLDBM
BuildRequires:  perl-Tie-Cache
BuildRequires:  perl-macros
Version:        0.30
Release:        0
Requires:       perl-MLDBM
Requires:       perl-Tie-Cache
Url:            http://cpan.org/modules/by-module/MLDBM
Summary:        Perl module for safe concurrent access to MLDBM databases
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Source:         MLDBM-Sync-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}

%description
This module wraps around the MLDBM interface, by handling concurrent
access to MLDBM databases with file locking, and flushes i/o explicity
per lock/unlock. The new [Read]Lock()/UnLock() API can be used to
serialize requests logically and improve performance for bundled reads
& writes.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}
dos2unix CHANGES

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc CHANGES Makefile README

%changelog
