#
# spec file for package rubygem-cssmin
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


Name:           rubygem-cssmin
Version:        1.0.3
Release:        0
%define mod_name cssmin
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 1.8.6}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
Url:            https://github.com/rgrove/cssmin/
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Summary:        Ruby library for minifying CSS
License:        BSD-3-Clause
Group:          Development/Languages/Ruby

%description
Ruby library for minifying CSS. Inspired by cssmin.js and YUI Compressor.

%prep

%build

%install
%gem_install \
  --doc-files="HISTORY.md LICENSE" \
  -f

%gem_packages

%changelog
