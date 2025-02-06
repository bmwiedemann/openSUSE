#
# spec file for package python-distro
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
%{!?license: %global license %doc}
%bcond_without test
Name:           python-distro
Version:        1.9.0
Release:        0
Summary:        Linux Distribution - a Linux OS platform information API
License:        Apache-2.0
URL:            https://github.com/python-distro/distro
Source:         https://files.pythonhosted.org/packages/source/d/distro/distro-%{version}.tar.gz
Patch0:         assert_locale.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
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
%autosetup -p1 -n distro-%{version}
# remove shebang. Has been added by upstream intentionally: https://github.com/python-distro/distro/commit/8032f16a1082ff72471c13ff665f3ad9c929f3b0
sed -i '1{/\/usr\/bin\/env python/d;}' src/distro/distro.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/distro
%python_expand %fdupes %{buildroot}%{$python_sitelib}/distro

%if %{with test}
%check
export LANG=C.UTF-8
%pytest
%endif

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative distro

%post
%python_install_alternative distro

%postun
%python_uninstall_alternative distro

%files %{python_files}
%doc CHANGELOG.md README.md
%python_alternative %{_bindir}/distro
%{python_sitelib}/distro
%{python_sitelib}/distro-%{version}.dist-info
%%license LICENSE

%changelog
