#
# spec file for package perl-Regexp-Shellish (Version 0.93)
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


Name:           perl-Regexp-Shellish
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://cpan.org/
AutoReqProv:    on
Summary:        Shell-like regular expressions
Version:        0.93
Release:        148
Source:         http://cpan.org/modules/by-module/Regexp/Regexp-Shellish-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
Provides shell-like regular expressions.  The wildcards provided are ?,
* and **, where ** is like * but matches /.  See compile_shellish for
details.



Authors:
--------
    Barrie Slaymaker <barries at slaysys dot com>

%prep
%setup -n Regexp-Shellish-%{version}

%build
perl Makefile.PL
%{__make} %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist

%clean
[ "${RPM_BUILD_ROOT}" != "/" -a -d ${RPM_BUILD_ROOT} ] && rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-, root, root)
%dir %{perl_vendorlib}/Regexp
%{perl_vendorlib}/Regexp/Shellish.pm
%dir %{perl_vendorarch}/auto/Regexp
%dir %{perl_vendorarch}/auto/Regexp/Shellish
%{_mandir}/man3/Regexp::Shellish.3pm.gz

%changelog
