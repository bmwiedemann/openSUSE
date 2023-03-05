#
# spec file for package yast2-alternatives
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


Name:           yast2-alternatives
Version:        4.6.0
Release:        0
Summary:        YaST2 - Manage Update-alternatives switching
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-alternatives
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-ruby-bindings
# For test
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
# For install
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)

%description
A YaST2 module to manage update alternatives switching

%prep
%setup -q

%build

%check
%yast_check

%install
%yast_install
%yast_metainfo

%files
%{yast_clientdir}
%{yast_libdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_icondir}
%license COPYING
%doc README.md

%changelog
