#
# spec file for package yast2-nfs-server
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


Name:           yast2-nfs-server
Summary:        YaST2 - NFS Server Configuration
Version:        5.0.1
Release:        0
URL:            https://github.com/yast/yast-nfs-server
Group:          System/YaST
License:        GPL-2.0-or-later

Source0:        %{name}-%{version}.tar.bz2

# SuSEFirewall2 replaced by firewalld (fate#323460)
BuildRequires:  yast2 >= 4.0.39
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

# SuSEFirewall2 replaced by firewalld (fate#323460)
Requires:       yast2 >= 4.0.39
Requires:       yast2-nfs-common
Requires:       yast2-ruby-bindings >= 1.0.0

Recommends:     nfs-kernel-server

Supplements:    autoyast(nfs_server)

BuildArch:      noarch

%description
The YaST2 component for configuration of an NFS server. NFS stands for
network file system access. It allows access to files on remote
machines.

%package -n yast2-nfs-common
Summary:        Configuration of NFS, common parts
Group:          System/YaST

%description -n yast2-nfs-common
Common data for the NFS client and server modules

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_clientdir}
%{yast_clientdir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}/etc_exports.scr
%{yast_agentdir}
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING
%{yast_schemadir}

%files -n yast2-nfs-common
%{yast_scrconfdir}/cfg_nfs.scr

%changelog
