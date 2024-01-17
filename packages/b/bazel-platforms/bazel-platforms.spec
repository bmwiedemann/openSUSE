#
# spec file for package bazel-platforms
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bazel-platforms
Version:        20190611
Release:        0
Summary:        Bazel constraint values for specifying platforms and toolchains 
License:        Apache-2.0
Url:            https://github.com/bazelbuild/platforms
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildArch:      noarch

%description
Bazel platforms contains all canonical constraint_settings, constraint_values
and platforms that are universally useful across languages and Bazel projects.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/bazel-platforms
cp -R * %{buildroot}%{_datadir}/bazel-platforms
fdupes %{buildroot}%{_datadir}/bazel-platforms

%files
%license LICENSE
%doc README.md
%{_datadir}/bazel-platforms

%changelog

