#
# spec file for package rubygem-mysql2
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

Name:           rubygem-mysql2
Version:        0.5.5
Release:        0
%define mod_name mysql2
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  mysql-devel
# /MANUAL
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel >= 2.0.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
URL:            https://github.com/brianmario/mysql2
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-mysql2-rpmlintrc
Source2:        series
Source3:        gem2rpm.yml
# MANUAL
Patch0:         workaround_mysql_config_libs.patch
# /MANUAL
Summary:        A simple, fast Mysql library for Ruby, binding to libmysql
License:        MIT

%description
A simple, fast Mysql library for Ruby, binding to libmysql.

%prep
%gem_unpack
%patch -P 0 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f
%gem_cleanup

%gem_packages

%changelog
