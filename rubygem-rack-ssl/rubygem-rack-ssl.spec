#
# spec file for package rubygem-rack-ssl
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           rubygem-rack-ssl
Version:        1.4.1
Release:        0
%define mod_name rack-ssl
%define mod_full_name %{mod_name}-%{version}

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/josh/rack-ssl
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Force SSL/TLS in your app
License:        MIT
Group:          Development/Languages/Ruby

%description
Rack middleware to force SSL/TLS.


%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="LICENSE README.md" \
  -f

%gem_packages

%changelog
