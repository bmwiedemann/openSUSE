#
# spec file for package rubygem-base32
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           rubygem-base32
Version:        0.3.2
Release:        0
%define mod_name base32
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://github.com/stesla/base32
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Ruby extension for base32 encoding and decoding
License:        MIT
Group:          Development/Languages/Ruby

%description
Ruby extension for base32 encoding and decoding.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LICENSE README" \
  -f

%gem_packages

%changelog
