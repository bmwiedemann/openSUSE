#
# spec file for package rubygem-binding_of_caller
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

Name:           rubygem-binding_of_caller
Version:        1.0.1
Release:        0
%define mod_name binding_of_caller
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{ruby >= 2.0.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/banister/binding_of_caller
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-binding_of_caller-rpmlintrc
Source2:        gem2rpm.yml
Summary:        Retrieve the binding of a method's caller, or further up the stack
License:        MIT

%description
Provides the Binding#of_caller method.
Using binding_of_caller we can grab bindings from higher up the call stack and
evaluate code in that context.
Allows access to bindings arbitrarily far up the call stack, not limited to
just the immediate caller.
Recommended for use only in debugging situations. Do not use this in
production apps.

%prep

%build

%install
%gem_install \
  --doc-files="LICENSE README.md" \
  -f

%gem_packages

%changelog
