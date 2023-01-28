#
# spec file for package python-loguru
#
# Copyright (c) 2023 SUSE LLC
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
%define skip_python36 1
Name:           python-loguru
Version:        0.6.0
Release:        0
Summary:        Python logging component with a simple interface
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Delgan/loguru
Source:         https://files.pythonhosted.org/packages/source/l/loguru/loguru-%{version}.tar.gz
# PATCH-FIX-UPSTREAM loguru-fix-repr-tests.patch https://github.com/Delgan/loguru/commit/4fe21f6 -- Fix "repr()" tests failing on Python 3.11 and Python 3.10.6
Patch1:         loguru-fix-repr-tests.patch
# PATCH-FIX-UPSTREAM https://github.com/Delgan/loguru/commit/5b77724ca75aa8f4b1c8866e0b786c3cbe30ca99
Patch2:         python311.patch
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
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
  donttest=" or (test_log_formatters and thread and not thread.name)"
fi
%pytest -k "not (donttestexprprefixdummy $donttest)"

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/loguru
%{python_sitelib}/loguru-%{version}*-info

%changelog
