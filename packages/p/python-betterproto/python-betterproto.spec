#
# spec file for package python-betterproto
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


Name:           python-betterproto
Version:        2.0.0b6
Release:        0
Summary:        A better Protobuf / gRPC generator & library
License:        MIT
URL:            http://github.com/danielgtaylor/python-betterproto
Source:         https://files.pythonhosted.org/packages/source/b/betterproto/betterproto-%{version}.tar.gz
Source99:       python-betterproto.rpmlintrc
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module grpclib}
BuildRequires:  %{python_module dateutil}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-grpclib
Requires:       python-dateutil
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A better Protobuf / gRPC generator & library

%prep
%autosetup -p1 -n betterproto-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %{$python_fix_shebang_path %{buildroot}%{$python_sitelib}/betterproto/plugin/main.py}
%python_compileall
%python_clone -a %{buildroot}%{_bindir}/protoc-gen-python_betterproto
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Disable tests, the generation doesn't work correctly
# python3 -m betterproto.tests.generate
# %%pytest
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -c "import betterproto"

%post
%python_install_alternative protoc-gen-python_betterproto

%postun
%python_uninstall_alternative protoc-gen-python_betterproto

%files %{python_files}
%doc README.md
%python_alternative %{_bindir}/protoc-gen-python_betterproto
%{python_sitelib}/betterproto
%{python_sitelib}/betterproto-%{version}.dist-info

%changelog
