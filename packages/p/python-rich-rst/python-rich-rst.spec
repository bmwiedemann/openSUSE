#
# spec file for package python-rich-rst
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


Name:           python-rich-rst
Version:        2.1.0
Release:        0
Summary:        A beautiful reStructuredText renderer for rich
License:        MIT
URL:            https://github.com/wasi-master/rich-rst
Source:         https://files.pythonhosted.org/packages/source/r/rich_rst/rich_rst-%{version}.tar.gz
BuildRequires:  %{python_module Pygments >= 2.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module rich >= 12.0.0}
BuildRequires:  %{python_module setuptools >= 64}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pygments >= 2.0.0
Requires:       python-rich >= 12.0.0
BuildArch:      noarch
%python_subpackages

%description
A beautiful and easy to use reStructuredText renderer for the rich
library, to render RST documents in the terminal.

%prep
%autosetup -p1 -n rich_rst-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# strip a spurious shebang from a vendored docutils helper (non-executable-script)
%python_expand sed -i '1{/^#!/d}' %{buildroot}%{$python_sitelib}/rich_rst/_vendor/docutils/utils/smartquotes.py
# the vendored docutils ships .py with old embedded mtimes; force hash-based .pyc
# so they don't trip python-bytecode-inconsistent-mtime after rpm mtime normalisation
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/rich_rst
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# -B so the import does not write fresh .pyc into the buildroot (mtime mismatch)
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import rich_rst"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/rich_rst
%{python_sitelib}/rich_rst-%{version}.dist-info

%changelog
