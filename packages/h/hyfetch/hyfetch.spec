#
# spec file for package hyfetch
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


%define skip_python2 1
Name:           hyfetch
Version:        1.4.10
Release:        0
Summary:        Customizable Linux System Information Script
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/hykilpikonna/HyFetch
Source:         https://files.pythonhosted.org/packages/source/H/HyFetch/HyFetch-%{version}.tar.gz
# PATCH-FIX-SUSE Fix E: env-script-interpreter
Patch0:         fix-shebang.patch
# PATCH-FIX-UPSTREAM -- bkasin - Fix config file flag
Patch1:         fix-config-flag.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module typing_extensions}
# /SECTION
BuildRequires:  fdupes
Requires:       python-setuptools
Requires:       python-typing_extensions
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     maim
Recommends:     w3m-inline-image
BuildArch:      noarch
%python_subpackages

%description
HyFetch is a command line script to display information about your
Linux system, such as amount of installed packages, OS and kernel
version, active GTK theme, CPU info, and used/available memory.
It is a fork of neofetch, and adds pride flag coloration to the OS logo.

%prep
%autosetup -p1 -n HyFetch-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}/%{_bindir}/hyfetch
%python_clone -a %{buildroot}/%{_bindir}/neowofetch
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%{python_install_alternative hyfetch neowofetch}

%postun
%python_uninstall_alternative hyfetch

%files %{python_files}
%doc README.md
%license LICENSE.md
%python_alternative %{_bindir}/neowofetch
%python_alternative %{_bindir}/hyfetch
%{python_sitelib}/hyfetch
%{python_sitelib}/HyFetch-%{version}.dist-info

%changelog
