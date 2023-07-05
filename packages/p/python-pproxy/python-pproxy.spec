#
# spec file for package python-pproxy
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


%{?sle15_python_module_pythons}
Name:           python-pproxy
Version:        2.7.8
Release:        0
Summary:        Proxy server that can tunnel among remote servers by regex rules
License:        MIT
URL:            https://github.com/qwj/python-proxy
Source:         https://files.pythonhosted.org/packages/source/p/pproxy/pproxy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-aioquic >= 0.9.7
Suggests:       python-asyncssh >= 2.5.0
Suggests:       python-pycryptodome >= 3.7.2
Suggests:       python-python-daemon >= 2.2.3
Suggests:       python-uvloop >= 0.13.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aioquic >= 0.9.7}
BuildRequires:  %{python_module asyncssh >= 2.5.0}
BuildRequires:  %{python_module pycryptodome >= 3.7.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-daemon >= 2.2.3}
BuildRequires:  %{python_module uvloop >= 0.13.0}
# /SECTION
%python_subpackages

%description
Proxy server that can tunnel among remote servers by regex rules.

%prep
%setup -q -n pproxy-%{version}
# See https://github.com/qwj/python-proxy/issues/101 for status of these tests
# cipher_* doesnt allow any cli args, so easiest way to run them is removing other tests
rm tests/api_*.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pproxy
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pproxy

%postun
%python_uninstall_alternative pproxy

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
for file in tests/*.py; do
  $python $file
done
}

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/pproxy
%{python_sitelib}/*

%changelog
