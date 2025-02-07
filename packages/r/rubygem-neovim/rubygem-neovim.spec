#
# spec file for package rubygem-neovim
#
# Copyright (c) 2024 SUSE LLC
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

Name:           rubygem-neovim
Version:        0.10.0
Release:        0
%define mod_name neovim
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 2.2.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  update-alternatives
URL:            https://github.com/neovim/neovim-ruby
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A Ruby client for Neovim
License:        MIT

%description
A Ruby client for Neovim.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="CHANGELOG.md LICENSE.txt README.md" \
  -f
# MANUAL
chmod -x %{buildroot}%{rb_dir}/gems/%{rb_ver}/gems/neovim-%{version}/script/host_wrapper.bat
rm -f %{buildroot}%{rb_dir}/gems/%{rb_ver}/gems/neovim-%{version}/.gitignore
rm -rf %{buildroot}%{rb_dir}/gems/%{rb_ver}/gems/neovim-%{version}/.github
sed -i 's|/usr/bin/env bash|/usr/bin/bash|g' %{buildroot}%{rb_dir}/gems/%{rb_ver}/gems/neovim-%{version}/script/ci/download_nvim.sh
sed -i 's|/usr/bin/env bash|/usr/bin/bash|g' %{buildroot}%{rb_dir}/gems/%{rb_ver}/gems/neovim-%{version}/script/host_wrapper.sh
# /MANUAL


%gem_packages

%changelog
