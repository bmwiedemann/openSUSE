#
# spec file for package python-xonsh
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-xonsh
Version:        0.9.17
Release:        0
Summary:        Python-powered, cross-platform, Unix-gazing shell
License:        BSD-2-Clause
URL:            https://github.com/xonsh/xonsh
Source:         https://files.pythonhosted.org/packages/source/x/xonsh/xonsh-%{version}.tar.gz
BuildRequires:  %{python_module distro}
BuildRequires:  %{python_module importlib_resources}
BuildRequires:  %{python_module prompt_toolkit}
BuildRequires:  %{python_module pygments >= 2.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setproctitle}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{pythons}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  make
BuildRequires:  python-rpm-macros
Requires:       python
Requires:       python-distro
Requires:       python-importlib_resources
Requires:       python-prompt_toolkit
Requires:       python-pygments >= 2.2
Requires:       python-setproctitle
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
xonsh is a Python-powered, cross-platform, Unix-gazing shell language and command prompt.
The language is a superset of Python 3.5+ with additional shell primitives.

%prep
%setup -q -n xonsh-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/xonsh-cat
%python_clone -a %{buildroot}%{_bindir}/xonsh
%python_clone -a %{buildroot}%{_bindir}/xon.sh
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PATH=$PATH:%{buildroot}%{_bindir}
# test_man_completion needs installed manpages
# test_xonsh_no_close_fds the makefile fails to compile
%{python_expand export PYTHONPATH=":%{buildroot}%{$python_sitelib}"
$python -m xonsh run-tests.xsh -k 'not (test_man_completion or test_xonsh_no_close_fds)'}

%post
%python_install_alternative xonsh-cat
%python_install_alternative xonsh
%python_install_alternative xon.sh

%postun
%python_uninstall_alternative xonsh-cat
%python_uninstall_alternative xonsh
%python_uninstall_alternative xon.sh

%files %{python_files}
%doc README.rst CHANGELOG.rst
%license license
%{python_sitelib}/*
%python_alternative %{_bindir}/xon.sh
%python_alternative %{_bindir}/xonsh
%python_alternative %{_bindir}/xonsh-cat

%changelog
