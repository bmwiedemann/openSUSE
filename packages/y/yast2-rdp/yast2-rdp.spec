#
# spec file for package yast2-rdp
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


Name:           yast2-rdp
Version:        4.6.0
Release:        0
License:        GPL-2.0-only
Group:          System/YaST
Summary:        Setup Remote Desktop Protocol service for remote administration
URL:            https://github.com/yast/yast-rdp

Source0:        %{name}-%{version}.tar.bz2

# SuSEFirewall2 replaced by firewalld (fate#323460)
BuildRequires:  yast2 >= 4.0.39
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
# for install task
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)
# for test:unit
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)

# SuSEFirewall2 replaced by firewalld (fate#323460)
Requires:       yast2 >= 4.0.39
Requires:       yast2-ruby-bindings

BuildArch:      noarch

%description
Configure RDP (remote desktop protocol) daemon to allow remote system administration.

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
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_icondir}
%license COPYING
%doc %{yast_docdir}

%changelog
