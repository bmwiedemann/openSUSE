#
# spec file for package rubygem-websocket-extensions
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


Name:           rubygem-websocket-extensions
Version:        0.1.5
Release:        0
%define mod_name websocket-extensions
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/faye/websocket-extensions-ruby
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Generic extension manager for WebSocket connections
License:        Apache-2.0
Group:          Development/Languages/Ruby

%description
Generic extension manager for WebSocket connections.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LICENSE.md README.md" \
  -f

%gem_packages

%changelog
