#
# spec file for package container-support-utils
#
# Copyright (c) 2020 SUSE LLC
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


Name:           container-support-utils
Version:        0.2.2
Release:        0
Summary:        Open a shell inside a running container
License:        GPL-2.0
Group:          System/Packages
URL:            https://github.com/okirch/container-support-utils
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This utility allows you to run a shell, and use diagnostic
utilities, inside an already running container. The main
purpose of this is problem diagnosis.

%prep
%setup -q -n %{name}-%{version}

%build
make COPT="$RPM_OPT_FLAGS"

%install
mkdir -p %{buildroot}/usr/bin
make -C ns-exec DESTDIR=%{buildroot} install

%fdupes %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/ns-exec
%{_bindir}/savelog
%{_mandir}/man1/ns-exec.1%{?ext_man}
%{_mandir}/man1/savelog.1%{?ext_man}

%changelog
