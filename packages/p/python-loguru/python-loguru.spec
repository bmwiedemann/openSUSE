#
# spec file for package python-loguru
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-loguru
Version:        0.5.3
Release:        0
Summary:        Python logging component with a simple interface
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Delgan/loguru
Source:         https://files.pythonhosted.org/packages/source/l/loguru/loguru-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pytest-6.2-excepthooks.patch
Patch0:         https://github.com/Delgan/loguru/commit/31cf758ee9d22dbfa125f38153782fe20ac9dce5.patch#/pytest-6.2-excepthooks.patch
# PATCH-FIX-UPSTREAM loguru-exception-formatting-py39.patch
Patch1:         https://github.com/Delgan/loguru/commit/19f518c5f1f355703ffc4ee62f0e1e397605863e.patch#/loguru-exception-formatting-py39.patch
BuildRequires:  %{python_module aiocontextvars if %python-base < 3.7}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?python_version_nodots} < 37
Requires:       python-aiocontextvars
%endif
Recommends:     python-colorama
BuildArch:      noarch

%python_subpackages

%description
Python logging component providing a single object
which dispatches log messages to configured handlers.

%prep
%autosetup -p1 -n loguru-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
if [ $(getconf LONG_BIT) = 32 ]; then
  # Threads have different references on 32-bit
  donttest="(test_log_formatters and thread and not thread.name)"
fi
%pytest ${donttest:+ -k "not ($donttest)"}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/loguru*

%changelog
