#
# spec file for package yast2-proxy
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


Name:           yast2-proxy
Version:        4.6.0
Release:        0
Summary:        YaST2 - Proxy Configuration
License:        GPL-2.0-or-later
Group:          System/YaST
URL:            https://github.com/yast/yast-proxy

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-buildtools >= 4.2.2
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)

Requires:       yast2
Requires:       yast2-ruby-bindings >= 1.0.0

# we split off that one
Conflicts:      yast2-network < 2.22.6

Supplements:    autoyast(proxy)

BuildArch:      noarch

%description
This package contains the YaST2 component for proxy configuration.

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
%yast_metainfo

%files
%{yast_clientdir}
%{yast_libdir}
%{yast_moduledir}
%{yast_yncludedir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}
%{yast_schemadir}
%{yast_icondir}
%license COPYING
%doc %{yast_docdir}

%changelog
