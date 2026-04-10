#
# spec file for package python-hatch-argparse-manpage
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-hatch-argparse-manpage
Version:        1.0.1
Release:        0
Summary:        Hatch build hook plugin to generate manual pages
License:        GPL-3.0-or-later
URL:            https://github.com/damonlynch/hatch-argparse-manpage
Source:         https://files.pythonhosted.org/packages/source/h/hatch-argparse-manpage/hatch_argparse_manpage-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-argparse-manpage
Requires:       python-rich

%python_subpackages

%description
A Hatch build hook plugin that automatically generates manual pages
from argparse-based command-line interfaces during the build process.

%prep
%autosetup -p1 -n hatch_argparse_manpage-%{version}
chmod -x README.md CHANGES.md LICENSE.txt
find . -name "*.py" -exec chmod -x {} \;
find . -name "*.typed" -exec chmod -x {} \;

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc README.md CHANGES.md
%{python_sitelib}/hatch_argparse_manpage/
%{python_sitelib}/hatch_argparse_manpage-%{version}.dist-info/

%changelog
