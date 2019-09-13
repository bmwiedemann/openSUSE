#
# spec file for package rubygem-mysql2-0.4
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-mysql2-0.4
Version:        0.4.10
Release:        0
%define mod_name mysql2
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -0.4
# MANUAL
BuildRequires: mysql-devel

%if 0%{?suse_version} && 0%{?suse_version} < 1330
%define rb_build_versions ruby23 ruby24 ruby25
%define rb_build_ruby_abi ruby:2.3.0 ruby:2.4.0 ruby:2.5.0
%endif
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
Url:            http://github.com/brianmario/mysql2
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-mysql2-0.4-rpmlintrc
Source2:        gem2rpm.yml
Summary:        A simple, fast Mysql library for Ruby, binding to libmysql
License:        MIT
Group:          Development/Languages/Ruby

%description
A simple, fast Mysql library for Ruby, binding to libmysql.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f
%gem_cleanup

%gem_packages

%changelog
