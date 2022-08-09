#
# spec file for package rubygem-rice
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

Name:           rubygem-rice
Version:        4.0.4
Release:        0
%define mod_name rice
%define mod_full_name %{mod_name}-%{version}
# MANUAL
Source2:        rice-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.5}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/jasonroelofs/rice
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Ruby Interface for C++ Extensions
License:        MIT
Group:          Development/Languages/Ruby

%description
Rice is a C++ interface to Ruby's C API. It provides a type-safe and
exception-safe interface in order to make embedding Ruby and writing
Ruby extensions with C++ easier.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md COPYING README.md" \
  -f

%gem_packages

%changelog
