#
# spec file for package python-vncdotool
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


%{?sle15_python_module_pythons}
Name:           python-vncdotool
Version:        1.0.0
Release:        0
Summary:        Command line VNC client
License:        MIT
URL:            https://github.com/sibson/vncdotool
Source:         https://files.pythonhosted.org/packages/source/v/vncdotool/vncdotool-%{version}.tar.gz
Patch0:         remove-nose.patch
Patch1:         fix-mocking.patch
# https://github.com/sibson/vncdotool/issues/218
Patch2:         python-vncdotool-no-mock.patch
# gh#python/cpython#88852
Patch3:         py311-compat.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-Twisted
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module Twisted}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Command line VNC client.

%prep
%setup -q -n vncdotool-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/vncdo
%python_clone -a %{buildroot}%{_bindir}/vncdotool
%python_clone -a %{buildroot}%{_bindir}/vnclog
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative vncdo
%python_install_alternative vncdotool
%python_install_alternative vnclog

%postun
%python_uninstall_alternative vncdo
%python_uninstall_alternative vncdotool
%python_uninstall_alternative vnclog

%check
%pytest -k 'not functional'

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/vncdo
%python_alternative %{_bindir}/vncdotool
%python_alternative %{_bindir}/vnclog
%{python_sitelib}/vncdotool
%{python_sitelib}/vncdotool-%{version}*-info

%changelog
