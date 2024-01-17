#
# spec file for package rubygem-cfa_grub2
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


Name:           rubygem-cfa_grub2
Version:        2.0.0
Release:        0
%define mod_name cfa_grub2
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/config-files-api/config_files_api_grub2
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Models for GRUB2 configuration files
License:        LGPL-3.0-only
Group:          Development/Languages/Ruby

%description
Models allowing easy read and modification of GRUB2 configuration files. It is
a plugin for cfa framework.

%prep

%build

%install
%gem_install \
  -f

%gem_packages

%changelog
