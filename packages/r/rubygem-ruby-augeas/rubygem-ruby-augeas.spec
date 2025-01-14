#
# spec file for package rubygem-ruby-augeas
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

Name:           rubygem-ruby-augeas
Version:        0.6.0
Release:        0
%define mod_name ruby-augeas
%define mod_full_name %{mod_name}-%{version}

Summary:        Ruby bindings for augeas
License:        LGPL-2.1-or-later
Group:          Development/Languages/Ruby
URL:            https://augeas.net/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
BuildRequires:  %{rubydevel >= 1.8.1}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
# MANUAL
BuildRequires:  augeas-devel
BuildRequires:  pkgconfig
%if 0%{?suse_version} == 1110
BuildRequires:  libxml2-devel
%endif
# /MANUAL

%description
Provides bindings for augeas.

%prep

%build

%install
%gem_install \
  --doc-files="COPYING NEWS README.md" \
  -f
%gem_cleanup

%gem_packages

%changelog
