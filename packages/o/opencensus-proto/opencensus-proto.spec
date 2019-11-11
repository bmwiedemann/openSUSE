#
# spec file for package opencensus-proto
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


%global provider        github
%global provider_tld    com
%global project         census-instrumentation
%global repo            opencensus-proto
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}

%define src_install_dir /usr/src/%{name}

Name:           opencensus-proto
Version:        0.2.1
Release:        0
Summary:        Protocol buffers for OpenCensus
License:        Apache-2.0
Group:          Development/Languages/Golang
Url:            https://%{provider_prefix}
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  golang-packaging
%{go_provides}

%description
Protocol buffers for OpenCensus - a framework for collecting metrics and
distributed traces from services.

%package source
Summary:        Source code of opencensus-proto
Group:          Development/Sources
BuildArch:      noarch

%description source
Protocol buffers for OpenCensus - a framework for collecting metrics and
distributed traces from services.

This package contains source code for googleapis.

%prep
%setup -q

%build
# TODO: Install go module from gen-go/ directory. It's not trivial, this
# project does not contain the vendor/ dir.

%install
# Install sources
mkdir -p %{buildroot}%{src_install_dir}
tar -xJf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
