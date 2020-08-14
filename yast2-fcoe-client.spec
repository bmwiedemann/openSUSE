#
# spec file for package yast2-fcoe-client
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


Name:           yast2-fcoe-client
Version:        4.3.0
Release:        0
Summary:        YaST2 - Configuration of Fibre Channel over Ethernet
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://github.com/yast/yast-fcoe-client

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)

# Yast2::Systemd::Service
Requires:       fcoe-utils
Requires:       yast2 >= 4.1.3
Requires:       yast2-ruby-bindings >= 1.0.0

Supplements:    autoyast(fcoe-client)

BuildArch:      noarch

%description
This package contains the YaST2 component for the Fibre Channel over
Ethernet (FCoE) configuration.

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}
%doc %{yast_docdir}
%{yast_icondir}
%license COPYING

%changelog
