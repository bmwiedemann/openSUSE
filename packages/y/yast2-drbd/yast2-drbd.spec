#
# spec file for package yast2-drbd
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _fwdefdir %{_libexecdir}/firewalld/services

Name:           yast2-drbd
Version:        4.2.2
Release:        0
Summary:        YaST2 - DRBD Configuration
License:        GPL-2.0-or-later
Group:          System/YaST
Url:            https://github.com/yast/yast-drbd

Source0:        %{name}-%{version}.tar.bz2
Source1:        drbd.firewalld.xml

BuildRequires:  ruby
BuildRequires:  update-desktop-files
# SuSEFirewall2 replaced by Firewalld(fate#323460)
BuildRequires:  firewall-macros
BuildRequires:  yast2 >= 4.0.39
BuildRequires:  yast2-devtools >= 4.2.2

# SuSEFirewall2 replaced by Firewalld(fate#323460)
Requires:       drbd >= 9.0
Requires:       yast2 >= 4.0.39
Requires:       yast2-ruby-bindings >= 1.0.0

BuildArch:      noarch

%description
YaST2 - Configuration of Distributed Replicated Block Devices. With
this module you can configure a distributed storage system, frequently
used on high availability (HA) clusters.

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

mkdir -p %{buildroot}%{_fwdefdir}
install -m 644 %{S:1} %{buildroot}%{_fwdefdir}/drbd.xml

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
%doc %{yast_docdir}
%license COPYING
%dir %{_libexecdir}/firewalld
%dir %{_fwdefdir}
%{_fwdefdir}/drbd.xml
%{yast_icondir}

%changelog
