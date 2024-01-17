#
# spec file for package yast2-caasp
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


Name:           yast2-caasp
Version:        4.6.0
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

# SystemRoleHandlersRunner
Requires:       yast2
BuildRequires:  yast2
# Overview widget
Requires:       yast2-installation >= 3.2.38
BuildRequires:  yast2-installation >= 3.2.38
# chrony support
Requires:       yast2-ntp-client   >= 4.0.3
BuildRequires:  yast2-ntp-client   >= 4.0.3
# Drop Yast::LanItems
Requires:       yast2-network      >= 4.4.7
BuildRequires:  yast2-network      >= 4.4.7

BuildRequires:  yast2-devtools     >= 3.1.39
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake) >= 0.2.13

BuildArch:      noarch

Summary:        YaST2 - CaaSP Module
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-caasp

%description
Containers as a Service Platform (CaaSP) and openSUSE Kubic specific module.

%prep
%setup -n %{name}-%{version}

%build

%check
%yast_check

%install
%yast_install

%files
%defattr(-,root,root)
%{yast_clientdir}/*.rb
%dir %{yast_libdir}/y2caasp
%{yast_libdir}/y2caasp/*.rb
%dir %{yast_libdir}/y2caasp/cfa
%{yast_libdir}/y2caasp/cfa/*.rb
%dir %{yast_libdir}/y2caasp/widgets
%{yast_libdir}/y2caasp/widgets/*.rb
%dir %{yast_libdir}/y2caasp/clients
%{yast_libdir}/y2caasp/clients/*.rb
%dir %{yast_libdir}/y2system_role_handlers
%{yast_libdir}/y2system_role_handlers/*.rb
%doc %{yast_docdir}
%license COPYING

%changelog
