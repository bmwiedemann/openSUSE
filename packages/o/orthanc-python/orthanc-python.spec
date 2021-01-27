#
# spec file for package orthanc-python
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020-2021 Dr. Axel Braun
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

Name:           orthanc-python
Summary:        Python plugin for Orthanc
License:        AGPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
Version:        3.1
Release:        0
URL:            https://orthanc-server.com
Source0:        https://www.orthanc-server.com/downloads/get.php?path=/plugin-python/OrthancPython-%{version}.tar.gz
Source11:       orthanc-python-readme.openSUSE
BuildRequires:  python3-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  jsoncpp-devel
BuildRequires:  libboost_atomic-devel >= 1.66
BuildRequires:  libboost_date_time-devel >= 1.66
BuildRequires:  libboost_filesystem-devel >= 1.66
BuildRequires:  libboost_iostreams-devel >= 1.66
BuildRequires:  libboost_locale-devel >= 1.66
BuildRequires:  libboost_regex-devel >= 1.66
BuildRequires:  libboost_system-devel >= 1.66
BuildRequires:  libboost_thread-devel >= 1.66
BuildRequires:  libuuid-devel
BuildRequires:  orthanc-devel
BuildRequires:  orthanc-source
BuildRequires:  pkgconfig(python3)
BuildRequires:  unzip

Requires:       orthanc

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This plugin can be used to write Orthanc plugins in Python instead of C++
See /usr/share/doc/packages/orthanc/orthanc-python-readme.openSUSE


%prep
%setup -q -n OrthancPython-%{version}

echo %{python3_version}

%build

%cmake .. \
       -DALLOW_DOWNLOADS=OFF \
       -DUSE_SYSTEM_GOOGLE_TEST=ON \
       -DUSE_SYSTEM_ORTHANC_SDK=ON \
       -DORTHANC_FRAMEWORK_SOURCE=path \
       -DBoost_NO_BOOST_CMAKE=ON \
       -DPYTHON_VERSION=%{python3_version} \
       -DORTHANC_FRAMEWORK_ROOT=/usr/src/orthanc/OrthancFramework/Sources \
       -DLIB_INSTALL_DIR=%{_libdir}/share/orthanc/plugins/

%cmake_build %{?_smp_mflags}

%install
%cmake_install

# architecture dependet files should not be in /usr/share... 
# create a directory
mkdir -p -m 755 %{buildroot}%{_libdir}/share/orthanc/plugins
mkdir -p -m 755 %{buildroot}%{_docdir}/orthanc

mv %{buildroot}%{_prefix}/share/orthanc/plugins/*.so* %{buildroot}%{_libdir}/share/orthanc/plugins/.

#Link from lib64 to orthanc plugin-directory, where it is expected
ln -s ../../../..%{_libdir}/share/orthanc/plugins/libOrthancPython.so.%{version} \
      %{buildroot}%{_prefix}/share/orthanc/plugins/libOrthancPython.so

rm %{buildroot}%{_libdir}/share/orthanc/plugins/*.so

cp %{S:11} %{buildroot}%{_docdir}/orthanc/.

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
