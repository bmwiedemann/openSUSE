#
# spec file for package kubernetes-node-image-pause
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


##
# The source code of the pause.c file has been taken directly from
# Kubernetes. You can take a look at Kubernetes upstream here:
# https://github.com/kubernetes/kubernetes. The file is inside of the
# `build/pause` directory, more precisely:
# https://raw.githubusercontent.com/kubernetes/kubernetes/master/build/pause/pause.c
#

%define executable pause
%define destination /usr/share/suse-docker-images/pause

Name:           kubernetes-node-image-pause
Version:        1.0.0
Release:        0
Summary:        Kubernetes pause image files
License:        Apache-2.0
Group:          System/Management
Url:            http://kubernetes.io
Source:         kubernetes-node-image-pause.tar.gz
Source1:        kubernetes-node-image-pause-rpmlintrc
BuildRequires:  glibc-devel-static
PreReq:         %fillup_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the files needed for building the pause Docker image used
by a Kubernetes cluster.

%prep
%setup -q -n %{name}

%build
gcc -Os -Wall -static -o %{executable} pause.c
strip %{executable}

%install
mkdir -p -m 0755 %{buildroot}%{destination}
install -D -m 0644 Dockerfile %{buildroot}%{destination}/Dockerfile
install -D -m 0755 %{executable} %{buildroot}%{destination}/%{executable}

%pre
cat >&2 <<EOF

In order to build the "pause" image you have to have the docker daemon running
and execute the following commands:

  $ cd /usr/share/suse-docker-images/pause
  $ docker build -t suse/pause:latest .
EOF
exit 0

%files
%defattr(-,root,root)
%dir /usr/share/suse-docker-images
%dir %{destination}
%{destination}/Dockerfile
%{destination}/%{executable}

%changelog
