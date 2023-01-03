#
# spec file for package python-distro
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%{!?license: %global license %doc}
%bcond_without test
Name:           python-distro
Version:        1.8.0
Release:        0
Summary:        Linux Distribution - a Linux OS platform information API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/nir0s/distro
Source:         https://files.pythonhosted.org/packages/source/d/distro/distro-%{version}.tar.gz
Patch0:         assert_locale.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
%python_subpackages

%description
distro (for: Linux Distribution) provides information about the Linux distribution it runs on, such as a reliable machine-readable ID, or version information.

It is a renewed alternative implementation for Python's original platform.linux_distribution function, but it also provides much more functionality which isn't necessarily Python bound like a command-line interface.

%prep
%setup -q -n distro-%{version}
# remove shebang. Has been added by upstream intentionally: https://github.com/python-distro/distro/commit/8032f16a1082ff72471c13ff665f3ad9c929f3b0
sed -i '1{/\/usr\/bin\/env python/d;}' src/distro/distro.py
%patch0 -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/distro

%if %{with test}
%check
export LANG=C.UTF-8
%pytest
%endif

%post
%python_install_alternative distro

%postun
%python_uninstall_alternative distro

%files %{python_files}
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/distro
%{python_sitelib}/*
%%license LICENSE

%changelog
