#
# spec file for package yast2-iscsi-lio-server
#
# Copyright (c) 2022 SUSE LLC
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


Name:           yast2-iscsi-lio-server
Version:        4.5.1
Release:        0
Summary:        Configuration of iSCSI LIO target
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-iscsi-lio-server

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
# Yast2::Execute.stdout
BuildRequires:  yast2 >= 4.1.42
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

Requires:       python3-configshell-fb
Requires:       python3-rtslib-fb
Requires:       python3-targetcli-fb
# Yast2::Execute.stdout
Requires:       yast2 >= 4.1.42
Requires:       yast2-ruby-bindings >= 1.0.0

BuildArch:      noarch

%description
This package contains configuration of iSCSI LIO target

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
%{yast_desktopdir}
%{yast_metainfodir}
%doc %{yast_docdir}
%{yast_icondir}
%license COPYING

%changelog
