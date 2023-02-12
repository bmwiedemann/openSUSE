#
# spec file for package yast2-iscsi-client
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


Name:           yast2-iscsi-client
Version:        4.5.7
Release:        0
Summary:        YaST2 - iSCSI Client Configuration
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-iscsi-client
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  update-desktop-files
# Yast2::Systemd::Socket
BuildRequires:  yast2 >= 4.1.3
# needed for test of finish client which include installation/misc
BuildRequires:  yast2-installation
BuildRequires:  yast2-devtools >= 4.4.0
BuildRequires:  yast2-packager
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
# Yast2::Systemd::Socket
Requires:       yast2 >= 4.1.3
Requires:       yast2-packager
Requires:       yast2-ruby-bindings >= 3.1.7
Supplements:    autoyast(iscsi-client)
BuildArch:      noarch

%description
This package contains the YaST2 component for configuration of an iSCSI
client.

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
%yast_metainfo

%files
%license COPYING
%doc %{yast_docdir}
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}
%{yast_schemadir}
%{yast_icondir}
%{yast_libdir}

%changelog
