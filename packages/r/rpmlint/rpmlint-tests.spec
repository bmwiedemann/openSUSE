#
# spec file for package rpmlint-tests
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#
# icecream 0


#!BuildIgnore: post-build-checks brp-check-suse

BuildRequires:  erlang
BuildRequires:  rpmlint-Factory-strict
BuildRequires:  rpmlint-mini

Name:           rpmlint-tests
Version:        84.87+git20190920.e27d431
Release:        0
Summary:        rpmlint regression tests
License:        SUSE-Public-Domain
Group:          Development/Tools/Building
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://www.opensuse.org/
Source:         rpmlint-tests-%version.tar.xz
Patch0:         rpmlint-tests-sle15.patch

%description
This package doesn't actually contain any files and is not meant to
be installed. It's only useful in the opensuse build service to run
regression tests against rpmlint(-mini).

%prep
%setup -q
%if 0%{?sle_version} >= 1500
%patch0 -p1
%endif

%build
mkdir rpms
make test

%install

%changelog
