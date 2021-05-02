#
# spec file for package yast2-ftp-server
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


Name:           yast2-ftp-server
Version:        4.4.0
Release:        0
Summary:        YaST2 - FTP configuration
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-ftp-server

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
# Yast2::CommandLine readonly parameter
BuildRequires:  yast2 >= 4.2.57
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

# Yast2::CommandLine readonly parameter
Requires:       yast2 >= 4.2.57
Requires:       yast2-ruby-bindings >= 1.0.0
# Do not log passwords
Requires:       yast2-users >= 4.2.4

Supplements:    autoyast(ftp-server)

BuildArch:      noarch

%description
This package contains the YaST2 component for FTP configuration. It can
configure vsftpd.

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
%{yast_libdir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_schemadir}
%{yast_scrconfdir}
%doc %{yast_docdir}
%license COPYING
%{yast_icondir}

%changelog
