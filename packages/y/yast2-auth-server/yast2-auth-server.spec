#
# spec file for package yast2-auth-server
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


Name:           yast2-auth-server
Group:          System/YaST
Summary:        A tool for creating identity management server instances
Version:        4.6.1
Release:        0
License:        GPL-2.0-or-later
URL:            https://github.com/yast/yast-auth-server

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)

Requires:       net-tools
Requires:       yast2
Requires:       yast2-ruby-bindings

BuildArch:      noarch

%description
The program assists system administrators to create new directory server and
Kerberos server instances that help to maintain centralised user identity
database for a network.

%prep
%setup -q

%build

%install
%yast_install
%yast_metainfo

%files
%doc %{yast_docdir}
%{yast_libdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_clientdir}
%{yast_icondir}
%license COPYING

%changelog
