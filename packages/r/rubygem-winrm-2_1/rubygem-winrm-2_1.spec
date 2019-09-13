#
# spec file for package rubygem-winrm-2_1
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-winrm-2_1
Version:        2.1.3
Release:        0
%define mod_name winrm
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -2_1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
Url:            https://github.com/WinRb/WinRM
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
# MANUAL
Patch0:         0001-Fix-line-endings-of-lib-winrm-psrp-powershell_output.patch
# /MANUAL
Summary:        Ruby library for Windows Remote Management
License:        Apache-2.0
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Ruby library for Windows Remote Management.

%prep
%gem_unpack
%patch0 -p1
find -type f -print0 | xargs -0 touch -r %{S:0}
%gem_build

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="LICENSE README.md changelog.md" \
  -f
# MANUAL
find %{buildroot}/%{_libdir}/ruby/gems/ \( -name '.rubocop.yml' -o -name '.travis.yml' -o -name '.gitignore' \) | xargs rm
find %{buildroot}/%{_libdir}/ruby/gems -name rwinrm | xargs sed -i 's/\r//g'
# /MANUAL

%gem_packages

%changelog
