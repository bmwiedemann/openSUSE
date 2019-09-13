#
# spec file for package rubygem-treetop-1_4
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


Name:           rubygem-treetop-1_4
Version:        1.4.15
Release:        0
%define mod_name treetop
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -1_4
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
Url:            https://github.com/cjheath/treetop
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A Ruby-based text parsing and interpretation DSL
License:        MIT
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
A Ruby-based text parsing and interpretation DSL.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="LICENSE README.md" \
  -f

%gem_packages

%changelog
