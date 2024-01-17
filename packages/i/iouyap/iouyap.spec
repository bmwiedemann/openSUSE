#
# spec file for package iouyap
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


Name:           iouyap
Version:        0.97
Release:        0
Summary:        Bridge IOU to TAP, UDP and Ethernet
License:        GPL-3.0-or-later
Group:          System/Emulators/Other
URL:            https://github.com/GNS3/iouyap
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  glibc-devel
Requires(pre):  shadow
%if 0%{?suse_version}
Requires(pre):  permissions
%endif

%description
Bridge IOU to TAP, UDP and Ethernet, mainly used by gns3server

In order to use iouyap as non-root user, the user needs to be member of the iouyap group!

%prep
%setup -q

%build
bison --yacc -dv netmap_parse.y
flex netmap_scan.l
gcc -I -Wall -fPIE %optflags -fcommon *.c iniparser/*.c -o %{name} -lpthread -pie

%install
%__mkdir_p %{buildroot}/%{_libexecdir}
%__mkdir_p %{buildroot}/%{_bindir}
%__mv %{name} %{buildroot}/%{_libexecdir}
ln -sf %{_libexecdir}/%{name} %{buildroot}/%{_bindir}/%{name}

%pre
%{_sbindir}/groupadd -r iouyap 2> /dev/null || :

%if 0%{?suse_version}
%post
%set_permissions %{_libexecdir}/%{name}

%verifyscript
%verify_permissions -e %{_libexecdir}/%{name}
%endif

%files
%license LICENSE
%doc README.rst
%verify(not caps) %attr(0750,root,iouyap) %{_libexecdir}/%{name}
%{_bindir}/%{name}

%changelog
