#
# spec file for package orthanc-postgresql
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Dr. Axel Braun
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

Name:           orthanc-postgresql
Summary:        Database plugin for Orthanc
License:        AGPL-3.0-or-later
Group:          Productivity/Databases/Tools
Version:        3.2
Release:        0
Url:            https://orthanc-server.com
Source0:        https://www.orthanc-server.com/downloads/get.php?path=/plugin-postgresql/OrthancPostgreSQL-%{version}.tar.gz
Source1:        orthanc-postgresql-readme.SUSE
Source2:        postgresql.json
Patch0:         psql114.patch
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  e2fsprogs-devel
BuildRequires:  googletest-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libboost_date_time-devel >= 1.66
BuildRequires:  libboost_filesystem-devel >= 1.66
BuildRequires:  libboost_locale-devel >= 1.66
BuildRequires:  libboost_regex-devel >= 1.66
BuildRequires:  libboost_system-devel >= 1.66
BuildRequires:  libboost_thread-devel >= 1.66
BuildRequires:  openssl-devel
BuildRequires:  orthanc-devel
BuildRequires:  orthanc-source
BuildRequires:  postgresql-devel
#Tumbleweed
%if 0%{?suse_version} >= 1550
BuildRequires:  postgresql-server-devel
%endif
BuildRequires:  unzip
BuildRequires:  uuid-devel
BuildRequires:  zlib-devel

Requires:       orthanc
Requires:       postgresql-server

BuildRoot:      OrthancPostgreSQL-%{version}-build

%description
PostgreSQL Database plugin for Orthanc, replaces SQLite database

%prep
%setup -q -n OrthancPostgreSQL-%{version}
%patch0 -p2

%build

%cmake ../PostgreSQL \
       -DALLOW_DOWNLOADS=ON \
       -DUSE_SYSTEM_GOOGLE_TEST=ON \
       -DUSE_SYSTEM_ORTHANC_SDK=ON \
       -DORTHANC_FRAMEWORK_SOURCE=path \
       -DORTHANC_FRAMEWORK_ROOT=/usr/src/orthanc/ \
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
ln -s ../../../..%{_libdir}/share/orthanc/plugins/libOrthancPostgreSQLIndex.so.%{version} \
      %{buildroot}%{_prefix}/share/orthanc/plugins/libOrthancPostgreSQLIndex.so
      
ln -s ../../../..%{_libdir}/share/orthanc/plugins/libOrthancPostgreSQLStorage.so.%{version} \
      %{buildroot}%{_prefix}/share/orthanc/plugins/libOrthancPostgreSQLStorage.so

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
