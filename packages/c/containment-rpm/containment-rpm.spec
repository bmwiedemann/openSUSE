#
# spec file for package containment-rpm
#
# Copyright (c) 2023 SUSE LLC
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


Name:           containment-rpm
Version:        2.0.0
Release:        0
Summary:        Wraps OBS docker/kiwi-built images in rpms
License:        MIT
Group:          System/Management
URL:            https://github.com/SUSE/containment-rpm-docker
Source:         https://github.com/SUSE/containment-rpm/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  filesystem
Requires:       jq
Requires:       libxml2-tools
BuildArch:      noarch
# disabled for now, not used for public cloud purpose
%if 0
Requires:       changelog-generator-data
Requires:       libxml2-tools
%if 0%{?suse_version} >= 1230
Requires:       rubygem(changelog_generator)
%else
Requires:       rubygem-changelog_generator
%endif
%endif

%description
OBS container_post_run hook to wrap a kiwi or docker image in an rpm package.

This package should be required by the Build Service project's meta
prjconf, so that the container_post_run hook is present in the container image
and gets executed at the end of the image build.  It will then build
an rpm which contains the newly-produced image from kiwi/docker (using
image.spec.in), and place the rpm in the correct location that it
becomes an additional build artefact.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/build/post_build.d
install -m 644 image.spec.in %{buildroot}%{_prefix}/lib/build/
install -m 755 container_post_run %{buildroot}%{_prefix}/lib/build/post_build.d/

%files
%dir %{_prefix}/lib/build/post_build.d
%{_prefix}/lib/build/post_build.d/*_post_run
%{_prefix}/lib/build/image.spec.in

%changelog
