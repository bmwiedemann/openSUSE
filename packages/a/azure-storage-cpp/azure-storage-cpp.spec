#
# spec file for package azure-storage-cpp
#
# Copyright (c) 2021 SUSE LLC
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


%define libname libazurestorage7
Name:           azure-storage-cpp
Version:        7.5.0
Release:        0
Summary:        Microsoft Azure Storage Client SDK for C++
License:        Apache-2.0
URL:            https://azure.github.io/azure-storage-cpp/
Source:         https://github.com/Azure/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.0
BuildRequires:  gcc-c++
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_log-devel
BuildRequires:  libboost_random-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  pkgconfig
BuildRequires:  unittest-cpp-devel
BuildRequires:  pkgconfig(cpprest)
BuildRequires:  pkgconfig(libssl) >= 1.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(uuid)

%description
A client library for working with Microsoft Azure storage services including blobs, files, tables, and queues.
This client library enables working with the Microsoft Azure storage services which include the blob service for storing binary and text data, the file service for storing binary and text data, the table service for storing structured non-relational data, and the queue service for storing messages that may be accessed by a client.

%package devel
Summary:        Devel files for Azure storage services
Requires:       %{libname} = %{version}
Requires:       libboost_chrono-devel
Requires:       libboost_date_time-devel
Requires:       libboost_filesystem-devel
Requires:       libboost_locale-devel
Requires:       libboost_log-devel
Requires:       libboost_random-devel
Requires:       libboost_regex-devel
Requires:       libboost_thread-devel
Requires:       pkgconfig(cpprest)
Requires:       pkgconfig(libssl) >= 1.0
Requires:       pkgconfig(libxml-2.0)
Requires:       pkgconfig(uuid)

%description devel
Development files for working with Microsoft Azure storage services

%package -n %{libname}
Summary:        Microsoft Azure Storage Client SDK for C++

%description -n %{libname}
A client library for working with Microsoft Azure storage services including blobs, files, tables, and queues.
This client library enables working with the Microsoft Azure storage services which include the blob service for storing binary and text data, the file service for storing binary and text data, the table service for storing structured non-relational data, and the queue service for storing messages that may be accessed by a client.

%prep
%setup -q -n %{name}-%{version}/Microsoft.WindowsAzure.Storage/

%build
%cmake \
    -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
# The tests need to connect to azure cloud and do operations -> can't do in OBS

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license ../LICENSE.txt
%{_libdir}/libazurestorage.so.*

%files devel
%dir %{_includedir}/was
%dir %{_includedir}/wascore
%{_includedir}/wascore/*
%{_includedir}/was/*
%{_libdir}/libazurestorage.so

%changelog
