#
# spec file for package python-notify-py
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-notify-py
Version:        0.3.43
Release:        0
Summary:        Cross-platform desktop notification library for Python
License:        MIT
URL:            https://github.com/ms7m/notify-py
Source:         https://files.pythonhosted.org/packages/source/n/notify_py/notify_py-%{version}.tar.gz
BuildRequires:  %{python_module loguru >= 0.5.3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jeepney
Requires:       python-loguru >= 0.5.3
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     libnotify-tools
BuildArch:      noarch
# SECTION test
BuildRequires:  %{python_module jeepney}
# /SECTION
%python_subpackages

%description
notify-py is a cross-platform desktop notification library for Python.
On Linux it sends notifications via notify-send (libnotify) and falls
back to D-Bus through jeepney; it can also play a notification sound.

%prep
%autosetup -p1 -n notify_py-%{version}
# Drop the bundled macOS notifier (prebuilt Mach-O binaries, useless on
# Linux and flagged by rpmlint as foreign architecture binaries)
rm -rf notifypy/os_notifiers/binaries

%build
%pyproject_wheel

%install
%pyproject_install
# poetry-core ships source files with inconsistent mtimes; drop pip-generated
# bytecode so the build-root byte-compile regenerates it consistently
find %{buildroot} -name __pycache__ -type d -exec rm -rf {} +
%python_clone -a %{buildroot}%{_bindir}/notifypy
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# upstream ships no test suite in the sdist; verify the module imports
%python_exec -c "import notifypy; from notifypy import Notify"

%post
%python_install_alternative notifypy

%postun
%python_uninstall_alternative notifypy

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/notifypy
%{python_sitelib}/notifypy
%{python_sitelib}/notify_py-%{version}.dist-info

%changelog
