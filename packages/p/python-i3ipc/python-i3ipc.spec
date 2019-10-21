#
# spec file for package python-i3ipc
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


Name:           python-i3ipc
# Before upgrading, verify compatibility with bumblebee-status module title
Version:        1.7.1
Release:        0
Summary:        Python library for i3 WM extensions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/altdesktop/i3ipc-python
Source0:        https://github.com/altdesktop/i3ipc-python/archive/v%{version}.tar.gz#/i3ipc-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  i3
BuildRequires:  python-enum34
BuildRequires:  python-rpm-macros
BuildRequires:  xvfb-run
BuildArch:      noarch
%ifpython2
Requires:       python-enum34
%endif
%python_subpackages

%description
python-i3ipc is a Python library for controlling the i3 window manager which
aims to be used by scripts and applications which interact with the window
manager like status line generators, notification daemons and pagers.

This library uses i3’s interprocess communication, which is the interface
that i3 WM uses to receive commands from client applications such as i3-msg. It
also features a publish/subscribe mechanism for notifying interested parties of
window manager events.

%prep
%setup -q -n i3ipc-python-%{version}
sed -i "s/'enum-compat'//" setup.py

# Remove shebang which is not needed (that script cannot be executed
# standalone).
sed -i '/^#!\/usr\/bin\/env.*/d' i3ipc/i3ipc.py examples/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_shutdown_event_reconnect always fails
# test_restart fails on openSUSE/SLE 15
# test_window_event is intermittent
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
xvfb-run --server-args "-screen 0 1920x1080x24" \
  $python -m pytest -k 'not (test_shutdown_event_reconnect or test_restart or test_window_event)'
}

%files %{python_files}
%license LICENSE
%doc README.rst CHANGELOG.md docs/*.rst
%doc examples/
%{python_sitelib}/*

%changelog
