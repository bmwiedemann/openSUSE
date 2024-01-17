#
# spec file for package cronic
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cronic
Version:        3
Release:        0
Summary:        A cure for Cron's chronic email problem
License:        SUSE-Public-Domain
Group:          System/Base
Url:            http://habilis.net/cronic/
Source0:        http://habilis.net/cronic/cronic
Source1:        cronic.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Cronic is a small shim shell script for wrapping cron jobs so that cron only
sends email when an error has occurred. Cronic defines an error as any non-
trace error output or a non-zero result code. Cronic filters Bash execution
traces (or anything matching PS4) from the error output, so jobs can be run
with execution tracing to aid forensic debugging. Cronic has no options, it
simply executes its arguments.

%prep
%setup -q -c -T
cp %{SOURCE0} .

%build

%install
mkdir -p %{buildroot}/%{_bindir}
cp cronic %{buildroot}/%{_bindir}/cronic

mkdir -p %{buildroot}/%{_mandir}/man1
gzip -c %{SOURCE1} >%{buildroot}/%{_mandir}/man1/cronic.1.gz

%files
%defattr (-, root, root)
%attr(755,root,root) %{_bindir}/cronic
%{_mandir}/man1/cronic.1.gz

%changelog
