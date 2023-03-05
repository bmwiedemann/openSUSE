#
# spec file for package yast2-audit-laf
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


Name:           yast2-audit-laf
Version:        4.6.0
Release:        0
Summary:        YaST2 - Configuration of Linux Auditing (LAF)
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-audit-laf
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-testsuite
# Wizard::SetDesktopTitleAndIcon
Requires:       yast2 >= 2.21.22
Requires:       yast2-ruby-bindings >= 1.0.0
Supplements:    autoyast(audit-laf)
BuildArch:      noarch

%description
This module allows the configuration of the audit daemon as well as to
add rules for the audit subsystem.

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
%license COPYING
%{yast_schemadir}
%{yast_icondir}

%changelog
