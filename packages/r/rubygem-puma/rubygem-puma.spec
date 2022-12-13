#
# spec file for package rubygem-puma
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

Name:           rubygem-puma
Version:        6.0.0
Release:        0
%define mod_name puma
%define mod_full_name %{mod_name}-%{version}
# MANUAL
BuildRequires:  openssl-devel
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubydevel >= 2.4}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://puma.io
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-puma-rpmlintrc
Source2:        gem2rpm.yml
Summary:        Puma is a simple, fast, threaded, and highly parallel HTTP 1.1
License:        BSD-3-Clause
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Puma is a simple, fast, threaded, and highly parallel HTTP 1.1 server for
Ruby/Rack applications. Puma is intended for use in both development and
production environments. It's great for highly parallel Ruby implementations
such as Rubinius and JRuby as well as as providing process worker support to
support CRuby well.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="History.md LICENSE README.md" \
  -f
%gem_cleanup

%gem_packages

%changelog
