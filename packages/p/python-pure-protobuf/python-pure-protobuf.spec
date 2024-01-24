#
# spec file for package python-pure-protobuf
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

%{?sle15_python_module_pythons}
Name:           python-pure-protobuf
Version:        2.3.0
Release:        0
Summary:        Protocol Buffers using Python type annotations
Group:          Development/Libraries/Python
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/eigenein/protobuf
Source:         https://files.pythonhosted.org/packages/source/p/pure-protobuf/pure_protobuf-%{version}.tar.gz
Source1:        pure_protobuf-tests-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  fdupes
## needed for tests
BuildRequires:  %{python_module pytest}
BuildArch:      noarch
%python_subpackages

%description
%{summary}.

%prep
%autosetup -a1 -p1 -n pure_protobuf-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
donttest="serializer"
%pytest -k "not $donttest"

%files %{python_files}
%{python_sitelib}/pure_protobuf
%{python_sitelib}/pure_protobuf-%{version}.dist-info

%changelog
