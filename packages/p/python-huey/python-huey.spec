#
# spec file for package python-huey
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


%{?sle15_python_module_pythons}
Name:           python-huey
Version:        2.5.2
Release:        0
Summary:        huey, a little task queue
License:        MIT
URL:            http://github.com/coleifer/huey/
Source:         https://files.pythonhosted.org/packages/source/h/huey/huey-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module redis}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-redis >= 3.0.0
BuildArch:      noarch
%python_subpackages

%description
huey, a little task queue

%prep
%autosetup -p1 -n huey-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/huey_consumer.py
%python_clone -a %{buildroot}%{_bindir}/huey_consumer

%{python_expand #
chmod 755 %{buildroot}%{$python_sitelib}/huey/bin/huey_consumer.py
%{$python_fix_shebang_path %{buildroot}%{$python_sitelib}/huey/bin/huey_consumer.py}
}

%python_expand %fdupes %{buildroot}%{$python_sitelib}

# all checks need a running REDIS instance

%post
%python_install_alternative huey_consumer.py huey_consumer

%postun
%python_uninstall_alternative huey_consumer.py

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%python_alternative %{_bindir}/huey_consumer.py
%python_alternative %{_bindir}/huey_consumer
%{python_sitelib}/huey
%{python_sitelib}/huey-%{version}.dist-info

%changelog
