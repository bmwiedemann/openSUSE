#
# spec file for package yast2-ycp-ui-bindings
#
# Copyright (c) 2024 SUSE LLC
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


%define min_yui_version	4.3.0
%define yui_so		16

Name:           yast2-ycp-ui-bindings
Version:        5.0.1
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

Group:          System/YaST
License:        GPL-2.0-only

BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  yast2-devtools >= 3.1.10

# autodocs + docbook docs
BuildRequires:  doxygen
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt
BuildRequires:  sgml-skel

Requires:       yast2-core
BuildRequires:  yast2-core-devel

BuildRequires:  libyui-devel >= %min_yui_version
Requires:       libyui%yui_so >= %min_yui_version

# libyui ImplPtr
BuildRequires:  boost-devel

Summary:        YaST2 - YCP Bindings for the YaST2 User Interface Engine

%description
This package makes the generic YaST2 user interface engine available
for YCP applications (YCP is the scripting language in which most YaST2
modules are written).

%package devel
Requires:       yast2-ycp-ui-bindings = %version
Group:          Development/Libraries

Summary:        YaST2 - YCP Bindings for the YaST2 User Interface Engine

Requires:       boost-devel
Requires:       glibc-devel
Requires:       libstdc++-devel
Requires:       libyui-devel >= %min_yui_version
Requires:       yast2-core-devel
Requires:       yast2-devtools

%description devel
This is the development package that makes the generic YaST2 user
interface engine available for YCP applications (YCP is the scripting
language in which most YaST2 modules are written).

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

mkdir -p "$RPM_BUILD_ROOT"%{yast_logdir}
%perl_process_packlist

%files
%defattr(-,root,root)

%dir %{_libdir}/YaST2
%dir %{yast_plugindir}

%{yast_plugindir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{yast_plugindir}/lib*.so
%{yast_plugindir}/lib*.la
%{yast_includedir}
%{_libdir}/pkgconfig/yast2-ycp-ui-bindings.pc
%doc %{yast_docdir}
%license COPYING

%changelog
