#
# spec file for package python-nkdfu
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
Name:           python-nkdfu
Version:        0.2
Release:        0
Summary:        DFU tool for updating Nitrokeys' firmware
License:        GPL-2.0-only
URL:            https://github.com/Nitrokey/nkdfu
Source:         https://files.pythonhosted.org/packages/source/n/nkdfu/nkdfu-0.2.tar.gz
BuildRequires:  %{python_module flit}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       intelhex
Requires:       python-fire
Requires:       python-libusb1
Requires:       python-tqdm
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
nkdfu is a Python DFU tool for updating Nitrokeys' firmware. Currently supports Nitrokey Pro only.
Based on python-dfu project, which brings implementation of USB DFU 1.1 spec.

%prep
%autosetup -p1 -n nkdfu-%{version}

sed -i -e '1{\@^#![[:blank:]]*%{_bindir}/env python@d}' nkdfu/dfu_flash.py
chmod -x nkdfu/dfu_flash.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/nkdfu
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# there are no checks available upstream

%post
%python_install_alternative nkdfu

%postun
%python_uninstall_alternative nkdfu

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/nkdfu
%{python_sitelib}/nkdfu
%{python_sitelib}/nkdfu-%{version}*-info

%changelog
