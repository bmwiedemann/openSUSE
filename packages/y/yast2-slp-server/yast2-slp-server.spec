#
# spec file for package yast2-slp-server
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


Name:           yast2-slp-server
Summary:        YaST2 SLP Daemon Server Configuration
Version:        4.6.0
Release:        0
Group:          System/YaST
License:        GPL-2.0-or-later
URL:            https://github.com/yast/yast-slp-server

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
# CWM::ServiceWidget
BuildRequires:  yast2 >= 4.1.0
# for install task
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)
# testsuite
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
# CWM::ServiceWidget
Requires:       yast2 >= 4.1.0
Requires:       yast2-ruby-bindings >= 1.0.0

Supplements:    autoyast(slp-server)

BuildArch:      noarch

%description
This package contains the YaST2 component for the configuration of an
SLP daemon.

%prep
%setup -q

%check
rake test:unit

%install
%yast_install
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_libdir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}
%{yast_icondir}

%doc %{yast_docdir}
%license COPYING

%build

%changelog
