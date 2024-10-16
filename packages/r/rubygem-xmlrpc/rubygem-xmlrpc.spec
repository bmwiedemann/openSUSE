#
# spec file for package rubygem-xmlrpc
#
# Copyright (c) 2023 SUSE LLC
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

Name:           rubygem-xmlrpc
Version:        0.3.3
Release:        0
%define mod_name xmlrpc
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%if 0%{?suse_version} < 1500
%define rb_build_versions ruby23
%define rb_default_ruby_abi ruby:2.3.0
%endif
# /MANUAL
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 2.3}
BuildRequires:  %{rubygem gem2rpm}
URL:            https://github.com/ruby/xmlrpc
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        XMLRPC is a lightweight protocol that enables remote procedure calls
License:        BSD-2-Clause AND Ruby

%description
XMLRPC is a lightweight protocol that enables remote procedure calls over
HTTP.

%prep

%build

%install
%gem_install \
  --doc-files="LICENSE.txt NEWS.md README.md" \
  -f

%gem_packages

%changelog
