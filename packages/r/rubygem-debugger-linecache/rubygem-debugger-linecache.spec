#
# spec file for package rubygem-debugger-linecache
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

Name:           rubygem-debugger-linecache
Version:        1.2.0
Release:        0
%define mod_name debugger-linecache
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
Url:            http://github.com/cldwalker/debugger-linecache
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Read file with caching
License:        MIT
Group:          Development/Languages/Ruby

%description
Linecache is a module for reading and caching lines. This may be useful for
example in a debugger where the same lines are shown many times.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LICENSE.txt README.md" \
  -f

%gem_packages

%changelog
