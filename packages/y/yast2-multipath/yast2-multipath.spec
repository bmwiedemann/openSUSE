#
# spec file for package yast2-multipath
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


Name:           yast2-multipath
Version:        4.6.0
Release:        0
Summary:        YaST2 - Multipath Configuration
License:        GPL-2.0-or-later
Group:          System/YaST
URL:            https://github.com/yast/yast-multipath
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.4.0
BuildRequires:  yast2-testsuite
Requires:       yast2
# StorageManager#deactivate
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       yast2-storage-ng >= 3.3.1
BuildArch:      noarch

%description
Multipath I/O is a fault tolerance technique whereby there is more than
one physical path between the CPU in a computer system and its mass
storage devices through the buses, controllers, switches, and bridge
devices connecting them.

You can configure your multipathed devices with this module.

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

%files
%license COPYING
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}
%{yast_agentdir}
%{yast_icondir}

%changelog
