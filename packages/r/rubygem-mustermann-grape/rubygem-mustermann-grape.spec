#
# spec file for package rubygem-mustermann-grape
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-mustermann-grape
Version:        1.0.0
Release:        0
%define mod_name mustermann-grape
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 2.1.0}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://github.com/ruby-grape/mustermann-grape
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Grape syntax for Mustermann
License:        MIT
Group:          Development/Languages/Ruby

%description
Adds Grape style patterns to Mustermman.

%prep

%build

%install
%gem_install \
  --doc-files="README.md" \
  -f

%gem_packages

%changelog
