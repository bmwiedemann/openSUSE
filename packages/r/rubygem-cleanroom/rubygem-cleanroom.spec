#
# spec file for package rubygem-cleanroom
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-cleanroom
Version:        1.0.0
Release:        0
%define mod_name cleanroom
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 1.9.3}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://github.com/sethvargo/cleanroom
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        (More) safely evaluate Ruby DSLs with cleanroom
License:        Apache-2.0
Group:          Development/Languages/Ruby

%description
Ruby is an excellent programming language for creating and managing custom
DSLs, but how can you securely evaluate a DSL while explicitly controlling the
methods exposed to the user? Our good friends instance_eval and instance_exec
are great, but they expose all methods - public, protected, and private - to
the user. Even worse, they expose the ability to accidentally or intentionally
alter the behavior of the system! The cleanroom pattern is a safer, more
convenient, Ruby-like approach for limiting the information exposed by a DSL
while giving users the ability to write awesome code!.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f

%gem_packages

%changelog
