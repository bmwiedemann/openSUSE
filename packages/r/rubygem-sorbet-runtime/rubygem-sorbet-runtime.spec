#
# spec file for package rubygem-sorbet-runtime
#
# Copyright (c) 2025 SUSE LLC
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

Name:           rubygem-sorbet-runtime
Version:        0.5.11633
Release:        0
%define mod_name sorbet-runtime
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 2.7.0}
BuildRequires:  %{rubygem gem2rpm}
URL:            https://sorbet.org
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Patch1:         LICENSE.patch
Summary:        Sorbet runtime
License:        Apache-2.0

%description
Sorbet's runtime type checking component.

%prep
%gem_unpack
%patch -P 1 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  -f

%gem_packages

%changelog
