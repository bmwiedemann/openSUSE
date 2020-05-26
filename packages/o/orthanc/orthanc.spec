#
# spec file for package orthanc
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


Name:           orthanc
Version:        1.7.0
Release:        0
Summary:        RESTful DICOM server for healthcare and medical research
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Visualization/Other
URL:            http://www.orthanc-server.com/
Source0:        http://www.orthanc-server.com/downloads/get.php?path=/orthanc/Orthanc-%{version}.tar.gz
Source1:        orthanc.service
Source2:        orthanc-readme.SUSE
Source3:        serve-folders.json
Source4:        worklists.json
Source5:        index.html
Source6:        VersionsTests.cpp
Source7:        orthanc-rpmlintrc
Source8:        Configuration.json
# Sources for plugin - need a defined version, so taking them from orthanc-server
Source10:       http://orthanc.osimis.io/ThirdPartyDownloads/dicom-web/bootstrap-4.3.1.zip
Source11:       http://orthanc.osimis.io/ThirdPartyDownloads/dicom-web/axios-0.19.0.tar.gz 
Source12:       http://orthanc.osimis.io/ThirdPartyDownloads/jquery-3.4.1.min.js
Source13:       http://orthanc.osimis.io/ThirdPartyDownloads/dicom-web/vuejs-2.6.10.tar.gz

BuildRequires:  civetweb-devel
BuildRequires:  cmake >= 2.8.0
BuildRequires:  curl-devel
BuildRequires:  dcmtk
BuildRequires:  dcmtk-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  googletest-devel
BuildRequires:  help2man
BuildRequires:  jsoncpp-devel
BuildRequires:  libboost_date_time-devel >= 1.66
BuildRequires:  libboost_filesystem-devel >= 1.66
BuildRequires:  libboost_locale-devel >= 1.66
BuildRequires:  libboost_regex-devel >= 1.66
BuildRequires:  libboost_system-devel >= 1.66
BuildRequires:  libboost_thread-devel >= 1.66
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libuuid-devel
BuildRequires:  libwrap0
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  pugixml-devel
BuildRequires:  sqlite3-devel
BuildRequires:  tcpd-devel
BuildRequires:  unzip
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(lua5.1)
BuildRequires:  pkgconfig(systemd)

Requires:       dcmtk
Requires(pre): 	/usr/sbin/groupadd
Requires(pre): 	/usr/sbin/useradd

%{?systemd_requires}

%description
Orthanc aims at providing a simple, yet powerful standalone DICOM server. 
Orthanc can turn any computer running Windows or Linux into a DICOM store 
(in other words, a mini-PACS system). Its architecture is lightweight, 
meaning that no complex database administration is required, nor the 
installation of third-party dependencies. What makes Orthanc unique 
is the fact that it provides a RESTful API. Thanks to this major 
feature, it is possible to drive Orthanc from any computer language. 

The DICOM tags of the stored medical images can be downloaded in the 
JSON file format. Furthermore, standard PNG images can be generated 
on-the-fly from the DICOM instances by Orthanc. Orthanc lets its 
users focus on the content of the DICOM files, hiding the complexity 
of the DICOM format and of the DICOM protocol. 	

%package -n %{name}-devel
Summary:        Header and source files for creating Orthanc plugins
Group:          Development/Libraries/C and C++
Provides:       orthanc-static = %{version}-%{release} 

%description -n %{name}-devel
This package includes the header files to develop C/C++ plugins for Orthanc.
  
%package -n %{name}-doc
Summary:        Documentation files for Orthanc
Group:          Productivity/Graphics/Visualization/Other
BuildArch:      noarch

%description -n %{name}-doc
This package includes the documentation and the sample codes available 
for Orthanc. 
It also includes the documentation to develop C/C++ plugins for Orthanc.

%package    source
Summary:        This package includes the source files for Orthanc
Group:          Development/Sources

%description source
This package includes the source files for Orthanc. Use it in conjunction with the -devel package

%prep
%setup -q -n Orthanc-%{version}

cp %{S:1} %{S:2} .	

cp %{S:6} UnitTestsSources/.

#slight change in standard configuration for OrthancStorage
cp %{S:8} Resources/.

#OrthanPlugins may ask for additional files to be loaded
#Putting them into this folder prevents download of sources from the web
mkdir -p Plugins/Samples/ConnectivityChecks/ThirdPartyDownloads
cp %{S:10} %{S:11} %{S:12} %{S:13} Plugins/Samples/ConnectivityChecks/ThirdPartyDownloads/.

%build
%cmake	.. \
    -DSTANDALONE_BUILD:BOOL=ON \
    -DSTATIC_BUILD:BOOL=OFF \
    -DENABLE_CIVETWEB=ON \
    -DUSE_SYSTEM_MONGOOSE=OFF \
    -DSYSTEM_MONGOOSE_USE_CALLBACKS=OFF \
    -DUNIT_TESTS_WITH_HTTP_CONNEXIONS=OFF \
    -DBoost_NO_BOOST_CMAKE=ON

%cmake_build %{?_smp_mflags}

# Generate the man page
help2man ./Orthanc -N -n "Lightweight, RESTful DICOM server for healthcare and medical research" > %{name}.1

%check
# we disable one test for i586
%ifarch != ix86
build/UnitTests 
%else
build/UnitTests --gtest_filter=-ImageProcessing.Convolution 
%endif

%install
# install: make some dirs...
mkdir -p -m 755 %{buildroot}
mkdir -p -m 755 %{buildroot}%{_sysconfdir}/%{name}
mkdir -p -m 755 %{buildroot}%{_unitdir}
mkdir -p -m 755 %{buildroot}%{_initddir}
mkdir -p -m 755 %{buildroot}%{_bindir}
mkdir -p -m 755 %{buildroot}%{_sbindir}
mkdir -p -m 755 %{buildroot}%{_libdir}
mkdir -p -m 755 %{buildroot}%{_mandir}
mkdir -p -m 755 %{buildroot}%{_docdir}/%{name}

##setup source directory
mkdir -p -m 755 %{buildroot}/usr/src/%{name}
# Copy sources
tar --strip-components 1 -xzf %{S:0} -C %{buildroot}/usr/src/%{name}/
#...and delete dot files
rm %{buildroot}/usr/src/%{name}/.hg*
rm %{buildroot}/usr/src/%{name}/.travis*

%cmake_install

##move the doc into 
cp -r %{buildroot}/usr/share/doc/%{name}/* %{buildroot}%{_docdir}/%{name}/.
rm -rf %{buildroot}/usr/share/doc/%{name}

install -m 755 -d %{buildroot}%{_mandir}/man1
cp build/%{name}.1 %{buildroot}%{_mandir}/man1

install -m 755 -d %{buildroot}%{_sysconfdir}/%{name}
cp %{S:3} %{buildroot}%{_sysconfdir}/%{name}
cp %{S:4} %{buildroot}%{_sysconfdir}/%{name}
cp %{S:8} %{buildroot}%{_sysconfdir}/%{name}

install -m 755 -d %{buildroot}%{_unitdir}
cp orthanc.service %{buildroot}%{_unitdir}

install -m 755 -d %{buildroot}%{_sharedstatedir}/%{name}/db-v6

# Move the plugins from "/usr/lib64/" to "/usr/lib64/orthanc", and
# remove the symbolic links generated by CMake
mkdir -p %{buildroot}%{_libdir}/%{name}
mv build/*.so.%{version} %{buildroot}%{_libdir}/%{name}
rm build/*.so

# move the executables to stay consistent 
mv %{buildroot}%{_bindir}/OrthancRecoverCompressedFile %{buildroot}%{_bindir}/orthancRecoverCompressedFile
mv %{buildroot}%{_sbindir}/Orthanc %{buildroot}%{_sbindir}/orthanc

# Create symbolic links to plugins in "/usr/share/orthanc/plugins"
# We stick to the "relative symlinks" section of the guideline

rm %{buildroot}%{_prefix}/share/%{name}/plugins/*.so*

ln -s ../../../..%{_libdir}/%{name}/libServeFolders.so.%{version} \
   %{buildroot}%{_prefix}/share/%{name}/plugins/libServeFolders.so
ln -s ../../../..%{_libdir}/%{name}/libModalityWorklists.so.%{version} \
   %{buildroot}%{_prefix}/share/%{name}/plugins/libModalityWorklists.so
ln -s ../../../..%{_libdir}/%{name}/libConnectivityChecks.so.%{version} \
   %{buildroot}%{_prefix}/share/%{name}/plugins/libConnectivityChecks.so

# Prepare documentation: "index.html", Doxygen of plugin SDK, and sample codes
cp -r %{S:5} %{buildroot}%{_docdir}/%{name}/
cp -r Resources/Samples/ %{buildroot}%{_docdir}/%{name}/Samples
cp -r Plugins/Samples/ %{buildroot}%{_docdir}/%{name}/OrthancPluginSamples

%pre 
getent group orthanc >/dev/null || groupadd -r orthanc
getent passwd orthanc >/dev/null || \
    useradd -r -g orthanc -G orthanc -d %{_sharedstatedir}/orthanc -s /sbin/nologin \
    -c "User account that holds information for Orthanc" orthanc

%service_add_pre orthanc.service

%preun 
%service_del_preun orthanc.service

%post 
/sbin/ldconfig
%service_add_post orthanc.service

%postun 
/sbin/ldconfig
%service_del_postun orthanc.service

%files
%doc AUTHORS NEWS README TODO orthanc-readme.SUSE
%license COPYING
%{_mandir}/man1/orthanc.1*
%{_bindir}/orthancRecoverCompressedFile
%{_sbindir}/orthanc
%{_unitdir}/orthanc.service
%{_libdir}/orthanc/*.so.%{version}
%{_prefix}/share/orthanc/plugins/*.so*
%dir %attr(0755, orthanc, orthanc) %{_sysconfdir}/orthanc
%dir %{_libdir}/orthanc
%dir %{_prefix}/share/orthanc
%dir %{_prefix}/share/orthanc/plugins
%defattr(0750, orthanc , orthanc)
%config(noreplace) %{_sysconfdir}/orthanc/*.json
%dir %attr(0755, orthanc, orthanc) %{_sharedstatedir}/orthanc
%dir %attr(0755, orthanc, orthanc) %{_sharedstatedir}/orthanc/db-v6

%files -n orthanc-devel
%dir %{_includedir}/orthanc
%{_includedir}/orthanc/*

%files -n orthanc-doc
%{_docdir}/orthanc/index.html
%{_docdir}/orthanc/Orthanc*
%{_docdir}/orthanc/Samples/*
%dir %attr(0755, orthanc, orthanc) %{_docdir}/orthanc/Samples

%files source
%defattr(-,root,root)
%dir /usr/src/%{name}
/usr/src/%{name}/*

%changelog
