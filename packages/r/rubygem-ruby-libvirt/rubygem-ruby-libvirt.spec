#
# spec file for package rubygem-ruby-libvirt
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

Name:           rubygem-ruby-libvirt
Version:        0.7.1
Release:        0
%define mod_name ruby-libvirt
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  libvirt
BuildRequires:  libvirt-devel
BuildRequires:  pkg-config
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel >= 1.8.1}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
Url:            http://libvirt.org/ruby/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-ruby-libvirt-rpmlintrc
Source2:        gem2rpm.yml
Summary:        Ruby bindings for LIBVIRT
License:        LGPL-2.0-only
Group:          Development/Languages/Ruby

%description
Ruby bindings for libvirt.

%prep

%build

%install
%gem_install \
  --doc-files="COPYING NEWS README README.rdoc" \
  -f
%gem_cleanup

%gem_packages

%changelog
