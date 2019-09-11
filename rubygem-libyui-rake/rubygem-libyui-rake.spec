#
# spec file for package rubygem-libyui-rake
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rubygem-libyui-rake
Version:        0.1.14
Release:        0
%define mod_name libyui-rake
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            http://github.org/openSUSE/libyui-rake
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Rake tasks providing basic work-flow for libyui development
License:        LGPL-2.1-only
Group:          Development/Languages/Ruby

%description
Rake tasks that support work-flow of libyui developer. It allows packaging
a repo, sending it to build service, creating submit request
to target repo or running client from git repo.
Heavily inspired in yast-rake.

%prep

%build

%install
%gem_install \
  --doc-files="COPYING README.md" \
  -f

%gem_packages

%changelog
