#
# spec file for package python-psygnal
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-psygnal
Version:        0.12.0
Release:        0
Summary:        Fast python callback/event system modeled after Qt Signals
License:        BSD-3-Clause
URL:            https://github.com/pyapp-kit/psygnal
Source:         https://files.pythonhosted.org/packages/source/p/psygnal/psygnal-%{version}.tar.gz
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling >= 1.8.0}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module mypy_extensions}
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module dask}
BuildRequires:  %{python_module msgspec}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pytest >= 6.0}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module toolz}
BuildRequires:  %{python_module typing-extensions >= 3.7.4.2}
BuildRequires:  %{python_module wrapt}
# /SECTION
BuildRequires:  fdupes
Requires:       python-mypy_extensions
Requires:       python-typing-extensions >= 3.7.4.2
Suggests:       python-dask
Suggests:       python-ipython
Suggests:       python-numpy
Suggests:       python-pydantic
Suggests:       python-qtpy
Suggests:       python-rich
Suggests:       python-wrapt
Suggests:       python-griffe == 0.25.5
Suggests:       python-wrapt
BuildArch:      noarch
%python_subpackages

%description
Psygnal (pronounced "signal") is a pure python implementation of the [observer
pattern](https://en.wikipedia.org/wiki/Observer_pattern), with the API of
[Qt-style Signals](https://doc.qt.io/qt-5/signalsandslots.html) with (optional)
signature and type checking, and support for threading.

%prep
%autosetup -p1 -n psygnal-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitelib}/psygnal
%{python_sitelib}/psygnal-%{version}.dist-info

%changelog
