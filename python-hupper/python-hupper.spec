#
# spec file for package python-hupper
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-hupper
Version:        1.8.1
Release:        0
Summary:        An in-process file monitor
License:        MIT
Group:          Development/Languages/Python
URL:            https://pylonsproject.org/
# Wheels lack files with problematic noncommercial license
Source:         https://files.pythonhosted.org/packages/py2.py3/h/hupper/hupper-%{version}-py2.py3-none-any.whl
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-watchdog
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%python_subpackages

%description
Hupper is an integrated process monitor that will track changes to any
imported Python files in sys.modules as well as custom paths.
When files are changed the process is restarted.

%prep
%setup -q -c -T

%build
# Not Needed

%install
%python_expand pip%{$python_bin_suffix} install --root=%{buildroot} %{SOURCE0}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/hupper

%post
%python_install_alternative hupper

%postun
%python_uninstall_alternative hupper

%files %{python_files}
%python_alternative %{_bindir}/hupper
%license %{python_sitelib}/hupper-%{version}.dist-info/LICENSE.txt
%{python_sitelib}/hupper-%{version}.dist-info/
%{python_sitelib}/hupper/

%changelog
