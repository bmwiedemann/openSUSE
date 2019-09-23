#
# spec file for package perl-File-Type (Version 0.22)
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


Name:           perl-File-Type
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://cpan.org/
AutoReqProv:    on
Summary:        determine file type using magic
Version:        0.22
Release:        147
Source:         http://cpan.org/modules/by-module/File/File-Type-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
File::Type uses magic numbers (typically at the start of a file) to
determine the MIME type of that file.



Authors:
--------
    Paul Mison <pmison at fotango dot com>

%prep
%setup -n File-Type-%{version}

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
%dir %{perl_vendorlib}/File
%dir %{perl_vendorlib}/File/Type
%{perl_vendorlib}/File/Type.pm
%{perl_vendorlib}/File/Type/Builder.pm
%dir %{perl_vendorarch}/auto/File
%dir %{perl_vendorarch}/auto/File/Type
%{_mandir}/man3/File::Type*.3pm.gz

%changelog
