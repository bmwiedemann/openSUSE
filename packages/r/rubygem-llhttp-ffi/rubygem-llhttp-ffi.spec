#
# spec file for package rubygem-llhttp-ffi
#
# Copyright (c) 2021 SUSE LLC
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


%define mod_name llhttp-ffi
%define mod_full_name %{mod_name}-%{version}
#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#
Name:           rubygem-llhttp-ffi
Version:        0.4.0
Release:        0
Summary:        Ruby FFI bindings for llhttp
License:        MPL-2.0
Group:          Development/Languages/Ruby
URL:            https://github.com/metabahn/llhttp/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
BuildRequires:  %{rubydevel >= 2.5.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
# MANUAL
BuildRequires:  %{rubygem ffi-compiler}
# /MANUAL

%description
Ruby FFI bindings for llhttp.

%prep

%build

%install
%gem_install \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f
%{gem_cleanup}
# MANUAL
# drop files from the git repository
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name '.rubocop*' -o -name '.github' -o -name '.yardopts' -o -name '.rspec' -o -name '.gitignore' \) | xargs rm -rf
# /MANUAL


%gem_packages

%changelog
