#
# spec file for package ruby-bundled-gems-rpmhelper
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


Name:           ruby-bundled-gems-rpmhelper
Version:        0.0.6
Release:        0
Summary:        A little helper to add provides for intree gems during a ruby build
License:        MIT
Group:          Development/Languages/Ruby
URL:            https://github.com/openSUSE/ruby-packaging/
Source0:        ruby_bundled_gems.pl
Source1:        ruby_bundled_gems.attr
BuildArch:      noarch
# Requires:       this-is-only-for-build-envs

%description
Just a little helper to add provides for intree gems during a ruby build

%prep

%build

%install
install -D -m 0755 %{SOURCE0} %{buildroot}%{_prefix}/lib/rpm/ruby_bundled_gems.pl
install -D -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/rpm/fileattrs/ruby_bundled_gems.attr

%files
%{_prefix}/lib/rpm/ruby_bundled_gems.pl
%{_prefix}/lib/rpm/fileattrs/ruby_bundled_gems.attr

%changelog
