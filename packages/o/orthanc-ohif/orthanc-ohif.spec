#
# spec file for package orthanc-ohif
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2023 Dr. Axel Braun <DocB@opensuse.org>
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

Name:           orthanc-ohif
Summary:        OHIF plugin for Orthanc
License:        AGPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
Version:        1.0
Release:        0
URL:            https://orthanc-server.com
Source0:        https://www.orthanc-server.com/downloads/get.php?path=/plugin-ohif/OrthancOHIF-%{version}.tar.gz
Source1:        https://lsb.orthanc-server.com/plugin-ohif/%{version}/dist.zip

BuildRequires:  cmake
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  googletest-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  libboost_date_time-devel >= 1.66
BuildRequires:  libboost_filesystem-devel >= 1.66
BuildRequires:  libboost_iostreams-devel >= 1.66
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
OHIF plugin for Orthanc
The homepage of OHIF can be found at:
https://ohif.org/

%prep
%setup -q -n OrthancOHIF-%{version}

#OrthanPlugins may ask for additional files to be loaded
#Putting them into this folder prevents download of sources from the web
#static assets of the OHIF viewer
mkdir OHIF
unzip %{S:1} -d OHIF

%build

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

mkdir -p -m 755 %{buildroot}%{_docdir}/orthanc-ohif

%cmake_install

# architecture dependent files should not be in /usr/share...
# create a directory

mkdir -p -m 755 %{buildroot}%{_libdir}/share/orthanc/plugins

mv %{buildroot}%{_prefix}/share/orthanc/plugins/*.so* %{buildroot}%{_libdir}/share/orthanc/plugins/.

#orthanc expects the libs in the plugin-directory

ln -s ../../../..%{_libdir}/share/orthanc/plugins/libOrthancOHIF.so.%{version} \
      %{buildroot}%{_prefix}/share/orthanc/plugins/libOrthancOHIF.so

rm %{buildroot}%{_libdir}/share/orthanc/plugins/libOrthancOHIF.so

cp NEWS README %{buildroot}%{_docdir}/orthanc-ohif/.

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSES/*
%dir %{_docdir}/orthanc-ohif
%{_docdir}/orthanc-ohif/*
%dir %{_libdir}/share
%dir %{_libdir}/share/orthanc
%dir %{_libdir}/share/orthanc/plugins
%{_libdir}/share/orthanc/plugins/*.so*
%dir %{_prefix}/share/orthanc
%dir %{_prefix}/share/orthanc/plugins
%{_prefix}/share/orthanc/plugins/*.so*

%changelog
