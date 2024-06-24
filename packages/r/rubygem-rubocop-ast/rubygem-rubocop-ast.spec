#
# spec file for package rubygem-rubocop-ast
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

Name:           rubygem-rubocop-ast
Version:        1.31.3
Release:        0
%define mod_name rubocop-ast
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  fdupes
# /MANUAL
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 2.7.0}
BuildRequires:  %{rubygem gem2rpm}
URL:            https://github.com/rubocop/rubocop-ast
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        RuboCop tools to deal with Ruby code AST
License:        MIT

%description
RuboCop's Node and NodePattern classes.

%prep

%build

%install
%gem_install \
  --doc-files="LICENSE.txt README.md" \
  -f
# MANUAL
for dir in %{buildroot}%{_libdir}/ruby/gems/* ; do
    %fdupes $dir
done
# /MANUAL

%gem_packages

%changelog
