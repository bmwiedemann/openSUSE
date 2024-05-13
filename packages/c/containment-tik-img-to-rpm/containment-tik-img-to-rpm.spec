#
# spec file for package containment-tik-img-to-rpm
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

# norootforbuild

Name:           containment-tik-img-to-rpm
Version:        1.0
Release:        0
Summary:	OBS Post check for containing tik-osimage-* images in RPM
License:        MIT
Source:         containment-tik-img-to-rpm
Source1:	image.spec.in
BuildRequires:  filesystem
BuildArch:	noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       jq
Requires:       gawk
Requires:       coreutils
Conflicts:	containment-rpm


%description
OBS Post check for containing tik-osimage-* images in RPM

%prep

%build

%install
mkdir -p %{buildroot}/usr/lib/build/post-build-checks/
install -m 755 %{SOURCE0} %{buildroot}/usr/lib/build/post-build-checks/
install -m 644 %{SOURCE1} %{buildroot}/usr/lib/build/

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/build/post-build-checks
%{_prefix}/lib/build/post-build-checks/containment-tik-img-to-rpm
%{_prefix}/lib/build/image.spec.in

%changelog

