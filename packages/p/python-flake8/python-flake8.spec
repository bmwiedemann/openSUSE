#
# spec file for package python-flake8
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
%bcond_without python2
Name:           python-flake8
Version:        3.8.4
Release:        0
Summary:        Modular source code checker: pep8, pyflakes and co
License:        MIT
URL:            https://gitlab.com/pycqa/flake8
Source:         https://files.pythonhosted.org/packages/source/f/flake8/flake8-%{version}.tar.gz
Patch0:         fix-mock-patch-with-python3.4.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-importlib-metadata
Requires:       python-mccabe >= 0.6.0
Requires:       python-pycodestyle >= 2.6.0~a1
Requires:       python-pyflakes >= 2.1.0
Requires:       python-typing
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module mccabe >= 0.6.0}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pycodestyle >= 2.6.0~a1}
BuildRequires:  %{python_module pyflakes >= 2.2.0}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing}
%if %{with python2}
BuildRequires:  python2-configparser >= 3.7.0
BuildRequires:  python2-enum34
BuildRequires:  python2-functools32
BuildRequires:  python2-mock
%endif
# /SECTION
%ifpython2
Requires:       python-configparser >= 3.7.0
Requires:       python-enum34
Requires:       python-functools32
%endif
%python_subpackages

%description
Flake8 is a modular extensible source code checker including wrappers
around these tools:

- PyFlakes
- pep8
- Ned Batchelder's McCabe script

Flake8 runs all the tools by launching the single ``flake8`` script.

%package -n %{name}-doc
Summary:        Documentation files for %{name}
Recommends:     %{name} = %{version}

%description -n %{name}-doc
Flake8 is a modular extensible source code checker.

This package provides documentation for %{name}.

%prep
%setup -q -n flake8-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/flake8
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative flake8

%postun
%python_uninstall_alternative flake8

%check
%pytest tests

%files %{python_files}
%license LICENSE
%doc docs/source/manpage.rst
%python_alternative %{_bindir}/flake8
%dir %{python_sitelib}/flake8
%{python_sitelib}/flake8/*
%{python_sitelib}/flake8-%{version}-py*.egg-info

%files -n %{name}-doc
%doc README.rst
%doc docs/source/index.rst docs/source/faq.rst docs/source/glossary.rst
%doc docs/source/internal/ docs/source/user docs/source/plugin-development
%license LICENSE

%changelog
