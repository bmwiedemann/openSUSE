#
# spec file for package rubygem-debase-ruby_core_source
#
# Copyright (c) 2022 SUSE LLC
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

Name:           rubygem-debase-ruby_core_source
Version:        0.10.18
Release:        0
%define mod_name debase-ruby_core_source
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  fdupes
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.0.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/ruby-debug/debase-ruby_core_source
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-debase-ruby_core_source-rpmlintrc
Source2:        gem2rpm.yml
Summary:        Provide Ruby core source files
License:        MIT
Group:          Development/Languages/Ruby

%description
Provide Ruby core source files for C extensions that need them.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LEGAL LICENSE.txt README.md" \
  -f
# MANUAL
# drop files from the git repository
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name '.gitignore' \) | xargs rm
%fdupes %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_full_name}/
# /MANUAL

%gem_packages

%changelog
