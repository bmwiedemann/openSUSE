#
# spec file for package gyp
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nurenberg, Germany.
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


Name:           gyp
Version:        0+git.20240207
Release:        0
Summary:        Generate Your Projects
License:        BSD-3-Clause
URL:            https://gyp.gsrc.io
Source:         %{name}-%{version}.tar.gz
Patch0:         gyp-rpmoptflags.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       ninja
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       gyp = %{version}
Obsoletes:      gyp < %{version}
BuildArch:      noarch
%python_subpackages

%description
GYP is a tool to generates native Visual Studio, Xcode and SCons and/or make
build files from a platform-independent input format. Its syntax is a universal
cross-platform build representation that still allows sufficient per-platform
flexibility to accommodate irreconcilable differences

%prep
%autosetup -p0
for i in $(find pylib -name '*.py'); do
	sed -e '\,#![ \t]*/.*python,{d}' $i > $i.new && touch -r $i $i.new && mv $i.new $i
done
sed -i '/^#!/d' ./pylib/%{name}/*.py
sed -i '/^#!/d' ./pylib/%{name}/generator/*.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/gyp
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative gyp

%postun
%python_uninstall_alternative gyp

%files %{python_files}
%license LICENSE
%doc AUTHORS
%python_alternative %{_bindir}/gyp
%{python_sitelib}/gyp
%{python_sitelib}/gyp-*-info

%changelog
