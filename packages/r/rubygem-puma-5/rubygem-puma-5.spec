#
# spec file for package rubygem-puma-5
#
# Copyright (c) 2023 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           rubygem-puma-5
Version:        5.6.5
Release:        0
%define mod_name puma
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -5
# MANUAL
BuildRequires:  openssl-devel
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{rubydevel >= 2.2}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  update-alternatives
Url:            https://puma.io
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-puma-5-rpmlintrc
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
# MANUAL
find %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version}/ \( -name "*.rb" -o -name "*.md" \) -exec chmod 644 {} \;
find %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version}/ -name "*.[h|c]" -exec rm {} \;
# /MANUAL


%gem_packages

%changelog
