#
# spec file for package rubygem-slim
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

Name:           rubygem-slim
Version:        4.1.0
Release:        0
%define mod_name slim
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.0.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            http://slim-lang.com/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        series
Source2:        gem2rpm.yml
# MANUAL
Patch0:         894.patch
# /MANUAL
Summary:        Slim is a template language
License:        MIT
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Slim is a template language whose goal is reduce the syntax to the essential
parts without becoming cryptic.

%prep
%gem_unpack
%patch0 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="CHANGES LICENSE README.md" \
  -f

%gem_packages

%changelog
