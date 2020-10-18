#
# spec file for package yast2-apparmor
#
# Copyright (c) 2020 SUSE LLC
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


Name:           yast2-apparmor
Version:        4.3.1
Release:        0
Summary:        YaST2 - Plugins for AppArmor Profile Management
License:        GPL-2.0-only
Group:          Productivity/Security
URL:            https://github.com/yast/yast-apparmor

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

#for install task
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

# Yast::Execute.locally!
Requires:       yast2 > 3.3.2
Requires:       yast2-ruby-bindings >= 1.0.0

# New JSON output format in aa-status; upstream change:
# aa-status: split profile from exec name
# bsc#1121274 / PR#35, bsc#1123258 / PR#36
Conflicts:      apparmor-utils < 2.12

BuildArch:      noarch

%description
YaST2 forms and components for the management of AppArmor
profiles.

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
%{yast_yncludedir}
%{yast_libdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING

%changelog
