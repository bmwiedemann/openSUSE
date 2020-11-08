#
# spec file for package orthanc-framework
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

%define modname orthanc
Name:           orthanc-framework
Version:        1.7.1
Release:        0
Summary:        Header and source files of a specific Orthanc-version
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Visualization/Other
URL:            https://www.orthanc-server.com/
Source0:        https://www.orthanc-server.com/downloads/get.php?path=/orthanc/Orthanc-%{version}.tar.gz
BuildArch:      noarch

%description
This is a package to provide include dirs and sources of a specific 
orthanc-version to build plugins. 

Unfortunately the plugin development goes not in line with orthanc development.

As a consequence, plugins mostly do not build against latest orthanc version.
In order to not mess around with a specific orthanc source package in each 
plugin, this package was created

%package -n %{name}-devel
Summary:        Header and source files for creating Orthanc plugins
Group:          Development/Libraries/C and C++
Provides:       orthanc-static = %{version}-%{release} 
Provides:       orthanc-devel = %version
Obsoletes:      orthanc-devel < %version

%description -n %{name}-devel
This package includes the header files to develop C/C++ plugins for Orthanc.
  
%package    source
Summary:        This package includes the source files for Orthanc
Group:          Development/Sources
Provides:       orthanc-source = %version
Obsoletes:      orthanc-source < %version

%description source
This package includes the source files for Orthanc. Use it in conjunction with 
the -devel package

%prep
%setup -q -n Orthanc-%{version}

##setup source directory
mkdir -p -m 755 %{buildroot}/usr/src/%{modname}
# Copy sources
tar --strip-components 1 -xzf %{S:0} -C %{buildroot}/usr/src/%{modname}/
#...and delete dot files
rm %{buildroot}/usr/src/%{modname}/.hg*
rm %{buildroot}/usr/src/%{modname}/.travis*

#includedir festlegen
mkdir -p -m 755 %{buildroot}%{_includedir}/orthanc
cp %{buildroot}/usr/src/%{modname}/Plugins/Include/orthanc/* %{buildroot}%{_includedir}/orthanc/.

%files
%doc AUTHORS NEWS README TODO 
%license COPYING

%files -n orthanc-framework-devel
%dir %{_includedir}/orthanc
%{_includedir}/orthanc/*

%files source
%defattr(-,root,root)
%dir /usr/src/%{modname}
/usr/src/%{modname}/*

%changelog
