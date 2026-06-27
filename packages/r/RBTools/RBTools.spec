#
# spec file for package RBTools
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


Name:           RBTools
Version:        6.0
Release:        0
Summary:        Command line tools for interacting with Review Board
License:        MIT
URL:            https://www.reviewboard.org
Source:         https://files.pythonhosted.org/packages/source/r/rbtools/rbtools-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 74}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-appdirs >= 1.4.4
Requires:       python-certifi >= 2023.5.7
Requires:       python-colorama
Requires:       python-housekeeping >= 1.1
Requires:       python-importlib-metadata >= 5.0
Requires:       python-importlib-resources >= 5.9
Requires:       python-packaging >= 21.3
Requires:       python-puremagic
Requires:       python-pydiffx >= 1.1
Requires:       python-texttable
Requires:       python-tqdm
Requires:       python-typelets >= 1.1
Requires:       python-typing_extensions >= 4.3.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
# RBTools used to be a single non-flavoured package shipping /usr/bin/rbt;
# the singlespec flavours now carry it, so supersede the old package.
Provides:       RBTools = %{version}-%{release}
Obsoletes:      RBTools < %{version}
BuildArch:      noarch
%python_subpackages

%description
RBTools is a set of client tools to use with Review Board. This
consists of the rbt command, which provides a number of sub-commands to
create and update review requests from local source trees and otherwise
interact with a Review Board server, along with a Python API client to
simplify interaction with the Review Board web API.

%prep
%autosetup -p1 -n rbtools-%{version}
# concrete interpreter for the shipped test-editor stub (env-script-interpreter)
sed -i '1s|^#!%{_bindir}/env python|#!%{_bindir}/python3|' rbtools/testing/scripts/editor.py

%build
%pyproject_wheel

%install
%pyproject_install
# drop the bundled test suites and fixtures (fake VCS repos, dotfiles,
# zero-length files) that otherwise ship into site-packages
%python_expand find %{buildroot}%{$python_sitelib}/rbtools -type d -name tests -prune -exec rm -rf {} +
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/rbtools
%python_clone -a %{buildroot}%{_bindir}/rbt
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# The full test suite drives external VCS tooling and a Review Board
# server; run a smoke check that the package imports instead.
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -c "import rbtools"

%post
%python_install_alternative rbt

%postun
%python_uninstall_alternative rbt

%files %{python_files}
%license COPYING
%doc AUTHORS NEWS README.md
%python_alternative %{_bindir}/rbt
%{python_sitelib}/rbtools
%{python_sitelib}/rbtools-%{version}.dist-info

%changelog
