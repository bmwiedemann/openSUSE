#
# spec file for package rabbitmq-c
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2012-2015 Remi Collet
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


%global libname     librabbitmq
%global majsonum    4
Name:           rabbitmq-c
Version:        0.15.0
Release:        0
Summary:        Client library for AMQP
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://github.com/alanxz/rabbitmq-c
Source0:        https://github.com/alanxz/rabbitmq-c/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# [bsc#1232541], https://github.com/alanxz/rabbitmq-c/issues/846
Patch0:         rabbitmq-c-default-cacert-location.patch
BuildRequires:  cmake > 2.8.12
BuildRequires:  gcc
BuildRequires:  openssl-devel
# For tools
BuildRequires:  popt-devel
# For man page
BuildRequires:  xmlto
# SECTION test requirements
BuildRequires:  rabbitmq-server
BuildRequires:  rabbitmq-server-plugins
# /SECTION

%description
This is a C-language AMQP client library for use with AMQP servers
speaking protocol versions 0-9-1.

%package -n %{libname}%{majsonum}
Summary:        Client library for AMQP
Group:          Development/Libraries/C and C++

%description -n %{libname}%{majsonum}
This is a C-language AMQP client library for use with AMQP servers
speaking protocol versions 0-9-1.

%package -n %{libname}-devel
Summary:        Header files and development libraries for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{majsonum} = %{version}

%description -n %{libname}-devel
This package contains the header files and development libraries
for %{name}.

%package -n %{name}-tools
Summary:        Example tools built using the librabbitmq package
Group:          Development/Libraries/C and C++

%description -n %{name}-tools
This package contains example tools built using %{name}. It provides:
amqp-consume        Consume messages from a queue on an AMQP server
amqp-declare-queue  Declare a queue on an AMQP server
amqp-delete-queue   Delete a queue from an AMQP server
amqp-get            Get a message from a queue on an AMQP server
amqp-publish        Publish a message on an AMQP server

%prep
%autosetup -p1

%build
# static lib required for tests
%cmake \
  -DBUILD_TOOLS_DOCS:BOOL=ON \
  -DBUILD_STATIC_LIBS:BOOL=ON \
  -DBUILD_TOOLS:BOOL=ON
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_libdir}/%{libname}.a

%check
# check .pc is usable
grep @ %{buildroot}%{_libdir}/pkgconfig/librabbitmq.pc && exit 1
# upstream tests
#
# https://github.com/alanxz/rabbitmq-c/issues/602
# rabbitmq-server needs to run only for test_basic,
# which can be skipped in case this will bring some
# issues
exit_code=0
echo "### Starting RabbitMQ server .."
pid_file="/home/abuild/rabbitmq/rabbitmq.pid"
export RABBITMQ_PID_FILE=$pid_file
export RABBITMQ_LOG_BASE=/home/abuild/rabbitmq/log
export RABBITMQ_MNESIA_BASE=/home/abuild/rabbitmq/mnesia
%if 0%{?suse_version} <= 1500
export RABBITMQ_SCHEMA_DIR=/home/abuild/rabbitmq/schema
export RABBITMQ_GENERATED_CONFIG_DIR=/home/abuild/rabbitmq/config
%endif
sbin_base=/usr/lib*/rabbitmq/lib/rabbitmq_server-*/sbin
$sbin_base/rabbitmq-server&
sleep 10
$sbin_base/rabbitmqctl await_startup
if ! $sbin_base/rabbitmqctl ping; then
  # bsc#1198202 - FTBFS: rabbitmq-c won't compile on SP4
  # handle the situation when rabbitmq server will not start
  # in time
  echo '### Server have not managed to start until now, giving up'
  epmd -kill || true
  exit 0
fi
echo "### Done, running tests"
%ctest || exit_code=1
echo "### Stopping RabbitMQ server .."
$sbin_base/rabbitmqctl stop
# needs to wait: Killing not allowed - living nodes in database.
sleep 10
# do not bother when kill won't succeed
epmd -kill || true
echo "### Done"
exit $exit_code

%post -n %{libname}%{majsonum} -p /sbin/ldconfig
%postun -n %{libname}%{majsonum} -p /sbin/ldconfig

%files -n %{libname}%{majsonum}
%license LICENSE
%{_libdir}/%{libname}.so.%{majsonum}
%{_libdir}/%{libname}.so.%{version}

%files -n %{libname}-devel
%doc AUTHORS THANKS *.md examples
%{_libdir}/%{libname}.so
%{_includedir}/amqp*
%{_includedir}/rabbitmq-c
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{libname}.pc

%files -n %{name}-tools
%{_bindir}/amqp-*
%{_mandir}/man1/amqp-*.1%{?ext_man}
%{_mandir}/man7/librabbitmq-tools.7%{?ext_man}

%changelog
