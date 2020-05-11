#
# spec file for package rubygem-tmuxinator
#
# Copyright (c) 2020 SUSE LLC
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

Name:           rubygem-tmuxinator
Version:        2.0.1
Release:        0
%define mod_name tmuxinator
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%if 0%{?suse_version} && 0%{?suse_version} < 1330
%define rb_build_versions ruby23 ruby24 ruby25
%define rb_default_ruby_abi ruby:2.3.0 ruby:2.4.0 ruby:2.5.0
%endif
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.5.8}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://github.com/tmuxinator/tmuxinator
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Create and manage complex tmux sessions easily
License:        MIT
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Create and manage complex tmux sessions easily.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  -f
# MANUAL
# delete custom files here or do other fancy stuff
for i in $(find %{buildroot} -type l -name mux.fish) ; do
  ln -s -v -f tmuxinator.fish $i ;
done
# /MANUAL

%gem_packages

%changelog
