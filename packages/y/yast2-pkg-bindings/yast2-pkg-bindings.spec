#
# spec file for package yast2-pkg-bindings
#
# Copyright (c) 2020 SUSE LLC
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


Name:           yast2-pkg-bindings
Version:        4.3.3
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libxslt
# zypp::VendorAttr API
BuildRequires:  libzypp-devel >= 17.25.0
BuildRequires:  yast2-core-devel
BuildRequires:  yast2-devtools >= 3.1.10

Summary:        YaST2 - Package Manager Access
License:        GPL-2.0-only
Group:          System/YaST

%description
This package contains a name space for accessing the package manager
library in YaST2.

%prep
%setup -n %{name}-%{version}
# build only the library, ignore documentation (it is in devel-doc package)
echo "src" > SUBDIRS

%build
%yast_build

%install
%yast_install

rm -rf %{buildroot}/%{yast_plugindir}/libpy2Pkg.la

%files
%defattr(-,root,root)
%{yast_plugindir}/libpy2Pkg.so.*
%{yast_plugindir}/libpy2Pkg.so
%doc %{yast_docdir}
%license COPYING

%changelog
