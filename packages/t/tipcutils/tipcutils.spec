#
# spec file for package tipcutils
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           tipcutils
Version:        3.0.6
Release:        0
Summary:        Transparent Inter Process Communication Protocol
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://sourceforge.net/projects/tipc/files/tipc-utils
Source0:        https://downloads.sourceforge.net/project/tipc/tipcutils_%{version}.tgz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libdaemon)
BuildRequires:  pkgconfig(libmnl)
BuildRequires:  pkgconfig(libnl-3.0)

%description
TIPC utilities (tipcutils) is a set of userspace programs used to
configure and manage TIPC (http://tipc.sourceforge.net/).

The Transparent Inter Process Communication protocol allows
applications in a clustered computer environment to communicate quickly
and reliably with other applications, regardless of their location
within the cluster.

%prep
%autosetup -p1 -n %{name}

%build
# Force autoreconf if libtool is oldest
if [ -f libtool ]; then
    libtool_ver=$(libtool --version | head -n 1 | awk '{print $NF}')
    used_ver=$(cat libtool | grep "^macro_version=*.*.*" | cut -d "=" -f 2)
    if [ "$libtool_ver" = "$((echo "$libtool_ver"; echo "$used_ver") | sort -V | head -n1)" ]; then
        echo "libtool is on oldest version: need to force the reconf!"
        autoreconf --force --install
    else
        ./bootstrap
    fi
else
    ./bootstrap
fi
%configure
%make_build clean
%make_build

%install
%make_install

%files
%{_sbindir}/tipc-link-watcher
%{_sbindir}/tipclog
%{_bindir}/tipc-pipe
%{_bindir}/tipc-trace
%{_mandir}/man1/tipc-pipe.1%{ext_man}

%changelog
