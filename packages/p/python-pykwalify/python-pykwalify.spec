#
# spec file for package python-pykwalify
#
# Copyright (c) 2020 SUSE LLC
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
%bcond_without test
Name:           python-pykwalify
Version:        1.7.0
Release:        0
Summary:        Python lib/cli for JSON/YAML schema validation
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/grokzen/pykwalify
Source:         https://files.pythonhosted.org/packages/source/p/pykwalify/pykwalify-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML >= 3.11
Requires:       python-docopt >= 0.6.2
Requires:       python-python-dateutil >= 2.4.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-ruamel.yaml >= 0.11.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module PyYAML >= 3.11}
BuildRequires:  %{python_module docopt >= 0.6.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.4.2}
BuildRequires:  %{python_module testfixtures}
%endif
%python_subpackages

%description
YAML/JSON validation library
This framework is a port with a lot added functionality of the java version of the framework kwalify that can be found at: http://www.kuwata-lab.com/kwalify/
The original source code can be found at: http://sourceforge.net/projects/kwalify/files/kwalify-java/0.5.1/
The source code of the latest release that has been used can be found at: https://github.com/sunaku/kwalify. Please note that source code is not the original authors code but a fork/upload of the last release available in ruby.
The schema this library is base and extended from: http://www.kuwata-lab.com/kwalify/ruby/users-guide.01.html#schema

%prep
%setup -q -n pykwalify-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pykwalify
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%if %{with test}
%check
%python_exec setup.py test
%endif

%post
%python_install_alternative pykwalify

%postun
%python_uninstall_alternative pykwalify

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pykwalify
%{python_sitelib}/*

%changelog
