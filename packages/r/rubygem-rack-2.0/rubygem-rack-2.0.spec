#
# spec file for package rubygem-rack-2.0
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

Name:           rubygem-rack-2.0
Version:        2.0.9
Release:        0
%define mod_name rack
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -2.0
# MANUAL
BuildRequires:  fdupes
Conflicts: rubygem(ruby:2.6.0:rack:2.0)

%if 0%{?suse_version} && 0%{?suse_version} < 1330
%define rb_build_versions ruby23 ruby24 ruby25
%define rb_build_ruby_abi ruby:2.3.0 ruby:2.4.0 ruby:2.5.0
%endif
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby >= 2.2.2}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  update-alternatives
Url:            https://rack.github.io/
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-rack-2.0-rpmlintrc
Source2:        gem2rpm.yml
Summary:        A modular Ruby webserver interface
License:        MIT
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Rack provides a minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.
Also see https://rack.github.io/.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="COPYING HISTORY.md README.rdoc" \
  -f
# MANUAL
%fdupes %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version}/
chmod 644 %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version}/test/cgi/test.gz
# /MANUAL


%gem_packages

%changelog
