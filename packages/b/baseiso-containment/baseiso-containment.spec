#
# spec file for package baseiso-containment
#
# Copyright (c) 2025 SUSE LLC
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


Name:           baseiso-containment
Version:        0.2.2
Release:        0
Summary:        Wraps Agama build for product composer
License:        MIT
Group:          System/Management
Source1:        baseiso.spec.in
Source2:        baseiso_post_run
BuildRequires:  filesystem
BuildArch:      noarch

%description
Wraps Agama build as base image for product composer

%install
mkdir -p %{buildroot}%{_prefix}/lib/build/post_build.d
install -m 644 %{S:1} %{buildroot}%{_prefix}/lib/build/
install -m 755 %{S:2} %{buildroot}%{_prefix}/lib/build/post_build.d/

%files
%dir %{_prefix}/lib/build/post_build.d
%{_prefix}/lib/build/post_build.d/*_post_run
%{_prefix}/lib/build/baseiso.spec.in

%changelog
