#
# spec file for package yast2-http-server
#
# Copyright (c) 2021 SUSE LLC
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


Name:           yast2-http-server
Version:        4.4.1
Release:        0
Summary:        YaST2 - HTTP Server Configuration
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-http-server
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  libxslt
BuildRequires:  libzio
BuildRequires:  perl-XML-Writer
BuildRequires:  popt-devel
BuildRequires:  sgml-skel
BuildRequires:  update-desktop-files
# Yast2::ServiceWidget
BuildRequires:  yast2 >= 4.1.0
BuildRequires:  yast2-devtools >= 4.4.0
BuildRequires:  yast2-network
BuildRequires:  yast2-packagemanager-devel
BuildRequires:  yast2-perl-bindings
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
Requires:       libzio
# Yast2::ServiceWidget
Requires:       yast2 >= 4.1.0
Requires:       yast2-network
Requires:       yast2-perl-bindings
Requires:       yast2-ruby-bindings >= 1.0.0
Supplements:    autoyast(http-server)
BuildArch:      noarch

%description
This package contains the YaST2 component for HTTP server (Apache2)
configuration.

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

%files
%license COPYING
%{yast_schemadir}
%{yast_yncludedir}
%{yast_libdir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}
%{yast_agentdir}
%{yast_icondir}

%changelog
