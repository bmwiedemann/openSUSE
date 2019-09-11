#
# spec file for package rubygem-memcache-client
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


Name:           rubygem-memcache-client
Version:        1.8.5
Release:        0
%define mod_name memcache-client
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
#
Url:            http://github.com/mperham/memcache-client
Source:         %{mod_name}-%{version}.gem
#
Summary:        A Ruby library for accessing memcached
License:        BSD-3-Clause
Group:          Development/Languages/Ruby

%description
A Ruby library for accessing memcached.

%prep
%build
%install
%gem_install \
  --symlink-binaries \
  --doc-files="LICENSE.txt" \
  -f

%gem_packages

%changelog
