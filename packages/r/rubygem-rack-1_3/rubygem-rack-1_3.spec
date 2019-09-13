#
# spec file for package rubygem-rack-1_3
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           rubygem-rack-1_3
Version:        1.3.10
Release:        0
%define mod_name rack
%define mod_full_name %{mod_name}-%{version}
%define mod_version_suffix -1_3
# MANUAL
BuildRequires:  fdupes
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{ruby}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
Url:            http://rack.github.com/
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        rubygem-rack-1_3-rpmlintrc
Source2:        gem2rpm.yml
Summary:        A modular Ruby webserver interface
License:        MIT
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
Rack provides minimal, modular and adaptable interface for developing
web applications in Ruby.  By wrapping HTTP requests and responses in
the simplest way possible, it unifies and distills the API for web
servers, web frameworks, and software in between (the so-called
middleware) into a single method call.
Also see http://rack.github.com/.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="COPYING README.rdoc" \
  -f
# MANUAL
%fdupes %{buildroot}%{_libdir}/ruby/gems/*/gems/%{mod_name}-%{version}/
# /MANUAL

%gem_packages

%changelog
