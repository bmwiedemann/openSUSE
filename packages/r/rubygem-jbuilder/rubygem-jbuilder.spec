#
# spec file for package rubygem-jbuilder
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

Name:           rubygem-jbuilder
Version:        2.13.0
Release:        0
%define mod_name jbuilder
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{ruby >= 2.2.2}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/rails/jbuilder
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        series
Source2:        gem2rpm.yml
# MANUAL
Patch0:         fix-shebang.patch
# /MANUAL
Summary:        Create JSON structures via a Builder-style DSL
License:        MIT

%description
Create JSON structures via a Builder-style DSL.

%prep
%gem_unpack
%patch -P 0 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  --doc-files="MIT-LICENSE README.md" \
  -f

%gem_packages

%changelog
