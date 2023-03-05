#
# spec file for package yast2-geo-cluster
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


Name:           yast2-geo-cluster
Version:        4.6.0
Release:        0
Summary:        Configuration of booth
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-geo-cluster
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.2.2
# SuSEFirewall2 replaced by Firewalld(fate#323460)
Requires:       autoyast2-installation
Requires:       yast2 >= 4.0.39
Requires:       yast2-ruby-bindings >= 1.0.0
Supplements:    autoyast(geo-cluster)
BuildArch:      noarch

%description
-

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
%{yast_moduledir}
%{yast_desktopdir}
%{yast_scrconfdir}
%{yast_agentdir}
%{yast_schemadir}
%{yast_clientdir}
%{yast_metainfodir}
%{yast_icondir}

%changelog
