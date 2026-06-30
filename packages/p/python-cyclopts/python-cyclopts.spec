#
# spec file for package python-cyclopts
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


Name:           python-cyclopts
Version:        4.20.0
Release:        0
Summary:        Intuitive, easy CLIs based on python type hints
License:        Apache-2.0
URL:            https://github.com/BrianPugh/cyclopts
Source:         https://files.pythonhosted.org/packages/source/c/cyclopts/cyclopts-%{version}.tar.gz
BuildRequires:  %{python_module attrs >= 23.1.0}
BuildRequires:  %{python_module docstring-parser >= 0.15}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module rich >= 13.6.0}
BuildRequires:  %{python_module rich-rst >= 1.3.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-attrs >= 23.1.0
Requires:       python-docstring-parser >= 0.15
Requires:       python-rich >= 13.6.0
Requires:       python-rich-rst >= 1.3.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{python_version_nodots} < 311
Requires:       python-tomli >= 2.0.0
Requires:       python-typing_extensions >= 4.8.0
%endif
%python_subpackages

%description
Cyclopts is a modern, easy-to-use command-line-interface library for
Python, based on type hints, with rich help output and intuitive
argument/sub-command resolution.

%prep
%autosetup -p1 -n cyclopts-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/cyclopts
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/cyclopts
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -B -c "import cyclopts"

%post
%python_install_alternative cyclopts

%postun
%python_uninstall_alternative cyclopts

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/cyclopts
%{python_sitelib}/cyclopts
%{python_sitelib}/cyclopts-%{version}.dist-info

%changelog
