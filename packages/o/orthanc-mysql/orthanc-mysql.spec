#
# spec file for package orthanc-mysql
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 Dr. Axel Braun
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


Name:           orthanc-mysql
Summary:        Database plugin for Orthanc
License:        AGPL-3.0-or-later
Group:          Productivity/Databases/Tools
Version:        3.0
Release:        0
URL:            http://orthanc-server.com
Source0:        https://www.orthanc-server.com/downloads/get.php?path=/plugin-mysql/OrthancMySQL-%{version}.tar.gz
Source1:        orthanc-mysql-readme.openSUSE
Source2:        mysql.json
BuildRequires:  cmake
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  googletest-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libboost_date_time-devel >= 1.66
BuildRequires:  libboost_filesystem-devel >= 1.66
BuildRequires:  libboost_iostreams-devel >= 1.66
BuildRequires:  libboost_locale-devel >= 1.66
BuildRequires:  libboost_regex-devel >= 1.66
BuildRequires:  libboost_system-devel >= 1.66
BuildRequires:  libboost_thread-devel >= 1.66
BuildRequires:  libcurl-devel
BuildRequires:  libmysqld-devel
BuildRequires:  openssl-devel
BuildRequires:  orthanc-devel
BuildRequires:  orthanc-source
BuildRequires:  unzip
BuildRequires:  uuid-devel
BuildRequires:  zlib-devel

Requires:       mariadb
Requires:       orthanc

%description
MySQL/mariadb Database plugin for Orthanc, replaces SQLite database

%prep
%setup -q -n OrthancMySQL-%{version}

%build

%cmake ../MySQL \
       -DALLOW_DOWNLOADS=ON \
       -DUSE_SYSTEM_GOOGLE_TEST=ON \
       -DUSE_SYSTEM_ORTHANC_SDK=ON \
       -DORTHANC_FRAMEWORK_SOURCE=path \
       -DORTHANC_FRAMEWORK_ROOT=/usr/src/orthanc/OrthancFramework/Sources \
       -DBoost_NO_BOOST_CMAKE=ON \
       -DLIB_INSTALL_DIR=%{_libdir}/share/orthanc/plugins/

%cmake_build %{?_smp_mflags}

%install

mkdir -p -m 755 %{buildroot}%{_docdir}/orthanc

%cmake_install

# architecture dependet files should not be in /usr/share... 
# create a directory
mkdir -p -m 755 %{buildroot}%{_libdir}/share/orthanc/plugins

mv %{buildroot}%{_prefix}/share/orthanc/plugins/*.so* %{buildroot}%{_libdir}/share/orthanc/plugins/.

#Link from lib64 to orthanc plugin-directory, where it is expected
ln -s ../../../..%{_libdir}/share/orthanc/plugins/libOrthancMySQLIndex.so.%{version} \
      %{buildroot}%{_prefix}/share/orthanc/plugins/libOrthancMySQLIndex.so

ln -s ../../../..%{_libdir}/share/orthanc/plugins/libOrthancMySQLStorage.so.%{version} \
      %{buildroot}%{_prefix}/share/orthanc/plugins/libOrthancMySQLStorage.so

rm %{buildroot}%{_libdir}/share/orthanc/plugins/*.so

cp %{S:1} %{S:2} %{buildroot}%{_docdir}/orthanc/.

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%dir %{_docdir}/orthanc
%{_docdir}/orthanc/*
%dir %{_libdir}/share
%dir %{_libdir}/share/orthanc
%dir %{_libdir}/share/orthanc/plugins
%{_libdir}/share/orthanc/plugins/*.so*
%dir %{_prefix}/share/orthanc
%dir %{_prefix}/share/orthanc/plugins
%{_prefix}/share/orthanc/plugins/*.so*

%changelog
