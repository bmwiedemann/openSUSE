#
# spec file for package ssldump
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


Name:           ssldump
%if 0%{?suse_version} > 1320 || 0%{?is_opensuse} && 0%{?leap_version} == 420300
BuildRequires:  libpcap-devel-static
%else
BuildRequires:  libpcap-devel
%endif
BuildRequires:  libtool
BuildRequires:  openssl-devel
Version:        0.9b3
Release:        0
Summary:        SSLv3/TLS Network Protocol Analyzer
License:        BSD-3-Clause
Group:          Productivity/Networking/Diagnostic
Url:            http://www.rtfm.com/ssldump
Source:         ssldump-%{version}.tar.gz
Patch:          ssldump-0.9b3-libpcap.diff
Patch1:         random_return.patch
Patch2:         ssldump-0.9b3-aes.patch
Patch3:         implicit_def.patch
Patch4:         ssldump-0.9b3-newssl.patch
Patch5:         ssldump-cvs-06-19-2006.diff
Patch6:         update-config.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ssldump is an SSLv3/TLS network protocol analyzer. It identifies TCP
connections on the chosen network interface and attempts to interpret
them as SSLv3/TLS traffic. When it identifies SSLv3/TLS traffic, it
decodes the records and outputs them in a textual form to stdout. If
provided with the appropriate keying material, it also decrypts the
connections and displays the application data traffic.



Authors:
--------
    Eric Rescorla <ekr@rtfm.com>

%prep
%setup -n ssldump-%{version}
%patch
%patch1
%patch2 -p 1
%patch3
%patch4
%patch5 -p 1
%patch6 -p1

%build
%{?suse_update_config:%{suse_update_config}}
libtoolize --force
autoreconf
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"
./configure --mandir=%{_mandir} \
	    --prefix=%{_prefix} \
	    --libdir=%{_libdir} \
	    --with-pcap-lib=%{_libdir}
make

%install
rm -rf $RPM_BUILD_ROOT
make BINDIR=$RPM_BUILD_ROOT/%{_prefix}/sbin MANDIR=$RPM_BUILD_ROOT/%{_mandir} install

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/sbin/*
%doc COPYRIGHT CREDITS ChangeLog FILES INSTALL* README VERSION
%doc %{_mandir}/man?/*.gz

%changelog
