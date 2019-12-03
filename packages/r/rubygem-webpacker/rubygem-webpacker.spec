#
# spec file for package rubygem-webpacker
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           rubygem-webpacker
Version:        4.2.0
Release:        0
%define mod_name webpacker
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 2.2.0}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://github.com/rails/webpacker
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Use webpack to manage app-like JavaScript modules in Rails
License:        MIT
Group:          Development/Languages/Ruby

%description
Use webpack to manage app-like JavaScript modules in Rails.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md MIT-LICENSE README.md" \
  -f

%gem_packages

%changelog
