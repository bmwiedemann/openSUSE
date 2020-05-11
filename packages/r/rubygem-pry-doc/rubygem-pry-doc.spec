#
# spec file for package rubygem-pry-doc
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

Name:           rubygem-pry-doc
Version:        1.1.0
Release:        0
%define mod_name pry-doc
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  etags
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
URL:            https://github.com/pry/pry-doc
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        Provides YARD and extended documentation support for Pry
License:        MIT
Group:          Development/Languages/Ruby

%description
Pry Doc is a Pry REPL plugin. It provides extended documentation support for
the REPL by means of improving the `show-doc` and `show-source` commands. With help
of the plugin the commands are be able to display the source code and the docs
of Ruby methods and classes implemented in C. 
%prep

%build

%install
%gem_install \
  --no-rdoc --no-ri \
  --doc-files="CHANGELOG.md LICENSE README.md" \
  -f
# MANUAL
rm -r %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version}/libexec
# /MANUAL

%gem_packages

%changelog
