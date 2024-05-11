#
# spec file for package prctl
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           prctl
Version:        1.6
Release:        0
Summary:        A utility to perform process operations
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://sourceforge.net/projects/prctl
Source0:        http://downloads.sourceforge.net/project/prctl/prctl/%{version}/prctl-%{version}.tar.gz
Source1:        COPYING
Patch0:         prctl-1.5-Makefile.patch
Patch1:         prctl-1.5-warnings.patch
# work with gcc14
Patch2:         prctl-gcc14.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The prctl utility allows a user to control certain process behaviors in
the runtime environment.

%prep
%autosetup -p1
cp %{SOURCE1} .

%build
%configure
make

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-, root, root)
%doc ChangeLog
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
