#
# spec file for package python-yapf
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
Name:           python-yapf
Version:        0.43.0
Release:        0
Summary:        A formatter for Python code
License:        Apache-2.0
URL:            https://github.com/google/yapf
Source:         https://files.pythonhosted.org/packages/source/y/yapf/yapf-%{version}.tar.gz
BuildRequires:  %{python_module devel >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module platformdirs}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tomli if %python-base < 3.11}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-platformdirs
%if 0%{?python_version_nodots} < 311
Requires:       python-tomli
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Recommends:     python-futures
%endif
%python_subpackages

%description
YAPF is based off clang-format and reformats it to the closest
formatting that conforms to the style guide, even if the original
code did not violate the style guide.

This is in contrast to other formatters like autopep8 and pep8ify
which are made to only remove lint errors from code, which has some
limitations, like, code that conforms to the PEP 8 guidelines may not
be reformatted.

%prep
%setup -q -n yapf-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/yapf
%python_clone -a %{buildroot}%{_bindir}/yapf-diff
%python_expand rm -r %{buildroot}%{$python_sitelib}/yapftests

%check
%pytest --capture=no

%post
%python_install_alternative yapf yapf-diff

%postun
%python_uninstall_alternative yapf

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%python_alternative %{_bindir}/yapf
%python_alternative %{_bindir}/yapf-diff
%{python_sitelib}/yapf/
%{python_sitelib}/yapf_third_party/
%{python_sitelib}/yapf-%{version}.dist-info

%changelog
