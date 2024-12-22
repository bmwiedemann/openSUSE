#
# spec file for package orthanc-wsi
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


Name:           orthanc-wsi
Summary:        Whole Slide Imaging for Orthanc
License:        AGPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
Version:        3.0
Release:        0
URL:            https://orthanc-server.com
Source0:        https://orthanc.uclouvain.be/downloads/sources/%{name}/OrthancWSI-%{version}.tar.gz
Source1:        openlayers-3.19.0-dist.zip
Source11:       orthanc-wsi-readme.SUSE

BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  dcmtk
BuildRequires:  dcmtk-devel
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150200
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  jsoncpp-devel
BuildRequires:  libboost_date_time-devel >= 1.66
BuildRequires:  libboost_filesystem-devel >= 1.66
BuildRequires:  libboost_iostreams-devel >= 1.66
BuildRequires:  libboost_locale-devel >= 1.66
BuildRequires:  libboost_program_options-devel >= 1.66
BuildRequires:  libboost_regex-devel >= 1.66
BuildRequires:  libboost_system-devel >= 1.66
BuildRequires:  libboost_thread-devel >= 1.66
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libuuid-devel
# Check was missing:
BuildRequires:  libxml2-devel
BuildRequires:  tcpd-devel
# Check was missing - end
BuildRequires:  openjpeg2-devel
BuildRequires:  openssl-devel
BuildRequires:  orthanc-devel
BuildRequires:  orthanc-source
BuildRequires:  unzip

Requires:       orthanc

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Orthanc project provides three official tools to support DICOM for whole-slide microscopic imaging (WSI):
- A so-called “DICOM-izer” command-line tool that converts whole-slide images to DICOM series, following Supplement 145.
- A plugin that extends Orthanc with a Web viewer of whole-slide images for digital pathology.
- Another command-line tool that converts a DICOM series stored inside Orthanc, to a standard hierarchical TIFF image.

%prep
%autosetup -n OrthancWSI-%{version}

#OrthanPlugin may ask for additional files to be loaded
#Putting them into this folder prevents download of sources from the web

mkdir ViewerPlugin/ThirdPartyDownloads
cp %{S:1} ViewerPlugin/ThirdPartyDownloads/.

%build
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150200
export CC=gcc-13
export CXX=g++-13
%endif
# build the applications
cd Applications

%cmake .. \
       -DALLOW_DOWNLOADS=OFF \
       -DUSE_SYSTEM_ORTHANC_SDK=ON \
       -DORTHANC_FRAMEWORK_SOURCE=path \
       -DBoost_NO_BOOST_CMAKE=ON \
       -DORTHANC_FRAMEWORK_ROOT=/usr/src/orthanc/OrthancFramework/Sources \
       -DLIB_INSTALL_DIR=%{_libdir}/share/orthanc/plugins/

%cmake_build %{?_smp_mflags}

#and the plugins
cd ../../ViewerPlugin

%cmake .. \
       -DALLOW_DOWNLOADS=OFF \
       -DUSE_SYSTEM_ORTHANC_SDK=ON \
       -DORTHANC_FRAMEWORK_SOURCE=path \
       -DBoost_NO_BOOST_CMAKE=ON \
       -DORTHANC_FRAMEWORK_ROOT=/usr/src/orthanc/OrthancFramework/Sources \
       -DLIB_INSTALL_DIR=%{_libdir}/share/orthanc/plugins/

%cmake_build %{?_smp_mflags}

%install
cd Applications
%cmake_install
cd ../ViewerPlugin
%cmake_install

# architecture dependet files should not be in /usr/share...
# create a directory
mkdir -p -m 755 %{buildroot}%{_libdir}/share/orthanc/plugins
mkdir -p -m 755 %{buildroot}%{_docdir}/orthanc

mv %{buildroot}%{_prefix}/share/orthanc/plugins/*.so* %{buildroot}%{_libdir}/share/orthanc/plugins/.

#Link from lib64 to orthanc plugin-directory, where it is expected
ln -s ../../../..%{_libdir}/share/orthanc/plugins/libOrthancWSI.so.%{version} \
      %{buildroot}%{_prefix}/share/orthanc/plugins/libOrthancWSI.so

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
%{_bindir}/OrthancWSIDicomizer
%{_bindir}/OrthancWSIDicomToTiff

%changelog
