#
# spec file for package rubygem-zeitwerk
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-zeitwerk
Version:        2.4.2
Release:        0
%define mod_name zeitwerk
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 2.4.4}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://github.com/fxn/zeitwerk
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Efficient and thread-safe constant autoloader
License:        MIT
Group:          Development/Languages/Ruby

%description
Zeitwerk implements constant autoloading with Ruby semantics. Each gem
and application may have their own independent autoloader, with its own
configuration, inflector, and logger. Supports autoloading,
reloading, and eager loading.

%prep

%build

%install
%gem_install \
  --doc-files="MIT-LICENSE README.md" \
  -f

%gem_packages

%changelog
