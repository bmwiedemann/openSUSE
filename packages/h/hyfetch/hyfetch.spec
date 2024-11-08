#
# spec file for package hyfetch
#
# Copyright (c) 2024 SUSE LLC
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
Version:        1.99.0
Release:        0
Summary:        Customizable Linux System Information Script
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/hykilpikonna/HyFetch
Source:         https://files.pythonhosted.org/packages/source/H/HyFetch/HyFetch-%{version}.tar.gz
# PATCH-FIX-SUSE Fix E: env-script-interpreter
Patch0:         fix-shebang.patch
# PATCH-FIX-UPSTREAM
Patch1:         https://patch-diff.githubusercontent.com/raw/hykilpikonna/hyfetch/pull/362.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
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

%package -n neowofetch
# version as reported by neowofetch --version
Version:        7.98.0
Summary:        CLI system information tool written in BASH
Provides:       neofetch = %{version}
Obsoletes:      neofetch < %{version}

%description -n neowofetch
Displays information about the system next to an image, the OS logo, or any
ASCII file of choice. The main purpose of Neofetch is to be used in
screenshots to show other users what OS/Distro is running, what Theme/Icons
are being used, etc.

Customizable through the use of command line flags or the user config file.
There are over 50 config options to mess around with and there's the `print_info()
function and friends which let you add your own custom info.

This is the forked version that is maintained together with hyfetch

%prep
%autosetup -p1 -n HyFetch-%{VERSION}
# copy the patched neofetch to scripts/ - in git, this is a symlink, but the tarball has it as a regular file
cp neofetch hyfetch/scripts/neowofetch

%build
sed -i 's/packages=find_namespace_packages(exclude=("tools", "tools.*")),/packages=find_namespace_packages(exclude=("tools", "tools.*", "docs")),/' setup.py
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}/%{_bindir}/hyfetch
%python_expand %fdupes %{buildroot}%{$python_sitelib}
ln -s %{_bindir}/neowofetch %{buildroot}%{_bindir}/neofetch

%post
%{python_install_alternative hyfetch}

%postun
%python_uninstall_alternative hyfetch

%check
[ "$(%{buildroot}%{_bindir}/neofetch --version)" == "Neofetch %{version}" ] || (
    echo "Neofetch version does not match the RPM version - please update"
    exit 1
)

%files %{python_files}
%doc README.md
%license LICENSE.md
%python_alternative %{_bindir}/hyfetch
%{python_sitelib}/hyfetch
%{python_sitelib}/HyFetch-%{VERSION}.dist-info

%files -n neowofetch
%{_bindir}/neofetch
%{_bindir}/neowofetch

%changelog
