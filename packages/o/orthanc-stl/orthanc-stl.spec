#
# spec file for package orthanc-neuro
#
# Copyright (c) 2025 Dr. Axel Braun <DocB@opensuse.org>
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


Name:           orthanc-stl
Summary:        plugin to provide support for DICOM STL in Orthanc
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
Version:        1.2
Release:        0
URL:            http://orthanc-server.com
Source0:        https://orthanc.uclouvain.be/downloads/sources/%{name}/OrthancSTL-%{version}.tar.gz
Source1:        https://orthanc.uclouvain.be/downloads/third-party-downloads/nifti_clib-3.0.0.tar.gz
Source2:        https://orthanc.uclouvain.be/downloads/third-party-downloads/STL/nexus-4.3.zip
Source3:        https://orthanc.uclouvain.be/downloads/third-party-downloads/STL/3DHOP_4.3.zip
Source4:        https://orthanc.uclouvain.be/downloads/third-party-downloads/STL/three-84.js.gz
Source5:        https://orthanc.uclouvain.be/downloads/third-party-downloads/STL/Online3DViewer-0.12.0.tar.gz
Source6:        https://orthanc.uclouvain.be/downloads/linux-standard-base/%{name}/%{version}/dist.zip

BuildRequires:  cmake
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150200
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  googletest-devel
BuildRequires:  dcmtk-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libboost_atomic-devel >= 1.66
BuildRequires:  libboost_date_time-devel >= 1.66
BuildRequires:  libboost_filesystem-devel >= 1.66
BuildRequires:  libboost_iostreams-devel >= 1.66
BuildRequires:  libboost_locale-devel >= 1.66
BuildRequires:  libboost_regex-devel >= 1.66
BuildRequires:  libboost_system-devel >= 1.66
BuildRequires:  libboost_thread-devel >= 1.66
BuildRequires:  libcurl-devel
BuildRequires:  libuuid-devel
BuildRequires:  orthanc-devel
BuildRequires:  orthanc-source
BuildRequires:  python311
BuildRequires:  unzip
BuildRequires:  vtk-devel
BuildRequires:  zlib-devel

Requires:       orthanc

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
plugin to provide support for DICOM STL in Orthanc (Encapsulated 3D Manufacturing Model IODs)

%prep
%autosetup -p2 -n OrthancSTL-%{version}

#OrthancPlugins may ask for additional files to be loaded
#Putting them into this folder prevents download of sources from the web
mkdir ThirdPartyDownloads
cd ThirdPartyDownloads
cp %{S:1} %{S:2} %{S:3} %{S:4} %{S:5} .

cd ..
mkdir -p JavaScriptLibraries/
unzip %{S:6} -d JavaScriptLibraries

%build
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150200
export CC=gcc-13
export CXX=g++-13
%endif

%cmake .. \
       -DALLOW_DOWNLOADS=OFF \
       -DUSE_SYSTEM_GOOGLE_TEST=ON \
       -DUSE_SYSTEM_ORTHANC_SDK=OFF \
       -DSTANDALONE_BUILD=ON \
       -DUSE_SYSTEM_NIFTILIB=OFF \
       -DORTHANC_FRAMEWORK_SOURCE=path \
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
ln -s ../../../..%{_libdir}/share/orthanc/plugins/libOrthancSTL.so.%{version} \
      %{buildroot}%{_prefix}/share/orthanc/plugins/libOrthancSTL.so

rm %{buildroot}%{_libdir}/share/orthanc/plugins/*.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%dir %{_libdir}/share
%dir %{_libdir}/share/orthanc
%dir %{_libdir}/share/orthanc/plugins
%{_libdir}/share/orthanc/plugins/*.so*
%dir %{_prefix}/share/orthanc
%dir %{_prefix}/share/orthanc/plugins
%{_prefix}/share/orthanc/plugins/*.so*

%changelog
