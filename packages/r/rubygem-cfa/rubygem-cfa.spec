#
# spec file for package rubygem-cfa
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


Name:           rubygem-cfa
Version:        1.0.1
Release:        0
%define mod_name cfa
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/config-files-api/config_files_api
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Summary:        CFA (Config Files API) provides an easy way to create models on top
License:        LGPL-3.0-only
Group:          Development/Languages/Ruby

%description
Library offering separation of parsing and file access from the rest of the
logic for managing configuraton files. It has built-in support for parsing
using augeas lenses and also for working with files directly in memory.

%prep

%build

%install
%gem_install \
  -f

%gem_packages

%changelog
