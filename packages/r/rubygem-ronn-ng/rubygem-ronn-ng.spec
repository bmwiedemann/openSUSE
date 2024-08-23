#
# spec file for package rubygem-ronn-ng
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


%define mod_name ronn-ng
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%define rb_build_versions     %{rb_default_ruby}
%define rb_build_ruby_abis    %{rb_default_ruby_abi}
# /MANUAL
#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#
Name:           rubygem-ronn-ng
Version:        0.10.1
Release:        0
Summary:        Builds man pages from Markdown
License:        MIT
Group:          Development/Languages/Ruby
URL:            https://github.com/apjanke/ronn-ng
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
BuildRequires:  %{ruby >= 2.7}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
PreReq:         update-alternatives

%description
Ronn-NG builds manuals in Unix man page and HTML format from Markdown. Ronn-NG
is a modern, maintained fork of the original Ronn.

%prep

%build

%install
%gem_install \
  --no-document \
  --symlink-binaries \
  --doc-files="CHANGELOG.md LICENSE.txt README.md" \
  -f

%gem_packages

%changelog
