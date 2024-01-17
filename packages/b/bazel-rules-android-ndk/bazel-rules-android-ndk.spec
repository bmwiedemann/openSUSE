#
# spec file
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


%define src_install_dir /usr/src/%{name}
%define base_name bazel-rules-android-ndk
%define commit 81ec8b79dc50ee97e336a25724fdbb28e33b8d41

Name:           %{base_name}
Version:        20220902
Release:        0
Summary:        Bazel rules to build software using Andoid NDK
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://github.com/bazelbuild/rules_android_ndk
# https://github.com/bazelbuild/rules_android_ndk/archive/${commit}.zip
Source0:        %{base_name}-%{commit}.zip
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  unzip

%description
Bazel rules to build software using Android NDK.

%package source
Summary:        Source code of bazel-rules-apple
BuildArch:      noarch

%description source
Bazel rules to build software using Android NDK.

This package contains source code for bazel-rules-android-ndk.

%prep
%setup -qn rules_android_ndk-%{commit}

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
