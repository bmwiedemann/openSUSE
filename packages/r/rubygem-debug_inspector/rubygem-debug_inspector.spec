#
# spec file for package rubygem-debug_inspector
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

Name:           rubygem-debug_inspector
Version:        1.2.0
Release:        0
%define mod_name debug_inspector
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  %{rubydevel >= 2.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/banister/debug_inspector
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A Ruby wrapper for the MRI 2.0 debug_inspector API
License:        MIT

%description
Adds methods to DebugInspector to allow for inspection of backtrace frames.
The debug_inspector C extension and API were designed and built by Koichi
Sasada, this project is just a gemification of his work.
This library makes use of the debug inspector API which was added to MRI
2.0.0.
Only works on MRI 2 and 3. Requiring it on unsupported Rubies will result in a
no-op.
Recommended for use only in debugging situations. Do not use this in
production apps.

%prep

%build

%install
%gem_install \
  --doc-files="LICENSE README.md" \
  -f
%gem_cleanup

%gem_packages

%changelog
