#
# spec file for package python-docopt-ng
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-docopt-ng
Version:        0.9.0
Release:        0
Summary:        Humane command line arguments parser
License:        MIT
URL:            https://github.com/jazzband/docopt-ng
Source:         https://files.pythonhosted.org/packages/source/d/docopt-ng/docopt_ng-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#jazzband/docopt-ng#66
Patch0:         support-pytest-9.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pdm-backend}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Conflicts:      python-docopt
BuildArch:      noarch
%python_subpackages

%description
**docopt-ng** helps you create beautiful command-line interfaces.

docopt-ng is a fork of the original docopt, now maintained by the jazzband
project. Now with maintenance, typehints, and complete test coverage!

%prep
%autosetup -p1 -n docopt_ng-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE-MIT
%{python_sitelib}/docopt
%{python_sitelib}/docopt_ng-%{version}.dist-info

%changelog
