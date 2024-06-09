#
# spec file for package orthanc-neuro
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2022-2024 Dr. Axel Braun <DocB@opensuse.org>
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


Name:           orthanc-neuro
Summary:        Neuroimaging plugin for Orthanc
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
Version:        1.1
Release:        0
URL:            http://orthanc-server.com
Source0:        https://orthanc.uclouvain.be/downloads/sources/%{name}/OrthancNeuro-%{version}.tar.gz
Source10:       https://orthanc.uclouvain.be/downloads/third-party-downloads/nifti_clib-3.0.0.tar.gz

Source20:       orthanc-neuro-readme.openSUSE

Patch0:         cassert.diff

BuildRequires:  cmake
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
BuildRequires:  libuuid-devel
BuildRequires:  orthanc-devel
BuildRequires:  orthanc-source
BuildRequires:  unzip
BuildRequires:  zlib-devel

Requires:       orthanc

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Plugin to import data from The Cancer Image Archive

%prep
%autosetup -p2 -n OrthancNeuro-%{version}

#OrthancPlugins may ask for additional files to be loaded
#Putting them into this folder prevents download of sources from the web
mkdir ThirdPartyDownloads
cp %{S:10} ThirdPartyDownloads/.

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
ln -s ../../../..%{_libdir}/share/orthanc/plugins/libOrthancNeuro.so.%{version} \
      %{buildroot}%{_prefix}/share/orthanc/plugins/libOrthancNeuro.so

rm %{buildroot}%{_libdir}/share/orthanc/plugins/*.so

cp %{S:20} %{buildroot}%{_docdir}/orthanc/.

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
