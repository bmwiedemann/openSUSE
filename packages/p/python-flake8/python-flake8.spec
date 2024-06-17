#
# spec file for package python-flake8
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-flake8
Version:        7.1.0
Release:        0
Summary:        Modular source code checker: pep8, pyflakes and co
License:        MIT
URL:            https://flake8.pycqa.org
Source:         https://github.com/PyCQA/flake8/archive/refs/tags/%{version}.tar.gz#/flake8-%{version}.tar.gz
# workaround for https://github.com/PyCQA/flake8/pull/1669
Source2:        https://raw.githubusercontent.com/PyCQA/flake8/%{version}/bin/gen-pycodestyle-plugin
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module mccabe >= 0.7.0 with %python-mccabe < 0.8.0}
BuildRequires:  %{python_module pycodestyle >= 2.12.0 with %python-pycodestyle < 2.13.0}
BuildRequires:  %{python_module pyflakes >= 3.2.0 with %python-pyflakes < 3.3.0}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch
# https://flake8.pycqa.org/en/latest/faq.html#why-does-flake8-use-ranges-for-its-dependencies
Requires:       (python-mccabe >= 0.7.0 with python-mccabe < 0.8.0)
Requires:       (python-pycodestyle >= 2.12.0 with python-pycodestyle < 2.13.0)
Requires:       (python-pyflakes >= 3.2.0 with python-pyflakes < 3.3.0)
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
%autosetup -p1 -n flake8-%{version}
install -m 0755 -D %{SOURCE2} bin/gen-pycodestyle-plugin

%build
%pyproject_wheel

%install
%pyproject_install
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
%python_alternative %{_bindir}/flake8
%{python_sitelib}/flake8
%{python_sitelib}/flake8-%{version}.dist-info

%files -n %{name}-doc
%doc README.rst
%doc docs/source/index.rst docs/source/faq.rst docs/source/glossary.rst
%doc docs/source/internal/ docs/source/user docs/source/plugin-development
%license LICENSE

%changelog
