#
# spec file for package yast2-transfer
#
# Copyright (c) 2023 SUSE LLC
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


Name:           yast2-transfer
Version:        4.5.1
Release:        0
Summary:        YaST2 - Agent for Various Transfer Protocols
License:        GPL-2.0-only
Group:          System/YaST
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  curl-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-core-devel
BuildRequires:  yast2-devtools >= 4.4.0
Requires:       curl
Requires:       yast2-ruby-bindings >= 1.0.0
Provides:       yast2-agent-curl
Provides:       yast2-agent-curl-devel
Provides:       yast2-agent-tftp
Provides:       yast2-agent-tftp-devel
Obsoletes:      yast2-agent-curl
Obsoletes:      yast2-agent-curl-devel
Obsoletes:      yast2-agent-tftp
Obsoletes:      yast2-agent-tftp-devel
Obsoletes:      yast2-transfer-devel-doc
%if 0%{?suse_version} < 1220
BuildRequires:  libxcrypt-devel
%endif

%description
A YaST2 Agent for various Transfer Protocols: FTP, HTTP, and TFTP.

%prep
%setup -q

%build
%yast_build

%install
%yast_install

rm -f %{buildroot}/%{yast_plugindir}/libpy2ag_curl.la
rm -f %{buildroot}/%{yast_plugindir}/libpy2ag_tftp.la

%files
%license COPYING
%{yast_scrconfdir}/*.scr
%{yast_plugindir}/libpy2ag_curl.so.*
%{yast_plugindir}/libpy2ag_curl.so
%{yast_plugindir}/libpy2ag_tftp.so.*
%{yast_plugindir}/libpy2ag_tftp.so
%{yast_moduledir}/*

%changelog
