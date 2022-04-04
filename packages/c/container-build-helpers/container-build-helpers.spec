#
# spec file for package container-build-helpers
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


Name:           container-build-helpers
Version:        0.0.1
Release:        0
Summary:        Scripts to cleanup container images after a build
License:        GPL-2.0-or-later
URL:            https://build.opensuse.org
Source0:        cleanup_container
Source1:        LICENSE
BuildArch:      noarch

%description
This is a simple script that removes the unecessary bits and pieces left on a
system after zypper has been run. This reduces the total size of the final
container image.

%prep

%build
cp %{SOURCE1} .

%install
install -D -p -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/cleanup_container

%files
%license LICENSE
%{_bindir}/cleanup_container

%changelog
