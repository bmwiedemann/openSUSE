#
# spec file for package perl-Readonly-XS
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

# norootforbuild


Name:           perl-Readonly-XS
%define cpan_name Readonly-XS
Summary:        Companion module for Readonly.pm, to speed up read-only scalar variables
Version:        1.05
Release:        7
License:        GPL-2.0+
Group:          Development/Libraries/Perl
AutoReqProv:    on
Url:            http://search.cpan.org/dist/Readonly-XS/
Source:         %{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros
#
BuildRequires:  perl(Readonly) >= 1.02
Requires:       perl(Readonly) >= 1.02
Provides:       %{cpan_name}

%description
This is a companion module to Readonly.pm.  You do not use
Readonly::XS directly.  Instead, once it is installed, Readonly.pm
will detect this and will use it for creating read-only scalars.  This
results in a significant speed improvement.  This does not speed up
read-only arrays or hashes.

Authors:
--------
    Eric Roode, <roode@cpan.org>

%prep 
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS -Wall"
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
%defattr(-, root, root)
%doc Changes README

%changelog
