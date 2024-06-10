#
# spec file for package python-wcmatch
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
%{?python_enable_dependency_generator}
Name:           python-wcmatch
Version:        8.5.2
Release:        0
Summary:        Wildcard/glob file name matcher
License:        MIT
URL:            https://github.com/facelessuser/wcmatch
Source:         https://files.pythonhosted.org/packages/source/w/wcmatch/wcmatch-%{version}.tar.gz
BuildRequires:  %{python_module base > 3.6}
BuildRequires:  %{python_module bracex}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Wildcard Match provides an enhanced `fnmatch`, `glob`, and `pathlib` library in order to provide file matching and
globbing that more closely follows the features found in Bash. In some ways these libraries are similar to Python's
builtin libraries as they provide a similar interface to match, filter, and glob the file system. But they also include
a number of features found in Bash's globbing such as backslash escaping, brace expansion, extended glob pattern groups,
etc. They also add a number of new useful functions as well, such as `globmatch` which functions like `fnmatch`, but for
paths.

Wildcard Match also adds a file search utility called `wcmatch` that is built on top of `fnmatch` and `globmatch`. It
was originally written for [Rummage](https://github.com/facelessuser/Rummage), but split out into this project to be
used by other projects that may find its approach useful.

Bash is used as a guide when making decisions on behavior for `fnmatch` and `glob`. Behavior may differ from Bash
version to Bash version, but an attempt is made to keep Wildcard Match up with the latest relevant changes. With all of
this said, there may be a few corner cases in which we've intentionally chosen to not *exactly* mirror Bash. If an issue
is found where Wildcard Match seems to deviate in an illogical way, we'd love to hear about it in the
[issue tracker](https://github.com/facelessuser/wcmatch/issues).

%prep
%setup -q -n wcmatch-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/wcmatch
%{python_sitelib}/wcmatch-%{version}.dist-info

%changelog
