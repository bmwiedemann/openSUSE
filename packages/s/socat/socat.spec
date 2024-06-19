#
# spec file for package socat
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2010 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           socat
Version:        1.8.0.0
Release:        0
Summary:        Multipurpose relay for bidirectional data transfer
License:        MIT AND SUSE-GPL-2.0-with-openssl-exception
Group:          Productivity/Networking/Other
URL:            http://www.dest-unreach.org/socat/
Source:         http://www.dest-unreach.org/socat/download/%{name}-%{version}.tar.gz
Source1:        %{name}.changes
Source2:        socat-test-dhparam
# TODO: as of 1.8.0.0, test.sh supports "--expect-fail <code>", this should be used
#       instead of ignoring all test failures
Patch1:         socat-ignore-tests-failure-boo1078346.patch
# Support build environments without a TTY
Patch2:         socat-test-without-tty.patch
# FIX from termux , https://bugzilla.suse.com/show_bug.cgi?id=1226459, https://github.com/termux/termux-packages/issues/18645
Patch3:         0004-udp-listen-bind4.patch
BuildRequires:  iputils
BuildRequires:  net-tools
BuildRequires:  openssl-devel
BuildRequires:  procps
BuildRequires:  readline-devel
%if 0%{?suse_version}
BuildRequires:  tcpd-devel
%endif
%if 0%{?suse_version}
BuildRequires:  iproute2
BuildRequires:  netcfg
%endif
%if 0%{?suse_version} >= 1330
BuildRequires:  net-tools-deprecated
%endif

%description
socat is a relay for bidirectional data transfer between two
independent data channels. Each of these data channels may be a file,
pipe, device (serial line etc. or a pseudo terminal), a socket (UNIX,
IP4, IP6 - raw, UDP, TCP), an SSL socket, proxy CONNECT connection, a
file descriptor (stdin etc.), the GNU line editor, a program, or a
combination of two of these.

%package extra
Summary:        Additional scripts for socat
Requires:       %{name} = %{version}

%description extra
This ships the following scripts:
- socat-broker.sh
- socat-chain.sh
- socat-mux.sh

%prep
%autosetup
sed 's|#! %{_bindir}/env bash|#!%{_bindir}/bash|' -i proxyecho.sh readline.sh

%build
# export deterministic BUILD_DATE, format like "__DATE__ __TIME__"
CL_DATE="$(awk -F " - " 'NR==2{print $1;}' %{SOURCE1})"
test -n "$CL_DATE"
export BUILD_DATE="$(LANG=C date --utc -d "${CL_DATE}" +"%{b} %{e} %{Y} %{T}")"
export CFLAGS="%{optflags} -fno-strict-aliasing -DHAVE_SSLv23_client_method -DHAVE_SSLv23_server_method -fno-common"
%configure
%make_build all
mkdir examples
cp -a daemon.sh ftp.sh mail.sh proxyecho.sh readline.sh examples

%install
mkdir -p \
	%{buildroot}/%{_bindir} \
	%{buildroot}/%{_mandir}/man1
%make_install

# avoid expensive dhparam generation on every build with enabled checks
cp %{SOURCE2} testcert.dh

%check
export TERM=ansi
# use a small but safe subset of all tests
sotests="filan consistency stdio fd pipe pipes exec gopen noatime system"
%ifnarch armv6l armv6hl aarch64
# add some more tests for fast machines only
sotests+=" unix"
%endif
# increase socket shutdown timeout, default 0.1 or 0.5 caused sometimes
# random failures on slow machines (armv6l, aarch64)
export OPTS="-t 2"
./test.sh $sotests

%files
%license COPYING COPYING.OpenSSL
%doc BUGREPORTS CHANGES DEVELOPMENT EXAMPLES FAQ FILES PORTING README SECURITY VERSION examples
%{_bindir}/socat
%{_bindir}/socat1
%{_bindir}/procan
%{_bindir}/filan
%{_mandir}/man1/socat.1%{?ext_man}
%{_mandir}/man1/socat1.1%{?ext_man}

%files extra
%{_bindir}/socat-broker.sh
%{_bindir}/socat-chain.sh
%{_bindir}/socat-mux.sh

%changelog
