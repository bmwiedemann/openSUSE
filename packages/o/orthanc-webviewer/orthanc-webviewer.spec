#
# spec file for package orthanc-webviewer
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019-2020 Dr. Axel Braun
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


Name:           orthanc-webviewer
Summary:        Web Viewer plugin for Orthanc
License:        AGPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
Version:        2.6
Release:        0
URL:            https://orthanc-server.com
Source0:        https://www.orthanc-server.com/downloads/get.php?path=/plugin-webviewer/OrthancWebViewer-%{version}.tar.gz
Source1:        cornerstone-0.11.0.zip
Source2:        jquery-ui-1.11.3.zip
Source3:        jsPanel-2.3.3-fixed.zip
Source4:        pako-0.2.5.zip
Source5:        js-url-1.8.6.zip
Source11:       orthanc-webviewer-readme.SUSE
Source12:       webviewer.json
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  googletest-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libboost_date_time-devel >= 1.66
BuildRequires:  libboost_filesystem-devel >= 1.66
BuildRequires:  libboost_locale-devel >= 1.66
BuildRequires:  libboost_regex-devel >= 1.66
BuildRequires:  libboost_system-devel >= 1.66
BuildRequires:  libboost_thread-devel >= 1.66
BuildRequires:  libuuid-devel
BuildRequires:  orthanc-devel
BuildRequires:  orthanc-gdcm
BuildRequires:  orthanc-source
BuildRequires:  sqlite3-devel
BuildRequires:  unzip

Requires:       orthanc

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Webviewer plugin for Orthanc

%prep
%setup -q -n OrthancWebViewer-%{version}

#OrthanPlugin may ask for additional files to be loaded
#Putting them into this folder prevents download of sources from the web
mkdir ThirdPartyDownloads
cd ThirdPartyDownloads
cp %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} .

%build

%cmake .. \
       -DALLOW_DOWNLOADS=OFF \
       -DUSE_SYSTEM_GOOGLE_TEST=ON \
       -DUSE_SYSTEM_ORTHANC_SDK=ON \
       -DORTHANC_FRAMEWORK_SOURCE=path \
       -DBoost_NO_BOOST_CMAKE=ON \
       -DORTHANC_FRAMEWORK_ROOT=/usr/src/orthanc/ \
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
ln -s ../../../..%{_libdir}/share/orthanc/plugins/libOrthancWebViewer.so.%{version} \
      %{buildroot}%{_prefix}/share/orthanc/plugins/libOrthancWebViewer.so

rm %{buildroot}%{_libdir}/share/orthanc/plugins/*.so

cp %{S:11} %{S:12} %{buildroot}%{_docdir}/orthanc/.

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
