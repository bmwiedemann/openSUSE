#
# spec file for package yast2-support
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


Name:           yast2-support
Summary:        YaST2 - Support Inquiries
Version:        4.6.0
Release:        0
URL:            https://github.com/yast/yast-support
Group:          System/YaST
License:        GPL-2.0-only

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)

BuildArch:      noarch

# Yast::CoreExt::AnsiString
Requires:       yast2-ruby-bindings >= 3.1.36
Requires:       yast2

Supplements:    autoyast(support)

%description
This module allows you to collect system information for installation
support in a standardized format.

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
%{yast_clientdir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING

%changelog
