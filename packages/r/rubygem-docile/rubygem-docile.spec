#
# spec file for package rubygem-docile
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

Name:           rubygem-docile
Version:        1.4.1
Release:        0
%define mod_name docile
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{ruby >= 2.5.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://ms-ati.github.io/docile/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Ruby gem to treat Ruby objects as a domain-specific language
License:        MIT

%description
Docile treats the methods of a given ruby object as a DSL (domain specific
language) within a given block.
Killer feature: you can also reference methods, instance variables, and local
variables from the original (non-DSL) context within the block.
Docile releases follow Semantic Versioning as defined at semver.org.

%prep

%build

%install
%gem_install \
  --doc-files="HISTORY.md LICENSE README.md" \
  -f

%gem_packages

%changelog
