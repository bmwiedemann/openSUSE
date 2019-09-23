#
# spec file for package cups-backends
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cups-backends
Summary:        Additional Backends for CUPS
License:        GPL-2.0
Group:          Hardware/Printing
Version:        1.1
Release:        0
Source0:        pipe
Source1:        http://www.openprinting.org/download/files/beh
Source100:      COPYING
Requires:       cups
# Conflict with foomatic-filters because /usr/lib/cups/backend/beh is provided by it.
# Instead of foomatic-filters now cups-filters-foomatic-rip should be used.
# Because cups-filters-foomatic-rip provides the RPM capability "foomatic-filters"
# there cannot be an unversioned conflict with foomatic-filters here
# (otherwise cups-backends would conflict with cups-filters-foomatic-rip).
# Because cups-filters-foomatic-rip provides at least "foomatic-filters = 4.0.17.256.1"
# (see cups-filters.spec) and because we will not upgrade the foomatic-filters package
# (its current version is 4.0.12) a conflict with foomatic-filters < 4.0.17.256 is used
# to let cups-backends only conflict with the old foomatic-filters package
# but not with the new cups-filters-foomatic-rip package:
Conflicts:      foomatic-filters < 4.0.17.256
# According to RPMLINT:
# "The package should be of the noarch architecture because it doesn't contain any binaries."
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains free additional backends for CUPS.

%prep
# There is nothing to do here because Source0 and Source1 are installed directly from RPM_SOURCE_DIR.

%build
# There is nothing to build because Source0 is a Bash script and Source1 is a Perl script.
# At least test if the syntax is o.k.:
bash -n ${RPM_SOURCE_DIR}/pipe
perl -c ${RPM_SOURCE_DIR}/beh &>/dev/null

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/cups/backend
# Source0: cups-pipe.sh
install -m 755 ${RPM_SOURCE_DIR}/pipe $RPM_BUILD_ROOT/usr/lib/cups/backend/pipe
# Source1: beh
# Since cups-filters version 1.6.0 the beh backend is provided
# by the cups-filters RPM as /usr/lib/cups/backend/beh which is
# a C re-write of the beh backend written in Perl that is still
# provided here but now named /usr/lib/cups/backend/beh.pl
# to avoid that cups-backends conflicts with cups-filters:
install -m 755 ${RPM_SOURCE_DIR}/beh $RPM_BUILD_ROOT/usr/lib/cups/backend/beh.pl
# Source100: COPYING
install -Dm 644 %{S:100} %{buildroot}%{_docdir}/%{name}/COPYING

%files
%defattr(-,root,root,-)
%dir /usr/lib/cups
%dir /usr/lib/cups/backend
%dir %{_docdir}/%{name}
/usr/lib/cups/backend/pipe
/usr/lib/cups/backend/beh.pl
%{_docdir}/%{name}/COPYING

%changelog
