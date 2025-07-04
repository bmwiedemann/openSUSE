#
# spec file for package python-wsproto
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


%{?sle15_python_module_pythons}
Name:           python-wsproto
Version:        1.2.0
Release:        0
Summary:        WebSockets state-machine based protocol implementation
License:        MIT
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/wsproto
Source:         https://files.pythonhosted.org/packages/source/w/wsproto/wsproto-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-h11 >= 0.9.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module h11 >= 0.9.0}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
This module contains a pure-Python implementation of a WebSocket
protocol stack. It's written from the ground up to be embeddable in
whatever program you choose to use, ensuring that you can
communicate via WebSockets, as defined in RFC6455
<https://tools.ietf.org/html/rfc6455>, regardless of your
programming paradigm.

This module does not provide a parsing layer, a network layer, or
any rules about concurrency. Instead, it's a purely in-memory
solution, defined in terms of data actions and WebSocket frames.
RFC6455 and Compression Extensions for WebSocket via RFC7692
<https://tools.ietf.org/html/rfc7692> are fully supported.

%prep
%autosetup -p1 -n wsproto-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/wsproto
%{python_sitelib}/wsproto-%{version}.dist-info

%changelog
