#
# spec file for package yast2-sudo
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


Name:           yast2-sudo
Summary:        YaST2 - Sudo configuration
License:        GPL-2.0-only
Group:          System/YaST
Version:        4.3.0
Release:        0
URL:            https://github.com/yast/yast-sudo

Source0:        %{name}-%{version}.tar.bz2

Requires:       yast2-users
# Wizard::SetDesktopTitleAndIcon
Requires:       yast2 >= 2.21.22
Requires:       yast2-ruby-bindings >= 1.0.0

BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-users
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

BuildArch:      noarch

%description
The YaST2 component for sudo configuration. It configures capabilities
of users to run commands as root or other user.

%prep
%setup -n %{name}-%{version}

%check
rake test:unit

%build

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
%{yast_agentdir}
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING

%changelog
