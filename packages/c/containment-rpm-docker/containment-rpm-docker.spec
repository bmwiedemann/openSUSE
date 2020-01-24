#
# spec file for package containment-rpm-docker
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           containment-rpm-docker
Version:        1.4.0+git20180612.c577fec
Release:        0
Summary:        Wraps OBS/kiwi-built images in rpms
License:        MIT
Group:          System/Management
Url:            https://github.com/SUSE/containment-rpm-docker
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  filesystem
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if !0%{?is_opensuse}
%if 0%{?suse_version} >= 1230
Recommends:     rubygem(changelog_generator)
%else
Recommends:     rubygem-changelog_generator
%endif
Recommends:     changelog-generator-data
%endif
Requires:       libxml2-tools
# Conflicts with other packages that provide /usr/lib/build/kiwi_post_run
Conflicts:      kiwi_post_run
Provides:       kiwi_post_run

%description
OBS kiwi_post_run hook to wrap a kiwi-produced image in an rpm package.

This package should be required by the Build Service project's meta
prjconf, so that the kiwi_post_run hook is present in the kiwi image
and gets executed at the end of the image build.  It will then build
an rpm which contains the newly-produced image from kiwi (using
image.spec.in), and place the rpm in the correct location that it
becomes an additional build artefact.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/lib/build/
install -m 644 image.spec.in %{buildroot}/usr/lib/build/
install -m 755 kiwi_post_run %{buildroot}/usr/lib/build/

%files
%defattr(-,root,root)
/usr/lib/build/kiwi_post_run
/usr/lib/build/image.spec.in

%changelog
