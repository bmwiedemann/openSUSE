#
# spec file for package rubygem-pairing_heap
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

Name:           rubygem-pairing_heap
Version:        3.1.0
Release:        0
%define mod_name pairing_heap
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{ruby >= 2.3.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/mhib/pairing_heap
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Performant priority queue in pure ruby with support for changing
License:        MIT

%description
Performant priority queue in pure ruby with support for changing priority
using pairing heap data structure.

%prep

%build

%install
%gem_install \
  --doc-files="LICENSE.txt README.md" \
  -f
# MANUAL
# drop files from the git repository
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name '.rubocop.yml' -o -name '.github' -o -name '.gitignore' \) | xargs rm -rf
# /MANUAL

%gem_packages

%changelog
