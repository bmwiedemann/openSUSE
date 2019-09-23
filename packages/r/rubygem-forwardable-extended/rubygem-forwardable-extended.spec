#
# spec file for package rubygem-forwardable-extended
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-forwardable-extended
Version:        2.6.0
Release:        0
%define mod_name forwardable-extended
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
Url:            http://github.com/envygeeks/forwardable-extended
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Forwardable with hash, and instance variable extensions
License:        MIT
Group:          Development/Languages/Ruby

%description
Forwardable with hash, and instance variable extensions.

%prep

%build

%install
%gem_install \
  --doc-files="LICENSE" \
  -f

%gem_packages

%changelog
