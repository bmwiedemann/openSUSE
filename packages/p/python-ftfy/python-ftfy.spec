#
# spec file for package python-ftfy
#
# Copyright (c) 2021 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-ftfy
Version:        6.0.1
Release:        0
Summary:        Python module for repairing mis-decoded Unicode text
License:        MIT
URL:            https://github.com/LuminosoInsight/python-ftfy
Source:         https://github.com/LuminosoInsight/python-ftfy/archive/v%{version}.tar.gz#/ftfy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-wcwidth
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wcwidth}
# /SECTION
%python_subpackages

%description
Ftfy attempts to repair Unicode text that has been erroneously
put through an encode/decode cycle with different encodings.

%prep
%setup -q -n python-ftfy-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/ftfy
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand # provide u-a controlled cli command for tests
mkdir -p build/testbin
ln -s %{buildroot}%{_bindir}/ftfy-%{python_bin_suffix} build/testbin/ftfy
}
export PATH="build/testbin:$PATH"
%pytest

%post
%python_install_alternative ftfy

%postun
%python_uninstall_alternative ftfy

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%python_alternative %{_bindir}/ftfy
%{python_sitelib}/*

%changelog
