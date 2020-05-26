#
# spec file for package python-msk
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
Name:           python-msk
Version:        0.3.14
Release:        0
Summary:        Mycroft Skills Kit
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/MycroftAI/mycroft-skills-kit
Source:         https://files.pythonhosted.org/packages/source/m/msk/msk-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/MycroftAI/mycroft-skills-kit/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-GitPython
Requires:       python-PyGithub
Requires:       python-msm >= 0.5.13
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%ifpython2
Requires:       python-typing
%endif
%python_subpackages

%description
Mycroft Skills Kit python module.

%prep
%setup -q -n msk-%{version}
sed -i -e "s/\(install_requires.*\)'typing',/\1/" setup.py
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/msk
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative msk

%postun
%python_uninstall_alternative msk

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/msk
%{python_sitelib}/*

%changelog
