#
# spec file for package dhcp-tools
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

Name:           dhcp-tools
Url:            http://www.mavetju.org/unix/general.php
%define DUMP dhcpdump-1.6
%define PING dhcping-1.2
License:        BSD-3-Clause
Group:          Productivity/Networking/Boot/Utilities
BuildRequires:  automake
Version:        1.6
Release:        0
Summary:        DHCP Tools
Source:         dhcpdump-1.6.tar.gz
Source1:        dhcping-1.2.tar.gz
Patch1:         dhcpdump-1.6-tcpdump-3.8.1.dif
Patch2:         dhcpdump-1.6-tcpdump-3.8.2.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Two utilities, written by Edwin Groothuis, to test and debug DHCP:

dhcpdump This parses tcpdump output to display the dhcp-packets for
easier checking and debugging.

dhcping This allows the system administrator to check if a remote DHCP
server is still functioning.

Home page: http://www.mavetju.org

%prep
%setup -c -n %{name}
%setup -n %{name} -T -D -a 1
%if %suse_version > 900
%patch1
%endif
%if %suse_version > 910
pushd dhcpdump*
%patch2 -p1
popd
%endif

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
for i in %{DUMP} %{PING}; do
	pushd $i
	aclocal
	autoconf
	touch NEWS README AUTHORS ChangeLog
	automake --add-missing
	%{configure}
	make %{?_smp_mflags}
	touch *.pod
	make *.pod
	popd
done

%install
make -C %{DUMP} DESTDIR=$RPM_BUILD_ROOT install
make -C %{PING} DESTDIR=$RPM_BUILD_ROOT install
mkdir dhcpdump dhcping
cp -p %{DUMP}/{CHANGES,CONTACT,FILES,dhcp_options.h,LICENSE} dhcpdump/
cp -p %{PING}/{CHANGES,CONTACT,FILES,LICENSE} dhcping/

%files
%defattr(-,root,root)
%doc dhcpdump
%doc dhcping
/usr/bin/dhcpdump
/usr/bin/dhcping
%{_mandir}/man1/dhcpdump.1.gz
%{_mandir}/man8/dhcping.8.gz

%changelog
