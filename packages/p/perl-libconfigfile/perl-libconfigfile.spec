#
# spec file for package perl-libconfigfile
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


Name:           perl-libconfigfile
Summary:        Parses simple configuration files
Version:        1.1.1
Release:        151
License:        GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://packages.qa.debian.org/libc/libconfigfile-perl.html
Source0:        libconfigfile-perl_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl perl-macros

%description
ConfigFile parses simple configuration files and stores its values in an
anonymous hash reference. The syntax of the configuration file is quite
simple:

1.  This is a comment VALUE_ONE = foo VALUE_TWO = $VALUE_ONE/bar
VALUE_THREE = The value contains a \# (hash). # This is a comment.
COMPOSED_VALUE[one] = The first component of a clustered value
COMPOSED_VALUE[two] = The second component of a clustered value



Authors:
--------
    Sebastien J. Gross <seb@sjgross.org>

%prep
%setup -q -n libconfigfile-perl-%{version}
# delete leftover old version to not cause race conditions on which ConfigFile.pm gets installed
rm -r libconfigfile-perl-1.1

%build
perl Makefile.PL
make %{?_smp_mflags}
# run 'make test' if you like

%install
%perl_make_install
%perl_process_packlist

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{perl_vendorlib}/ConfigFile.pm
%{perl_vendorarch}/auto/ConfigFile
%{_mandir}/*/*
%doc debian/changelog debian/copyright

%changelog
