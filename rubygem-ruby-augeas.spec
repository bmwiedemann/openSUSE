#
# spec file for package rubygem-ruby-augeas
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           rubygem-ruby-augeas
Version:        0.5.0
Release:        0
%define mod_name ruby-augeas
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires: pkgconfig
BuildRequires: augeas-devel
%if 0%{?suse_version} == 1110
BuildRequires: libxml2-devel
%endif
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel >= 1.8.1}
BuildRequires:  %{rubygem gem2rpm}
Url:            http://augeas.net/
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
# MANUAL
Patch0:  COPYING.patch
# /MANUAL
Summary:        Ruby bindings for augeas
License:        LGPL-2.1+
Group:          Development/Languages/Ruby

%description
Provides bindings for augeas.

%prep
%gem_unpack
%patch -P 0 -p0
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  --doc-files="COPYING README.rdoc" \
  -f
%gem_cleanup

%gem_packages

%changelog
