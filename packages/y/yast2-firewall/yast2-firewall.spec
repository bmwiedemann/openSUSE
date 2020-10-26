#
# spec file for package yast2-firewall
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


Name:           yast2-firewall
Version:        4.3.8
Release:        0
Summary:        YaST2 - Firewall Configuration
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-firewall

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-testsuite
# Y2Firewall::Firewalld#modified_from_default
BuildRequires:  yast2 >= 4.3.17
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

# Y2Firewall::Firewalld#modified_from_default
Requires:       yast2 >= 4.3.17
Requires:       yast2-ruby-bindings >= 1.0.0

# ButtonBox widget
Conflicts:      yast2-ycp-ui-bindings < 2.17.3
# CpiMitigations
Conflicts:      yast2-bootloader < 4.2.1

Provides:       yast2-config-firewall
Provides:       yast2-trans-firewall

Obsoletes:      yast2-config-firewall
Obsoletes:      yast2-trans-firewall

Supplements:    autoyast(firewall)

BuildArch:      noarch

%description
A YaST2 module to be used for configuring a firewall.

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
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_schemadir}
%{yast_icondir}
%license COPYING
%doc README.md

%changelog
