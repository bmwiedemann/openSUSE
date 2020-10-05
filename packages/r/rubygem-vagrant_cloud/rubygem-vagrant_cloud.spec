#
# spec file for package rubygem-vagrant_cloud
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-vagrant_cloud
Version:        3.0.0
Release:        0
%define mod_name vagrant_cloud
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/hashicorp/vagrant_cloud
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Ruby library for the HashiCorp Vagrant Cloud API
License:        MIT
Group:          Development/Languages/Ruby

%description
Ruby library for the HashiCorp Vagrant Cloud API.

%prep

%build

%install
# MANUAL
%gem_unpack
sed -i 's|\(.*<rest-client>.freeze, \)\["~> 2.0.2"\]|\1\["~> 2.0"\]|' %{mod_full_name}.gemspec
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build
# HACK: %%gem_install uses the gem from %%{_sourcedir} by default, so we *must* put it back there
mv %{mod_full_name}.gem %{_sourcedir}/
# /MANUAL
%gem_install \
  --doc-files="LICENSE README.md" \
  -f

%gem_packages

%changelog
