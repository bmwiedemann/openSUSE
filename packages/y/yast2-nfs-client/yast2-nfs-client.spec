#
# spec file for package yast2-nfs-client
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           yast2-nfs-client
Version:        4.3.1
Release:        0
Url:            https://github.com/yast/yast-nfs-client
Summary:        YaST2 - NFS Configuration
License:        GPL-2.0-or-later
Group:          System/YaST

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-testsuite
# Yast::Execute.locally
BuildRequires:  yast2 >= 4.1.42
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
#for install task
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)
# path_matching (RSpec argument matcher)
BuildRequires:  yast2-ruby-bindings >= 3.1.31
# Y2Storage::Filesystems::LegacyNfs#configure_from
BuildRequires:  yast2-storage-ng >= 4.2.73
# Unfortunately we cannot move this to macros.yast,
# bcond within macros are ignored by osc/OBS.
%bcond_with yast_run_ci_tests
%if %{with yast_run_ci_tests}
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake-ci)
%endif

# Yast::Execute.locally
BuildRequires:  yast2 >= 4.1.42
#idmapd_conf agent
Requires:       yast2-nfs-common >= 2.24.0
# showmount, #150382, #286300
Recommends:     nfs-client
# Y2Storage::Filesystems::LegacyNfs#configure_from
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       yast2-storage-ng >= 4.2.73

Provides:       yast2-config-network:/usr/lib/YaST2/clients/lan_nfs_client.ycp
Provides:       yast2-config-nfs
Provides:       yast2-config-nfs-devel
Provides:       yast2-trans-nfs

Obsoletes:      yast2-config-nfs
Obsoletes:      yast2-config-nfs-devel
Obsoletes:      yast2-trans-nfs

BuildArch:      noarch

%description
The YaST2 component for configuration of NFS. NFS stands for network
file system access. It allows access to files on remote machines.

%prep
%setup -q

%build

%check
%yast_check

%install
%yast_install
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_moduledir}
%{yast_libdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_icondir}
%doc %{yast_docdir}
%{yast_schemadir}
%license COPYING

%changelog
