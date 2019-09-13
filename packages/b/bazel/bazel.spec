#
# spec file for package bazel
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


%define bashcompdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)
Name:           bazel
Version:        0.26
Release:        0
Summary:        Tool for the automation of building and testing of software
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            http://bazel.io/
Source:         README
Provides:       bazel = %{version}
Requires:       bazel%{version}
%ifarch armv7l
ExclusiveArch:  do_not_build
%endif

%description
Tool for the automation of building and testing of software. It supports Java,
C++ and Go as programing languages. It also has a support for Android and iOS
as mobile operating systems.

%prep
cp %{SOURCE0} .

%build

%install

%files
%doc README

%changelog
