#
# spec file for package rubygem-securerandom
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

Name:           rubygem-securerandom
Version:        0.4.0
Release:        0
%define mod_name securerandom
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 3.1.0}
BuildRequires:  %{rubygem gem2rpm}
URL:            https://github.com/ruby/securerandom
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Interface for secure random number generator
License:        Ruby and BSD-2-Clause

%description
Interface for secure random number generator.

%prep

%build

%install
%gem_install \
  --doc-files="COPYING README.md" \
  -f

%gem_packages

%changelog
