#
# spec file for package python-distro
#
# Copyright (c) 2020 SUSE LLC
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
Version:        1.5.0
Release:        0
Summary:        Linux Distribution - a Linux OS platform information API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/nir0s/distro
Source:         https://files.pythonhosted.org/packages/source/d/distro/distro-%{version}.tar.gz
Patch0:         assert_locale.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test
%if %{with test}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
%endif
# /SECTION
%python_subpackages

%description
distro (for: Linux Distribution) provides information about the Linux distribution it runs on, such as a reliable machine-readable ID, or version information.

It is a renewed alternative implementation for Python's original platform.linux_distribution function, but it also provides much more functionality which isn't necessarily Python bound like a command-line interface.

%prep
%setup -q -n distro-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/distro

%if %{with test}
%check
# Explicit settings of locale is necessary gh#nir0s/distro#223
LANG=en_US.utf8 %python_exec setup.py pytest
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
