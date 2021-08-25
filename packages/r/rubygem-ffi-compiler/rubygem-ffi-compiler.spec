#
# spec file for package rubygem-ffi-compiler
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define mod_name ffi-compiler
%define mod_full_name %{mod_name}-%{version}
Name:           rubygem-ffi-compiler
Version:        1.0.1
Release:        0
Summary:        Ruby FFI Rakefile generator
License:        Apache-2.0
Group:          Development/Languages/Ruby
URL:            http://wiki.github.com/ffi/ffi
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
BuildRequires:  %{ruby >= 1.9}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5

%description
A ruby library for automating compilation of native libraries for
use with ffi.

%prep

%build

%install
%gem_install \
  --doc-files="LICENSE README.md" \
  -f

%gem_packages

%changelog
