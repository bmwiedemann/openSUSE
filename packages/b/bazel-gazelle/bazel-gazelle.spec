#
# spec file for package bazel-gazelle
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


%global provider        github
%global provider_tld    com
%global project         bazelbuild
%global repo            bazel-gazelle
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

%define src_install_dir /usr/src/%{name}

Name:           bazel-gazelle
Version:        0.16.0
Release:        0
Summary:        Generator of Bazel build files for Go projects
License:        Apache-2.0
Group:          Development/Tools/Building
Url:            https://github.com/bazelbuild/bazel-gazelle
Source:         %{name}-%{version}.tar.xz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.10
%{go_provides}

%description
Gazelle is a generator of Bazel build files for Go projects. It can create new
BUILD.bazel files for a project that follows "go build" conventions, and it can
update existing build files to include new sources, dependencies, and options.
Gazelle may be run by Bazel using the gazelle rule, or it can be run as a
command line tool. Gazelle can also be run in an external repository as part of
the go_repository rule. Gazelle may be extended to support new languages and
custom rule sets.

%package source
Summary:        Source code of bazel-gazelle
Group:          Development/Sources
BuildArch:      noarch

%description source
Gazelle is a generator of Bazel build files for Go projects. It can create new
BUILD.bazel files for a project that follows "go build" conventions, and it can
update existing build files to include new sources, dependencies, and options.
Gazelle may be run by Bazel using the gazelle rule, or it can be run as a
command line tool. Gazelle can also be run in an external repository as part of
the go_repository rule. Gazelle may be extended to support new languages and
custom rule sets.

This package contains source code for Gazelle.

%prep
%setup -q
rm -f ./go.mod ./go.sum

%build
%goprep %{provider_prefix}
%gobuild cmd/gazelle

%install
%goinstall

mkdir -p %{buildroot}%{src_install_dir}
tar -xJf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}

%files
%license LICENSE
%doc README.rst
%{_bindir}/gazelle

%files source
%{src_install_dir}

%changelog

