#
# spec file for package rubygem-redcarpet
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

Name:           rubygem-redcarpet
Version:        3.6.0
Release:        0
%define mod_name redcarpet
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%if 0%{?suse_version} == 1110
%define rb_build_versions ruby21
%endif
# /MANUAL
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel >= 1.9.2}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  update-alternatives
URL:            https://github.com/vmg/redcarpet
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-redcarpet-rpmlintrc
Source2:        gem2rpm.yml
Summary:        Markdown that smells nice
License:        MIT

%description
A fast, safe and extensible Markdown to (X)HTML parser.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="CHANGELOG.md COPYING README.markdown" \
  -f
%gem_cleanup

%gem_packages

%changelog
