#
# spec file for package orthanc-dicomweb
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2019-2024 Dr. Axel Braun
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


Name:           orthanc-dicomweb
Summary:        WebViewer plugin for Orthanc
License:        AGPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
Version:        1.17
Release:        0
URL:            https://orthanc-server.com
Source0:        https://orthanc.uclouvain.be/downloads/sources/%{name}/OrthancDicomWeb-%{version}.tar.gz
Source1:        cornerstone.css
Source2:        cornerstone.min.js
Source3:        bootstrap-4.3.1.zip
Source4:        Font-Awesome-4.7.0.tar.gz
Source5:        axios-0.19.0.tar.gz
Source6:        vuejs-2.6.10.tar.gz
Source7:        bootstrap-vue-2.0.0-rc.24-dist.tar.gz
Source8:        babel-polyfill-6.26.0.min.js.gz
Source9:        orthanc-dicomweb-readme.SUSE
Source10:       dicomweb.json
Patch0:         framework.diff

BuildRequires:  cmake
BuildRequires:  e2fsprogs-devel
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150200
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  googletest-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libboost_date_time-devel >= 1.66
BuildRequires:  libboost_filesystem-devel >= 1.66
BuildRequires:  libboost_iostreams-devel >= 1.66
BuildRequires:  libboost_locale-devel >= 1.66
BuildRequires:  libboost_regex-devel >= 1.66
BuildRequires:  libboost_system-devel >= 1.66
BuildRequires:  libboost_thread-devel >= 1.66
BuildRequires:  openssl-devel
BuildRequires:  orthanc-devel
BuildRequires:  orthanc-source
BuildRequires:  pugixml-devel
BuildRequires:  unzip
BuildRequires:  uuid-devel

Requires:       orthanc

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
WebViewer plugin for Orthanc

%prep
%autosetup -p1 -n OrthancDicomWeb-%{version}

#OrthanPlugins may ask for additional files to be loaded
#Putting them into this folder prevents download of sources from the web
mkdir ThirdPartyDownloads
cd ThirdPartyDownloads
cp %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} %{S:6} %{S:7} %{S:8}  .
cd ..

%build
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150200
export CC=gcc-13
export CXX=g++-13
%endif
%cmake ../ \
       -DALLOW_DOWNLOADS=OFF \
       -DUSE_SYSTEM_GOOGLE_TEST=ON \
       -DUSE_SYSTEM_ORTHANC_SDK=ON \
       -DORTHANC_FRAMEWORK_SOURCE=path \
       -DBoost_NO_BOOST_CMAKE=ON \
       -DORTHANC_FRAMEWORK_ROOT=/usr/src/orthanc/OrthancFramework/Sources \
       -DLIB_INSTALL_DIR=%{_libdir}/share/orthanc/plugins/

%cmake_build %{?_smp_mflags}

%install

mkdir -p -m 755 %{buildroot}%{_docdir}/orthanc

%cmake_install

# architecture dependent files should not be in /usr/share...
# create a directory

mkdir -p -m 755 %{buildroot}%{_libdir}/share/orthanc/plugins

mv %{buildroot}%{_prefix}/share/orthanc/plugins/*.so* %{buildroot}%{_libdir}/share/orthanc/plugins/.

#orthanc expects the libs in the plugin-directory

ln -s ../../../..%{_libdir}/share/orthanc/plugins/libOrthancDicomWeb.so.%{version} \
      %{buildroot}%{_prefix}/share/orthanc/plugins/libOrthancDicomWeb.so

rm %{buildroot}%{_libdir}/share/orthanc/plugins/libOrthancDicomWeb.so

cp %{S:1} %{S:9} %{S:10} %{buildroot}%{_docdir}/orthanc/.

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
