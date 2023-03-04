#
# spec file for package yast2-instserver
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


Name:           yast2-instserver
Version:        4.6.0
Release:        0
Summary:        YaST2 - Installation Server Configuration and Management
URL:            https://github.com/yast/yast-instserver
Group:          System/YaST
License:        GPL-2.0-or-later

Source0:        %{name}-%{version}.tar.bz2
Source1:        inst_server.conf.in

BuildRequires:  update-desktop-files
# Yast2::Systemd::Socket
BuildRequires:  yast2 >= 4.1.3
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)

Requires:       yast2 >= 4.1.3
Requires:       yast2-ruby-bindings >= 1.0.0

# file conflict, move of ag_content
Conflicts:      yast2 <= 3.3.4

Obsoletes:      yast2-instserver-devel-doc

BuildArch:      noarch

%description
This package allows you to configure an installation server suitable
for installaing SUSE Linux over the network. Currently FTP, HTTP and
NFS sources are supported.

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
install -D %{SOURCE1} %{buildroot}/etc/apache2/conf.d/inst_server.conf.in
mkdir -p %{buildroot}/etc/YaST2/instserver
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}
%{yast_agentdir}
%{_sysconfdir}/YaST2/instserver
%{_sysconfdir}/apache2
%license COPYING
%doc %{yast_docdir}
%{yast_icondir}

%changelog
