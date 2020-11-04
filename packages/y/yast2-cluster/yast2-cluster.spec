#
# spec file for package yast2-cluster
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


%define _fwdefdir %{_prefix}/lib/firewalld/services

Name:           yast2-cluster
Version:        4.3.4
Release:        0
Summary:        Configuration of cluster
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-cluster

Source0:        %{name}-%{version}.tar.bz2
Source1:        cluster.firewalld.xml

BuildRequires:  firewall-macros
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)

Requires:       yast2 >= 4.1.3
Requires:       yast2-ruby-bindings >= 1.0.0

Supplements:    autoyast(cluster)

BuildArch:      noarch

%description
-

%prep
%setup -q

%build

%install
%yast_install
%yast_metainfo

install -D -m 0644 %{S:1} %{buildroot}%{_fwdefdir}/cluster.xml

%post
%firewalld_reload

%files
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}
%{yast_agentdir}
%dir %{_prefix}/lib/firewalld
%dir %{_fwdefdir}
%{_fwdefdir}/cluster.xml
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING

%changelog
