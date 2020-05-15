#
# spec file for package yast2-nis-server
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


Name:           yast2-nis-server
Version:        4.3.0
Release:        0
Summary:        YaST2 - Network Information Services (NIS) Server Configuration
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://github.com/yast/yast-nis-server

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2-network
BuildRequires:  yast2-nis-client
# SuSEFirewall2 replaced by firewalld (fate#323460)
BuildRequires:  yast2 >= 4.0.39
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

Requires:       yast2-network
Requires:       yast2-nis-client
# SuSEFirewall2 replaced by firewalld (fate#323460)
Requires:       yast2 >= 4.0.39
Requires:       yast2-ruby-bindings >= 1.0.0

Provides:       yast2-config-nis-server
Provides:       yast2-trans-nis-server

Obsoletes:      yast2-config-nis-server
Obsoletes:      yast2-nis-server-devel-doc
Obsoletes:      yast2-trans-nis-server

BuildArch:      noarch

%description 
The YaST2 component for NIS server configuration. NIS is a service
similar to yellow pages.

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
%{yast_moduledir}
%{yast_clientdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}
%{yast_schemadir}
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING

%changelog
