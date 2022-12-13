#
# spec file for package rubygem-benchmark
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

Name:           rubygem-benchmark
Version:        0.2.1
Release:        0
%define mod_name benchmark
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/ruby/benchmark
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
# MANUAL
Patch0:         0001-Change-shebang-from-usr-bin-env-bash-to-usr-bin-bash.patch
# /MANUAL
Summary:        A performance benchmarking library
License:        BSD-2-Clause AND Ruby
Group:          Development/Languages/Ruby

%description
The Benchmark module provides methods for benchmarking Ruby code, giving
detailed reports on the time taken for each task.

%prep
%gem_unpack
%patch0 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  --doc-files="LICENSE.txt README.md" \
  -f
# MANUAL
find %{buildroot}/%{_libdir}/ruby/gems \( -name .gitignore -o -name .travis.yml \) | xargs rm
# /MANUAL

%gem_packages

%changelog
