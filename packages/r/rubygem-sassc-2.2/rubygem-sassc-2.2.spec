#
# spec file for package rubygem-sassc-2.2
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-sassc-2.2
Version:        2.2.1
Release:        0
%define mod_name sassc
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -2.2
# MANUAL
BuildRequires:  gcc-c++
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel >= 2.0.0}
BuildRequires:  %{rubygem gem2rpm}
Url:            https://github.com/sass/sassc-ruby
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rpmlintrc
Source2:        gem2rpm.yml
# MANUAL
Patch0:  reproducible.patch
# /MANUAL
Summary:        Use libsass with Ruby!
License:        MIT
Group:          Development/Languages/Ruby

%description
Use libsass with Ruby!.

%prep
%gem_unpack
%patch0 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  --extconf-opts=--disable-march-tune-native \
  --doc-files="CHANGELOG.md LICENSE.txt README.md" \
  -f
%gem_cleanup
# MANUAL
find %{buildroot}%{_libdir} -name sassc-2.\*.info -delete
# /MANUAL


%gem_packages

%changelog
