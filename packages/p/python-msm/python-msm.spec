#
# spec file for package python-msm
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-msm
Version:        0.8.5
Release:        0
Summary:        Mycroft Skills Manager
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/MycroftAI/mycroft-skills-manager
Source:         https://github.com/MycroftAI/mycroft-skills-manager/archive/v%{version}.tar.gz
Patch1:         do-not-run-pip-or-requirements-script.patch
Patch2:         add-local-patch-support.patch
BuildRequires:  %{python_module GitPython}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module fasteners}
BuildRequires:  %{python_module lazy}
BuildRequires:  %{python_module pako}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       patch
Requires:       python-GitPython
Requires:       python-PyYAML
Requires:       python-fasteners
Requires:       python-lazy
Requires:       python-pako
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-typing
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
msm is Mycroft Skills Manager, a command line tool to install/list/remove
Mycroft skills.

%prep
%setup -q -n mycroft-skills-manager-%{version}
%patch1 -p1
%patch2 -p1
sed -i -e "s/install_requires=\['GitPython', 'typing'/install_requires=['GitPython'/" setup.py
sed -i -e "s/data_files=\[('msm', \['LICENSE'\])\]//" setup.py
chmod -x LICENSE

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/msm
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_mycroft_skills_manager.py and test_skill_repo.py clone a git repo from GitHub already in their __init__
# test_main.py also clones a repo in init via self.base_params
# run_pip calls pip to install some dependencies
%pytest --ignore tests/test_mycroft_skills_manager.py --ignore tests/test_skill_repo.py --ignore tests/test_main.py -k "not run_pip" tests

%post
%python_install_alternative msm

%postun
%python_uninstall_alternative msm

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/msm
%{python_sitelib}/msm
%{python_sitelib}/msm-%{version}-py%{python_version}.egg-info

%changelog
