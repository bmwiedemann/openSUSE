#
# spec file for package post-build-checks-containers
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           post-build-checks-containers
Version:        0.1
Release:        0
Summary:        OBS post-build hooks for Containers
License:        GPL-2.0-only
Group:          Development/Tools/Building
URL:            http://www.suse.com/security
Source0:        80-antivirus-scan-clamav
Source1:        80-vulnerability-scan-trivy
Source2:        80-vulnerability-scan-neuvector

# the scanner-databases and neuvector-scanner are only on SLES.
%if ! 0%{?is_opensuse}

# clamav stuff
Requires:       clamav
Requires:       clamav-database
Requires:       jq

# neuvector stuff
%ifarch x86_64 aarch64
Requires:       neuvector-scanner
Requires:       neuvector-scanner-database
# docker needs bridge, need kernel-default
Requires:       docker
Requires:       kernel-default
%endif

# Trivy
Requires:       trivy
Requires:       coreutils
Requires:       python3
Requires:       trivy-database

%endif

%description
OBS post-build hooks to be executed for scanning containers. These hooks mainly
consists of performing actions such as antivirus scans (via ClamAV) or
vulnerability scans (via Trivy, NeuVector), generating artifacts that can later
be attached to relevant OCI container image artifacts as OCI attestations.

%prep

%build

%install
%if 0%{?is_opensuse}
mkdir  -p %{buildroot}%{_prefix}/lib/build/post-build-checks
ln -s  /bin/true %{buildroot}%{_prefix}/lib/build/post-build-checks/brp-99-true
%else
# sles

install -D -m 0755 -t %{buildroot}%{_prefix}/lib/build/post-build-checks %{SOURCE0}

%ifnarch s390x
# currently have a bit of endianess issue with the trivy db
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/build/post-build-checks %{SOURCE1}
%endif

# neuvector scanner did not build on anything but x86_64 and aarch64 yet
%ifarch x86_64 aarch64
install -D -m 0755 -t %{buildroot}%{_prefix}/lib/build/post-build-checks %{SOURCE2}
%endif
%endif

%files
%dir %{_prefix}/lib/build
%dir %{_prefix}/lib/build/post-build-checks
%{_prefix}/lib/build/post-build-checks/*

%changelog
