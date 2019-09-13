#
# spec file for package bazel-rules-proto
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


%define src_install_dir /usr/src/%{name}

Name:           bazel-rules-proto
Version:        20190115
Release:        0
Summary:        Bazel build rules for Protocol Buffers
License:        Apache-2.0
Group:          Development/Tools/Building
Url:            https://github.com/stackb/rules_proto
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes

%description
bazel-rules-proto is a set of Bazel rules for building Protocol Buffers.

%package source
Summary:        Source code of bazel-rules-proto
Group:          Development/Sources
BuildArch:      noarch

%description source
bazel-rules-proto is a set of Bazel rules for building Protocol Buffers.

This package contains source code of bazel-rules-proto.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
tar -xJf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
# Fix hidden-dile-or-dir warning.
find %{buildroot}%{src_install_dir} -name ".*" -exec rm -rf "{}" +
# Remove files for Dart language - it's not packaged in openSUSE.
find %{buildroot}%{src_install_dir} -type f -name "*.dart" -exec rm -f "{}" +
# Fix env-script-interpreter error.
find %{buildroot}%{src_install_dir} -type f -name "*.py" -exec sed -i 's|#!/usr/bin/env python3|#!/usr/bin/python3|' "{}" +
find %{buildroot}%{src_install_dir} -type f -name "*.rb" -exec sed -i 's|#!/usr/bin/env ruby|#!/usr/bin/ruby|' "{}" +
# Fix non-executable-script warning.
chmod +x %{buildroot}%{src_install_dir}/ruby/example/routeguide/client.rb
chmod +x %{buildroot}%{src_install_dir}/ruby/example/routeguide/server.rb

%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog

